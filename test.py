# ---------------------------------------------------------------------------------
#  ,_     _          
#  |\_,-~/          
#  / _  _ |    ,--.  🌐 This module was loaded through https://t.me/hikkamods_bot
# (  @  @ )   / ,-'  🔐 Licensed under the Copyleft license.
#  \  _T_/-._( (     
#  /         `. \    ⚠️ Owner of this bot doesn't take responsibility for any
# |         _  \ |   errors caused by this module or this module being non-working
#  \ \ ,  /      |   and doesn't take ownership of any copyrighted material.
#   || |-_\__   /    
#  ((_/`(____,-'     
# ---------------------------------------------------------------------------------
# Name: RandomCats
# Description: No description
# Author: shadowhikka
# Commands:
# .randcat
# ---------------------------------------------------------------------------------

# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

from .. import loader, utils

from telethon.tl.types import Message

# meta developer: @shadow_modules
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta banner: https://i.imgur.com/OM64rlU.jpeg


@loader.tds
class RandomCatsMod(loader.Module):
    strings = {"name": "RandomCats"}
    memes_bot = "@Kesylkenbot"

    async def on_dlmod(self):
        await utils.dnd(self._client, self.memes_bot, True)

    async def randcatcmd(self, message: Message):
        async with self._client.conversation(self.memes_bot) as conv:
            await conv.send_message("/cat")
            phtmem = await conv.get_response()
            await conv.mark_read()
            await message.delete()
            await utils.answer(message, phtmem)
