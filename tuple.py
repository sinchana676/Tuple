#program to demonstrate tuple and related functions

t = (10, 20, 30, 40, 50)

print("Tuple:", t)
print("First Element:", t[0])
print("Length:", len(t))
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Sum:", sum(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

print("After Concatenation:", t + (60, 70))
print("After Repetition:", t * 2)
print("After Slicing:", t[1:4])

print("Is 30 present?", 30 in t)
print("Loop through tuple:")
for i in t:
    print(i)
