import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
turn = ""
player1 = ""
player2 =  ""
game_over = True
game_win = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
game = [":white_large_square:",":white_large_square:",":white_large_square:",
        ":white_large_square:",":white_large_square:",":white_large_square:",
        ":white_large_square:",":white_large_square:",":white_large_square:"]
# Run the bot
# TOKEN = 'MTM1ODg1OTYxMDMyMDI3NzUyNA.GBOxg1.3_R_Ty_kJEkUaXkpF2ljOp7uPnsFFPzWNJ5COE'
# Define the bot prefix
intents=discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix='!',intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command handler for the 'game' command to start a new game

@bot.command()
async def game(ctx,Player1:discord.Member,Player2:discord.Member):
    global turn
    global player1 
    global player2
    global game_over
    if game_over != True:
        await ctx.send("there is a game in progress, you should finish it before start new one")
        return 
    player1 = Player1
    player2 = Player2
    turn = random.randint(1,2)
    game_over = False
    Len =''
    for i in range(len(game)):
                if i == 2 or i == 5 or i == 8:
                    Len += " "+game[i]
                    await ctx.send(Len)
                    Len = ""
                else:
                    Len += " "+game[i]
    if turn == 1:
        turn = player1
        player_Start = str(player1)+"start"
        await ctx.send(player_Start)
    else:
        turn = player2
        player_Start = str(player2)+"start"
        await ctx.send(player_Start)
    
#game handler for the "place" command to place a mark on the board
@bot.command()
async def place(ctx,args):
    if game_over:
        await ctx.send("Game is over!")
        return
    global turn
    if int(args)>10 or int(args)<1:
        await ctx.send("Invalid position!")
        return
    if int(args)>len(game):
        await ctx.send("Invalid position!")
        return
    else:
        if turn == player1:
            if game[int(args)-1] != ":white_large_square:":
                await ctx.send("Invalid position!")
                return 
            game[int(args)-1]= ":x:"
            await ctx.send("Placed!")
            turn = player2
            Len =''
            for i in range(len(game)):
                if i == 2 or i == 5 or i == 8:
                    Len += " "+game[i]
                    await ctx.send(Len)
                    Len = ""
                else:
                    Len += " "+game[i]
            await check_winner(ctx,player1)
            if game_over:
                return 
            else:
                turn_string  = "it\'s"+str(turn)+"\'s turn"
                await ctx.send(turn_string)
        else:
            if game[int(args)-1] != ":white_large_square:":
                await ctx.send("Invalid position!")
                return
            game[int(args)-1]= ":o:"
            await ctx.send("Placed!")
            turn = player1
            Len =''
            for i in range(len(game)):
                if i == 2 or i == 5 or i == 8:
                    Len += " "+game[i]
                    await ctx.send(Len)
                    Len = ""
                else:
                    Len += " "+game[i]
            await check_winner(ctx,player2)
            if game_over:
                return
            else:
                turn_string  = "it's"+str(turn)+"'s turn"
                await ctx.send(turn_string)
#game handle for the "stop" command to stop the game
@bot.command()
async def stop(ctx):
    global game_over
    global game
    global turn
    global player1
    global player2
    turn = ""
    player1 = ""
    player2 =  ""
    game_over = True
    game = [":white_large_square:",":white_large_square:",":white_large_square:",
        ":white_large_square:",":white_large_square:",":white_large_square:",
        ":white_large_square:",":white_large_square:",":white_large_square:"]
    await ctx.send("Game stopped")
def reset_game():
    global game_over
    global game
    global turn
    global player1
    global player2
    turn = ""
    player1 = ""
    player2 =  ""
    game_over = True
    game = [":white_large_square:",":white_large_square:",":white_large_square:",
        ":white_large_square:",":white_large_square:",":white_large_square:",
        ":white_large_square:",":white_large_square:",":white_large_square:"]
#function to check for a winner
async def check_winner(ctx,player):
    global game_over
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    if((game[game_win[zero][0]]  == ":o:"and game[game_win[zero][1]] == ":o:" and game[game_win[zero][2]] == ":o:") or (game[game_win[one][0]]  == ":o:"and game[game_win[one][1]]  == ":o:"and game[game_win[one][2]] == ":o:" )or (game[game_win[two][0]]  == ":o:"and game[game_win[two][1]]  == ":o:"and game[game_win[two][2]] == ":o:") or (game[game_win[three][0]]  == ":o:"and game[game_win[three][1]]  == ":o:"and game[game_win[three][2]] == ":o:" )or (game[game_win[four][0]]  == ":o:"and game[game_win[four][1]]  == ":o:"and game[game_win[four][2]] == ":o:") or (game[game_win[five][0]]  == ":o:"and game[game_win[five][1]]  == ":o:"and game[game_win[five][2]] == ":o:") or (game[game_win[six][0]]  == ":o:"and game[game_win[six][1]]  == ":o:"and game[game_win[six][2]] == ":o:") or (game[game_win[seven][0]]  == ":o:"and game[game_win[seven][1]]  == ":o:"and game[game_win[seven][2]] == ":o:")):
                    winner = str(player) + " "+"is the winner" 
                    await ctx.send(winner)
                    await ctx.send("Game over...!")
                    game_over = True
                    reset_game()
                    return
    elif((game[game_win[zero][0]]== ":x:" and game[game_win[zero][1]]== ":x:" and game[game_win[zero][2]] == ":x:") or (game[game_win[one][0]] == ":x:"and game[game_win[one][1]]== ":x:" and game[game_win[one][2]] == ":x:" )or (game[game_win[two][0]]== ":x:" and game[game_win[two][1]] == ":x:"and game[game_win[two][2]] == ":x:") or (game[game_win[three][0]]== ":x:" and game[game_win[three][1]]== ":x:" and game[game_win[three][2]] == ":x:" )or (game[game_win[four][0]]== ":x:" and game[game_win[four][1]] == ":x:"and game[game_win[four][2]] == ":x:") or (game[game_win[five][0]] == ":x:"and game[game_win[five][1]] == ":x:"and game[game_win[five][2]] == ":x:")or(game[game_win[six][0]]== ":x:" and game[game_win[six][1]] == ":x:"and game[game_win[six][2]] == ":x:") or (game[game_win[seven][0]]== ":x:" and game[game_win[seven][1]] == ":x:"and game[game_win[seven][2]] == ":x:")):
                    winner = str(player) + " "+"is the winner" 
                    await ctx.send(winner)
                    await ctx.send("Game over...!")
                    game_over =True
                    reset_game()
                    return
    else:
        return
    
#error handler for the game command use if user input wrong command
@game.error
async def game_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention two players to start the game...!")
        return
    else:
        await ctx.send("An error occurred while starting the game...!")
        return

#error handler for the place command use if use input wrong command
@place.error
async def place_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a position to place your mark...!")
        return
    else:
        await ctx.send("An error occurred while placing your mark...!")
        return

#error handler for the stop command use if user input wrong command        
@stop.error
async def stop_error(ctx,error):
    if isinstance(error, commands.missingRequiredArgument):
        await ctx.send("An error occurred while stopping the game...!, please try again later..!")
        return
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
bot.run(TOKEN)