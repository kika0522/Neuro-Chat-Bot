import pandas as pd
from datetime import datetime
import re


def get_chat_dataframe(file):
    data = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n\n\n')

        for line in lines:
            try:
                username_message = line.split('—')[1:]
                username_message = '—'.join(username_message).strip()

                username, channel, message = re.search(
                        ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
                ).groups()

                print(f"{username}: {message}")
            except Exception:
                pass

    return pd.DataFrame().from_records(data)
df = get_chat_dataframe('chat.log')