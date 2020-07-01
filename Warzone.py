import requests
import os
from dotenv import load_dotenv

load_dotenv()

gamertag = input('what is your gamer tag ')

url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/"  + gamertag[:gamertag.find('#')] + '%2523' + gamertag[gamertag.find('#')+1:] + "/battle"
print(url)

headers = {
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    'x-rapidapi-key': os.getenv("API_KEY")
    }

response = requests.request("GET", url, headers=headers)

all_player_info = response.json()

def getKDA():
    kda = all_player_info['br']['kdRatio']
    rounded_kda = round(kda*1000)
    return rounded_kda/1000

print(gamertag + " has a kda of " + str(getKDA()))