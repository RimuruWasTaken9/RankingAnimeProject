import random
import os
from smalltournament import *
import time

THELIST = os.listdir(r'tierlist extended images')
TierList = 0
SaveFlip = 0

def validation(var):
    while var == 0:
        print("\nError: input can't be 0.")
        var = int(input("what place? (type integer rank): "))
    return var

#save the final product to a folder on the desktop
def save():
    global TierList
    global SaveFlip
    open('tierlist1.txt','w').close()
    TierList = open('tierlist1.txt', 'w')
    TierList.write("RANKING OF ANIME THAT I'VE SEEN:\n\n\n")
    SaveFlip = 1

def edit(list):
    prompt = input("Do you want to edit the last response or a prior one? (type last or prior): ")
    while prompt != 'last' and prompt != 'prior':
        print('Please type a valid response: ')
        prompt = input("Do you want to edit the last response or a prior one? (type last or prior): ")
    if prompt == 'last':

        anime = list[-1]
        del list[-1]
        place = int(input("what place would you like it to be? (type integer rank): "))
        place = validation(place)
        list.insert(place, anime)

    if prompt == 'prior':

        alter = int(input("what is the current rank of the anime you want to change? (type integer rank): "))
        alter = validation(alter)
        anime = list[alter]
        del list[alter]
        place = int(input("what place would you like it to be? (type integer rank): "))
        place = validation(place)
        list.insert(place, anime)
    for anime in list:
        if anime == list[0]:
            continue
        print(f'#{list.index(anime)}\t{anime}')

def ranking(length):
    global TierList
    global SaveFlip
    animeList = getAnime(length)
    random.shuffle(animeList)
    currentRank = ['ignore index zero']

    for anime in animeList:
        LINE = len(anime)+5
        print('-'*LINE + f'\n#{animeList.index(anime)+1} {anime}\n' + '-'*LINE)
        if anime == animeList[0]:
            currentRank.append(anime)
            time.sleep(.5)
            continue
        future = input(f"Is {anime} above its current position (y/n): ")
        while future != 'y' and future != 'n' and future != '0':
            if future == '':
                print('\nError: input needs to be y or n.')
            elif future[0] == 'y' and future[1:].isdigit():

                if int(future[1:]) == 0:
                    print("Error: Input can't be zero.")
                    future = input(f"Is {anime} above its current position (y/n): ")
                    continue

                elif int(future[1:]) > len(currentRank):
                    currentRank.append(anime)
                    break
                else:
                    currentRank.insert(int(future[1:]), anime)
                    break
            elif future == 'edit':
                edit(currentRank)
                print('-' * LINE + f'\n#{animeList.index(anime) + 1} {anime}\n' + '-' * LINE)
            else:
                print('\nError: input needs to be y or n.')
            future = input(f"Is {anime} above its current position (y/n): ")

        if future == 'y':
            place = input("what place? (type integer rank): ")
            while place == '':
                print('Error: enter a valid integer: ')
                place = input("what place? (type integer rank): ")
            validation(place)
            currentRank.insert(int(place),anime)
        elif future == 'n':
            currentRank.append(anime)
        elif future == '0':
            print('going back to menu')
            break

        print('Total Number of Anime: ',(len(currentRank)-1),'\n')
        for anime in currentRank:
            if anime == currentRank[0]:
                continue
            
            
            print(f'#{currentRank.index(anime)}\t{anime}')
    if SaveFlip == 1:
        for anime in currentRank:
            if anime == currentRank[0]:
                continue
            TierList.write(f'#{currentRank.index(anime)}\t{anime}\n')
        TierList.close()
        SaveFlip = 0
    print("The List Is Done.")
#make a random order every time the program is executed


def menu():
    loopControl = True
    while loopControl:
        print('\nMenu for Listing Anime:\n')
        print('\tPress 0 to exit program')
        print('\tPress 1 to execute the ranking program')
        print('\tPress 2 to execute the short ranking program')
        print('\tPress 3 to execute the elimination style program')
        print('\tPress 4 to execute the short elimination style program')
        print('\tPress 5 to save the next ranking that is run after this')

        outcome = int(input('>>> : '))
        if outcome == 0:
            loopControl = False
        elif outcome == 1:
            ranking(len(THELIST))
        elif outcome == 2:
            ranking(32)
        elif outcome == 3:
            tournament()
        elif outcome == 4:
            smallTournament()
        elif outcome == 5:
            save()
            print("The next ranking program will be saved.")
        else:
            print("\nEnter valid input")

menu()
'''
notes for what to do: (optional things, since this is complete enough)
need to format the way ranking looks better
need to find how to add images and where exactly to put them
'''
