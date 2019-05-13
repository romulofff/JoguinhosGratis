'''
This Telegram Bot was developed to send Game Deals to a Telegram Channel
The deals are retrieved from subreddit r/gamedeals

Only deals over 60% discount is shared.

Developed by: Rômulo Férrer Filho
Github: github.com/romulofff
Telegram: @Romulofff
'''

#! python3
# |\
import praw
import telegram 
import os
import re
client_id = os.environ['id']
client_secret = os.environ['secret']
user_agent = os.environ['agent']
username = os.environ['username']
password = os.environ['password']
telegram_token = os.environ['token']
# Connecting to Telegram Bot
bot = telegram.Bot(token=telegram_token)

# Connecting to Reddit App
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)
subreddit = reddit.subreddit("gamedeals")

status = bot.send_message(chat_id="@Testesrfff", text="NOVO TESTE INICIANDO", parse_mode=telegram.ParseMode.HTML)
INDEX = 0
for submission in subreddit.stream.submissions(skip_existing=True):
    
    title = submission.title
    url = submission.url
    msg = ""
    if "%" in title:
        if title[title.find("%")-3:title.find("%")+1] == "100%":
            msg = "*------------ESSE É GRÁTIS------------* \n"
            msg += title + " " + url
            print(INDEX,msg)
            status = bot.send_message(chat_id="@Testesrfff", text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
        elif int(title[title.find("%")-2:title.find("%")]) > 60:
            percent = title.find("%")
            msg += title + " " + url
            print(INDEX,msg)
            status = bot.send_message(chat_id="@Testesrfff", text=msg, parse_mode=telegram.ParseMode.HTML)
    INDEX+=1