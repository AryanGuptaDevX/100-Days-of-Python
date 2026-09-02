# 🐍 Python — Day 9: Type Casting

## 1. What is Type Casting?

**Type Casting / Type Conversion** means converting one data type into another data type.

Example:

```python
a = "1"
b = "2"

print(a + b)
```

Output:

```text
12
```

Because both `a` and `b` are **Strings**, Python concatenates them instead of adding them.

---

## 2. Explicit Type Casting

When **the programmer manually converts** one data type into another, it is called **Explicit Type Casting**.

Example:

```python
a = "1"
b = "2"

print(int(a) + int(b))
```

Output:

```text
3
```

Here:

* `"1"` → `1`
* `"2"` → `2`
* `1 + 2` → `3`

### Common conversion functions:

```text
int()    → Integer
float()  → Float
str()    → String
list()   → List
tuple()  → Tuple
set()    → Set
dict()   → Dictionary
hex()    → Hexadecimal
oct()    → Octal
```

### ⚠️ Important

The value must be valid for the target data type.

```python
int("27")       # ✅ Works
int("1Harry")   # ❌ Error
int("Harry")    # ❌ Error
```

---

## 3. Implicit Type Casting

When **Python automatically converts** a data type into another data type during an operation, it is called **Implicit Type Casting**.

Example:

```python
c = 1.9
d = 8

print(c + d)
```

Output:

```text
9.9
```

Python converts the `int` value `8` into a `float` so that no precision/data is lost.

Conceptually:

```text
1.9 + 8
↓
1.9 + 8.0
↓
9.9
```

---

## 4. Explicit vs Implicit

| Type         | Who converts?        | Example         |
| ------------ | -------------------- | --------------- |
| **Explicit** | Programmer           | `int("10")`     |
| **Implicit** | Python automatically | `1.5 + 2 → 3.5` |

### Remember:

**Explicit = I tell Python to convert.**
**Implicit = Python converts automatically.**

---

## 5. Checking Data Type

Use the `type()` function:

```python
a = 10
print(type(a))
```

Output:

```text
<class 'int'>
```

Example:

```python
c = 1.9
d = 8

result = c + d

print(type(result))
```

Output:

```text
<class 'float'>
```

---

## 🧠 Day 9 Key Takeaways

1. **Type Casting** = converting one data type into another.
2. `"1" + "2"` gives **`"12"`** because both are strings.
3. `int("1") + int("2")` gives **`3`**.
4. **Explicit casting** is done manually by the programmer.
5. **Implicit casting** is done automatically by Python.
6. Python generally converts a lower-order type to a higher-order type to **prevent data loss**.
7. `type()` tells you the data type of a value.
8. `int("Harry")` or `int("1Harry")` causes an error because they aren't valid integers.

### 📌 Day 9 Formula to Remember

```text
String + String → Concatenation
Integer + Integer → Addition
Explicit → Programmer converts
Implicit → Python converts
```
