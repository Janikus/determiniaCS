n = int(input("Introduce un número: "))

primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False

if primo:
    print("El número", n, "es primo")
else:
    print("El número", n, "no es primo")
