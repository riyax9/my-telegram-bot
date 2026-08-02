import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiohttp import web

# Render Environment Variable থেকে টোকেন নেওয়া
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://ais-dev-ghmeiplktkbuoreu74birv-782579731932.asia-southeast1.run.app"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN) if BOT_TOKEN else None
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎬 Open App & Watch Videos", 
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢 Official Telegram Channel", 
                    url="https://t.me/banglavideos99"
                )
            ]
        ]
    )
    
    welcome_text = (
        f"👋 Welcome {user_name} to Mini App Bot!\n\n"
        "• Watch Movies & Anime Streams\n"
        "• Earn Coins & Get Rewards\n"
        "• Instant Binance Pay & USDT Withdrawals\n\n"
        "Click the button below to launch the Mini App!"
    )
    
    await message.answer(welcome_text, reply_markup=keyboard)

# Render Port Health Check Server (Render Web Service Active রাখার জন্য)
async def handle_health_check(request):
    return web.Response(text="Bot is running live!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Web server started on port {port}")

async def main():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN environment variable missing!")
        return
        
    print("Bot is starting...")
    # Render-এর জন্য Web Server চালু
    await start_web_server()
    # টেলিগ্রাম বট Polling চালু
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
