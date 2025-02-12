import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7904577369:AAEpsAAWS6RB8ZZpCliInc7bkf-Vi3CfnMQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Категории и ссылки
resources = {
    "YouTube подкасты": [
        {"title": "Qazaqsha Podcast", "url": "https://www.youtube.com/@qazaqshapodcast"},
        {"title": "Bilim Tube", "url": "https://www.youtube.com/@bilimtube"}
    ],
    "TikTok аккаунты": [
        {"title": "Kazakh Talk", "url": "https://www.tiktok.com/@kazaq_talk"},
        {"title": "QazaqStudy", "url": "https://www.tiktok.com/@qazaqstudy"}
    ],
    "Блоги": [
        {"title": "KazLing Blog", "url": "https://kazling.kz"},
        {"title": "Qazaq Grammar", "url": "https://qazaqgrammar.com"}
    ]
}

# Главное меню
def get_main_keyboard():
    buttons = [KeyboardButton(text=category) for category in resources.keys()]
    return ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Выбери интересующий тебя формат:", reply_markup=get_main_keyboard())

@dp.message()
async def send_links(message: Message):
    category = message.text
    if category in resources:
        response = f"📌 Ссылки по категории *{category}*:\n\n"
        for item in resources[category]:
            response += f"🔗 [{item['title']}]({item['url']})\n"
        await message.answer(response, parse_mode="Markdown", disable_web_page_preview=True)
    else:
        await message.answer("Выбери категорию из списка ниже ⬇️", reply_markup=get_main_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
