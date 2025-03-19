sin = 3000
tri = 3 
n = ""  

while tri > 0:
    print(f"saldo actual: {sin}")
    n = int(input("ingrese la cantidad que quiere retirar: "))
    if n <= 3000:
        sin -= n
    if sin <= 0 or tri == 0:
        break
    else: tri -= 1 
