from tkinter import *
import requests
import json
from datetime import datetime

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Weather App - AskPython.com')


city_value = StringVar()


def show_weather():
    api_key = 'f2572ec654c9ddead2a46e0d13b5777d'

    city_name = city_value.get()

    weather_url = 'https://openweathermap.org/'

    