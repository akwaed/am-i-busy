# Requires ics to work!!
import requests
from ics import Calendar
from datetime import datetime

def is_user_busy(webcal_link):
    try:
        # Fetch iCalendar data from the webcal link
        response = requests.get(webcal_link)
        response.raise_for_status()

        # Parse the iCalendar data
        cal = Calendar(response.text)

        # Get current datetime
        now = datetime.now()

        # Check if the user is currently busy
        for event in cal.events:
            if event.begin <= now <= event.end:
                return True

        return False

    except Exception as e:
        print("An error occurred:", e)
        return False

def main():
    webcal_link = 'https://p123-caldav.icloud.com/published/2/ODA1MDc3NzgyODA1MDc3N84UnVcJslljZ5hZAAslbSfdaG5rUr-dr0AOaue246bmeiYj3ffRxtW3CZhOloHeGEnqRv3s4hMJMaetp-IreMo'
    busy = is_user_busy(webcal_link)

    if busy:
        print("User is currently busy.")
    else:
        print("User is currently not busy.")

if __name__ == "__main__":
    main()
