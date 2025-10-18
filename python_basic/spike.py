import time, sys

try:
    print('try loop')
    while True:
        print('while true')
        for i in range(1,9):
            print('increasing')
            print('-'*(i*i))
            time.sleep(0.1)
        
        for i in range(7,1,-1):
            print('decreasing')
            print('-'*(i*i))
            time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()