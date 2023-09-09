import requests

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"Python developer in Texas, USA","page":"1","num_pages":"1"}

headers = {
	"X-RapidAPI-Key": "694f0fe02dmsh7051194a1a288f7p129e8djsnaf598d58405a",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())