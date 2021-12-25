# d1 = {}
# print(type(d1))
#
# d2 = {"san": "burger", "abhi": "pizza", "op": "goo" }
# print(d2)

d3 = {"san": "burger", "abhi": "pizza", "op": "goo" , "meal":{"b":"paav","l":"roti","d":"chicken"}}
# print(d3["meal"]["l"])

# d3["motu"]="mut"
# d3[760]="matan"
# del d3[760]
# print(d3)
d4 = d3.copy()
print(d4)
del d4["abhi"]
print(d4)
print(d4.get("meal"))
d4.update({"lee":"pee"})
print(d4)
print(d4.keys())
print(d4.items())