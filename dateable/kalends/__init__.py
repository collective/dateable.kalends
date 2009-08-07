from zope.interface import Interface, Attribute

class IEventProvider(Interface):
    """An IEventProvider provides events to the client.
    """
    
    # XXX The **kw used to be a SearchCriteria object. Discuss which is better.
    def getEvents(start, stop, **kw):
        """Get all events.
        """

    # XXX The **kw used to be a SearchCriteria object. Discuss which is better.
    def getOccurrences(start, stop, **kw):
        """Get all occurrences of event in period. Period must be bounded.
        """

    def getEventsInDay(date):
        """Get all events on a day, indicated by date.
        """

    def getOccurrenceURI(occurrence):
        """Returns the URI or URL for the event or occurrence"""


class IWebEventCreator(Interface):
    
    def url(start=None, stop=None):
        """Returns a url to a page that can create an event.
        
        Optional start and stop times to pre-fill start and end of event.
        """
        
    def typeTitle():
        """Returns the type name of the event type created"""
        
    def canCreate():
        """Test to know if the current user can create events"""
    
        

class IOccurrence(Interface):
    """An occurrence on a calendar. This stands in for a real event."""

    unique_id = Attribute("The unique ID of the event.")

    start = Attribute("Date and time when this event starts.")
    
    end = Attribute("Date and time when this event ends.")

    title = Attribute("The title of the event.")

    description = Attribute("A description of the event.")

class ITimezoned(Interface):

    timezone = Attribute("""The timezone the event occurs in.
                            May be none for timezone naive objects.""")
    
class IRecurring(Interface):
    
    recurrence_rule = Attribute("""A dateutil.rrule for the recurrence""")

class ITimezonedOccurrence(IOccurrence, ITimezoned):
    pass

class ITimezonedRecurringEvent(IOccurrence, ITimezoned, IRecurring):
    pass
