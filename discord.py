@client.event
async def on_message(message):

    if message.content.lower().startswith("!lol"):
        embed1 =discord.Embed(
            title="Escolha seu Elo!",
            color=COR,
            description="- Unranked = \n"
                        "- Ferro = \n"
                        "- Bronze = 🐤\n"
                        "- Prata  =  📘 \n"
                        "- Ouro  = 📙\n"
                        "- Platina = \n"
                        "- Diamante = "
        ,)
        embed1 =discord.Embed(
            title="Escolha seu Elo!",
            color=COR,
            description="Após completar sua configuração, você irá ganhar acesso aos outros chats.",)

    botmsg = await client.send_message(message.channel, embed=embed1)

    await client.add_reaction(botmsg, "🐤")
    await client.add_reaction(botmsg, "📘")
    await client.add_reaction(botmsg, "📙")


    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🐤" and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "📘" and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "📙" and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🐤" and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "📘" and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "📙" and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

client.run(token)