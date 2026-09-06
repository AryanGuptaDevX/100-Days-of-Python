# MOM – Python String Methods

**Topic:** Python String Methods
**Session:** 100 Days of Code
**Main Objective:** Understand commonly used Python string methods and the concept of string immutability.

## 1. Key Discussion Points

### String Immutability

* Python strings are **immutable**, meaning the original string cannot be modified in-place.
* String methods operate on the existing string and generally **return a new string**.
* Example:

  * `a.upper()` → returns the uppercase version.
  * `a.lower()` → returns the lowercase version.

### String Methods Covered

| Method          | Purpose                                                                |
| --------------- | ---------------------------------------------------------------------- |
| `len()`         | Finds the length of a string                                           |
| `upper()`       | Converts characters to uppercase                                       |
| `lower()`       | Converts characters to lowercase                                       |
| `rstrip()`      | Removes trailing characters                                            |
| `replace()`     | Replaces occurrences of one string with another                        |
| `split()`       | Splits a string into a list                                            |
| `capitalize()`  | Makes the first character uppercase and remaining characters lowercase |
| `center()`      | Centers a string within a specified width                              |
| `count()`       | Counts occurrences of a character/string                               |
| `endswith()`    | Checks whether a string ends with specified characters                 |
| `find()`        | Returns the index of the first occurrence; returns `-1` if not found   |
| `index()`       | Returns the index of an occurrence; raises `ValueError` if not found   |
| `isalnum()`     | Checks whether all characters are letters/numbers                      |
| `isalpha()`     | Checks whether all characters are alphabetic                           |
| `islower()`     | Checks whether all characters are lowercase                            |
| `isprintable()` | Checks whether all characters are printable                            |
| `isspace()`     | Checks whether the string contains only whitespace                     |
| `istitle()`     | Checks whether each word starts with a capital letter                  |
| `isupper()`     | Checks whether all characters are uppercase                            |
| `startswith()`  | Checks whether a string starts with specified characters               |
| `swapcase()`    | Swaps uppercase ↔ lowercase                                            |
| `title()`       | Converts words to title case                                           |

## 2. Important Concepts

* **`find()` vs `index()`**

  * `find()` returns `-1` when the substring isn't found.
  * `index()` raises a `ValueError` when the substring isn't found.

* **`endswith()` / `startswith()`**

  * Both return a Boolean value: `True` or `False`.
  * They can also work with specified start/end index positions.

* **`isalnum()` vs `isalpha()`**

  * `isalnum()` → letters + numbers are allowed.
  * `isalpha()` → only letters are allowed.

* **`capitalize()`**

  * First character becomes uppercase.
  * Remaining characters become lowercase.

* **`rstrip()`**

  * Removes characters from the **right/trailing end**, not the beginning.

## 3. Practical Learning

The lecture emphasized practicing the methods directly in **Replit**. The recommended workflow was to fork the provided Repl so that a personal editable copy can be created and practiced.

## 4. Learning Outcome

After completing the session, the learner should be able to:

1. Explain why Python strings are immutable.
2. Convert strings between uppercase/lowercase.
3. Search and count text inside strings.
4. Replace and split string content.
5. Validate strings using `is...()` methods.
6. Check prefixes and suffixes.
7. Understand the difference between `find()` and `index()`.
8. Format strings using `capitalize()`, `title()`, and `center()`.

## 5. Action Items

* Practice **every string method** covered in the lecture.
* Write small examples for each method.
* Specifically practice:

  * `find()` vs `index()`
  * `isalnum()` vs `isalpha()`
  * `startswith()` vs `endswith()`
  * `capitalize()` vs `title()`
* Build a small Python program that takes user input and applies multiple string methods.

## 6. Overall Summary

**Main takeaway:** Python provides many built-in string methods for transforming, searching, validating, and formatting text. The most important concept from this session is that **strings are immutable**—methods don't modify the original string in-place; they produce a new result.
