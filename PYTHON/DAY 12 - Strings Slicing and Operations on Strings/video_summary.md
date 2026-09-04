## 🎯 Video Summary — Python String Slicing

This video teaches **String Slicing in Python**, along with string length, positive/negative indexing, and how slicing ranges work. 

### 1. What is String Slicing?

**Slicing** means extracting a portion of a string.

Example:

```python
name = "Harry"
```

Indexes:

```text
 H   a   r   r   y
[0] [1] [2] [3] [4]
```

If you want `"rry"`, you can slice a portion of the string. 

---

### 2. Basic Slicing Syntax ⭐

The syntax is:

```python
string[start:end]
```

Example:

```python
fruit = "Mango"

print(fruit[0:4])
```

Output:

```text
Mang
```

**Important rule:**

> Start index is included, but end index is NOT included.

So:

```python
fruit[0:4]
```

means:

```text
0 → M
1 → a
2 → n
3 → g
4 → ❌ not included
```



---

### 3. Omitting the Start Index

You can leave the starting index blank:

```python
print(fruit[:4])
```

Python automatically treats the missing start as `0`.

So:

```python
fruit[:4]
```

is equivalent to:

```python
fruit[0:4]
```

Output:

```text
Mang
```



---

### 4. Omitting the End Index

You can also leave the ending index blank:

```python
print(fruit[0:])
```

Python automatically uses the **length of the string** as the ending point.

For `"Mango"`:

```python
len(fruit)   # 5
```

Therefore:

```python
fruit[0:]
```

is effectively:

```python
fruit[0:5]
```

Output:

```text
Mango
```



---

## 5. `len()` Function

The `len()` function tells you how many characters are in a string.

```python
fruit = "Mango"

print(len(fruit))
```

Output:

```text
5
```

Spaces and other characters are also counted as characters. 

---

# 6. Negative Indexing / Negative Slicing ⭐

Python also allows **negative indexes**.

For:

```python
fruit = "Mango"
```

Think of it as:

```text
 M    a    n    g    o
 0    1    2    3    4
-5   -4   -3   -2   -1
```

So:

```python
fruit[-1]
```

refers to the last character:

```text
o
```

The video explains negative slicing by converting negative indexes using the string's length. 

---

### Example from the video

```python
fruit = "Mango"

print(fruit[0:-3])
```

String length = `5`

Python interprets:

```text
-3 → 5 - 3 → 2
```

So it effectively becomes:

```python
fruit[0:2]
```

Output:

```text
Ma
```



---

## 7. Another Negative Slicing Example

The video demonstrates:

```python
fruit[-3:-1]
```

For `"Mango"`:

```text
-3 → index 2 → n
-2 → index 3 → g
-1 → index 4 → o
```

Because the ending index isn't included:

```python
fruit[-3:-1]
```

produces:

```text
ng
```



---

# 🧠 The Most Important Rule

Remember this:

### `string[start:end]`

**START = included**
**END = excluded**

For example:

```python
fruit = "Mango"

print(fruit[1:4])
```

Indexes:

```text
 M    a    n    g    o
[0]  [1]  [2]  [3]  [4]
      ↑         ↑
    start      end
```

Output:

```text
ang
```

Index `1`, `2`, `3` → included
Index `4` → excluded. 

---

## 🔥 Quick Cheat Sheet

| Code           | Meaning              |
| -------------- | -------------------- |
| `fruit[0:4]`   | Index 0 → 3          |
| `fruit[:4]`    | Same as `fruit[0:4]` |
| `fruit[1:4]`   | Index 1 → 3          |
| `fruit[0:]`    | Entire string        |
| `fruit[:]`     | Entire string        |
| `fruit[-1]`    | Last character       |
| `fruit[-3:-1]` | Negative slicing     |
| `len(fruit)`   | String length        |

### You should memorize these 3 things:

```python
len(string)
string[start:end]
# start included, end excluded
```

And the key concept from this video is:

**String Slicing = taking a specific portion of a string using `[start:end]`.** 

### 🎯 Video Quiz

The video ends with:

```python
nm = "Harry"
print(nm[-4:-2])
```

The task is to determine the output **without running the program**. 

**Answer: `ar`**

Reason:

```text
H   a   r   r   y
0   1   2   3   4
-5 -4  -3  -2  -1
    ↑       ↑
   -4      -2
```

`[-4:-2]` includes `-4` and `-3`, but excludes `-2` → **`ar`**.
