import sys

# print("hello, my name is", sys.argv[1])

# $ python name.py Mabu
# hello, my name is Mabu

#  $ python name.py
# IndexError: list index out of range



# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# $ python name.py Mabu
# hello, my name is Mabu
# $ python name.py     
# Too few arguments



# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

# $ python name.py 
# Too few arguments
# $ python name.py  da da
# Too many arguments
# $ python name.py  da     
# hello, my name is da



# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")   
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

# $ python name.py     
# Too few arguments
# $ python name.py  da da
# Too many arguments
# $ python name.py  da 
# hello, my name is da



if len(sys.argv) < 2:
    sys.exit("Too few arguments")   

# for  arg in sys.argv[:]:
# for  arg in sys.argv[1:]:
for  arg in sys.argv[1: -1]:
    print("hello, my name is", arg)

# $ python name.py  1 2 3
# hello, my name is name.py
# hello, my name is 1
# hello, my name is 2
# hello, my name is 3

# $ python name.py  1 2 3
# hello, my name is 1
# hello, my name is 2
# hello, my name is 3
    
# $ python name.py  1 2 3
# hello, my name is 1
# hello, my name is 2