#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists."""
    new = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i]/my_list_2[i]
            new.append(div)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            if not div:
                new.append(0)
    return new

my_l_1 = [10, 0, 4]
my_l_2 = [2, 4, 0]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)