import asyncio

from aiogram import Bot, Dispatcher

from config.config import Config, load_config
from handlers.user_handlers import push_user_handlers
from handlers.other_handlers import push_other_handlers


# Функция конфигурирования и запуска бота
async def main():
    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    #Инициализируем хэндлеры
    push_user_handlers(dp)
    push_other_handlers(dp)

    # Запускаем polling
    try:
        await dp.skip_updates()
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        # Запускаем функцию main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e:
        print(e)
