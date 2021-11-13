# ImpressBot
## A telegram bot created for django practical test

## Table of contents
* [Setting Up The Bot](#setting-up-the-bot)
* [Setting Up The Webhook](#setting-up-the-webhook)
* [Setting Up The Django App](#setting-up-the-django-app)
* [Afterword](#afterword)

## Setting Up The Bot
Create a telegram bot by messaging @BotFather in telegram and get the api_key 
add the api_key to settings.py >> BOT_TOKEN

## Setting Up The Webhook
* Download and run Ngrok (since localhost cant be accessed by telegram to send messages) 
* Open Ngrok and use : ngrok http 8000
![Ngrok](https://i.imgur.com/mPbOZYP.png)
* Copy the HTTPS link given by ngrok and replace it with <url> in the below link
* Replace the <token> with your api_key and run this whole link on a browser to setup your webhook
```
https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/joke/
```

## Setting Up The Django App
* Open the project install the requirments from the requirments.txt
* Create a postgres db and link the name, password in the settings.py - DATABASE section
* Use the following commands in console to set up the database
```
py manage.py makemigrations
py manage.py migrate
```
* Now run the whole project by using
```
py manage.py runserver
```

## Afterword
DM through either my discord - #Master Flame#2911 or through my email if you face any errors. Also DM if you want to just screencast and show the project or if you need my
api-key

ALL three steps plus the 2 bonus tasks were covered.
opening the localhost default page should display the stats(all the user calls based on user id) 
![Display Sample](https://i.imgur.com/mGrJykO.png)


The entire project was fun especially due to some time constraints on my side.
I have not completely build it from the github repository that was given because it was way too outdated. Built it from ground up, I did try to just make it using the 
github project but some of the modules are too outdated that the pip refuses to install it. But I did learn a lot from that app to build this one. It was a fun project 
to talk about if I do get the interview.
Thank you
