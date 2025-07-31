from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELUCJhGiacm9ro5nAJXr_GlzPrpV3UgAACNwIAAkGdiFW9ustLyOBHoiAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I'm Bot For group's voice call. I can Play Music On groups voice Calls.**

__Powered by @anshuplugs__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Source Code •", url="https://github.com/anshuplugs11/telegram")
                  ],[ 
                    InlineKeyboardButton(
                        "• Support Group •", url="https://t.me/dickcutter"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Music Player Is Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/dickcutter")
                ]
            ]
        )
   )

