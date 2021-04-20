import requests

url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

querystring = {"langpair": "ru|en", "q": "стакан!", "mt": "1", "onlyprivate": "0", "de": "a@b.c"}

headers = {
    'x-rapidapi-key': "ff62ce869dmsh19d414c170f39aep18e37ajsn5ee33a675609",
    'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

print(response['responseData']['translatedText'])
