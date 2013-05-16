A Python Client for Socrata
======================

Socrata-python is dead (or, at least "deprecated"). Long live socratic. 

We are _starting_ with a fork of that deprecated codebase, but it will evolve in ways that break backward compatability. This will NOT be a drop-in replacement for socrata-python! 

Thanks to Aiden Scandella and Socrata for getting it this far!

This library provides an interface to the [SODA][] Publisher API. If you're new to all this, you may want to brush up on the [getting started][] guide.

If you're curious about how things work under the hood, you can also browse the [API documentation][] directly.

[soda]: http://dev.socrata.com/
[getting started]: http://dev.socrata.com/publisher/getting-started
[api documentation]: http://opendata.socrata.com/api/docs/

Goals
------------------------
* clean up and modernize the library, including adding tests and docs
* more flexible configuration options
* a command-line wrapper for common socrata operations

