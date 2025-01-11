# School Grading System - Python Project

This is a simple Python-based School Grading System that allows users to input student scores and calculates the corresponding grades. The program takes in the number of students, their names, and their scores, and it outputs the grades according to predefined thresholds.

## Features

- Input student names and scores.
- Calculate grades based on given score thresholds.
- Display student names along with their scores and corresponding grades.

## Grading Criteria

| Score Range | Grade |
|-------------|-------|
| 90 - 100    | A     |
| 80 - 89     | B     |
| 70 - 79     | C     |
| 60 - 69     | D     |
| 0 - 59      | F     |

## Requirements

- Python 3.x
- No external libraries are required for this basic implementation.

## Installation

1. Ensure that Python 3 is installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. Clone or download the project repository to your local machine.

   ```bash
   git clone https://github.com/your-username/school-grading-system.git
   ```

3. Navigate to the project folder.

   ```bash
   cd school-grading-system
   ```

4. Run the Python script.

   ```bash
   python grading_system.py
   ```

## Usage

### Step 1: Input number of students

When the program starts, it will prompt you to enter the number of students.

Example:
```
Enter number of students: 3
```

### Step 2: Input student names and scores

Next, the program will prompt you to enter the name and score of each student.

Example:
```
Enter name of student 1: John Doe
Enter score of John Doe: 85
```

### Step 3: Display results

The program will calculate and display the grade for each student based on their score.

Example output:
```
Student Name    Score   Grade
--------------------------------
John Doe        85      B
Jane Smith      92      A
Mark Brown      78      C
```

## Code Example

```python
# Function to calculate grade based on score
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main program
def main():
    print("Welcome to the School Grading System!")
    
    # Number of students
    num_students = int(input("Enter number of students: "))
    
    # Collect student data
    students = []
    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        score = float(input(f"Enter score of {name}: "))
        grade = calculate_grade(score)
        students.append((name, score, grade))
    
    # Display results
    print("\nStudent Name    Score   Grade")
    print("--------------------------------")
    for student in students:
        print(f"{student[0]:<15} {student[1]:<7} {student[2]}")

# Run the program
if __name__ == "__main__":
    main()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute by submitting pull requests, reporting issues, or suggesting improvements.

---

For any questions or feedback, feel free to open an issue or reach out to the project maintainers. Happy coding!
