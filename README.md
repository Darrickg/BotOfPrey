# BotOfPrey

Discord bot for the Birds of Prey friend group discord server. Mostly used to learn how to code a discord bot but also used for random things within the server.

## Features

- Fetch Pokémon information using the `!dex [pokemon_name]` command.
- Suggest activities using the `!bored`, `!bored_recreational`, `!bored_social`, and `!imbored [participants]` commands.
- Respond with specific messages when certain phrases are detected.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- A .env file with all the secret ingredients (ask darrick)

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```sh
git clone https://github.com/yourusername/BotOfPrey.git
cd BotOfPrey
```

### 2. Install Dependencies

Install the necessary dependencies listed in `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 3. Run the Bot

Run the bot using the following command:

```sh
python3 main.py
```

### Directory Structure

```
BotOfPrey/
│
├── cogs/
│   ├── pokemon.py
│   ├── bored.py
│   ├── [other random things].py
│
├── data/
│   └── config.json
│
├── .env
├── main.py
├── README.md
├── requirements.txt
```