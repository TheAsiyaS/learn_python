class StudentMarks:
    def __init__(self, subject_name, marks):#constructor
        self.subject_name = subject_name
        self.marks = marks

    # Overloading the '+' operator
    def __add__(self, other):
        # Adds the marks of 'self' and 'other' student objects together
        total_score = self.marks + other.marks
        return total_score

# Example Usage
term1 = StudentMarks("Maths", 85)
term2 = StudentMarks("Maths", 90)

# The '+' symbol automatically triggers term1.__add__(term2)
total_marks = term1 + term2

print(f"Total Combined Marks: {total_marks}")  # Output: 175