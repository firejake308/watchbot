from fetch_last_webpage import fetch_last_webpage, mydb, save_new_version
from fetch_current_webpage import fetch_current_webpage
from compare_webpages import compare_webpages
from generate_message import generate_message
import discord
import os
import asyncio
import logging

URL_TO_FETCH = 'http://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2025'

def run_bot():
    curr = fetch_current_webpage(URL_TO_FETCH)
    prev = fetch_last_webpage()
    web_comparison = compare_webpages(prev,curr)
    output = None
    if web_comparison:
        output = generate_message(web_comparison,"BCM 2025")
    save_new_version(curr)
    return output

if __name__ == '__main__':
    client = discord.Client()
    print(run_bot())
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == 'website-changes':
                    output = run_bot()
                    if output:
                        print('changes detected, sending message')
                        await channel.send(output)
                    else:
                        print('No changes')
        await client.close()
        print('closing bot')

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.start(os.environ.get('BOT_TOKEN')))
    except KeyboardInterrupt:
        print('Detected KeyboardInterrupt, canceling remaining tasks')
        loop.run_until_complete(client.close())
        # cancel all tasks lingering
    except Exception as e:
        logging.exception(e)
        loop.run_until_complete(client.close())
    finally:
        loop.close()
        mydb.close()
