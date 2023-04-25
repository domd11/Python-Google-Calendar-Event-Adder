from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import datetime
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'service account json location'
CALENDAR_ID = 'your calendar id' # or the calendar ID of the calendar you want to add the event to

creds = None
try:
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
except HttpError as error:
    print(f'An error occurred: {error}')
    creds = None

service = build('calendar', 'v3', credentials=creds)

event_name = input("Input event name: ")

description = input("Input event description: ")

location = input("Input event location: ")

start_date = input("Input start date here (ex: 4/25/2023 @ 10am): ")

dt_start = datetime.datetime.strptime(start_date, '%m/%d/%Y @ %I%p')
tz_start = pytz.timezone('US/Eastern')
dt_tz_start = tz_start.localize(dt_start)
iso_string_start = dt_tz_start.isoformat()


end_date = input("Input end date here (ex: 4/25/2023 @ 10am): ")

dt_end = datetime.datetime.strptime(end_date, '%m/%d/%Y @ %I%p')
tz_end = pytz.timezone('US/Eastern')
dt_tz_end = tz_end.localize(dt_end)
iso_string_end = dt_tz_end.isoformat()

event = {
  'summary': event_name,
  'location': location,
  'description': description,
  'start': {
    'dateTime': iso_string_start,
    'timeZone': 'America/New_York',
  },
  'end': {
    'dateTime': iso_string_end,
    'timeZone': 'America/New_York',
  },
}


event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
print(f'Event created: {event.get("htmlLink")}')
