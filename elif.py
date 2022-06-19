x=range(30)
for y in x:
    if y%3==0:
        print(f"{y} is divided by 3")
    elif y%5==0:
        print(f"{y} is divided by 5")
    elif y%4==0:
        print(f"{y} is divided by 4")
    elif y%6==0:
        print(f"{y} is divided by 6")
    else:
        print(f"{y} is divided by 3,5,4,6")
        
            