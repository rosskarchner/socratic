A Socrata publisher written in Python
======================
This library provides a Python interface to the [Socrata Publishing API], and a nifty command line client ('socratic').


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

