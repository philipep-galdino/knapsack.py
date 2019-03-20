'''
Just a simple lists and clean code practicing with python functions.
I brought this idea of a knapsack from a MIT opencourseware lesson on
'''

items = [
    'Golden Bar',
    'Gold Dust',
    'Antique Pot',
    'Antique Paint',
    'Silver Fork',
    'Silver Spoon',
    'Silver Knife',
    'Normal Paint'
    ]

knapsack = []


def showKnapsack():
    
    '''
    This function shows each item present on the knapsack list in a single
    line per item.
    '''
    
    for item in knapsack:
        print(item)


def showItem():
    
    '''
    This function returns the items around the room you'd be able to reach
    and pack them into your knapsack.
    '''
    
    for item in items:
        print(item)
    
def capacityCheck():
    
    '''
    Making a capacity check on your knapsack, with a limit of 10.
    '''
    
    actualCapacity = 0
    maximumCapacity = 10
        
    for item in knapsack:
        actualCapacity = len(knapsack)
        if actualCapacity >= maximumCapacity:
            return 'Your knapsack is at maximum capacity and can not handle any more item!'
        else:
            continue

def isItemReal(item):
    
    '''
    Just a quick check on if the user is writing the correct name of the item, so
    we won't have problems on items that aren't listed on items list.
    '''
    
    if item not in items:
        return 'Seems like you are trying to pick up an item that does not exist. Retype the item name again, please.'
    else:
        capacityCheck()
        knapsack.append(item)
        
        

def packItem():
    
    '''
    The main function, where the whole action occurs. You pack the item into your
    knapsack with this function here, and then it makes a check if you're typing
    a real item and if you're not reaching the capacity of your knapsack.
    '''
    
    showItem()
    print('\nHere you can see the items around you. You have literally 5 seconds to choose anything you want to pack in.\n')
    item = input('Type in the name of the item you want to pick up:\n')
    print('You would be searching for the item around the room...')
    isItemReal(item)
    print(f'You have just added a {item} to your knapsack.\n')
    print('Here goes what you been carrying on your knapsack;')
    return showKnapsack()


packItem()
        

            
        


