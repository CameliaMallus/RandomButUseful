import time, random
score=0
attempts=0
starttime = time.time()
print("You have 60 seconds")
print("Enter to quit :)")
print("Time ;Score:  Mult ->RESULT")
print(f"\n0.00", end="")
while time.time()-starttime<=60:
    x=random.randint(11,99)
    y=random.randint(11,99)
    put = input(f" ; {score}/{attempts} : {x}*{y} -> ")
    timestring = "{:.2f}".format(time.time()-starttime)
    print(timestring)
    try:
        if put=="":
            break
        elif int(put)==x*y:
            score+=1
            print(True)
        else:
            print(False)
            print(f"Answer was {x*y}")
            time.sleep(1)
        attempts+=1
    except:
        print("Wrong input…")
        print("Terminated.")
        exit()
print(f"{score}/{attempts}")