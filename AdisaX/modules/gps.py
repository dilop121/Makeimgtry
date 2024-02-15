from pyrogram import  enums, filters, idle
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from requests import get
import asyncio
from AdisaX import pbot as adisa
from pyrogram.handlers import MessageHandler
from geopy.geocoders import Nominatim
from geopy.distance import great_circle


@adisa.on_message(filters.command(["gps"]))
async def gps(bot, message):
#     await message.delete()
    if len(message.command) < 2:
        return await message.reply_text(
            "**Example:**\n\n`/gps [latitude , longitude]`")
    x = message.text.split(' ')[1].split(',')
   

    try:
        geolocator = Nominatim(user_agent="adisa")
#         zoom=[0-18]


        location = geolocator.reverse(x,addressdetails=True, zoom=18)
        address=location.raw['address'] 
        # Traverse the data
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        latitude = location.latitude
        longitude = location.longitude
        url=[

            [IKB

             ("Open with:🌏ɢᴏᴏɢʟᴇ ᴍᴀᴘs ",url=f"https://www.google.com/maps/search/{latitude},{longitude}")

            ]

            ]

    #     await message.reply_text(f"{gm}")
        await message.reply_venue(latitude, longitude,f"{city}",f"{state} ,{country}",reply_markup=IKM(url))
    except Exception as e:
        await message.reply_text(f"I can't find that \nDue to {e}")
@adisa.on_message(filters.command(["distance"]))
async def distance(bot, message):
    await message.delete()
    if len(message.command) < 2:
        return await message.reply_text(
            "**Example:**\n\n`/distance [latitude , longitude],[latitude , longitude]`")

    x = message.text.split(" ")[1].split(',',2)[0:2]
    y = message.text.split(" ")[1].split(',',4)[2:4]

    


    try:
        distance=(great_circle(x,y).miles)

        await message.reply_text(f"Total distance between {x[0]},{x[1]} and {y[0]},{y[1]} is {distance}")
        
    except Exception as e:
        await message.reply_text(f"I can't find that \nDue to {e}")
        

__help__ = """
sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ...

 ❍ /gps <ʟᴏᴄᴀᴛɪᴏɴ>*:* ɢᴇᴛ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ.
 ❍ /distance  to measure distance 
"""

__mod_name__ = "Gᴘs"