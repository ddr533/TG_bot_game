from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU


# Хэндлер для текстовых сообщений, которые не попали в другие хэндлеры
def push_other_handlers(dp: Dispatcher):
    @dp.message_handler(content_types='text')
    async def process_any_msg(message: Message):
        await message.reply(text='Бот не понимает тебя')