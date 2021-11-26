import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
#from parcer import get_habr_posts
from celery_settings import app


TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

min_now = datetime.datetime.now().strftime("%M")


# @dp.message_handler(content_types=['text'])
# async def get_text_messages(msg: types.Message):
#     while min_now != 00:
#         for article_dict in get_habr_posts():
#             print(article_dict['title'])
#             full_article = f'{article_dict["title"]} ' \
#                            f'\n ' \
#                            f'\n ' \
#                            f'{article_dict["description"][0]}' \
#                            f'\n ' \
#                            f'Ссылка на пост- {article_dict["link"]}'
#
#             await msg.answer(full_article)
#         await msg.answer(f'Количество статей - {str(len(get_habr_posts()))}')


# @dp.message_handler(content_types=['text'])
# async def get_text_messages(msg: types.Message):
#     if msg.text.lower() == 'новости':
#         for article_dict in get_habr_posts():
#             print(article_dict['title'])
#             full_article = f'{article_dict["title"]} ' \
#                            f'\n ' \
#                            f'\n ' \
#                            f'{article_dict["description"][0]}' \
#                            f'\n ' \
#                            f'Ссылка на пост- {article_dict["link"]}'
#
#             await msg.answer(full_article)
#         await msg.answer(f'Количество статей - {str(len(get_habr_posts()))}')


if __name__ == '__main__':
    executor.start_polling(dp)
