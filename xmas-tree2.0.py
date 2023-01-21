
s = " "

ch = input("What will your christmas tree be built of? ")

while len(ch) != 1:
    ch = input("Your christmas tree can be built of only one thing, please choose again: ")

o = input("How far away from the left screen side should your tree stand? ")


if not o.isnumeric():
    o = input("Please choose an integer instead: ")
    offset = s * int(o)
else:
    offset = s * int(o)

print(offset, s * 3 + ch)
print(offset, s * 2 + ch * 3)
print(offset, s + ch * 5)
print(offset, ch * 7)
print(offset, s * 3 + ch)
