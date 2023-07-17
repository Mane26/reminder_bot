# Reminder_bot
```
1. Бот должен быть реализован на языке Python с использованием библиотеки aiogram.
2. Бот должен быть оформлен в виде отдельного модуля или пакета.
3. Бот должен быть устойчив к ошибкам пользователя и корректно обрабатывать исключительные ситуации.
4. Код бота должен быть чистым, асинхронным, хорошо организованным и содержать комментарии, объясняющие логику работы.
5. Бот должен успешно выполнять все описанные функции.
```

### Стэк:
aiogram==2.25.1
aiohttp==3.8.3
aiosignal==1.2.0
anyio==3.7.1
APScheduler==3.6.3
async-cb-rate==1.0.0
async-timeout==4.0.2
attrs==22.1.0
Babel==2.9.1
beautifulsoup4==4.11.0
bs4==0.0.1
cachetools==4.2.2
certifi==2022.6.15
chardet==4.0.0
charset-normalizer==2.1.0
click==8.1.5
colorama==0.4.6
exceptiongroup==1.1.2
fastapi==0.88.0
flake8==3.9.2
flake8-docstrings==1.6.0
frozenlist==1.3.1
h11==0.14.0
idna==2.10
importlib-metadata==4.12.0
iniconfig==2.0.0
isort==5.11.5
lxml==4.9.1
magic-filter==1.0.9
mccabe==0.6.1
multidict==6.0.2
packaging==23.1
pluggy==1.2.0
py==1.11.0
pyaes==1.6.1
pycodestyle==2.7.0
pydantic==1.10.2
pydocstyle==6.3.0
pyflakes==2.3.1
Pyrogram==2.0.106
PySocks==1.7.1
pyTelegramBotAPI==4.12.0
pytest==7.1.3
python-dotenv==0.19.0
python-telegram-bot==13.7
pytz==2022.2.1
redis==4.4.0
requests==2.25.1
six==1.16.0
sniffio==1.3.0
snowballstemmer==2.2.0
soupsieve==2.4.1
starlette==0.22.0
timeloop==1.0.2
tomli==2.0.1
tornado==6.3.2
typing_extensions==4.5.0
tzdata==2023.3
tzlocal==5.0.1
urllib3==1.26.16
uvicorn==0.20.0
yarl==1.8.1
zipp==3.16.2

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Записать в переменные окружения (файл .env) необходимые ключи:
- токен телеграм-бота
- свой ID в телеграме


Запустить проект:

```
python bot.py
```
Работу выполнила Python-разработчик
Саркисян Мелине