import os, time, random

NULL = ""
null = ""

def cls():os.system("cls")
def pause():os.system("pause")

cls()

class team:
    # Basic Team Structure with names and points useing 1d and 2d arrays 

    name    = ["n1", "n2", "n3", "n4"]# 1D
    
    players = [
            ["t1p1", "t1p2", "t1p3", "t1p4"],
            ["t2p1", "t2p2", "t2p3", "t2p4"],
            ["t3p1", "t3p2", "t3p3", "t3p4"],
            ["t4p1", "t4p2", "t4p3", "t4p4"]
              ]# 2D
    
    class points:
        # total points for team 1,2,3 and 4
        total=  [0,0,0,0]
        gold =  [0,0,0,0]
        silver= [0,0,0,0]
        bronze= [0,0,0,0]
    

class game:
    # all game related funtions 

    AssignedNames = False
    class random:

        def _int(n1,n2):rn = random.randint(n1, n2);return(rn)   # returns sudo random int from given range 
        def choice(n1,n2):rn = random.choice(n1, n2);return(rn)    # returns one of two numbers or string, (likey unused)
        
    pass

# Main Loop
while __name__ == __name__:
    # Gets Input as a string for names and such

    def userInputString():
        return(input("> "))
    

    # Gets Input as a interger for team numbers and such
    def userInputInt():

        isInt = False

        while isInt != True:

            try:

                ret = int(input("> "))
                isInt = True
                return(ret)

            except:
                print("error input is not a valid INT")
    

    print("""
    Welcome to the best wilberforce sports management program (TBWSMP tm).

    Basic instructions are as follows:
    -    Get students in to four groups of four,
    -    Come up with some cool names,
    -    Assign Team names,
    -    Assign Player names,
    -    Give out meadels,

    Resulting in teams placed 1st, 2nd and 3rd along with top playes sorted by points given out via the program.
    """)


    # Geting Team Names in team Class
    # Geting Team Names in team Class
    # Geting Team Names in team Class
    # Geting Team Names in team Class
    def defineingNamesAndTeams():
        
        print("Start adding team names, press ctrl + c to quit")
        teamNames = False
        while teamNames != True:

            count = 0
            # Makes sure teams are uniqe
            while count <= len(team.name)-1:

                try:

                    tname = userInputString()

                    if tname not in team.name:

                        team.name[count] = tname
                        count += 1

                    else:

                        print("Must be a uniqe team name!")
                except:

                    pass

            teamNames = True

        # print(f'{team.name[0]}, {team.name[1]}, {team.name[2]}, {team.name[3]}')


        # Geting Team players in team.players
        # Geting Team players in team.players
        # Geting Team players in team.players
        # Geting Team players in team.players
        
        print("Start adding player names, press ctrl + c to quit")
        teamPlayers = False
        TeamPlayerIndex = 0
        while teamPlayers != True:

            Tcount = 0
            Pcount = 0
            
            #print(len(team.players)-1)
            print(f'Players For {team.name[TeamPlayerIndex]}...')
            while Tcount <= len(team.players)-1:
                team.players[Tcount][Pcount] = userInputString()
                Pcount += 1
            
                if Pcount == 4:
                    Tcount += 1
                    Pcount = 0
                
                    TeamPlayerIndex +=1
                    # Show what team the players are going to be assinged to...
                    try:print(f'Players For {team.name[TeamPlayerIndex]}...');
                    except:pass

                if Tcount == 3:
                    teamPlayers = True
        
            teamPlayers = True
        game.AssignedNames = True

            

    if game.AssignedNames == False:
        defineingNamesAndTeams()
    
    # print(f'{team.players[0][0]}, {team.players[0][1]}, {team.players[0][2]}, {team.players[0][3]}')
    # print(f'{team.players[1][0]}, {team.players[1][1]}, {team.players[1][2]}, {team.players[1][3]}')
    # print(f'{team.players[2][0]}, {team.players[2][1]}, {team.players[2][2]}, {team.players[2][3]}')
    # print(f'{team.players[3][0]}, {team.players[3][1]}, {team.players[3][2]}, {team.players[3][3]}')
    
    pause() # Resets Interface
    cls()   #



    #                   1111   
    #                     11   
    #                     11   
    #                     11            
    #                   111111   



    TeamList = [team.name[0], team.name[1], team.name[2], team.name[3]]

    print(f'Right-o! {team.name[0]} (1) will be versing {team.name[1]} (2) in one of theise games:')
    print(f"1. Tennis,\n2. FootBall,\n3. Basket Ball,\n4. Archery,")
    print(f"\n1st or 2nd place only. (50 to 100pts given to the top team)\n")
    print(f"Okay now you must choose what game to play, you could take a vote or decide for them.\n !!Choose game via the numbers on the left!!")
    
    Games =     ["Tennis", "FootBall", "Basket Ball", "Archery"]
    gameChoice = userInputInt()-1
    
    print(f'So you chose {Games[gameChoice]}? sounds fun.')
    print(f'Now play the game and come back with the winner...')
    
    # time.sleep(2) # immersion XD
    
    pause() # Resets Interface
    cls()   #
    
    print(f'Wow that was qick!')
    print(f'Im sure both teams did great. \nNow type the winner team number below. [1 for {team.name[0]}, 2 for {team.name[1]}]')
    
    

    # *This loop assings the winning team number for code to continue.
    # !Also it -1 from the user input because python counts from 0 not 1 like us humans
    
    inList = False

    while inList != True:

        try:

            ClientsNumber = userInputInt()- 1
            teamWinner = TeamList[ClientsNumber]   #* Winning Team assigned here!
            inList = True
            break

        except:

            print("Invalid Input (try 1 or 2)")

        # if teamWinner in TeamList:
        #    inList = True
        #    break
    
    
    
    #* Winning team
    #* Winning team will only get points between 50 - 100
    # *and one gold point

    #* Winning team points and meadles assinged here
    WinnerPoints = game.random._int(50, 100)
    team.points.gold[ClientsNumber]   += 1
    team.points.total[ClientsNumber]  += WinnerPoints
    
    print(f'Welldone team {teamWinner}! you got first place!\nThats {WinnerPoints} points!')

    
    # time.sleep(2)
    pause() # Resets Interface
    cls()   #
    
    #* looseing team
    #* Looseing team will only get points between 20 - 50
    # *and one silver point 

    #* Looseing Team assinged & points given here
    LooserPoints = game.random._int(20, 50)

    teamLooser = TeamList[ClientsNumber+1] 
    team.points.total[ClientsNumber+1]  += LooserPoints
    team.points.silver[ClientsNumber+1]   += 1

    print(f'Im sure you tried your hardest team {teamLooser} but you got seccond place!\nThats {LooserPoints} points. not bad.')
    

    pause() # Resets Interface
    cls()   #


    #                 2222
    #                22  22
    #                   22
    #                  22
    #                222222

    TeamList = [null, null, team.name[2], team.name[3]]

    print(f'Meanwhile; {team.name[2]} (3) will be versing {team.name[3]} (4) in theise games:')
    print("1. Darts,\n2. Pong,\n3. Table Tennis,\n4. 100m Sprint,")
    print("\n1st or 2nd only. (50 to 100 points per team)")

    Games =     ["Darts", "Pong", "Table Tennis", "100m Sprint"]
    gameChoice = userInputInt()-1
    
    print(f'So you chose {Games[gameChoice]}? sounds fun.')
    print(f'Now play the game and come back with the winner...')
    
    # time.sleep(2) # immersion XD
    
    pause() # Resets Interface
    cls()   #
    
    print(f'Wow that was qick!')
    print(f'Im sure both teams did great. \nNow type the winner team number below. [3 for {team.name[2]}, 4 for {team.name[3]}]')
    
    

    # *This loop assings the winning team number for code to continue.
    # !Also it -1 from the user input because python counts from 0 not 1 like us humans
    
    inList = False

    while inList != True:

        try:
            
            ClientsNumber = userInputInt()- 1
            teamWinner = TeamList[ClientsNumber]   #* Winning Team assigned here!
            inList = True
            break

        except:

            print("Invalid Input (try 3 or 4)")

        # if teamWinner in TeamList:
        #    inList = True
        #    break
    
    
    
    #* Winning team
    #* Winning team will only get points between 50 - 100
    # *and one gold point


    #* Winning team points and meadles assinged here
    WinnerPoints = game.random._int(50, 100)
    team.points.gold[ClientsNumber]   += 1
    team.points.total[ClientsNumber]  += WinnerPoints
    
    print(f'Welldone team {teamWinner}! you got first place!\nThats {WinnerPoints} points!')
    
    # time.sleep(2)
    
    pause() # Resets Interface
    cls()   #

    #* looseing team
    #* Looseing team will only get points between 20 - 50
    # *and one silver point 

    #* Looseing Team assinged & points given here
    LooserPoints = game.random._int(20, 50)

    teamLooser = TeamList[ClientsNumber+1] 
    team.points.total[ClientsNumber+1]  += LooserPoints
    team.points.silver[ClientsNumber+1]   += 1
    

    print(f'Im sure you tried your hardest team {teamLooser}\nYou guys got seccond \nThats {LooserPoints} points. not bad.')

    pause() # Resets Interface
    cls()   #
    



    print("Their is enough points to finnish the game, however you can continue if you want.")
    print("Finnish? (y/n)")



    # print("--End of program--")

    # print(f'FOR DEBUGING: teams    !{team.name}!')
    # print(f'FOR DEBUGING: players  !{team.players}!')
    # print(f'FOR DEBUGING: total    !{team.points.total}!')
    # print(f'FOR DEBUGING: gold     !{team.points.gold}!')
    # print(f'FOR DEBUGING: silver   !{team.points.silver}!')
    # print(f'FOR DEBUGING: bronze   !{team.points.bronze}! likely not used')


#team.players[1][0] = "dave"
#print(team.players[1][0])