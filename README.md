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
