# Instagram to Telegram Media Copier

![Project Logo](https://independent.ng/wp-content/uploads/2017/12/Telegram-and-Instagram.jpg)


This is a Python script that copies new media from an Instagram account to a Telegram chat using the Telegram Bot API. 

## Requirements

- Python 3.x
- Telegram bot token 
- Telegram chat ID
- Instaloader (`pip install instaloader`)
- Requests (`pip install requests`)

## Usage

1. Clone this repository

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add your Telegram bot token and Telegram chat ID to the `.env` file

4. Run `sender.py` to start the bot:

```
python sender.py
```

The script will monitor the `./{INSTA_USERNAME}` folder for new media files from the Instagram account and send them to Telegram automatically.

`bot.py` contains the Instaloader logic to download new posts from a specified Instagram account. This runs on a loop to continually check for new media.

Media types supported:

- Images (JPG, PNG)
- Videos (MP4)
- Image captions (scraped from JSON metadata)

New media is detected based on file modified time, so only newly downloaded files within the last 5 minutes will be sent.

## Customization

- Change the Instagram account username in `bot.py`
- Adjust the time interval for detecting new files in `sender.py`

## License

This project is open source - Feel free to use it :)