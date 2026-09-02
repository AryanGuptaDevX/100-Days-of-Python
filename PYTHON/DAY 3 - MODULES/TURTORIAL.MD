# 🐍 Day 3 — Modules & pip

### 📦 What is a Module?

A **module** is a collection of Python code that we can **reuse** in our program.

### Types of Modules

1. **Built-in Modules** → Already included with Python. No installation needed.
2. **External Modules** → Created by others; install using **pip** or **conda**.

### 🔧 What is pip?

**pip** is Python's **package manager** used to install external modules.

```bash
pip install pandas
```

### 📥 How to Import a Module

Use the `import` keyword:

```python
import pandas
```

Example:

```python
import pandas

df = pandas.read_csv("words.csv")
print(df)
```

### 📝 One-line Revision

**Module = Reusable code | pip = Install packages | import = Use a module in Python**
