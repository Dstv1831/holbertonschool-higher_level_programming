#!/usr/bin/python3
def uppercase(s):
    """ Write a function that prints a string in uppercase 
    followed by a new line. """
    
    for c in s:
        if (ord(i) >= 97 and ord(i) <= 122):
            i = chr(ord(i) - 32)
        print('{0}'.format(i), end="")
    print("")

# #!/usr/bin/python3
# def uppercase(s):
#     """makes all characters in a string uppercase."""
#     for c in s:
#         if (ord(c) >= 97 and ord(c) <= 122):
#             c = chr(ord(c) - 32)
#         print('{0}'.format(c), end="")
#     print("")