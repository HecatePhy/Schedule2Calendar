import sys

from EventCrawler import *
from CalendarWriter import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] No url provided")
        exit(1)
    url = sys.argv[1]
    event_list = eventCrawler(url, parse_dodgers_2025_schedule)
    writeCalendar(event_list)
