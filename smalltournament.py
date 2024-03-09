import random
import os
import time
THELIST = os.listdir(r'c:\\Users\\rimuru\\Desktop\\tierlist extended images')
advance = []
remain = []
def getAnime(amount):
    global advance
    for animes in THELIST:
        animes = animes.removesuffix('.jpg')
        animes = animes.removesuffix('.png')
        advance.append(animes)
    advance = advance[0:amount]
    random.shuffle(advance)
    return advance

def individualRound(roundNumber,matchesRemaining):
    global advance
    global remain

    remain = advance
    advance = []
    random.shuffle(remain)
    top = random.choice(remain)
    bottom = random.choice(remain)
        
    for i in range(matchesRemaining):
        while top == bottom:
            top = random.choice(remain)
            print('bottom and top are the same, rerolling')

        print(f'------------------------------------------\n\n\n{top}\n\n\n\
------------------------------------------\n\n\n{bottom}\n\n\n\
------------------------------------------')

        future = str(input("Pick one of the two: '1' for the top and '2' for the bottom: "))
        
        while future != '1' and future != '2' and future != '0':
            print("\nError: input isn't 1 or 2.")
            future = input("Pick one of the two: '1' for the top and '2' for the bottom: ")
        if int(future) == 1:
            advance.append(top)
            
        elif int(future) == 2:
            advance.append(bottom)

        elif int(future) == 0:
            print('ending immediately')
            break
            
        remain.remove(top)
        remain.remove(bottom)
        if remain != []:
            bottom = random.choice(remain)
            top = random.choice(remain)
    if len(advance) != 1:
        print(f'\n\nEnd of round {roundNumber}: {advance}')
        print(f'{len(advance)} remaining')

def smallTournament():
    getAnime(32)
    individualRound(1,16)
    individualRound(2,8)
    individualRound(3,4)
    individualRound(4,2)
    individualRound(5,1)

    print(f'\n\n\n\n\n\n\tTHE WINNER IS {advance[0].upper()}!!!\n\n')


def tournament():
    advance = getAnime(len(THELIST))
    random.shuffle(advance)
    
    for i in range(len(THELIST)-1):
        print(len(advance))
        top = advance[0]
        bottom = advance[1]
        while top == bottom:
            top = random.choice(advance)
            print('bottom and top are the same, rerolling')

        print(f'------------------------------------------\n\n\n{top}\n\n\n\
------------------------------------------\n\n\n{bottom}\n\n\n\
------------------------------------------')
        future = str(input("Pick one of the two: '1' for the top and '2' for the bottom: "))
        
        while future != '1' and future != '2' and future != '0':
            print("\nError: input isn't 1 or 2.")
            future = input("Pick one of the two: '1' for the top and '2' for the bottom: ")
        if int(future) == 1:
            advance.append(top)

        elif int(future) == 2:
            advance.append(bottom)

        elif int(future) == 0:
            print('ending immediately')
            break
        advance.remove(top)
        advance.remove(bottom) 

    print(f'\n\n\n\n\n\n\tTHE WINNER IS {advance[0].upper()}!!!\n\n')
