#!d/usr/bin/python3
def roman_to_int(roman_string):
    """Transform Roman numbers into Decimals """
    romans = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    if isinstance(roman_string, str) and roman_string == "None":
        return 0
    else:
        rom_lis = [romans[items.upper()] for items in roman_string]
        number = 0
        for i in range(len(rom_lis) - 1):
            if rom_lis[i] >= rom_lis[i+1]:
                number += rom_lis[i]
            else: 
                number -= rom_lis[i]
        number += rom_lis[i+1]
    return number          
