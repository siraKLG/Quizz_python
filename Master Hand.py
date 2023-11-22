import discord 
import asyncio
import random
from discord.ext import commands
from time import sleep
import nest_asyncio 
nest_asyncio.apply()
intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.typing = True


async def longtimer():
  
  global program
  import time
  program = time.time()

async def longtimerdisplay(ctx):
  global secs
  global mins
  global program
  import time
    
  secs = int(time.time() - program)
  hey = secs % 3600
  mins = hey // 60
  secs = hey % 60
  await ctx.send (f"- Quiz terminé en : {mins}:{secs} !")

async def shortimer():
  global shortquestion
  import time
  shortquestion = time.time()
async def shortimerdisplay(ctx):
  global secs
  global mins
  global shortquestion
  import time
    
  secs = int(time.time() - shortquestion)
  hey = secs % 3600
  mins = hey // 60
  secs = hey % 60
  await ctx.send (f"- Temps de réponse : {mins}:{secs} !")
def compteur_points(tries):
  global secs
  global mins
  from random import randint
  global points
  global totalpoints
  #points = viennent du programme
  #tries = viennent du programme
  #totalpoints = vient du programme
  points = tries * 4 * 5
  totalpoints = totalpoints + points

    

async def question_win(ctx):
  global answered
  global mins
  global secs
  await ctx.channel.send("Correct !")
  answered = True
  compteur_points(tries)
  await ctx.send(f"- Répondu en {tries} essais restants, cela vaut : {points} points !\n- Points : {points}")
async def question_lose(ctx):
  global tries
  global answered
  if tries > 0 :
    tries = tries - 1
    await ctx.send(f"Faux ! Réssayez. \nEssais restants : {tries}.")
    await hints(ctx)
  if tries == 0 :
    await ctx.send("Plus d'essais disponibles. Question suivante !")
    tries = tries + 5
    answered = True

#Nous passons à un système de commande.
#Ici le bot initialise les commandes et sera appelé par "!"


bot = commands.Bot(command_prefix="!", intents = intents)
@bot.event
async def on_ready():
    print("Le bot est prêt !")


@bot.command()
#^ Ceci permet au programme de comprendre que c'est une commande invoquable par "!".
async def info(ctx):

#Se lance quand l'utilisateur écrit "!info".
#"ctx" est le "context" et représente comment la commande a été exécutée.

  await ctx.send(ctx.guild)
  await ctx.send(ctx.author)
  await ctx.send(ctx.message.id)


@bot.command()  
async def create_embed(ctx):
  embed=discord.Embed(colour=discord.Colour.red())
  embed.add_field(
    name='Consigne : le but est de repondre au quiz et avoir des points pour chaque bonne reponse.',
    value='bonne chance ,le meilleur gagne !', 
    inline=False)
  await ctx.channel.send(embed=embed)

async def hints(ctx):
  global tries
  if question[0] == 1 and tries == 3:
    await ctx.send(f"Indice :\nSurnom: Le Robot")
  if question[0] == 1 and tries == 1:    #pour le deuxième indice je sais pas quoi mettre c toi qui le connait le mieux medhy
    await ctx.send(f"Indice :\nIl a des lunettes")
  if question[0] == 2 and tries == 3:
    await ctx.send(f"Indice :\nIl fait parti de la team Solary")
  if question[0] == 2 and tries == 1:
    await ctx.send(f"Indice :\nSon perso pète énormément")     #également pour ici sur le gdoc il y a marqué "son perso pète beaucoup" je sais pas si c super en indice
  if question[0] == 3 and tries == 3:
    await ctx.send(f"Indice :\nIl peut se changer en pierre")
  if question[0] == 3 and tries == 1:
    await ctx.send(f"Indice :\nIl a plusieurs sauts")
  if question[0] == 4 and tries == 3:
    await ctx.send(f"Indice :\nUSA")
  if question[0] == 4 and tries == 1:
    await ctx.send(f"Indice :\nJackpot")
  if question[0] == 5 and tries == 3:
    await ctx.send(f"Indice :\nIl a créé Kirby")
  if question[0] == 5 and tries == 1:
    await ctx.send(f"Indice :\nIl est très très actif sur Youtube en ce moment")
  #a partir de la ce sont les questions mp4 donc pas besoin de mettre d'indice enfin c trop compliqué
  if question[0] == 6 and tries == 1 :
    await ctx.send(f"Indice :\nFranchement allez regarder sur google ! Vous nous faites quoi là...")
  if question[0] == 7 and tries == 3:
    await ctx.send(f"Indice :\nEveryone is here !")
  if question[0] == 7 and tries == 1:
    await ctx.send(f"Indice :\nInkling et Smash, ça vous dit quelque chose?")
  if question[0] == 8 and tries == 3:
    await ctx.send(f"Indice :\nEncore joué compétitivement aujourd'hui !")
  if question[0] == 8 and tries == 1:
    await ctx.send(f"Indice :\nWavedash, waveshines...")
  if question[0] == 9 and tries == 3:
    await ctx.send(f"Indice :\nL'émissaire subspatial !")
  if question[0] == 9 and tries == 1:
    await ctx.send(f"Indice :\nL'apparition de la balle Smash...")
  if question[0] == 10 and tries == 3:
    await ctx.send(f"Indice :\nLe commencement...")
  if question[0] == 9 and tries == 1:
    await ctx.send(f"Indice :\n12 personnages.")

