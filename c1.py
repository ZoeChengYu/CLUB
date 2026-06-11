import random

def main():
    target=(int)(input("target:"))
    range_down=(int)(input("from:"))
    range_up=(int)(input("to:"))
    time=(int)(input("times:"))
    point=0
    if range_up>=target>=range_down:
        for i in range(time):
            guess=0
            rt=0
            while(guess!=target or rt==0):
                guess=random.randint(range_down,range_up)
                rt+=1
            #print(i,"-",rt)
            point+=rt
        print(point/time)
    else:
        print("error")
            
        
main()