weight=int(input("weight:"))
unit=input('(L)bs or k(g):' )
if unit.upper()=='L':
    converted=weight*.45
    print(f'You are converted {converted} kilos')
    converted=weight/.45
    print(f'You are converted {converted} pounds')