@bot.command()
async def smash(ctx):
  global totalpoints
  global points
  global answered
  global tries
  global question
  points = 0
  totalpoints = 0
  tries = 5
  question = [1,2,3,4,5,6,7,8,9,10]
  await longtimer()
  #Notre Liste de questions  
  #           0,1,2,3,4,5,6,7,8,9
  random.shuffle(question)
  print(question)
  
  embed=discord.Embed(colour=discord.Colour.red())
  embed.add_field(
    name='Bienvenue dans ce quiz mortel sur Smash. Répondez au questions sans vous tromper pour gagner un maximum de points ! Chaque erreur vous coutera cher !',
    value='Bonne chance à vous !', 
    inline=False)
  await ctx.channel.send(embed=embed)

  #Un compteur len qui nous permettra de savoir quand est-ce que cinq questions ont été posées
  #Un shuffle pour la liste afin de la randomiser

  while len(question) > 4 :
  
    if question[0] == 1 :
      
      embed=discord.Embed(
        title="Question 1 !", 
        description="Qui est le meilleur joueur de smash de tous les temps ?", 
        color=0x7c5fe3)
      await shortimer()
      await ctx.channel.send(embed=embed)
      joueurs = ["jason zimmerman", "jason zimmerman", "m2k", "mew2king", "zimmerman"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in joueurs :
         await question_win(ctx)
        else :
         await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(1)
    
    if question[0] == 2 :

      embed=discord.Embed(
        title="Question 2 !",
        description="Qui est le meilleur joueur de Smash en France?", 
        color=0x5f73e3)
      await shortimer()
      await ctx.channel.send(embed=embed)
      answered = False
      gluto = ["glutonny","gluto","william belaid","glu"]
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in gluto :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await ctx.send(f"- Points : {totalpoints}")
      await shortimerdisplay(ctx)
      question.remove(2)

    if question[0] == 3 :
      embed=discord.Embed(
        title="Question 3 !", 
        description="Quel est le meilleur personnage pour débutants, et très populaire chez eux?", 
        color=0xE5E242)
      await shortimer()
      await ctx.channel.send(embed=embed)
      beginner = ["kirby", "boule rose", "kirb"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in beginner :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(3)
    
    if question[0] == 4 :
      embed=discord.Embed(
        title="Question 4 !",
        description="Citez l'endroit ou l'EVO 2019 à eu lieu.", 
        color=0xf21f18)
      await shortimer()
      await ctx.channel.send(embed=embed)
      vegas = ["las vegas", "vegas", "nevada", "mandalay bay", "mandalay", "lv", "nv"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in vegas :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(4)
      

    if question[0] == 5 :
      embed=discord.Embed(
        title="Question 5 !",
        description="Donnez le nom du créateur de Smash Bros.", 
        color=0x1adb64)
      await shortimer()
      await ctx.channel.send(embed=embed)
      sakurai = ["sakurai", "masahiro sakurai", "masahiro"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in sakurai :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(5)

    if question[0] == 6 :
      embed=discord.Embed(
        title="Question 6!",
        description="Mettre dans l'ordre les versions de Super Smash Bros., de la plus anciennne à la plus récente. (Par exemple, DCBA)?", 
        color=0x992d22)
      await shortimer()
      await ctx.channel.send(embed=embed)
      embed = discord.Embed()
      imageurl = 'https://cdn.discordapp.com/attachments/1044903296697118763/1050773921785450506/Super_mario_bros_Chronologie.png'
      embed.set_image(url = imageurl)
      await ctx.channel.send(embed=embed)
      await ctx.channel.send ("Mettre dans l'ordre les versions de Super Smash Bros., de la plus anciennne à la plus récente. (Par exemple, DCBA)")
      order = ["BADC", "badc"]
      answered = False
      while answered == False and tries > 0 :
        await hints(ctx)
        response = await bot.wait_for('message')
        if response.content.lower() in order :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(6)

    if question [0] ==  7 :
      embed=discord.Embed(
        title= "Question 7!",
        description="A quel opus de SSB appartient cette chanson ?",
        color = 0x7289da)
      await ctx.channel.send(embed=embed)
      await shortimer()
      await ctx.channel.send(file=discord.File(r'SSBsong\song 4.mp4')) #C:\Users\Memed\Desktop\Discord Bot\SSBsong\song 4.mp4
      Opus1 = ["ultimate menu theme", "ultimate", "smash ult", "menu 1", "ssbu menu"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in Opus1 :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(7)
      


    if question [0] ==  8 :
      embed=discord.Embed(
        title="Question 8!", 
        description="A quel opus de Super Smash Bros appartient cette chanson?", 
        color=0x979c9f)
      await ctx.channel.send(embed=embed)
      await shortimer()
      await ctx.channel.send(file=discord.File(r'SSBsong\song 2.mp4'))
      Opus2 = ["melee opening", "melee","ssbm"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in Opus2 :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(8)


    if question [0] ==  9 :
      embed=discord.Embed(
        title="Question 9!", 
        description=" A quel opus de Super Smash Bros appartient cette chanson?", 
        color=0x979c9f)
      await ctx.channel.send(embed=embed)
      await shortimer()
      await ctx.channel.send(file=discord.File(r'SSBsong\song 3.mp4'))
      Opus3 = ["brawl theme", "brawl", "ssbb"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in Opus3 :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(9)


    if question [0] ==  10 :
      embed=discord.Embed(
        title="Question 10!", 
        description=" A quel opus de Super Smash Bros appartient cette chanson?", 
        color=0x979c9f)
      await ctx.channel.send(embed=embed)
      await shortimer()
      await ctx.channel.send(file=discord.File(r'SSBsong\song 5.mp4'))
      Opus4 = ["super smash bros opening", "super smash bros","ssb64","64"]
      answered = False
      while answered == False and tries != 0 :
        response = await bot.wait_for('message')
        if response.content.lower() in Opus4 :
          await question_win(ctx)
        else :
          await question_lose(ctx)
      await shortimerdisplay(ctx)
      question.remove(10)
  
  if totalpoints > 250 :
    embed=discord.Embed(title="Voici votre cadeau !", description="Il est très puissant...", color=0xffbb00)
    embed.set_image(url ="https://i.kym-cdn.com/entries/icons/original/000/015/565/image.jpg")
    embed.set_footer(text="Merci beaucoup d'avoir joué !")
    await ctx.send(embed=embed)
  if totalpoints <= 250 :
    await ctx.send("Vous avez perdu.")
    await longtimerdisplay(ctx)
  
  print("test")
  await ctx.send("Voulez-vous rejouer?")
  replay = ["yes", "oui", "y", "stp"]
  response = await bot.wait_for('message')
  if response.content.lower() in replay :
    await smash(ctx)


bot.run("MTA0NDg5OTMzNzI4MjUyNzI2Mg.G1eKbe.tFVcM4v5qG3ZGvhwJf_tqAGg6v89cQp50AxOok")