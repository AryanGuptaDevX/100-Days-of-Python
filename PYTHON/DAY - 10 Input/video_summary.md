# 🐍 Python — Day 10: User Input

## 1. What is User Input?

**User Input** allows a Python program to interact with the user by taking information from the keyboard.

Python uses the **`input()`** function for this.

```python
a = input()
print(a)
```

If the user enters:

```text
Harry
```

Output:

```text
Harry
```

The program waits for the user to enter something.

---

## 2. `input()` Function

You can also display a message while asking for input:

```python
name = input("Enter your name: ")
print("My name is", name)
```

Example:

```text
Enter your name: Harry
My name is Harry
```

The text inside `input()` is called the **prompt**.

---

## 3. Important Rule of `input()`

The most important thing from Day 10:

> **`input()` always returns the user's input as a String.**

Even if the user enters a number, Python stores it as a **String**.

```python
x = input("Enter first number: ")
```

If the user enters:

```text
12
```

`x` contains:

```text
"12"
```

NOT:

```text
12
```

This is why arithmetic operations can produce unexpected results.

---

## 4. Why `input()` Causes Problems With Numbers

Example:

```python
x = input("Enter first number: ")
y = input("Enter second number: ")

print(x + y)
```

Suppose:

```text
x = 12
y = 100
```

You might expect:

```text
112
```

But the output will be:

```text
12100
```

Why?

Because Python actually has:

```text
"12" + "100"
```

Both are Strings, so Python **concatenates** them.

### Concatenation

Concatenation means joining Strings together.

```text
"12" + "100" → "12100"
"Harry" + "Bhai" → "HarryBhai"
```

---

## 5. Converting Input to Integer

If you want to perform arithmetic, convert the input into an Integer using `int()`.

```python
x = input("Enter first number: ")
y = input("Enter second number: ")

print(int(x) + int(y))
```

If:

```text
x = 45
y = 8
```

Output:

```text
53
```

Here:

```text
"45" → 45
"8"  → 8

45 + 8 → 53
```

---

## 6. String vs Integer

| Input          | Data Type | `+` Result |
| -------------- | --------- | ---------- |
| `"45"` + `"8"` | String    | `"458"`    |
| `45` + `8`     | Integer   | `53`       |

### Remember:

```text
String + String → Concatenation
Integer + Integer → Arithmetic Addition
```

---

## 7. Invalid Type Conversion

You cannot convert every String into an Integer.

```python
x = "89"
y = "Harry"

print(int(x) + int(y))
```

`int("89")` works.

But:

```python
int("Harry")
```

causes a **ValueError** because `"Harry"` is not a valid integer.

Similarly:

```python
int("1Harry")
```

will also cause an error.

---

## 8. Input Can Be Converted to Float

You can also convert user input into a Float:

```python
num = input("Enter a number: ")

num = float(num)
```

This is useful when the user needs to enter decimal numbers.

The key idea is: **convert the input into the appropriate data type before performing the operation.**

---

# 🧠 Day 10 Key Takeaways

1. `input()` is used to take **user input**.
2. `input()` returns input as a **String by default**.
3. Even numbers entered through `input()` are initially Strings.
4. String + String performs **concatenation**.
5. Use `int()` to convert numeric input into an Integer.
6. Use `float()` to convert numeric input into a Float.
7. Invalid values cannot be converted into an Integer.
8. `int("Harry")` → **ValueError**.
9. For arithmetic operations, make sure the values have the correct numeric data type.
10. Day 10 connects directly with **Day 9 — Type Casting**.

---

## 📌 Most Important Example

```python
x = input("Enter first number: ")
y = input("Enter second number: ")

print(x + y)              # String concatenation
print(int(x) + int(y))    # Integer addition
```

If the user enters:

```text
45
8
```

Output:

```text
458
53
```

### 🔥 One-line memory trick

**`input()` → String → Type Cast → Arithmetic**
