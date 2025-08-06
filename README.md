# adult-check
A Python script that asks for the birth year of 7 people and counts how many of them have reached the age of majority (18 years old).

# 🔞 Group Adulthood Checker

This is a command-line Python program that determines, for a group of seven people, how many have reached the age of majority (18 years old) and how many are still minors.

The script first prompts for the current year. It then enters a loop that asks for the birth year of seven people, one by one. For each person, the program calculates their age and increments either an "adult" or a "minor" counter. Finally, it displays the total for each group.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `adult_check.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python adult_check.py
    ```
5.  First, enter the current year and press Enter.
6.  Next, enter the birth year for each of the seven people, pressing Enter after each one.
7.  After the seventh birth year is entered, the program will display the totals.

## Program Logic

* **Counters:** Two variables, `adult_check` and `minor_check`, are initialized to 0 to serve as counters.
* **Fixed Loop:** A `for` loop with `range(0, 7)` ensures the program will request data for exactly seven people.
* **Age Calculation:** In each iteration, the person's age is calculated by subtracting the `birth_year` from the `current_year`.
* **Conditional Check:** An `if/else` structure checks if the calculated age is greater than or equal to 18.
    * If true, the `adult_check` counter is incremented.
    * Otherwise, the `minor_check` counter is incremented.
* **Final Result:** After the loop finishes, the final values of the two counters are printed to the screen.
