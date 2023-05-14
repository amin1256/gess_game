import random
number_system = random.randint(1,100)
number_system = int(number_system)
print(number_system)

while True :
    gess = input("is number bigger or smaller?")
    if gess == "bigger":
       number_system2 = random.randint(number_system ,100 )
       print(number_system2) 

    elif gess == "smaller":
        number_system3 = random.randint(1 , number_system)
        print(number_system3)

    elif gess == "ok thats right":
        print("wooooow im amazing")
        break