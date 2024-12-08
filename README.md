# Arrays and Strings

## Arrays

#### Appending - O(1)

```python
a = [1, 2, 3]
a.append(4)
```

#### Popping - O(1)

```python
a = [1, 2, 3]
a.pop()
```

#### Inserting - O(n)

```python
a = [1, 2, 3]
a.insert(1, 5)
```

#### Modifying an element - O(1)

```python
a = [1, 2, 3]
a[1] = 0
```

#### Accessing an element - O(1)

```python
a = [1, 2, 3]
print(a[1])
```

#### Checking if an element is in an array - O(n)

```python
a = [1, 2, 3]
print(1 in a)
```

#### Checking the length of an array - O(1)

```python
a = [1, 2, 3]
print(len(a))
```

## Strings
##### Strings are immutable objects, therefore appending creates a new string
##### That means that time complexity for this action is O(n)

#### Appending - O(n)

```python
a = "Hello"
a += " World"
```

#### Checking if an element is in a string - O(n)

```python
a = "abc"
print("a" in a)
```

#### Checking the length of a string - O(1)

```python
a = "Cookie"
print(len(a))
```

#### Accessing positions - O(1)

```python
a = "Son Goku"
print(a[1])
```

# Linked Lists

## Singly Linked Lists

##### Singly Linked List is a list of items called "Linked List Nodes" where each node points to the next.
##### Last node points to None, which represents the end of the list.
##### Each node has a completely different memory address
##### The first node is called a head.
##### 1 -> 2 -> 3 -> 4 -> None.

##### Nodes can be represented in Python in the following way:

```python
class Node():
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
```

##### As you can see, node class has two variables:
- value - contains the value of the current node
- next - contains the memory address of the next node

##### Here are some operations on Singly Linked Lists in python:

```python
class SinglyNode():
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    return str(self.val)

head = SinglyNode(1)
a = SinglyNode(3)
b = SinglyNode(4)
c = SinglyNode(5)

head.next = a
a.next = b
b.next = c

print(head) # This will print 1 to the console

# Traverse the list - O(n)
cur = head

while cur:
  print(cur)
  cur = cur.next

# Display the linked list - O(n)
def display(head):
  cur = head
  elements = []
  while cur:
    elements.append(str(cur.val))
    cur = cur.next

  print(' -> '.join(elements)) # This will display 1 -> 3 -> 4 -> 5

display(head)

# Search for a node value - O(n)
def search(head, val):
  cur = head
  while cur:
    if val == cur.val:
      return True
    cur = cur.next

  return False

search(head, 5) # This will return True
search(head, 6) # This will return False
```

## Doubly Linked Lists

##### Doubly Linked List is the same as Singly Linked List except each node points to the next and the previous node.
##### None <-> 1 <-> 2 <-> 3 <-> 4 <-> None
##### The first node is called a head and the last is called a tail

##### Nodes can be represented in Python in the following way:

```python
class Node():
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev
```
##### Here are some doubly linked list operations:

```python
class DoublyNode():
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev
  def __str__(self):
    return str(self.val)

head = tail = DoublyNode(1)

# Display - O(n)
def display(head):
  cur = head
  elements = []
  while cur:
    elements.append(str(cur.val))
    cur = cur.next

  print(' <-> '.join(elements))

display(head) # prints 1

# Insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
  new_node = DoublyNode(val, next=head)
  head.prev = new_node
  return new_node, tail

head, tail = insert_at_beginning(head, tail, 2)
display(head) # prints 2 <-> 1

# Insert at end - O(1)
def insert_at_end(head, tail, val):
  new_node = DoublyNode(val, prev=tail)
  tail.next = new_node
  return head, new_node

head, tail = insert_at_end(head, tail, 3)
display(head) # prints 2 <-> 1 <-> 3
```
