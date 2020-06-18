import requests
gamertag = input('what is your gamer tag ')

url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/"  + gamertag[:gamertag.find('#')] + '%2523' + gamertag[gamertag.find('#')+1:] + "/battle"
print(url)

headers = {
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    'x-rapidapi-key': "9bff173d48msh533ff8d9d5169efp12a7d7jsn48691a065575"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)