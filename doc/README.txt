Kalends: Python calendaring API
===============================

Introduction
------------
Kalends is a python module using the Component Architecture technologies of
interfaces and adapters to separate the storage and display of calendar events.
The purpose is to provide a generic python API so that any calendar UI can
display calendars coming from any calendar source. The idea of this is to
make it possible to focus efforts on user interfaces onto making good useable
user interfaces, without these people needing to create a good full-featured
Kalendaring product, while letting those who need specific calendaring 
functionality reuse these user-interfaces.

For example, if you have a group-ware system with a good calendaring UI, but 
you need to use an external server for your calendars, you should not need
to rewrite or for the user interface.

A secondary goal is also to provide an API for calendaring to help people
around some of the obstacles you will sooner or later arrive at, like 
how to handle reccurring events, searching and more, by providing them with
an API known to be able to handle the issues.

The two main concepts of this API are event providers, who are the sources
of events, and event users, who takes the Events and displays them or exports
them and similar things. More information on how to use Kalends to make an
EventProvider is in doc/PROVIDING.txt, and more information on how to use
Kalends to get events from an EventProvider is in doc/USING.txt.


Requirements
------------
Although the creation of Kalends was prompted by the desire for having one
set of advanced Kalendaring views available for all calendars in Plone, and 
although the Component Architecture was created by Zope corporation, Kalends
is in no way specific to Plone, Zope or even web applications. It's a Python
module, installable for any Python version (after python 2.3) on any system
that can install the Component Architecture, that is pretty much any Python
system with a C-compiler.

Kalends requires:
- Python 2.3 or later (last version tested: 2.4.3)
- zope.interface 3.2 or later (last version tested: 3.2.2)


Known implementations
---------------------
Currently the Dateable (https://svn.plone.org/svn/collective/dateable/)
module set is using Kalends. It contains chronos, a set of views for Zope that 
implements a Kalends UI, and Plone4ArtistCalendar, a Plone product that makes
Plone folders into event providers.
