s = set()
print(s)
print(type(s))

set1 = set([1,2,3,4,5,6])
print(set1)

set1.add(22)
print(set1)
# will not add duplicate value again
set1.add(22)
print(set1)
set1.remove(22)
print(set1)

s= set1.union({1,2,4,5,16})
print(s)
s= set1.intersection({1,2,4,5,16})
print(s)
print(max(s))
print(min(s))
print(len(s))
s1 = set({2,4,6})
print(s.isdisjoint(s1))
