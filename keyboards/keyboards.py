from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon import LEXICON_RU

keyboard_start: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                     one_time_keyboard=True,
                                                     input_field_placeholder='Клавиатура-->')
keyboard_start.add(*(KeyboardButton(text) for text in (LEXICON_RU['yes_button'], LEXICON_RU['no_button'])))

keyboard_game: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                     one_time_keyboard=True,
                                                    input_field_placeholder='Клавиатура-->')
keyboard_game.add(LEXICON_RU['rock']).add(LEXICON_RU['scissors']).add(LEXICON_RU['paper'])