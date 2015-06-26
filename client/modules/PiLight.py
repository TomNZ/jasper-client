# -*- coding: utf-8-*-
import re
import urllib
import requests

WORDS = ["LIGHT", "LIGHTS"]


def handle(text, mic, profile):
    """
    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    # Super simple for now
    if 'off' in text:
        mic.say('Turning off the lights.')
        requests.post('http://snorkelpi.local:8000/driver/stop')

    elif 'on' in text:
        mic.say('Turning on the lights.')
        requests.post('http://snorkelpi.local:8000/driver/start')


def isValid(text):
    return bool(re.search(r'^lights?\b(on|off)\b', text, re.IGNORECASE))


