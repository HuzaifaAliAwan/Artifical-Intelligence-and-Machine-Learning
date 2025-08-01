# Author : Huzaifa Ali
# Email : huzaifaa0303@gmail.com

# Real-World Project: Student Grade Calculator
# Description: Build a Python program to manage student grades, calculate averages, assign grades, and generate a report.
# Dataset: Create a simple dataset (e.g., a FacetGrid Steps:
# 1. Prompt the user to input a student's name, roll number, and marks for three subjects (Math, Science, English).
# 2. Validate inputs using try-except to handle non-numeric marks.
# 3. Calculate total marks, average, and assign a grade (A: ≥80, B: ≥60, C: ≥40, else F).
# 4. Save the results to a text file in a formatted report.
# 5. Display the report on the console.


def get_percentage(obtained, total):
    return int((obtained/total)*100)


def get_grade(percentage):
    if percentage >= 80:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 40:
        grade = 'C'
    else:
        grade = 'F'
    return grade

def generate_result(data):
    
    formatted_data = f'''---------------------------------------------
Student Name : {data['Student Name']}
Roll No : {data['Roll No']}
---------------------------------------------
Total Marks : {data['Total Marks']}

Maths : {data['Maths Marks']}
Science : {data['Science Marks']}
English : {data['English Marks']}
---------------------------------------------
Obtained Marks : {data['Obtained Marks']}
Average Marks : {data['Average Marks']}
Percentage : {data['Percentage']} %
Grade : {data['Grade']}
---------------------------------------------'''

    file = open(f'results/{data['Roll No']}.txt', 'w')
    
    if(file.write(formatted_data)):
        print('Result generate and stored in file')

    return formatted_data

def main():
    try:
        name = input('Enter name : ').lower()
        roll_no = input('Enter RollNo : ').lower()
        maths_marks = int(input('Enter Maths Marks : '))
        science_marks = int(input('Enter Science Marks : '))
        english_marks = int(input('Enter English Marks : '))

        # total marks
        total_marks  = 300

        # calculate Obtained marks
        obtained_marks = maths_marks + science_marks + english_marks

        # Avg marks 
        avg_marks = obtained_marks//3

        # Percentage
        percentage = get_percentage(obtained=obtained_marks, total= total_marks)

        # Grade 
        grade = get_grade(percentage)

        # generate result and write in to a file 
        data = {
            'Student Name' : name,
            'Roll No' : roll_no,
            'Maths Marks' : maths_marks,
            'Science Marks' : science_marks,
            'English Marks': english_marks,
            'Total Marks' : total_marks,
            'Obtained Marks' : obtained_marks,
            'Average Marks' : avg_marks,
            'Percentage' : percentage,
            'Grade' : grade
        }

        result = generate_result(data)

        print(result)

    except ValueError as e:
        print('Invalid Entry, Try Again ..... !')

if __name__ == '__main__':
    main()