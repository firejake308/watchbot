import discord
import os

if __name__ == '__main__':
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        # TODO
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == 'admin-chat':
                    channel.

    client.run(os.environ.get('BOT_TOKEN'))
