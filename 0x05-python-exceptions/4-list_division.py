#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    '''
     function that divides element by element 2 lists.
    '''
    listing = []
    for element in range(0, list_length):
        try:
            division = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            listing.append(division)
    return (listing)
