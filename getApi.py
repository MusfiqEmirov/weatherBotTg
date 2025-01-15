import requests
import time
from telegram import Update
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
open_weather_token = os.getenv("OPEN_WEATHER_TOKEN")
tg_bot_token = os.getenv("TG_BOT_TOKEN")

def get_weather(city,open_weather_token):

    weather_text = {

        "Clear":"aciq hava\U00002600",
        "Partly cloudy":"qismen buludlu\U00002601",
        "Cloudy":"buludlu\U00002602",
        "Rainy":"yagisli\U00002614",
        "Sunny":"gunesli\U00002600",
        "Windy":"yelledir az maz\U0001F32C",
        "Patchy rain nearby":"hardasa babat leysan gedir\U00002614",
        "Overcast": "Buludlu \U00002601",
        "Drizzle": "ciskili hava  \U00002614",
        "Thunderstorm": "firtina  gedir \U000026A1",
        "Snowy": "babat qar yagir \U00002603",
        "Foggy": "goz gozu gormeyen duman \U000026C5",
        "Mist": "az maz  duman \U0001F32B",
        "Hail": "duzlu qarda varmiw \U0001F4A3",
        "Freezing rain": "Buzlu yagiw \U000026A7",
        "Tornado": "qasirga \U0001F32A",
        "Hot": "isti hava \U00002600",
        "Cold": "Soyuq hava \U00002744",
        "Dust": "Tozlu hava \U0001F32B",
        "Blizzard": "Qar firtinasi \U0001F32A",
        "Squalls": "adam aparan kulek \U0001F32C"
    }

    try:
        r = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={open_weather_token}&q={city}&aqi=no"
        )
        data = r.json()
        city_name = data["location"]["name"]
        city_temprature = data["current"]["temp_c"]
        local_time = data["location"]["localtime"]
        weather_description = data["current"]["condition"]["text"]
        wd = weather_text[weather_description]
        print(
            f"\nSizin seher adi>> {city_name} city\n"
            f"Hal hazirki tempuratur>> {city_temprature} °C\n"
            f"Zonaya aid vaxt>> {local_time}\n"
            f"Hava durumu>> {wd}\n"
        )

    except Exception as ex:
        print(ex)


def main():
    city = input("seheri daxil ele")
    get_weather(city,open_weather_token)

if __name__ == "__main__":
    main()







































# class WeatherAPI:
#     def __init__(self, access_key):
#         self.url = "http://api.weatherapi.com/v1/current.json" # weather.com adligimiz API
#         self.access_key = access_key

#     def get_weather(self,city):
#         response = requests.get(self.url, params={ # parametrleri
#             "key": self.access_key,
#             "q": city,
#             "lang": "AZ"
#         })

#         if response.status_code != 200:
#             print("xeta bas verdi.ERROR CODE:response.status_code")
#             return None
#         return response.json() # eger status codu ugurludsa bise json deyerlrini qaytracaq
        

# class WeatherTranslator:
#     def __init__(self):
#         # API ile avtomatik azeri diiline cevrilmediyi ucun elle yazilib
#         self.translation_dict = {
            
#             "Clear":"aciq hava\U00002600",
#             "Partly cloudy":"qismen buludlu\U00002601",
#             "Cloudy":"buludlu\U00002602",
#             "Rainy":"yagisli\U00002614",
#             "Sunny":"gunesli\U00002600",
#             "Windy":"yelledir az maz\U0001F32C",
#             "Patchy rain nearby":"hardasa babat leysan gedir\U00002614"
#         }        
        
#     def translate_condition(self, condition):
#         return self.translation_dict.get(condition, f"{condition}")
    
# class Weather_add:
#     def __init__(self,acceskey):
#         self.weather_api = WeatherAPI(acceskey)  
#         self.weather_translator = WeatherTranslator()

#     def to_start(self):
#         city = input("Seher daxil edin>>")
#         result = self.weather_api.get_weather(city)

#         if result:
#             city_name = result["location"]["name"]
#             city_temprature = result["current"]["temp_c"]
#             condition_text = result["current"]["condition"]["text"]
#             local_time = result["location"]["localtime"]
#             contion_text_add = self.weather_translator.translate_condition(condition_text)

#             print(f"seher adi:{city_name}")
#             print(f"Hazirki tempuratr:{city_temprature} °C")
#             print(f"Saat:{local_time}")
#             print(f"hava ile bagli werh:{contion_text_add}")

# if __name__ == "__main__":
#     accesskey = "fec541a967a5476f836184125250101"
#     Weather_add = Weather_add(accesskey)
#     Weather_add.to_start()
