nume = input("Cum te cheamă? ") 
print(f"Salut, {nume}! Mă bucur să te cunosc!\n")


varsta = int(input("Câți ani ai? ")) 

dublu = varsta * 2         
peste_5_ani = varsta + 5   

print(f"Dublul vârstei tale este: {dublu}")
print(f"Peste 5 ani vei avea: {peste_5_ani} ani")

if varsta % 2 == 0:
    print("Vârsta ta este un număr par.\n")
else:
    print("Vârsta ta este un număr impar.\n")




scor = int(input("Introdu scorul tău de la test (1-10): "))

if scor >= 7:
    print("Bravo! Ai obținut un scor excelent!")
elif scor == 4 or scor == 5:
    print("Ai fost la limită. Se putea și mai bine!")
else:
    print("Mai încearcă! Data viitoare va fi mult mai bine.")