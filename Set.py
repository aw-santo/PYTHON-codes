s = set()
print(type(s))
s.add(1)
s.add(2)
# s1=s.union({1,3})
s1={4,7,5}
print(s,s1)
# s1=s.intersection({1,2})
# print(s,s1)
print(s.isdisjoint(s1))

