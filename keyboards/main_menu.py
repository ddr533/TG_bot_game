from aiogram import Dispatcher
from aiogram.types import BotCommand


async def set_menu_command(dp: Dispatcher):
    menu_commands = [BotCommand(command='/start', description='Начать новую игру'),
                    BotCommand(command='/help', description='Получить справку'),
                    BotCommand(command='/stat', description='Поcмотреть статистику игр')]
    await dp.bot.set_my_commands(commands=menu_commands)


