import json
from telegram.error import BadRequest as err_badrequest
from telegram import Update
from telegram.ext import (Application, ContextTypes, MessageHandler, filters)

with open('data.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

our_bot_token = config["bot_token"]

async def remove_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This will check if the message matches group status updates and delete it"""
    message = update.message
    if (message.new_chat_members or message.left_chat_member) and message.chat.type in ('supergroup', 'group'):
        print(f"Deleted message ID {message.message_id} from {message.chat.id} at {message.date}")
        try:
            await message.delete()
        except err_badrequest as err:
            print(err)


def main() -> None:
    """Run the bot."""
    try:
        print("Building application...")
        application = Application.builder().token(our_bot_token).build()

        print("Adding remove message handler...")
        application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS | filters.StatusUpdate.LEFT_CHAT_MEMBER, remove_message))

        print("Bot running!")
        application.run_polling()
    except KeyboardInterrupt:
        print("KeyboardInterrupted by user (Ctrl+C)")
        
    print("Bot has been stopped!")


if __name__ == "__main__":
    main()