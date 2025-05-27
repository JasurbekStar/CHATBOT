import asyncio
import logging
import sys,os
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("API")
dp = Dispatcher()

def Chat(A:str):
    client = OpenAI(
        base_url="https://api.langdock.com/openai/eu/v1",
        api_key="sk-DLIFylwSaEclxUoZ-KO-TVH5lbCU4PpZVqbPgHdlmaf5A5EMcmKw5vNHaALWu8NxU4JojgMN3Rp5D3A5G2_ERg"
    )
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": A}
        ]
    )

    return (completion.choices[0].message.content)

@dp.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer(f"Assalomu allekum, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def message(message: Message):
    try:
        await message.answer(Chat(message.text))
    except:
        await message.answer("Bu mavzu yo`q❌, boshqa yozing❗")


async def main():
    bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

