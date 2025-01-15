# burdaki setrlerdeki reyler gelecekde istifade etdikde anlaya bilmeyim ucundur

from aiogram import Bot, Dispatcher, types  # telegram bot kitabxanasidir
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F
import requests
from dotenv import load_dotenv # .env faylini oxumag ucundur
import os

load_dotenv() # kitabxansai yuklenir
open_weather_token = os.getenv("OPEN_WEATHER_TOKEN")
tg_bot_token = os.getenv("TG_BOT_TOKEN") # dotenve elave olunan env fayli cagirlir

bot = Bot(token=tg_bot_token)
dp = Dispatcher() # bot ve onun dospaceti ise salinir

@dp.message(Command("start","help")) # esas baslangic komandalar ucun
async def beginning(message: types.Message):
    await message.reply("Salam Ekologiya ve tebii servteler nazirliyiniz millihidrometallurgiya departamentinin verdiyi meluamatlara gore bir seher secin))")

@dp.message()
async def get_weather(message: types.Message):
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
        r = requests.get( # Api ile elaqe qururuq
            f"http://api.weatherapi.com/v1/current.json?key={open_weather_token}&q={message.text}&aqi=no"
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

        await message.reply(
            f"\nSizin seher adi>> {city_name} city\n"
            f"Hal hazirki tempuratur>> {city_temprature} °C\n"
            f"Zonaya aid vaxt>> {local_time}\n"
            f"Hava durumu>> {wd}\n"
        )
    except: # eger Apide prablem yaranarsa status kodunun bize verecek
        await message.reply("xeta bas verdi.ERROR CODE:response.status_code")

async def on_start():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(on_start())
