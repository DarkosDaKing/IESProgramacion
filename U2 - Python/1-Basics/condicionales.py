import time
##import math

seg = 0; min = 0; hor = 0

while seg < 10 and min < 5 and hor < 2:
    seg += 1
    time.sleep(0.02)
    
    if seg == 10:
        min += 1
        seg = 0   
        ##* Condicionales anidadas 
        if min == 5:
            min = 0
            hor += 1
    
    print(hor, ' : ', min, ' : ', seg)
    