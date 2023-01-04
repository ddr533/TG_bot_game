from __future__ import annotations
from environs import Env


class DatabaseConfig:
    def __init__(self, db_name: str, db_host: str, db_user: str, db_psw: str):
        self.db_name = db_name
        self.db_host = db_host
        self.db_user = db_user
        self.db_psw = db_psw


class TgBot:
    def __init__(self, token: str, admin_ids: list[int]):
        self.token = token  # Токен для доступа к телеграм-боту
        self.admin_ids = admin_ids  # Список id администраторов бота


class Config:
    def __init__(self, tg_bot: TgBot, db: DatabaseConfig):
        self.tg_bot = tg_bot
        self.db = db


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int,
                                                  env.list('ADMIN_IDS')))),
                  db=DatabaseConfig(db_name=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_psw=env('DB_PASSWORD')))


__all__ = ['load_config']
