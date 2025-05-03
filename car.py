"""askdfjf this massage i dont understand
start=car started....ready to go
stop=car stopped...."""
command=""
while command!="quite":
    command=input("> ")
    if command=="start":
        pritn("car started...")
    elif command=="stop":
        print("car stopped..")
    elif command=="help":
        print("""
        start-to start the car
        stop - to stop the car
        quit-to quit""")
    elif command=="quite":
        break
    else:
        print("sorry,i dont understand")




