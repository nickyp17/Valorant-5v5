from random import shuffle


def main(guiInput):
    #num of players
    x = 10

    #! input comes in form of player1 [name, rankStr] and player 2 [name, rankStr]
    # * we can call the new input guiInput which will have the form of [[p1, p1rank], [p2, p2rank]...]

    rawInput = []

    #intro

    print("i = iron ; b = bronze ; s = silver ; g = gold ; p = plat ; d = diamond ; i = immortal")
    print(guiInput)
    #input
    #*input is already put in as guiInput

    #*not in range 10
    for item in guiInput:
        """ newPlayer = input("name of player: \n")
        #getting rank of player
        newRank = input("rank of player:\n")
        #converting rank into number
        newRank = newRank.lower() """

        newPlayer = item[0]

        if item[1][:-1] == 'iron':
            numRank = 1
            numRank += int(item[1][-1])/ 10
        elif item[1][:-1] == 'bronze':
            numRank = 2
            numRank += int(item[1][-1]) / 10
        elif item[1][:-1] == 'silver':
            numRank = 3
            numRank += int(item[1][-1]) / 10
        elif item[1][:-1] == 'gold':
            numRank = 4
            numRank += int(item[1][-1]) / 10
        elif item[1][:-1] == 'plat':
            numRank = 5
            numRank += int(item[1][-1]) / 10
        elif item[1][:-1] == 'diamond':
            numRank = 6
            numRank += int(item[1][-1]) / 10
        elif item[1][:-1] == 'immortal':
            numRank = 7
            numRank += int(item[1][-1]) / 10
        elif item[1][:-1] == 'valorant':
            numRank = 8
        else:
            print("invalid input")

        numRank = str(numRank)

        rawInput.append(newPlayer + ', ' + numRank)
        
        print(rawInput)


    #shuffling raw input to get random teams
    shuffle(rawInput)

    #splitting players and theyre ranks into two seperate lists
    #! these lists order should not change
    #*not in range 10
    players = []
    ranks = []

    for i in range(x):
        currentPlayer = rawInput[i]
        currentPlayer = currentPlayer.split()
        currentPlayer[1] = float(currentPlayer[1])

        players.append(currentPlayer[0])
        print('Ranks: ',currentPlayer[1])
        ranks.append(currentPlayer[1])

    #right now its printing
    #[['nick,', '4.1']]
    #[['ojus,', '3.3']]
    #this could be split up as a list
    #could turn into [['nick', 4.1], ['ojus', 3.3]]
    #or could turn into two seperate lists where players and ranks r seperated
    #if go w/ first option ul have to find lowest player by searching through the list manually

    #putting into teams
    team1 = []
    team2 = []

    while len(players) >> 0:

        print(len(players))

        #lowest player
        print(f'len of ranks ----- {len(ranks)}')
        lowestRank = min(ranks)
        lowIndex = ranks.index(lowestRank)

        lowestPlayer = players[lowIndex]

        team1.append(lowestPlayer)

        #removing lowest player from the list of players and ranks
        print(len(ranks))
        players.pop(lowIndex)
        ranks.pop(lowIndex)

        #lowest player
        if len(ranks) != 0:
            lowestRank = min(ranks)
            lowIndex = ranks.index(lowestRank)

            lowestPlayer = players[lowIndex]

            team2.append(lowestPlayer)

            #removing lowest player from the list of players and ranks
            players.pop(lowIndex)
            ranks.pop(lowIndex)

        else:
            team2.append(ranks[0])


    print(team1)
    print(team2)

    return team1, team2

