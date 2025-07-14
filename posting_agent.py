import schedule # For scheduling tasks
import time # For time management
import asyncio # For asynchronous operations
import logging
import os # To demonstrate using environment variables for API keys (recommended)
import telegram

# --- Configuration ---
# It's highly recommended to use environment variables for sensitive API keys.
# Example: os.environ.get('TELEGRAM_BOT_TOKEN')

# Telegram API credentials
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '7799178734:AAF006-kMQUP6JCXKTbiaUXHxxc1tHgIngQ')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '5887040686') # e.g., '@yourchannelname'

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Social Media Agent Core Logic ---

class SocialMediaAgent:
    def __init__(self):
        self.telegram_bot = None # Initialize to None
        logging.info("SocialMediaAgent initialized.")

    async def setup(self):
        self.telegram_bot = await self._authenticate_telegram_bot()
        if self.telegram_bot:
            logging.info("SocialMediaAgent setup complete for Telegram.")
        else:
            logging.error("SocialMediaAgent setup failed for Telegram.")

    async def _authenticate_telegram_bot(self):
        """Authenticates to the Telegram Bot API."""
        if 'YOUR_TELEGRAM_BOT_TOKEN' in TELEGRAM_BOT_TOKEN:
            logging.warning("Telegram Bot Token is a placeholder. Please set environment variable or update code.")
            return None
        try:
            bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
            logging.info("Successfully authenticated to Telegram Bot API.")
            return bot
        except Exception as e:
            logging.error(f"Error authenticating to Telegram Bot API: {e}")
            return None

    # --- Telegram Integration ---
    async def post_to_telegram(self, message):
        """Posts a message to a Telegram channel."""
        if not self.telegram_bot:
            logging.error("Telegram bot not initialized. Cannot post.")
            return False
        if 'YOUR_TELEGRAM_CHAT_ID' in TELEGRAM_CHAT_ID:
            logging.warning("Telegram Chat ID is a placeholder. Please set environment variable or update code.")
            return False
        try:
            await self.telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
            logging.info(f"Successfully posted to Telegram: '{message}'")
            return True
        except telegram.error.TelegramError as e:
            logging.error(f"Telegram API Error: {e} - Message: '{message}'")
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred while posting to Telegram: {e} - Message: '{message}'")
            return False

    def get_message(self):
        """
        Retrieves the message to be posted.
        """
        return "Welcome to Pauline's channel, how may I help you"

# --- Main Automation Logic ---

async def job():
    """The job to be executed by the scheduler."""
    logging.info("Running scheduled Telegram post job...")
    agent = SocialMediaAgent()
    await agent.setup()
    message_to_post = agent.get_message()

    # Attempt to post to Telegram
    posted_telegram = await agent.post_to_telegram(message_to_post)

    if posted_telegram:
        logging.info("Telegram posting job completed successfully.")
    else:
        logging.warning("Telegram post failed.")

async def main():
    # Prompt user to set environment variables if placeholders are detected
    if 'YOUR_TELEGRAM_BOT_TOKEN' in TELEGRAM_BOT_TOKEN or 'YOUR_TELEGRAM_CHAT_ID' in TELEGRAM_CHAT_ID:
        logging.error("Please set your Telegram API credentials as environment variables.")
        logging.error("Example: export TELEGRAM_BOT_TOKEN='your_token'")
        logging.error("Example: export TELEGRAM_CHAT_ID='@yourchannel'")
        logging.error("Or update the placeholder values directly in the script (not recommended for production).")

    logging.info("Telegram Automation Agent started.")

    # Schedule the job to run every 30 seconds
    schedule.every(30).seconds.do(lambda: asyncio.create_task(job()))
    logging.info("Job scheduled to run every 30 seconds.")

    # Keep the script running to allow the scheduler to work
    while True:
        schedule.run_pending()
        await asyncio.sleep(1) # Wait 1 second before checking again

if __name__ == "__main__":
    asyncio.run(main())
