"""

File Name: RetailItemClass.py

Developer: Lawrence Andriese

Date last modified: 10/28/18

Description: This program is designed to make a class for retail items store
the data and spit the data back out in table format.

email address: andriesel@student.vvc.edu

"""

#define the retailitem class
class RetailItem:
    def __init__(self, description, units, price):
        self._description = description
        self._units = units
        self._price = price
    
    def __str__(self):
        d = '%+10s %10d %+10s' % (self._description, self._units, self._price)
        return d

#make definitions

def item_list():
    desc = input('Enter description of item: ')
    units = int(input('Enter number of units in inventory: '))
    price = float(input('Enter price of item: '))
    price = str(format(price, '.2f'))
    print()
    items = RetailItem(desc, units, price)
    return items

def main():
    print('Please enter information for 3 items:')
    item1 = item_list()
    item2 = item_list()
    item3 = item_list()
    print('Item  Description  Units  Inventory Price')
    print('1', item1)
    print('2', item2)
    print('3', item3)


    
#run main function to execute program

main()




    
