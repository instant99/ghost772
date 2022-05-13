from .. import loader
from asyncio import sleep

class CumMod(loader.Module):
 strings = {"name": "Smile"}
 
 async def cumcmd(self, message):
  for _ in range(10):
   await message.edit("👉         👊")
   await sleep(0.3)
   await message.edit("👉        👊")
   await sleep(0.3)
   await message.edit("👉       👊")
   await sleep(0.3)
   await message.edit("👉      👊")
   await sleep(0.3)
   await message.edit("👉     👊")
   await sleep(0.3)
   await message.edit("👉    👊")
   await sleep(0.3)
   await message.edit("👉   👊")
   await sleep(0.3)
   await message.edit("👉  👊")
   await sleep(0.3)
   await message.edit("👉 👊")
   await sleep(0.3)
   await message.edit("👉👊")
   await sleep(0.3)
   await message.edit("👉👊💦")
   return
