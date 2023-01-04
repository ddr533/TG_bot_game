import asyncio
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers.user_handlers import push_user_handlers
from handlers.other_handlers import push_other_handlers
from utils.utils import open_dict, dump_dict
from keyboards.main_menu import set_menu_command


async def main() -> None:
    '''Функция конфигурирования и запуска бота'''
    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    # считываем словарь со статистикой пользователей из файла
    user_dict: dict = open_dict('data.pickle')

    # запускаем дамп словаря со статистикой пользователей в файл
    asyncio.create_task(dump_dict(user_dict))

    # Создаем список команд в меню
    await set_menu_command(dp)

    # Инициализируем хэндлеры
    push_user_handlers(dp, user_dict)
    push_other_handlers(dp)

    # Запускаем polling
    try:
        await dp.skip_updates()
        await dp.start_polling()

    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit) as e:
        print(e)
