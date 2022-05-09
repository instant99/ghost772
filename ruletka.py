# utils.answer(message) - message обязательный аргумент в utils.answer
# strings - выводится когда в юзер-боте стоит английский язык
# strings_ru - выводится когда в юзер-боте стоит русский язык
# self.strings("строка") - вывод strings, strings_ru
# asyncio.sleep(время) - остановка команды на определенное время
# sleep - остановка всего юзер-бота(не советую использовать)
# Получение аргументов после команды - args = utils.get_args_raw(message)

from .. import loader, utils
from telethon.tl.types import Message
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.types import Message
import random
import time
# scope: meta developer: @imloveonegirl

@loader.tds
class RuletkaMod(loader.Module):
    """сыграть в русскую рулетку"""
    # Английские strings
    strings = {
    "name": "Ruletka",
    "killed": "❗ You died",
    "alive": "✔ You survived"
    }

    # Русские strings
    strings_ru = {
    "killed": "❗ Ты умер",
    "alive": "✔ Ты выжил"
    }

    async def igratcmd(self, message: Message) -> None:
        args = utils.get_args_raw(message)
        rand = random.randrange(0, 7)
        if int(args) == int(rand):
            await utils.answer(message, self.strings("killed"))
            await asyncio.sleep(3)
            await message.client(LeaveChannelRequest(message.chat_id))
        else :
            await utils.answer(message, self.strings("alive"))