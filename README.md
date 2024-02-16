# Netflix News and Releases Discord Bot

## Description

This Discord bot is designed to keep your server updated with the latest Netflix news, releases, and top 10 rankings. It fetches updates from Netflix's official sources and posts them in designated channels within your Discord server. With this bot, ensure your community is always in the loop about the newest shows, movies, and more.

## Setup

### Requirements

- Python 3.6 or newer
- `discord.py` library
- `requests` library
- A Discord Bot Token ([How to get a Discord Bot Token](https://discordpy.readthedocs.io/en/stable/discord.html))
- An SQLite database (`database.sqlite`) setup with the necessary tables

### Installation

1. Clone this repository or download the bot code.
2. Install required Python libraries:
   ```bash pip install discord.py requests```
3. Create a config.json file in the same directory as the bot code with the following structure:
```
{
  "token": "YOUR_DISCORD_BOT_TOKEN",
  "newsRoom": "NEWS_CHANNEL_ID",
  "releaseRoom": "RELEASES_CHANNEL_ID",
  "top10": "TOP10_CHANNEL_ID"
}
```
4. Adjust the SQLite database setup as per your needs.

## Running the Bot
Execute the bot script with Python:
```python bot_script_name.py```

## Features
News Room: The bot fetches and posts the latest Netflix news articles to a designated Discord channel.
New Releases: It also tracks new Netflix releases, including movies, series, and specials, and shares them in another channel.
Top 10 Rankings: Get daily updates on the top 10 Netflix movies and series in your server.

## Commands
!start: Activates the bot to start monitoring and posting updates.

## Configuration
Ensure you have the correct channel IDs in your config.json file for the bot to function properly. The SQLite database should also be set up with tables corresponding to the features: newsRoom, NewReleases, and top10.

## Contributing
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.
