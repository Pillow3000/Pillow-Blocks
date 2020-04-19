def discordbot_start():
    import discord
    from discord.ext import commands

    client = commands.Bot(command_prefix='.' or '')
    client.remove_command('help')
    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Awaiting Commands'))
        print('Bot is Ready to Role')
        
    @client.command(aliases=['Ping'])
    async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    @client.command()
    async def clear(ctx, amount=6):
        if amount > 50:
            await ctx.send('Delete a smaller amount of messages for the command to run')
        else:
            await ctx.channel.purge(limit=amount)

    client.run('---ENTER TOKEN HERE---')