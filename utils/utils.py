import asyncio
import pickle
import os

def open_dict(file_name):
    try:
        with open(file_name, 'rb') as f:
            user: dict = pickle.load(f)
        return user if isinstance(user, dict) else None
    except FileNotFoundError:
        user: dict = {}
        return user
    except Exception as e:
        print('Словарь прочитан с ошибками', e)


async def dump_dict(user_dict: dict):
    while True:
        print(user_dict)
        with open('data.pickle', 'wb') as f:
            pickle.dump(user_dict, f)
        await asyncio.sleep(10)

