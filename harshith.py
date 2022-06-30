# Created By Mutyala Harshith
# Don't Sell Source Code For Being Money
# Read The License ✓ https://github.com/MutyalaHarshith/JoiNHidER/main/license
# Fork & give Star to me
# Don't Change The Code and Text on your wish

import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")
bot = Client(
        "hide",
        bot_token=BOT_TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )


@bot.on_message(filters.new_chat_members)
async def welcome(bot,message):
	await message.delete()	
	
@bot.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	await message.delete()	


	
bot.run()
