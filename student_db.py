import sqlite3, random


#make/connect to student database
conn = sqlite3.connect('student_chart.db')


#create student cards table if it's not there
def createTable():
    conn.execute("CREATE TABLE if not exists \
                STUDENT_CARDS( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                NAME TEXT, \
                CARD_COLOR TEXT, \
                WEEKLY_POINTS INT);")


#function to add new students to table, start with green card color and 0 points
def newStudent(name, cardColor = 'green', weeklyPoints = 0):
    #grab new student values
    newValues = " '{}', '{}', '{}' ".format(name, cardColor, weeklyPoints)
    sql_string = "INSERT INTO STUDENT_CARDS \
                (NAME, CARD_COLOR, WEEKLY_POINTS) \
                VALUES ({});".format(newValues)
    #insert values to table
    conn.execute(sql_string)
    conn.commit()
#    readout = conn.execute("SELECT * FROM STUDENT_CARDS;")
#    lines = readout.fetchall()
#    for line in lines:
#        print(line)

    
#function to remove student
def removeStudent(name):
    #check all names currently in db
    read_string = "SELECT * FROM STUDENT_CARDS"
    readout = conn.execute(read_string)
    lines = readout.fetchall()
    #create name check variable with 0 value
    nameCheck = 0
    for line in lines:
        if str(name) == str(line[1]):
            #if entered name is in db, set name check variable to 1
            nameCheck = 1
    #if name was found, delete student with that name
    if nameCheck == 1:
        delete_string = "DELETE FROM STUDENT_CARDS WHERE NAME = '{}';".format(name)
        conn.execute(delete_string)
        conn.commit()
        return True
    #if no name matches, return false
    if nameCheck == 0:
        return False

#run table creation function
createTable()


#function to turn card color down for student
def turnCardDown(name):
    turnDown = True
    #get current card color for student
    read_string = "SELECT CARD_COLOR from STUDENT_CARDS \
                WHERE NAME = '{}';".format(name)
    cursor = conn.execute(read_string)
    #get data from cursor
    color = cursor.fetchone()[0]
    #set new color
    if color == "gold":
        newColor = "green"
    elif color == "green":
        newColor = "yellow"
    elif color == "yellow":
        newColor = "orange"
    elif color == "orange":
        newColor = "red"
    else:
        turnDown = False
    #update new color if not red
    if turnDown == True:
        nameToTurn = " '{}' ".format(name)
        updateColor = " '{}' ".format(newColor)
        update_string = "UPDATE STUDENT_CARDS SET CARD_COLOR = {} \
                    WHERE NAME = {};".format(updateColor,nameToTurn)
        conn.execute(update_string)
        conn.commit()
#    readout = conn.execute("SELECT * FROM STUDENT_CARDS;")
#    lines = readout.fetchall()
#    for line in lines:
#        print(line)


#function to turn card color up for student
def turnCardUp(name):
    turnUp = True
    #get current card color for student
    read_string = "SELECT CARD_COLOR from STUDENT_CARDS \
                WHERE NAME = '{}';".format(name)
    cursor = conn.execute(read_string)
    #get data from cursor
    color = cursor.fetchone()[0]
    #set new color
    if color == "red":
        newColor = "orange"
    elif color == "orange":
        newColor = "yellow"
    elif color == "yellow":
        newColor = "green"
    elif color == "green":
        newColor = "gold"
    else:
        turnUp = False
    #update new color if not gold
    if turnUp == True:
        nameToTurn = " '{}' ".format(name)
        updateColor = " '{}' ".format(newColor)
        update_string = "UPDATE STUDENT_CARDS SET CARD_COLOR = {} \
                    WHERE NAME = {};".format(updateColor,nameToTurn)
        conn.execute(update_string)
        conn.commit()
#    readout = conn.execute("SELECT * FROM STUDENT_CARDS;")
#    lines = readout.fetchall()
#    for line in lines:
#        print(line)


    
#function to change all cards back to green
def resetAllCards():
    reset_string = "UPDATE STUDENT_CARDS SET CARD_COLOR = 'green';"
    conn.execute(reset_string)
    conn.commit()
#    readout = conn.execute("SELECT * FROM STUDENT_CARDS;")
#    lines = readout.fetchall()
#    for line in lines:
#        print(line)


#function to add points for card color
def addPoints():
    #get student info
    read_string = "SELECT * FROM STUDENT_CARDS;"
    readout = conn.execute(read_string)
    lines = readout.fetchall()
    #add points based on card color by looping through student info
    for line in lines:
        if line[2] == 'gold':
            pointsToAdd = random.randint(16,20)
        elif line[2] == 'green':
            pointsToAdd = random.randint(11,15)
        elif line[2] == 'yellow':
            pointsToAdd = random.randint(6,10)
        elif line[2] == 'orange':
            pointsToAdd = random.randint(1,5)
        else:
            pointsToAdd = 0
        #get student's current points
        currentPoints = int(line[3])
        newPoints = currentPoints + pointsToAdd
        #turn newPoints into string
        pointsString = " '{}' ".format(newPoints)
        #get student name
        name = line[1]
        #update WeeklyPoints for student with newPoints
        updateString = "UPDATE STUDENT_CARDS SET WEEKLY_POINTS = {} \
                    WHERE NAME = '{}';".format(pointsString,name)
        conn.execute(updateString)
        conn.commit()
#    readout = conn.execute("SELECT * FROM STUDENT_CARDS;")
#    lines = readout.fetchall()
#    for line in lines:
#        print(line)

#function to reset weekly points
def resetPoints():
    reset_string = "UPDATE STUDENT_CARDS SET WEEKLY_POINTS = '0'"
    conn.execute(reset_string)
    conn.commit()
#    readout = conn.execute("SELECT * FROM STUDENT_CARDS;")
#    lines = readout.fetchall()
#    for line in lines:
#        print(line)


#function to view current student info
def viewAll():
    #get student info
    read_string = "SELECT * FROM STUDENT_CARDS;"
    readout = conn.execute(read_string)
    lines = readout.fetchall()
#    for line in lines:
#        print("ID:", line[0])
#        print("Name:", line[1])
#        print("Card Color:", line[2])
#        print("Weekly Points:", line[3])
#        print()
    return lines



