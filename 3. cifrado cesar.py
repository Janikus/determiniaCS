k = int(input("Introduce value for k: "))

plain = input("Introduce a plain text: ")
cipher = ""

for i in range(len(plain)):
    cipher += chr(((ord(plain[i]) + k - 65) % 26) + 65)

print(cipher)
