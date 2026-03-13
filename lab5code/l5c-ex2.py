'''
Author: Michael Davis
KUID: 3223493
Date: 3-10-26
Lab: lab05
Last modified: 3-12-26
Purpose: code for lab 5 exercise 2
'''
missionOver = 'n'
planetsVisited = []
while missionOver != 'y':
    planetAt = str(input('Enter planet name: '))
    missionOver = str(input('Is the mission over? (y/n): ')).lower()
    planetsVisited.append(planetAt)

neighboringPlanets = str(input('Which planet do you want the neighbors for?: '))
n = 0
for planets in planetsVisited:
    if (n-1) >= 0:
        beforePlanet = planetsVisited[n-1]
    if (n+1) < len(planetsVisited):
        afterPlanet = planetsVisited[n+1]
    if planets == neighboringPlanets:
        print(f'Planets neighboring {neighboringPlanets}:')
        if (n-1) < 0:
            print('\t',afterPlanet)
        elif (n+1) >= len(planetsVisited):
            print('\t',beforePlanet)
        elif ((n-1) >= 0) and ((n+1) < len(planetsVisited)):
            print(f'\t{beforePlanet}\n\t{afterPlanet}')
    n += 1
 print('Program ending...')
    
    
