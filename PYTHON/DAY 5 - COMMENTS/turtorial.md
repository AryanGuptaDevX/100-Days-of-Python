# 🐍 Day 5 — Comments, Escape Sequences & `print()`

### 💬 Comments

Comments are notes in code that **Python does not execute**.

**Single-line:**

```python
# This is a comment
print("Hello")
```

**Multi-line:**

```python
# Line 1
# Line 2
# Line 3
```

You may also see `""" ... """` used for multi-line text/docstrings.

---

### 🔤 Escape Sequences

Escape sequences use **`\` (backslash)** to represent special characters inside strings.

Common ones:

| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | New line     |
| `\t`   | Tab space    |
| `\"`   | Double quote |
| `\'`   | Single quote |
| `\\`   | Backslash    |

Example:

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

### 🖨️ `print()` Statement

`print()` is used to **display output**.

```python
print("Hello World")
```

You can print multiple values:

```python
print("Hello", "Aryan")
```

### `sep`

Controls the separator between multiple values.

```python
print("Hello", "World", sep="-")
```

Output:

```text
Hello-World
```

### `end`

Controls what comes at the end of the output.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

### 📝 One-line Revision

**Comments = Notes | `\` = Escape character | `print()` = Display output | `sep` = Separator | `end` = Ending character**
