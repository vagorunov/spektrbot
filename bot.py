from __future__ import print_function
import telebot
import pyowm

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']



bot = telebot.TeleBot("971546843:AAERjgQEMuzu8jQhTlfY5TheTzFmqgLyCJU")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    # place = input('What city?\n')
    place = 'Novosibirsk'
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    answer = "В городе " + place + " сейчас " + w.get_detailed_status() + ', температура ' + str(temp) + '°C' + '\n'

    if temp < 10:
        answer += 'Сейчас холодно одевайся теплее' + '\n'
    elif temp < 20:
        answer += 'Сейчас тепло зачем лишняя одежда?' + '\n'

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        CALENDAR_ID = 'tami5g20oecqipekok4f33eorg@group.calendar.google.com'
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
     #   print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        answer += 'Список мероприятий СПЕКТРА:' + '\n'
        if not events:
            answer += 'Событий к сожалению нет'+ '\n'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            answer +=  start + ' ' + event['summary'] + ' ' + event['description'] + '\n'

        bot.send_message(message.char.id, answer)
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
bot.polling( none_stop=True)

