## 🎯 Video Summary — Python Strings

This video is about **Strings in Python** and goes deeper into how they are created, accessed, and processed. 

### 1. What is a String?

A **string** is textual data enclosed inside quotation marks.

```python
name = "Harry"
friend = 'Rohan'
```

Both **single quotes `' '`** and **double quotes `" "`** can be used. 

---

### 2. Quotes inside a String

You **cannot directly put double quotes inside a double-quoted string** because Python may interpret them as the end of the string.

❌ Problem:

```python
apple = "He said "I want to eat an apple""
```

You can solve it using an **escape sequence**:

```python
apple = "He said \"I want to eat an apple\""
```

Or use single quotes outside:

```python
apple = 'He said "I want to eat an apple"'
```



---

### 3. Multi-line Strings

For strings containing multiple lines, Python provides **triple quotes**:

```python
text = '''Hello Harry
He said "Hi Harry"
Hey I am good
I want to eat an apple'''
```

You can also use:

```python
text = """Hello Harry
He said "Hi Harry"
Hey I am good"""
```

Triple quotes allow new lines to be included naturally. 

---

### 4. String Indexing ⭐

A string behaves **like a sequence/array of characters**.

For:

```python
name = "Harry"
```

The indexes are:

```text
 H   a   r   r   y
[0] [1] [2] [3] [4]
```

So:

```python
print(name[0])  # H
print(name[1])  # a
print(name[4])  # y
```

**Important:** Python indexing starts from **0**, not 1. 

---

### 5. IndexError

If you try to access an index that doesn't exist:

```python
name = "Harry"
print(name[5])
```

You'll get an **IndexError**, because the available indexes are only `0–4`. 

---

### 6. Looping Through a String

You can use a `for` loop to access every character one by one:

```python
name = "Harry"

for character in name:
    print(character)
```

Output:

```text
H
a
r
r
y
```

The loop goes through the string character-by-character, including spaces. 

The video says not to worry too much about the `for` loop yet because **loops are explained later** in the course. 

---

## 🧠 What you should remember

| Concept       | Key Point                         |
| ------------- | --------------------------------- |
| String        | Textual data                      |
| `' '`         | Single quotes create strings      |
| `" "`         | Double quotes create strings      |
| `''' '''`     | Multi-line string                 |
| `""" """`     | Multi-line string                 |
| Indexing      | Starts at `0`                     |
| `name[0]`     | First character                   |
| Invalid index | Causes `IndexError`               |
| `for` loop    | Can process characters one by one |

### 🔥 Most important examples

```python
name = "Harry"

print(name[0])  # H
print(name[1])  # a
print(name[4])  # y

for character in name:
    print(character)
```

**Core idea:** A Python string is textual data and can be treated **like a sequence of characters**, allowing you to access individual characters using indexes and process them one by one with loops. 

If you're making notes for your **Python learning roadmap**, this video is essentially: **Strings → Quotes → Escape sequences → Multiline strings → Indexing → IndexError → Looping through strings.**
