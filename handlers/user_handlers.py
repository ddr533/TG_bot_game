from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import keyboard_start, keyboard_game
from services.services import get_bot_choice, get_winner



def push_user_handlers(dp: Dispatcher, user_dict: dict):
    # Этот хэндлер срабатывает на команду /start
    @dp.message_handler(commands=['start'])
    async def process_start_command(message: Message):
        user_id = message.from_user.id
        if user_id not in user_dict:
            user_dict.setdefault(user_id, {'total_games': 0, 'total_wins': 0, 'nobody_wins': 0})
        await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard_start)

    # Этот хэндлер срабатывает на команду /help
    @dp.message_handler(commands=['help'])
    async def process_help_command(message: Message):
        await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboard_start)

    # Этот хэндлер срабатывает на команду /stat
    @dp.message_handler(commands=['stat'])
    async def get_stat(message: Message):
        user_id = message.from_user.id
        await message.answer(
            text=f'Всего игр: {user_dict[user_id]["total_games"]}\nКоличество побед: {user_dict[user_id]["total_wins"]}\n'
                 f'Ничьих: {user_dict[user_id]["nobody_wins"]}')

    # Этот хэндлер срабатывает на согласие пользователя играть в игру
    @dp.message_handler(Text(equals=[LEXICON_RU['yes_button']], ignore_case=True))
    async def process_yes_answer(message: Message):
        user_id = message.from_user.id
        user_dict[user_id]['total_games'] += 1
        await message.answer(text=LEXICON_RU['yes'], reply_markup=keyboard_game)

    # Этот хэндлер срабатывает на отказ пользователя играть в игру
    @dp.message_handler(Text(equals=[LEXICON_RU['no_button']], ignore_case=True))
    async def process_no_answer(message: Message):
        await message.answer(text=LEXICON_RU['no'])

    # Этот хэндлер срабатывает на любую из игровых кнопок
    @dp.message_handler(Text(equals=[LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']], ignore_case=True))
    async def process_game_button(message: Message):
        user_id = message.from_user.id
        bot_choice = get_bot_choice()
        await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')
        winner = get_winner(message.text, bot_choice)
        await message.answer(text=LEXICON_RU[winner], reply_markup=keyboard_start)
        user_dict[user_id]['total_wins'] += 1 if winner == 'user_won' else 0
        user_dict[user_id]['nobody_wins'] +=1 if winner == 'nobody_won' else 0
