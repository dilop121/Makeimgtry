
import requests

from AdisaX import pbot
from pyrogram import filters


@pbot.on_message(filters.command("loveshayri"))

async def love_shayri(b,m):
    "dont remove this line \n credit  |n github : dilop"
    love = requests.get("https://mukesh-api.vercel.app/loveshayri").json()["results"]    
    await m.reply_text(love)
          
@pbot.on_message(filters.command("hateshayri"))
async def hate_shayri(b,m):
    "dont remove this line \n credit  |n github : dilop"
    hate= requests.get("https://mukesh-api.vercel.app/hateshayri").json()["results"]    
    await m.reply_text(hate)          
__mod_name__="​​Sʜᴀʏʀɪ"
__help__="""ꜱᴇɴᴅ ʀᴀɴᴅᴏᴍ ꜱʜᴀʏʀɪ
❍ /loveshayri : ʟᴏᴠᴇ ꜱʜᴀʏʀɪ
❍ /hateshayri : ʜᴀᴛᴇ ꜱʜᴀʏʀɪ"""
