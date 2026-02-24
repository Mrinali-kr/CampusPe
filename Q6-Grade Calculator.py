# Calculates academic performance based on subject marks
def q5_grade_calculator():
    """
    Calculates total marks, percentage, and letter grade while 
    ensuring student passes all individual subjects.
    """
    try:
        marks = []
        num_subjects = 5
        pass_mark = 40  # Minimum marks required to pass an individual subject

        for i in range(1, num_subjects + 1):
            score = float(input(f"Enter marks for subject {i} (0-100): "))
            
            # Validation: Ensure marks are within a realistic range
            if score < 0 or score > 100:
                print("Error: Marks must be between 0 and 100.")
                return
            
            marks.append(score)

        # Calculate metrics
        total = sum(marks)
        percentage = total / num_subjects

        # Determine individual subject pass status
        # If any single subject is below 40, the student fails regardless of average
        passed_all_subjects = all(m >= pass_mark for m in marks)

        # Logic for Grade and Final Result
        if not passed_all_subjects:
            grade = "F"
            result = "Fail"
        else:
            result = "Pass"
            if percentage >= 90:   grade = "A+"
            elif percentage >= 80: grade = "A"
            elif percentage >= 70: grade = "B"
            elif percentage >= 60: grade = "C"
            elif percentage >= 50: grade = "D"
            else:                  grade = "E"

        # Formatted Output
        print("\n--- PERFORMANCE REPORT ---")
        print(f"Total Marks: {total:g} / {num_subjects * 100}")
        print(f"Percentage:  {percentage:.2f}%")
        print(f"Final Grade: {grade}")
        print(f"Result:      {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    q5_grade_calculator()