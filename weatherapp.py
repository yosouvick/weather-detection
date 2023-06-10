import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city=input("Enter the name of te city:")
url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r=requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])
str=wdic["current"]["temp_c"]
text = f"The current temprature at {city} is {str} degree celcius"
speak.Speak(text)
