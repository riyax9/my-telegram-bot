import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# আপনার BotFather API Token এখানে বসান
BOT_TOKEN = "8807675193:AAElKX_uiGRTezFzKXIFK5S_-KOP1ELs_2M"
# আপনার মিনি অ্যাপের WebApp URL (বা WebApp লিংক)
WEBAPP_URL = "https://ais-dev-ghmeiplktkbuoreu74birv-782579731932.asia-southeast1.run.app"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
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

async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
