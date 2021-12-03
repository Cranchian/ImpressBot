import json
import random

import requests
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render

from ImpressBot.settings import BOT_TOKEN
from .models import Item

TELEGRAM_URL = "https://api.telegram.org/bot"


# TO SET WEBHOOK
# add Ngrok url in place of <url> and run the entire url in ur browser to set up webhook
# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/joke/

def display(request):
    """
    displays the stats in the browser
    """
    Items = Item.objects.all()
    return render(request, 'index.html', {'Items': Items})


def receive_message(request):
    """
    receive messages from the webhook
    """

    t_data = json.loads(request.body)

    # for callback query's
    if "callback_query" in t_data:
        chatMsg = t_data['callback_query']['data']
        chatId = t_data['callback_query']['from']['id']
        process_message(chatId, chatMsg)
        return JsonResponse({"ok": "POST request processed"})

    chatId = t_data['message']['chat']['id']
    chatMsg = t_data['message']['text']
    process_message(chatId, chatMsg)

    # try:
    #     chatMsg = message["text"].strip().lower()
    # except Exception as e:
    #     return JsonResponse({"ok": "POST request processed"})

    return JsonResponse({"ok": "POST request processed"})



def process_message(chatId, chatMsg):
    """
    process the message:
    counts and stores the user calls in db and sends the appropriate response
    """

    jokes = {
        'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                   """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
        'fat': ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
        'dumb': [
            """Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
            """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
    }

    if Item.objects.filter(cid=chatId).exists():
        if 'fat' == chatMsg:
            Item.objects.filter(cid=chatId).update(fat=F('fat') + 1)
            result_message = random.choice(jokes['fat'])

        elif 'stupid' == chatMsg:
            Item.objects.filter(cid=chatId).update(stupid=F('stupid') + 1)
            result_message = random.choice(jokes['stupid'])

        elif 'dumb' == chatMsg:
            Item.objects.filter(cid=chatId).update(dumb=F('dumb') + 1)
            result_message = random.choice(jokes['dumb'])
        else:
            result_message = "Hello, please choose one of the options for the joke"
    else:
        Item.objects.create(cid=chatId)

    send_message(result_message, chatId)


def send_message(message, chat_id):
    """
    Send message to the bot
    """
    print("activated")
    data = {
        "chat_id": chat_id,
        "text": message,
        "reply_markup": {"inline_keyboard": [
            [
                {
                    "text": "stupid",
                    "callback_data": "stupid"
                },
                {
                    "text": "dumb",
                    "callback_data": "dumb"
                },
                {
                    "text": "fat",
                    "callback_data": "fat"
                }
            ]
        ]
        }
    }
    response = requests.post(
        f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", json=data
    )

    print(response)
