import random
import sys
import time

print('Welcome to Rock, Paper, Scissors, Lizard, Spock')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties'%(wins, losses, ties))
    while True:
        print('Enter Your move (R)ock, (P)aper, (S)cissors, (L)izard, (SP)ock')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S' or playerMove == 'L' or playerMove == 'SP':
            break
        print('Type one of R, P, S, L, SP')


# Player Move Loop
    if playerMove == 'R':
        print('Rock versus...')
        time.sleep(1)
    elif playerMove == 'P':
        print('Paper versus...')
        time.sleep(1)
    elif playerMove == 'S':
        print('Scissors versus...')
        time.sleep(1)
    elif playerMove == 'L':
        print('Lizard versus...')
        time.sleep(1)
    elif playerMove == 'SP':
        print('Spock versus...')
        time.sleep(1)

    randomNumber = random.randint(1,5)
#  Computer Moves
    if randomNumber == 1:
        computerMove = 'R'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'P'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 'S'
        print('Scissors')
    elif randomNumber == 4:
        computerMove = 'L'
        print('Lizard')
    elif randomNumber == 5:
        computerMove = 'SP'
        print('Spock')


    if computerMove == playerMove:
        print('It is a Tie')
        ties += 1

#  Losses
    elif computerMove == 'R' and playerMove == 'S':
        time.sleep(1)
        print('Rock smashes scissors')
        print('You Lose')
        losses += 1
    elif computerMove == 'S' and playerMove == 'P':
        time.sleep(1)
        print('Scissors cuts paper')
        print('You Lose')
        losses += 1
    elif computerMove == 'P' and playerMove == 'R':
        time.sleep(1)
        print('Paper covers rock')
        print('You Lose')
        losses += 1
    elif computerMove == 'R' and playerMove == 'L':
        time.sleep(1)
        print('Rock crushes Lizard')
        print('You Lose')
        losses += 1
    elif computerMove == 'L' and playerMove == 'SP':
        time.sleep(1)
        print('Lizard poisons Spock')
        print('You Lose')
        losses += 1
    elif computerMove == 'L' and playerMove == 'P':
        time.sleep(1)
        print('Lizard eats Paper')
        print('You Lose')
        losses += 1
    elif computerMove == 'P' and playerMove == 'SP':
        time.sleep(1)
        print('Paper disproves Spock')
        print('You Lose')
        losses += 1
    elif computerMove == 'S' and playerMove == 'L':
        time.sleep(1)
        print('Scissors beheads Lizard')
        print('You Lose')
        losses += 1
    elif computerMove == 'SP' and playerMove == 'S':
        time.sleep(1)
        print('Spock smashes scissors')
        print('You Lose')
        losses += 1
    elif computerMove == 'SP' and playerMove == 'R':
        time.sleep(1)
        print('Spock vaporizes Rock')
        print('You Lose')
        losses += 1

#  Wins
    elif playerMove == 'R' and computerMove == 'S':
        time.sleep(1)
        print('Rock smashes scissors')
        print('You Win')
        wins += 1
    elif playerMove == 'S' and computerMove == 'P':
        time.sleep(1)
        print('Scissors cuts Paper')
        print('You Win')
        wins += 1
    elif playerMove == 'P' and computerMove == 'R':
        time.sleep(1)
        print('Paper covers Rock')
        print('You Win')
        wins += 1
    elif playerMove == 'R' and computerMove == 'L':
        time.sleep(1)
        print('Rock smashes Lizard')
        print('You Win')
        wins += 1
    elif playerMove == 'L' and computerMove == 'SP':
        time.sleep(1)
        print('Lizard poisons Spock')
        print('You Win')
        wins += 1
    elif playerMove == 'L' and computerMove == 'P':
        time.sleep(1)
        print('Lizard eats Paper')
        print('You Win')
        wins += 1
    elif playerMove == 'P' and computerMove == 'SP':
        time.sleep(1)
        print('Paper disproves Spock')
        print('You Win')
        wins += 1
    elif playerMove == 'S' and computerMove == 'L':
        time.sleep(1)
        print('Scissors behead Lizard')
        print('You Win')
        wins += 1
    elif playerMove == 'SP' and computerMove == 'S':
        time.sleep(1)
        print('Spock smashes Scissors')
        print('You Win')
        wins += 1
    elif playerMove == 'SP' and computerMove == 'R':
        time.sleep(1)
        print('Spock vaporizes Rock')
        print('You Win')
        wins += 1



















