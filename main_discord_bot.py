import discord
from discord.ext import commands
from teste4 import ajuste
from array_nova import text_turner
import time
import cv2
import os

send = []
for c in range(19, 75):
    bmw = text_turner('C:\poar mano\discord_web_cam\cache_img\img{}.jpg'.format(c))
    send.append(ajuste(bmw))

here_value = text_turner('C:\poar mano\discord_web_cam\cache_img\img19.jpg')
fixed = ajuste(here_value)

bot = commands.Bot("!")

@bot.event
async  def on_ready():
    print(f'estou pronto !!')


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    time.sleep(3)

    response = "ola, " + name

    await ctx.send(response)

@bot.command(name='onwc')
async def web_cam(ctx):

    response = fixed

    await ctx.send(response)

# @bot.command(name='wc')
# async def test(ctx):
#     message = await ctx.send(send[0])
#     try:
#       for c in range(len(send) - 1):
#           await message.edit(content=send[c])
#           # time.sleep(0.80)
#     except:
#         pass


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
                cv2.imwrite('F:\code\discord_bot\cache_interno\img1.jpg', frame) # some folder in your computer
                bmw = text_turner('F:\code\discord_bot\cache_interno\img1.jpg')
                bmw = ajuste(bmw)
                await message.edit(content=bmw)
                os.remove(r'F:\code\discord_bot\cache_interno\img1.jpg')
                key = cv2.waitKey(700)
                if key == 27:
                    break

    except:
        pass

bot.run('--your_bot_token_here--')

