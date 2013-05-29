A Socrata publisher written in Python
======================
This library provides a Python interface to the [Socrata Publishing API], and a nifty command line client ('socratic').

API docs are coming soon, but here is the command line usage:

```
usage: socratic [-h] [--replace XXXX-XXXX] [--append XXXX-XXXX]
                [--blueprint blueprint.json] [--publish]
                {import} target

import or export data from a SODA source

positional arguments:
  {import}              operation to perform (currently, only "import" is
                        supported)
  target                (import only) file to upload

optional arguments:
  -h, --help            show this help message and exit
  --replace XXXX-XXXX   Socrata view to replace with the uploaded data
  --append XXXX-XXXX    Socrata view to append the uploaded data to
  --blueprint blueprint.json
                        Path to a json document describing column layout for a
                        NEW dataset
  --publish             Operations above will produce a working copy. Use this
                        flag to actually publish
```


History
---------
Socrata-python is dead (or, at least "deprecated"). Long live socratic. 

We are _starting_ with a fork of that deprecated codebase, but it will evolve in ways that break backward compatability. This will NOT be a drop-in replacement for socrata-python! 

Thanks to Aiden Scandella and Socrata for getting it this far!


[Socrata Publishing API]: http://dev.socrata.com/publisher/getting-started

Goals
------------------------
* clean up and modernize the library, including adding tests and docs
* more flexible configuration options
* a command-line wrapper for common socrata operations
* Clear seperation between Socrata-proprietary methods and the SODA2 API

