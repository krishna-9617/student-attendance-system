# student-attendance-system
🎯 Overview of the Project
This project is a console-based application built using Python, designed to simplify the manual process of recording and analyzing student attendance. It offers a straightforward, menu-driven interface for teachers or administrators to log attendance and quickly generate basic statistics. 

✨ Features 

The Attendance Manager system provides the following capabilities:

Mark Attendance: Allows the user to enter student names and mark their status as 'Present' or 'Absent'.

Update Records: If a student's name is entered again, their attendance status is updated in the system.

View Records: Displays the current list of all students and their recorded attendance status.

Attendance Analysis: Calculates and displays key metrics, including the total number of students, the count of present/absent students, and the overall attendance percentage.

🛠️ Technologies/Tools Used 

Language: Python 3.x

Data Structure: Built-in Python Dictionary (for storing records)

🚀 Steps to Install & Run the Project 

Prerequisites
Ensure Python 3.x is installed on your computer.

Running the Application
Download the Code: Obtain the attendance_system.py file.

Open Terminal: Navigate to the folder where you saved the file using your terminal or command prompt.

Execute the Script: Run the program using the command:

Bash

python attendance_system.py
Follow the Menu: Interact with the system using the numerical menu options (1, 2, 3, or 4).

🧪 Instructions for Testing 

Since this is a simple console application, testing primarily involves user interaction validation:

Test Case 1: Marking and Updating

Choose Option 1 (Mark Attendance).

Enter a name (e.g., Alice) and mark her p (Present).

Enter the same name (Alice) again and mark her a (Absent).

Choose Option 2 (View All Attendance) and verify Alice is listed as ABSENT. (Test Update)

Test Case 2: Analysis Accuracy

Mark a total of 5 students (e.g., 3 Present, 2 Absent).

Choose Option 3 (Analyze Attendance).

Verify the output: Total Students Count should be 5, Students Present should be 3, and Presentation Percentage should be 60.00%
