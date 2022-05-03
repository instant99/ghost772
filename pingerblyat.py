__version__ = (1,0,0)
#module by:
#█▀ █▄▀ █ █░░ █░░ ▀█ 
#▄█ █░█ █ █▄▄ █▄▄ █▄ 

#█▀▄▀█ █▀▀ █▀█ █░█░█
#█░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
#2022
from .. import loader, utils
from asyncio import sleep
import random
from telethon.tl.types import Message

#meta developer: @skillzmeow
@loader.tds
class PingerBlyaMod(loader.Module):
	strings = {"name": "EbanutiyPinger", "pinger": "<b>⏱ Ping:</b>" }
	strings_ru = {"pinger": "<b>⏱ Пинг:</b>"}
	
	async def pigcmd(self, message:Message) -> None:
	    pidor = self.strings("pinger")
	    pig = random.choice(30, 45000)
	    rofl = random.choice(100, 999)
	    await utils.answer(message, "🐻 Bear with us while ping is checking... ")
	    await sleep (0.5)
	    await utils.answer(message, f"{pidor} {pig}.{rofl} <b>ms</b>")
	