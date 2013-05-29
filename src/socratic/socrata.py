import json
import requests
import os
import os.path
import time
from urllib import urlencode
from urlparse import urljoin
from time import sleep


def authenticated_session():
    username = os.environ.get('SOCRATA_USER')
    password= os.environ.get('SOCRATA_PASSWORD')
    app_token= os.environ.get('SOCRATA_TOKEN')

    session = requests.Session()
    session.auth=(username,password)
    session.headers.update({'X-App-Token': app_token})
    return session

class API(object):
    def __init__(self, host=None, session=None, debug=False):
        self.session = session or request.Session()
        self.host = host or os.environ.get('SOCRATA_HOST')

    def call(self, resource='', method="GET", data=None, headers=None, json=True, files=None, debug=False):
        url = urljoin (self.host, resource)
        client = getattr(self.session,method.lower())
        resp = client(url, data=data, headers=headers, files=files)
        if debug:
            print resp.content
        return resp

    def call_publish(self,view_id, operation=None):
        publish_url = "/api/views/%s/publication.json" % view_id
        if operation:
            publish_url += "?method=%s" % operation
        resp = self.call(publish_url, method="POST")
        while True:
            if resp.status_code == 200:
                metadata = json.loads(resp.content)
                return metadata['id']
            elif resp.status_code != 202:
                resp.raise_for_status()        
         
        
    def create_working_copy(self, original_view):
        return self.call_publish(original_view, operation="copy")  
            
    def publish_working_copy(self, working_copy):
        return self.call_publish(original_view)  

    def wait_for_ticket(self, ticket):
        time.sleep(120)
        resp = self.call('/api/imports2.json?ticket=%s' % ticket, debug=True)
        if resp.status_code == 202:
            message = json.loads(resp.content)
            print "import status: %s Sleeping for a minute" % message['details']['status']
            return self.wait_for_ticket(ticket)
        if resp.status_code == 200:
            dataset_id = json.loads(resp.content)['id']
            return dataset_id

    def upload(self, path, replace=None, append=None, blueprint_path=None, debug=False):
        f=open(path)
        filename=os.path.split(path)[1]

        response= self.call('/api/imports2?method=scan', method='POST', files={filename:f}, debug=debug)
        parsed_response = json.loads(response.content)
        file_id= parsed_response['fileId']

        import_data ={'fileId': file_id,
                      'name': filename}

        extra_args=''
        if replace or append:
            working_copy = self.create_working_copy(replace or append)
            import_data['viewUid'] = working_copy
            if replace:
                extra_args = '?method=replace'

            if append:
                extra_args = '?method=append'

            blueprint_path = None #blueprints only apply to "new" datasets

        if blueprint_path:
            bp_data= file(blueprint_path).read()
            import_data['blueprint'] = bp_data
        import_response = self.call('/api/imports2.json%s' % extra_args, method='POST', data=import_data, debug=debug)
        return import_response



            






        return
