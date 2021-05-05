# Lists: Ex-1 can take values of same type
item = ["pen","book","chair","table","laptop"]
print(item)

# Lists : Ex-2 can take values of different  type
item1 = ["pen","book","chair","table","laptop","10",20]
print(item1)
print(item1[3])

# Lists : Ex-3 Apply Function on list
num = [1,22,13,18,9,29,34]
print(num)
print(num[4])
num.sort()
print(num)
num.append(100)
print(num)
num.reverse()
print(num)

print(num[0:6])
print(num[2:6])
print(num[:6])
print(num[3:])
print(num[:])
print(num[::6])
print(num[1:6:2])
print(num[::-1])
print(len(num))
print(max(num))
print(min(num))


n = []
n.append(2)
n.append(3)
print(n)

n1 = [1,2,3,4,5,6,7,8,9]
n1.insert(5,3363)
print(n1)
n1.remove(3)
print(n1)
n1.pop()
print(n1)
