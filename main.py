# Arrays and Strings

# Arrays

A = [1,2,3]

# Appending - O(1)

A.append(4)

# Popping - O(1)

A.pop()

# Inserting - O(n)

A.insert(1, 5)

# Modifying - O(1)

A[0] = 0

# Accessing - O(1)

print(A[0])

# Searching - O(n)

if 5 in A:
   print(True)

# Strings

s = "Hello"
# Appending - O(n)

s += " World"

# Something in string - O(n)

if "H" in s:
   print(True)

# Access positions - O(1)

print(s[0])

# Checking length - O(1)

len(s)