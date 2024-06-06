week=["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]

day=input("Enter a day :")
day=day.lower()

if day =="sunday":
    print("hello padai suru vayo")
    del week[:1]
    print(week)
    
elif day =="monday":
    del week[:2]
    print(week)
    
elif day =="tuesady":
    del week[:3]
    print(week)

elif day =="wednesday":
    del week[:4]
    print(week)
    
elif day =="thrusday":
    del week[:5]
    print(week)
    
elif day =="friday":
    del week[:6]
    print(week)

else:
    print("BIDA")