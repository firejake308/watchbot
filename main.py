import discord
import os
import asyncio

# 'https://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2025'

if __name__ == '__main__':
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        # TODO
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == 'bot-configuration':
                    print(channel.last_message)
                    await channel.send('hello world')
        await client.close()
        print('closing bot')

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.start(os.environ.get('BOT_TOKEN')))
    except KeyboardInterrupt:
        print('Detected KeyboardInterrupt, canceling remaining tasks')
        loop.run_until_complete(client.close())
        # cancel all tasks lingering
    except discord.errors.Forbidden:
        loop.run_until_complete(client.close())
    finally:
        loop.close()
