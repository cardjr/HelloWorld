string1 = "he's "
string2 = "probably "
string3 = "pinning "
string4 = "for the "
string5 = "fjords "

print(string1 + string2 + string3 + string4 + string5)
print("he's " + "probably " + "pinning " + "for the " + "fjords ")

print("hello " * 5)

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")


today = "Friday"
print("day" in today)       # true
print("Fri" in today)       # True
print("thur" in today)      # false
print("parrot" in "fjord")  # false