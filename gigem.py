#! /usr/bin/python3
import sys 




if len(sys.argv) < 2:
    print('usage: {} <n:integer>'.format(sys.argv[0]))
    sys.exit(0)


n = int(sys.argv[1])
one = int(sys.argv[2])
two = int(sys.argv[3])
if one == two:
    print("Don't put the same number twice DUM DUM!!!")
    sys.exit(0);
#TODO: catch ValueError on non-integer data


for i in range(1, n+1):
    if i % one == 0 and i %two == 0:
        print("gig 'em")
    elif i %one == 0:
        print('gig')
    elif i % two ==0:
        print("'em")
    else:
        print(i)
    
