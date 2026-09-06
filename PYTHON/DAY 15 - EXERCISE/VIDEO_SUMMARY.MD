# MOM – Python Exercise: Good Morning Sir

**Topic:** Practical use of `if/else` + `time` module
**Exercise:** Good Morning Sir
**Objective:** Create a Python program that greets the user based on the current time.

## 1. Exercise Overview

The task is to create a program that displays:

* **Good Morning**
* **Good Afternoon**
* **Good Evening**

depending on the current time.

The exercise is designed to provide practical experience with **`if/else` statements**.

## 2. Module Used

### `time` Module

* `time` is a **built-in Python module**.
* It does **not require installation using `pip`**.
* The program can use `strftime()` to obtain the current:

  * Hours → `%H`
  * Minutes → `%M`
  * Seconds → `%S`

## 3. Important Concept – Time Zone

The time returned depends on where the program is running:

* **Replit:** The lecture notes that Replit runs in the USA time zone.
* **Local computer:** The program uses the local computer's time zone.

Therefore, the greeting may differ between Replit and your own computer.

## 4. Important Hint – `int()`

A key challenge is that the value obtained from `strftime()` needs to be converted into an **integer** before using numerical comparisons such as:

```python
>
<
>=
<=
```

The lecture specifically recommends using:

```python
int()
```

This converts the time value into an integer so it can be compared with other numbers.

## 5. Expected Logic

The program should follow a structure similar to:

```text
Get current hour
       ↓
Convert hour to integer
       ↓
Check the time
       ↓
Morning / Afternoon / Evening
       ↓
Display appropriate greeting
```

The exact solution was intentionally provided as a **hint**, with the recommendation to attempt the exercise independently first.

## 6. Learning Outcome

After completing this exercise, you should understand:

1. How to import and use a built-in module.
2. How to obtain the current time.
3. How `strftime()` works.
4. How to extract hours, minutes, and seconds.
5. How to convert a value using `int()`.
6. How to use time values with `if/else`.
7. How conditional statements can solve practical problems.

## 7. Action Item

**Create the `Good Morning Sir` program yourself before looking at the provided solution.**

The main goal is not just getting the final output—it is practicing the process of converting a real-world requirement into conditional logic.

### Final Takeaway

This exercise connects the previous **If/Else lesson** with a real-world use case: **making decisions based on the current time**. The main technical challenge is obtaining the hour with `strftime()` and converting it to an integer using `int()` so it can be compared numerically.
