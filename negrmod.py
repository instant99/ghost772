from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import requests
import random as r
from asyncio import sleep

logger = logging.getLogger(__name__)


def register(cb):
    cb(NegrMod())
    cb(NonegrMod())

n = ['Я не негр, и вам не советую!', 'Щас бы негра сюда.. Эх..', 'Я никогда ночью не видел негров.. Интересно почему?🤔', 'Едет дальнобойщик. Уже на улице темно.. Едет, и как вдруг что-то гупнуло по фуре спепеду. Это был негр. \nОн остановил транспорт и вышел, но там никого не было, он удивился, и поехал дальше','У меня есть друг негр, так вот, я часто его теряю когда на улице потемнеет😂','Ооо, а что если написать модуль или бота, который будет работать как антиараб только **АНТИНЕГР**','Какой хлеб едят негры? Черный😂🤔','Какой кофе пьют негры? Чёрный😂🤔']
nn = ['Нету больше негра, всё, забудь','NEGR ITʼS BAD GOOD', 'Ау, где вы негра дели сука','Где майо ниггер? 😭', 'Мама негра что вы мне на др подарили, УКРАЛИ СУКА', 'Активирован анти негр мод, прячьтесь сучки, УХАХА', 'Продам негра (на литовский номерах)']
my_ad = ['@xyeta_mems', '@LOG_DEV']

@loader.tds
class NegrMod(loader.Module):
    """Мемасики"""

    strings = {"name": "negrmod"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def negrcmd(self, message):
        """.negr <код>"""
        rand_ad = r.choice(my_ad) 
        code = int(message.text.replace('.negr ', '')) 
        your_code = int(message.sender_id*2-5) 
        if code == None:
            await message.edit("Введите (.negr <код>\n<i>Ну а если ты, ещё не догадался какой код, то напиши:</i> @LOGDEV") 
        else:
            if code != your_code:
                await message.edit("<b>Не верный код доступа!</b>")
            else:
                await message.edit(f"<b>МЕМЫ против негров чек.</b>\nПодписку - {rand_ad}❤️") 
                await sleep(1)
                await message.edit(r.choice(n))