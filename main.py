import requests
from ics import Calendar
from datetime import date
from typing import List

class Event:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

class EventCalendar:
    def __init__(self, url: str):
        self.url = url
        self.events = self.fetch_events()

    def fetch_events(self) -> List[Event]:
        ical_data = requests.get(self.url).text
        cal = Calendar(ical_data)
        events = []
        for event in cal.events:
            events.append(Event(event.name, event.begin, event.end))
        return events

    def get_events_on_date(self, target_date: date) -> List[Event]:
        return [event for event in self.events if event.start.date() == target_date]

def main():
    url = "https://urlab.be/events/urlab.ics"
    url2 = "https://calendar.google.com/calendar/ical/classroom116127324412214743868%40group.calendar.google.com/public/basic.ics"

    # Create event calendars
    event_calendar1 = EventCalendar(url)
    event_calendar2 = EventCalendar(url2)

    # Choose a specific date for which you want to see events
    target_date = date.today()  # You can change this to any date
    print(target_date)
    target_date = date(2023, 8, 29)

    # Get events for the chosen date
    events_on_target_date = event_calendar1.get_events_on_date(target_date) + event_calendar2.get_events_on_date(target_date)

    # Display the events for the chosen date
    if events_on_target_date:
        print(f"Events on {target_date}:")
        for event in events_on_target_date:
            print(f"Title: {event.name}")
            print(f"Start Time: {event.start}")
            print(f"End Time: {event.end}")
            print("=" * 30)
    else:
        print(f"No events found on {target_date}.")

if __name__ == "__main__":
    main()
