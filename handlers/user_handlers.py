from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import keyboard_start, keyboard_game
from services.services import get_bot_choice, get_winner


def push_user_handlers(dp: Dispatcher):
    # Этот хэндлер срабатывает на команду /start
    @dp.message_handler(commands=['start'])
    async def process_start_command(message: Message):
        await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard_start)

    # Этот хэндлер срабатывает на команду /help
    @dp.message_handler(commands=['help'])
    async def process_help_command(message: Message):
        await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboard_start)

    # Этот хэндлер срабатывает на согласие пользователя играть в игру
    @dp.message_handler(Text(equals=[LEXICON_RU['yes_button']], ignore_case=True))
    async def process_yes_answer(message: Message):
        await message.answer(text=LEXICON_RU['yes'], reply_markup=keyboard_game)

    # Этот хэндлер срабатывает на отказ пользователя играть в игру
    @dp.message_handler(Text(equals=[LEXICON_RU['no_button']], ignore_case=True))
    async def process_no_answer(message: Message):
        await message.answer(text=LEXICON_RU['no'])

    # Этот хэндлер срабатывает на любую из игровых кнопок
    @dp.message_handler(Text(equals=[LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']], ignore_case=True))
    async def process_game_button(message: Message):
        bot_choice = get_bot_choice()
        await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')
        winner = get_winner(message.text, bot_choice)
        await message.answer(text=LEXICON_RU[winner], reply_markup=keyboard_start)
