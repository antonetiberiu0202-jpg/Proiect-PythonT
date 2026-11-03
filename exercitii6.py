scoruri = []

print("Introdu 3 scoruri pentru lista ta:")

scor1 = int(input("Introdu primul scor: "))
scoruri.append(scor1)

scor2 = int(input("Introdu al doilea scor: "))
scoruri.append(scor2)

scor3 = int(input("Introdu al treilea scor: "))
scoruri.append(scor3)

print("Scorurile din lista ta sunt:")
for s in scoruri:
    print(s)

total = len(scoruri)
print("În listă ai un număr total de elemente:")
print(total)