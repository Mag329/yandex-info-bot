import random


# Можно было сделать код адаптивным, но мне было лень ¯\_(ツ)_/¯

# data
nick = 'Mag329'
name  = 'н/д'
age = 'н/д'
github = 'https://github.com/Mag329'
langs = 'Python и C#'
exp_py = '4 года'
exp_cs = '1 год'
projects_py = 'Telegram и Discord боты, умный дом с голосовым ассистентом'
projects_cs = 'Игра на unity'


# /start
def start_message():
    text = f'Привет, Я бот, который расскажет о таком разработчике как {nick}\n\nСписок доступных команд: /help'
    return text


# /help
commands  = {
    '/start': 'запустить бота',
    '/help': 'показать это сообщение',
    '/info': f'информация о {nick}',
    '/photos': f'фото {nick}',
}

def commands_list():
    text = ''
    for command, desc in commands.items():
        text += f'{command} - {desc}\n'
    return text

# /info


def info():
    text = f'Ник: {nick}\n'
    text += f'Имя: {name}\n'
    text += f'Возраст: {age}\n'
    text += f'GitHub: {github}\n\n'
    text += f'{langs} разработчик\n\n\n'
    text += f'Опыт разработки на Python - {exp_py}\n'
    text += f'Успешные проекты: {projects_py}\n\n'
    text += f'Опыт разработки на C# - {exp_cs}\n'
    text += f'Успешные проекты: {projects_cs}'
    
    return text
    
    
# /photos
photos = [
    'https://avatars.githubusercontent.com/u/92212582?v=4', 
    'https://cdn.discordapp.com/avatars/508350823592362014/1552281c346a5f8675267cb4770189f9.webp?size=128'
]
    
    
# for incorrect messages
def random_message():
    responses = ['бим бим бам бам', 'I don`t know', 'Please use commands from /help']
    
    index = random.randint(0, len(responses) - 1)
    return responses[index]
