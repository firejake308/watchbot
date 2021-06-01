from fetch_last_webpage import fetch_last_webpage, mydb, save_new_version
from fetch_current_webpage import fetch_current_webpage
import discord
import os
import asyncio

URL_TO_FETCH = 'https://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2025'

if __name__ == '__main__':
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        # TODO
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == 'bot-configuration':
                    curr = fetch_current_webpage(URL_TO_FETCH)
                    save_new_version(curr)
                    prev = fetch_last_webpage()
                    print(len(curr), len(prev))
                    # await channel.send('hello world')
        await client.close()
        print('closing bot')

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.start(os.environ.get('BOT_TOKEN')))
    except KeyboardInterrupt:
        print('Detected KeyboardInterrupt, canceling remaining tasks')
        loop.run_until_complete(client.close())
        # cancel all tasks lingering
    except Exception:
        loop.run_until_complete(client.close())
    finally:
        loop.close()
        mydb.close()
