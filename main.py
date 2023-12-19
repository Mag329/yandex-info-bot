from telebot.async_telebot import AsyncTeleBot
import asyncio
import info


token = 'SECRET'
bot = AsyncTeleBot(token)


@bot.message_handler(content_types=['text'])
async def main_handler(message):
    if message.text.lower() == '/start':
        await start_message(message)

    elif message.text.lower() == '/help':
        await help_message(message)
    
    elif message.text.lower() == '/info':
        await info_message(message)
        
    elif message.text.lower() == '/photos':
        await photo_message(message)
    
    else:
        await other_message(message)


# /start
async def start_message(message):
    await bot.send_message(message.chat.id, info.start_message())
    
    
# /help
async def help_message(message):
    await bot.send_message(message.chat.id, info.commands_list())
    

# /info
async def info_message(message):
    await bot.send_message(message.chat.id, info.info())
    
# /photos
async def photo_message(message):    
    for photo in info.photos:
        await bot.send_photo(message.chat.id, photo)


# for incorrect messages
# Была идея нейронку подключить, но в последней версии g4f что-то сломали, и поэтому в этот раз без нейронок
async def other_message(message):
    await bot.send_message(message.chat.id, info.random_message())


asyncio.run(bot.polling())