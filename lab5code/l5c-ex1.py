'''
Author: Michael Davis
KUID: 3223493
Date: 3-5-26
Lab: lab05
Last modified: 3-10-26
Purpose: code for lab 5 exercise 1
'''
choice = 0
userList = []
while choice != 4:
    print('\nWelcome to your Shoping List')
    print('1) Add Item \n2) Check off item \n3) Print List \n4) Exit')
    choice = int(input('Enter a choice: '))

    if choice == 1:
        userList.append(str(input('What would u like to add to your list?: ')))
        
    elif choice == 2:
        checkOff = int(input('What item would u like to check off?: '))-1
        item = list(userList[checkOff])
        n = 1
        lenItem = len(item)
        while n < lenItem-1:
            item[n] = '-'
            n += 1
        userList[checkOff] = ''.join(item)
        
    elif choice == 3:
        n = 1
        for items in userList:
            print(n,')',items)
            n += 1
        
    if choice == 4:
        print('Goodbye!')
