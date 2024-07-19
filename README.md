# RemoveJoinLeaveMsg for Telegram
This is a python-telegram-bot that deletes user join/leave/invite messages in a group.

# How it works

This bot will delete messages that are automatically sent by Telegram when a user joins or leaves the chat or if the user has been added or kicked from the group. 

Nothing special tbh.
There's also a similar bot already running for free made by [@Bot442](https://t.me/Bot442) named [RemoveJoinGroupMsgBot](https://t.me/RemoveJoinGroupMsgBot)

# Installation

You can run this bot on your own, install the required lib by running this command: 

```bash
pip install python-telegram-bot
```

In the `data.json` file you will find the bot_token variable, get your bot's token from the [BotFather](https://telegram.me/botfather) and replace `YOUR_TOKEN_HERE` with your token:

```python
"bot_token": "YOUR_TOKEN_HERE"
```

Now you can simply run the bot by running `main.py`

Make sure the bot has permissions to delete messages!
