# Creat an empty set
s = set()

#add element

s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)
s.add(2) #cannot add duplicate value
print(s)
s.remove(3) #removing value
print(s)
print(f"This set has {len(s)} elements")