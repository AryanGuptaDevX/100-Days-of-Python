# MOM – Python If/Else Statements

**Topic:** If / Elif / Else Statements
**Day:** Day #14
**Main Objective:** Understand decision-making and conditional statements in Python.

## 1. Key Discussion Points

### Conditional Decision Making

Python uses conditional statements to make decisions based on whether a condition evaluates to **True or False**.

Real-life example:

* If it is raining → don't go to school.
* Else → go to school.

Python provides:

* `if`
* `elif`
* `else`

## 2. Conditional Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |

**Important:** `=` is an assignment operator, not a conditional/equality operator. `==` is used to check equality.

All these comparisons produce a **Boolean value**: `True` or `False`.

## 3. `if` Statement

The `if` statement executes a block of code when its condition is `True`.

Example concept:

```python
if age > 18:
    print("You can drive")
```

If the condition is `False`, the `if` block is skipped.

## 4. `else` Statement

`else` executes when the `if` condition is `False`.

```python
if age > 18:
    print("You can drive")
else:
    print("You cannot drive")
```

Only one of these two branches executes.

## 5. Indentation

**Indentation is extremely important in Python.**

Python uses indentation to define blocks of code instead of curly brackets `{}` commonly used in languages such as C.

```python
if age > 18:
    print("You can drive")
```

The indented line belongs to the `if` block. Incorrect indentation can produce an error.

## 6. `elif` Statement

`elif` means **"else if"**.

It is used when there are multiple conditions to check.

Basic structure:

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

Python checks the conditions sequentially:

1. Check `if`.
2. If false → check `elif`.
3. Continue checking additional `elif` conditions.
4. If none match → execute `else`.

Once a condition becomes `True`, the corresponding block executes and the remaining conditions in that ladder are ignored.

## 7. Example: Positive, Negative or Zero

A number can be classified using `if/elif/else`:

```python
if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is 0")
else:
    print("Number is positive")
```

Examples:

* `7` → Positive
* `-8` → Negative
* `0` → Zero

## 8. Nested `if/else`

A **nested conditional** means placing one `if/else` structure inside another.

Example concept:

```python
if num > 0:
    if num > 10:
        print("Number is greater than 10")
    else:
        print("Number is between 1-10")
```

Nested conditions can have multiple levels of indentation.

## 9. Important Python Practice Rule

Do **not** name your Python files after:

* Python keywords
* Python modules/packages

For example, `if.py` is a bad filename because `if` is a Python keyword. A filename that conflicts with a module can also cause import-related problems.

## 10. Files/Programs Practiced

The lecture demonstrated separate Python files for practicing:

* `if-else.py`
* `myelif.py`
* `nested.py`

The examples included:

* Age/Driving eligibility
* Apple price vs. budget
* Positive/negative/zero numbers
* Special number conditions
* Nested number ranges

## 11. Learning Outcome

After completing this session, the learner should be able to:

1. Understand conditional decision-making.
2. Use comparison operators.
3. Write `if` statements.
4. Use `if/else` for two-way decisions.
5. Use multiple `elif` conditions.
6. Understand Boolean results.
7. Use indentation correctly.
8. Create nested `if/else` structures.
9. Understand how Python evaluates an `if/elif/else` ladder.
10. Create small programs based on real-world conditions.

## 12. Action Items

**Practice is the main requirement.**

Create small programs using:

* Age verification
* Even/odd number
* Positive/negative/zero
* Marks → grade
* Shopping budget
* Temperature → condition
* Login/password validation
* Number range checking
* Nested conditions

### Final Takeaway

The most important concept is **not memorizing the syntax**. You need to understand how Python evaluates conditions and practice writing your own programs. The lecture specifically emphasizes that repeatedly practicing and creating programs matters more than simply completing or memorizing individual "100 Days of Code" exercises.
