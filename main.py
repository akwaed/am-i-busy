import requests
from ics import Calendar
from datetime import datetime, date

# URL of the iCal feed
ical_url = "https://uk.instructure.com/feeds/calendars/user_M8AICdwjOhquql0ZIleTQblvXr5UOrAztDCed5oK.ics"
ical_url2 = "webcal://p123-caldav.icloud.com/published/2/ODA1MDc3NzgyODA1MDc3N84UnVcJslljZ5hZAAslbSfdaG5rUr-dr0AOaue246bmeiYj3ffRxtW3CZhOloHeGEnqRv3s4hMJMaetp-IreMo"
# Get the iCal data from the URL
response = requests.get(ical_url2)
ical_data = response.text

# Parse the iCal data
cal = Calendar(ical_data)

# Choose a specific date for which you want to see events
target_date = date.today()  # You can change this to any date

# Filter events for the chosen date
events_on_target_date = [event for event in cal.events if event.begin.date() == target_date]

# Display the events for the chosen date
if events_on_target_date:
    print(f"Events on {target_date}:")
    for event in events_on_target_date:
        print(f"Title: {event.name}")
        print(f"Start Time: {event.begin}")
        print(f"End Time: {event.end}")
        print("=" * 30)
else:
    print(f"No events found on {target_date}.")
