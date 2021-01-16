# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


import requests


def Weather(city):


    url_api = "http://api.openweathermap.org/data/2.5/weather?appid=fd8d7aee7a3abd2babf88bff433775b8&q="

    url = url_api + city

    data = requests.get(url).json()

    weather_info = data["weather"][0]["main"]  

    imp_data = data["main"]

    temp_min = ( imp_data["temp_min"] - 273 )

    temp_max = (imp_data["temp_max"] - 273)

    msg = "The Weather looks {0} \n The Min. Temperature is {1} \n The Max. Temperature is {2}". format(
        weather_info, temp_min, temp_max)


    return msg


class ActionWeatherInfo(Action):

    def name(self) -> Text:
        return "action_weather_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.latest_message["text"]   # tracker.get_slot("city")

        msg = Weather(city)

        dispatcher.utter_message(text= msg)

        return []
