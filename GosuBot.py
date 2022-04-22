from .. import loader, utils

@loader.tds
class DotaGosuMod(loader.Module):
    strings = {"name": "GosuBot"}

    async def gosucmd(self, message):
        reply = await message.get_reply_message()
        try:
            tralka = await message.client.inline_query('DotaGosuBot', "")
            await message.edit(tralka[1].result.send_message.message)
        except: return await message.edit('<code>Ошибка...</code>')