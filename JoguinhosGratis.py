'''
This Telegram Bot was developed to send Game Deals to a Telegram Channel.
Check t.me/joguinhosgratis
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
import traceback

client_id = os.environ['id']
client_secret = os.environ['secret']
user_agent = os.environ['agent']
username = os.environ['username']
password = os.environ['password']
telegram_token = os.environ['token']

# Connecting to Telegram Bot
bot = telegram.Bot(token=telegram_token)

# Connecting to Reddit App
reddit = praw.Reddit(user_agent=user_agent, client_secret=client_secret, client_id=client_id, username=username, password=password)
subreddit = reddit.subreddit("gamedeals")

status = bot.send_message(chat_id="@Testesrfff", text="It's alive from rasp.", parse_mode=telegram.ParseMode.HTML)

banned_stores = ["reddit.com", "amazon.com", "bestbuy.com", "game.co.uk", "gamebillet.com", "groupees.com", "itch.io"]        

INDEX = 0
while True:
    try:
        for submission in subreddit.stream.submissions(skip_existing=True):
            title = submission.title
            url = submission.url
            msg = ""
            skip = False
            for store in banned_stores:
                if store in submission.url:
                    skip = True
                    break
            if skip:
                continue
            elif "%" in title:
                if title[title.find("%")-3:title.find("%")+1] == "100%":
                    msg = "*-------------- ESSE É GRÁTIS --------------* \n"
                    msg += title + " \n" + url + " #gratis #free"
                    print(INDEX,msg)
                    try:
                        status = bot.send_message(chat_id="@joguinhosgratis", text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
                    except:
                        status = bot.send_message(chat_id="@joguinhosgratis", text=msg, parse_mode=telegram.ParseMode.HTML)
                elif int(title[title.find("%")-2:title.find("%")]) > 60:
                    percent = title.find("%")
                    msg += title + " \n" + url
                    print(INDEX,msg)
                    try:
                        status = bot.send_message(chat_id="@joguinhosgratis", text=msg, parse_mode=telegram.ParseMode.HTML)
                    except:
                        status = bot.send_message(chat_id="@joguinhosgratis", text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
                INDEX+=1
            else: continue

    except (KeyboardInterrupt):
        print("Keyboard Interrupt")
        exit()

    except:
        exec_info = traceback.format_exc()
        try:
            status = bot.send_message(chat_id="@Testesrfff", text=("**Live log:**\n\n{}").format(exec_info), parse_mode=telegram.ParseMode.HTML)
        except:
            status = bot.send_message(chat_id="@Testesrfff", text=("**Live log:**\n\n{}").format(exec_info), parse_mode=telegram.ParseMode.MARKDOWN)
    