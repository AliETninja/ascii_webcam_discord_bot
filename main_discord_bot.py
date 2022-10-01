import discord
from discord.ext import commands
from teste4 import ajuste
from array_nova import text_turner
import time
import cv2
import os

bot = commands.Bot("!")

@bot.event
async  def on_ready():
    print(f'ready')

#com cache
# @bot.command(name='wc')
# async def test(ctx):
#     message = await ctx.send(send[0])
#     try:
#         reff_pick = 18
#         webcam = cv2.VideoCapture(0)
#         if webcam.isOpened():
#             validacao, frame = webcam.read()
#             while validacao:
#                 validacao, frame = webcam.read()
#                 reff_pick += 1
#                 cv2.imwrite('F:\code\discord_bot\cache_interno\img{}.jpg'.format(reff_pick), frame)
#                 bmw = text_turner('F:\code\discord_bot\cache_interno\img{}.jpg'.format(reff_pick))
#                 bmw = ajuste(bmw)
#                 await message.edit(content=bmw)
#                 key = cv2.waitKey(700)
#                 if key == 27:
#                     break
#     except:
#         pass

#sem cache
@bot.command(name='wc')
async def test(ctx):
    message = await ctx.send(send[0])
    try:
        reff_pick = 18
        webcam = cv2.VideoCapture(0)
        if webcam.isOpened():
            validacao, frame = webcam.read()
            while validacao:
                validacao, frame = webcam.read()
                reff_pick += 1
                cv2.imwrite('C:\your_directory\img1.jpg', frame) # some folder in your computer
                bmw = text_turner('C:\your_directory\img1.jpg')
                bmw = ajuste(bmw)
                await message.edit(content=bmw)
                os.remove(r'C:\your_directory\img1.jpg')
                key = cv2.waitKey(700)
                if key == 27:
                    break

    except:
        pass

bot.run('--your_bot_token_here--')

