import twitter
from contextlib import closing
from urllib.request import urlopen
from datetime import date
import json


# FILE OPENING AND JSON GET INFO (modify url if you want to use api, it's meteoconcept)
with closing(urlopen('https://api.meteo-concept.com/api/forecast/daily/0?token=YOURTOKEN&insee=CODEOFYOURCITY')) as f:
    decoded = json.loads(f.read())
    (city, forecast) = (decoded[k] for k in ('city', 'forecast'))


# VARIABLES
today = date.today()
today = today.strftime("%d/%m/%Y")
weather = ""
probarain = f"{forecast['probarain'] } %"
Toulouse = city['name']
current_time = date.today().strftime("%H")


# CONDITIONS WEATHER CODES
if forecast['weather'] == 0:
    weather = "Soleil"
elif forecast['weather'] >= 1 and forecast['weather'] <= 9:
    weather = "Ciel nuageux"
elif forecast['weather'] == 10 or 11:
    weather = "Pluies faibles"
elif forecast['weather'] >= 12 and forecast['weather'] < 20:
    weather = "Pluies fortes"
elif forecast['weather'] >= 20 and forecast['weather'] <= 78:
    weather = "Neiges"
elif forecast['weather'] >= 40 and forecast['weather'] < 104:
    weather = "Averses"
elif forecast['weather'] == 104:
    weather = "Orages"
elif forecast['weather'] >= 105 and forecast['weather'] < 140:
    weather = "Orages forts"
elif forecast['weather'] >= 140 and forecast['weather'] <= 235:
    weather = "Pluies orageuses"
elif forecast['weather'] >= 235:
    weather = "Averses de grêle"


# TWITTER API TO POST STATUS
api = twitter.Api(consumer_key='your consumer key',
                      consumer_secret='your secret key',
                      access_token_key='your token',
                      access_token_secret='your secret token')


print(api.PostUpdate("Bonjour !! Aujourd'hui ({}) \nLa prévision météo de Toulouse est la suivante : {} \navec une probabilité de {} de pluie ! ".format(today, weather, probarain),"https://media4.giphy.com/media/jsm7XMcyeTFJE4vHzO/giphy.gif?cid=790b761193143354e63b153c3b889d7057a8ac63a5774c86&rid=giphy.gif&ct=g"))
