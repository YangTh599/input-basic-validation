**Python: Tiered Programming Assignment**

**Objective:**  
This assignment is designed to help you practice basic string manipulation and input validation in Python. 

You will write a Python script that prompts the user for a string input and then validates that input using some combination of the `isalpha()` string method, `isdigit()` string method, and the built-in `len()` function. 

The assignment has three levels, each progressively more challenging.

Choose a level you and your partner think you can complete and write (and submit) the script for that level.  **You only need to complete ONE LEVEL.**

Before you write any code, research these string methods and the `len( )` function.

- the `isalpha()` string method
- the `isdigit()` string method
- the `len( )` function (which we already used with Python lists, but can also be used to determine the length (number of characters) in a string)

Look on the [w3schools.com](https://www.w3schools.com/python/python_ref_string.asp) website for examples of how to use these string methods and the `len ( )` function.

---

### **Submission Instructions:**
1. Write your Python script for each level in separate files (e.g., `input_validation1.py`, `input_validation2.py`, and `input_validation3.py`).
2. Follow the instructions provided for each script.
3. Upload your script to GitHub and share the link to your repo with your teacher on Google Classroom.

---

**Grading Criteria:**
- **Level 1:** Correctly checks if the input contains only alphabetic characters.
- **Level 2:** Properly checks both for numeric input and length.
- **Level 3:** Effectively handles multiple validation conditions (alphabetic or numeric, length constraints, etc.).
---

### **Level 1: Simple String Validation**

**Task:**  
1. Prompt the user for input.
2. Use the `isalpha()` method to check if the string contains only alphabetic characters.
3. If the input is valid, print a message saying, "Valid input: [user's input]."
4. If the input is invalid, print a message saying, "Invalid input. Please enter only alphabetic characters."

---

### **Level 2: Checking for a Numeric Input with Length Validation**

**Task:**  
1. Prompt the user for input.
2. Use the `isdigit()` method to check if the input consists of only digits.
3. Use the `len()` function to check if the length of the string is 5 or more characters.
4. If both conditions are true, print: "Valid numeric input with enough length: [user's input]."
5. If either condition fails, print a corresponding error message:
   - "Input must be a number."
   - "Input must be at least 5 characters long."

---

### **Level 3: Advanced Input Validation for Mixed Conditions**

**Task:**  
1. Prompt the user to enter a string.
2. Use the `isalpha()` method to check if the input consists only of letters OR use `isdigit()` to check if the input consists only of digits (use `OR` to combine the checks).
3. Use the `len()` function to check if the length of the string is between 6 and 10 characters (inclusive).
4. If both conditions are met, print: "Valid input: [user's input]."
5. If any condition fails, print the corresponding error message:
   - "Input must be alphabetic or numeric (but not both)."
   - "Input must be between 6 and 10 characters long."

---





