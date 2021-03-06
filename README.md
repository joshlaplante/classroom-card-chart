### Classroom Card Chart GUI
***
This Python 3.4 application is designed to assist elementary schoolteachers in monitoring and rewarding the behavior of their students over time and to replace hanging card charts already in existence. It utilizes a SQLite database connection to manage student information.

#### How existing card charts work:

Each student in a class has their own set of ranked colored cards (gold, green, yellow, orange, red) with each color representing a specific conduct level, and a chart hangs on the wall with a slot for each student to display their current card. Every student starts off the day with a green card in their slot, and each student's displayed colored card is switched depending on how that individual acts over the course of the day. If behavior is exemplary the student gets to switch their displayed card up to gold; if behavior is inappropriate the student must switch their card down to yellow. The state of the card displayed is fluid, and can change as many times as is appropriate daily. Each card move down the rank is accompanied by a warning from the teacher, and each card move up the rank is coupled with praise for that student. Once a student reaches a red card level, disciplinary action is typically taken, whether that be a call to the student's parents, a trip down to the office to visit the school principal, etc. Whether the cards are adjusted by students or the teacher is left to the teacher's discretion.

![alt tag](https://cloud.githubusercontent.com/assets/16564250/19530478/e7246ce4-95e8-11e6-9f6d-585bfbc1121c.jpg)

#### How this GUI works:
The base premise is the same as the physical hanging card charts in this application. I envision the GUI to run on a tablet or a computer visible to the students as are the charts that hang on classroom walls. Students or teachers can adjust a specific student's current displayed card color with one click and get back to the teaching lesson at hand. In addition to monitoring the daily behavior, points are awarded in differing amounts to a student dependent upon the color of their card displayed at the end of each day. At the end of the week, rewards and prizes can be given out to students based upon the points they accumulate. The GUI itself allows teachers to add or remove students to the displayed chart to reflect classroom shifts throughout the year, and quickly and easily reset the cards back to green and update the students' earned points for each new day of class. As opposed to physical charts, this GUI saves time for the teachers, allows students more interaction with technology, and reduces space on already cluttered classroom walls.
***
[return to my works in progress](https://github.com/joshlaplante/works-in-progress)
