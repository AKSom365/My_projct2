d1 = {}
print(type(d1))

d2 = {"Amit":"Rice","Mohit":"Burger","Rachit":"Roti"}
print(d2)
print(d2["Mohit"])

d3 = {"Amit":"Rice","Mohit":"Burger","Rachit":{"B":"Juice","L":"Dahi","D":"Milk"}}
print(d3)
print(d3["Rachit"])
print(d3["Rachit"]["D"])

d2["Ankit"] = "Junk Food"
d2[20] = "Banana"
print(d2)
del d2[20]
print(d2)

print(d2.update({"Leena":"Ice"}))
print(d2)
print(d2.get("Amit"))
print(d2.keys())
print(d2.items())



