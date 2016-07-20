import tkinter, student_db
from PIL import ImageTk, Image

#create window
window = tkinter.Tk()
#title window
window.title("Student Card Chart GUI")
#size window
window.geometry("1000x700")
#color window
window.configure(background = "azure")

#make exit function
def exitGUI():
    window.destroy()
    
#set menu tear off to false
window.option_add('*tearOff', False)
#create menubar
menuBar = tkinter.Menu(window)
window['menu'] = menuBar
#add menubar items
menu_file = tkinter.Menu(menuBar)
menu_edit = tkinter.Menu(menuBar)
menuBar.add_cascade(menu = menu_file, label = "File")
menuBar.add_cascade(menu = menu_edit, label = "Edit")
#add file_menu items
menu_file.add_command(label = "Exit", command = exitGUI)


#make card space
cardSpace = tkinter.Frame(window, bg = "azure")
cardSpace.grid(row = 0, column = 0)

#make button space
buttonSpace = tkinter.Frame(window, bg = "azure")
buttonSpace.grid(row = 1, column = 1)



#fill cardSpace with student cards
def fillWindow():
    #loops through returned student info values
    for line in (student_db.viewAll()):
        #create label text
        labelText = "ID: " + str(line[0]) + "\n" + \
                    "Name: " + str(line[1]) + "\n" + \
                    "Card Color: " + str(line[2]) + "\n" + \
                    "Weekly Points: " + str(line[3])
        #create student card frame
        cardFrame = tkinter.Frame(cardSpace, bg = "pale goldenrod", \
                              relief = 'ridge', \
                              borderwidth = 1)
        cardFrame.grid(padx = 5, pady = 5, row = 0, column = line[0])
        #add label with text to frame
        studentInfo = tkinter.Label(cardFrame, text = labelText, \
                                bg = "pale goldenrod")
        studentInfo.grid()
        #add correct card color to frame
        if line[2] == 'green':
            orgGreenImage = Image.open('card_green.png')
            orgGreenImage = orgGreenImage.resize((95,95),Image.ANTIALIAS)
            greenImage = ImageTk.PhotoImage(orgGreenImage)
            greenImage.image = greenImage
            photo = tkinter.Label(cardFrame, image = greenImage.image, \
                                  bg = "pale goldenrod").grid()
        elif line[2] == 'yellow':
            orgYellowImage = Image.open('card_yellow.png')
            orgYellowImage = orgYellowImage.resize((95,95),Image.ANTIALIAS)
            yellowImage = ImageTk.PhotoImage(orgYellowImage)
            yellowImage.image = yellowImage
            photo = tkinter.Label(cardFrame, image = yellowImage.image, \
                                  bg = "pale goldenrod").grid()
        elif line[2] == 'orange':
            orgOrangeImage = Image.open('card_orange.png')
            orgOrangeImage = orgOrangeImage.resize((95,95),Image.ANTIALIAS)
            orangeImage = ImageTk.PhotoImage(orgOrangeImage)
            orangeImage.image = orangeImage
            photo = tkinter.Label(cardFrame, image = orangeImage.image, \
                                  bg = "pale goldenrod").grid()
        else:
            orgRedImage = Image.open('card_red.png')
            orgRedImage = orgRedImage.resize((95,95),Image.ANTIALIAS)
            redImage = ImageTk.PhotoImage(orgRedImage)
            redImage.image = redImage
            photo = tkinter.Label(cardFrame, image = redImage.image, \
                                  bg = "pale goldenrod").grid()
        #add card turn button to frame
        button = tkinter.Button(cardFrame, text = 'Turn Card', \
                                command = lambda name = str(line[1]): \
                                cardTurnClick(name))
        button.grid(pady = (0,5))


#setup card turn button
def cardTurnClick(student):
    student_db.turnCard(student)
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()

#setup card reset button
def resetCardsClick():
    student_db.resetAllCards()
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()

#make card reset button
resetCardsButton = tkinter.Button(buttonSpace, text = 'Reset All Cards', \
                             command = resetCardsClick )
resetCardsButton.grid(row = 2, column = 5, pady = (20,5))

#setup add points button
def pointsAddClick():
    student_db.addPoints()
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()
    
#make add points button
pointsAddButton = tkinter.Button(buttonSpace, text = "Add Today's Points", \
                              command = pointsAddClick )
pointsAddButton.grid(row = 3, column = 5, pady = (0,5))


#setup point reset button
def resetPointsClick():
    student_db.resetPoints()
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()
    

#make point reset button
resetPointsButton = tkinter.Button(buttonSpace, text = "Reset Weekly Points", \
                                   command = resetPointsClick )
resetPointsButton.grid(row = 4, column = 5, pady = (0,5))



fillWindow()

window.mainloop()

print(u'\U263A')
