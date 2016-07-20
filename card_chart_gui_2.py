from tkinter import *
from tkinter import ttk
import student_db as db
from PIL import ImageTk, Image

#create window
window = Tk()
#title window
window.title("Student Card Chart GUI")
#size window
window.geometry("1000x700")
#color window
window.configure(background = "azure")

#setup card images
orgGreenImage = Image.open('card_green.png')
orgGreenImage = orgGreenImage.resize((50,50),Image.ANTIALIAS)
greenImage = ImageTk.PhotoImage(orgGreenImage)
greenImage.image = greenImage

orgYellowImage = Image.open('card_yellow.png')
orgYellowImage = orgYellowImage.resize((50,50),Image.ANTIALIAS)
yellowImage = ImageTk.PhotoImage(orgYellowImage)
yellowImage.image = yellowImage

orgOrangeImage = Image.open('card_orange.png')
orgOrangeImage = orgOrangeImage.resize((50,50),Image.ANTIALIAS)
orangeImage = ImageTk.PhotoImage(orgOrangeImage)
orangeImage.image = orangeImage

orgRedImage = Image.open('card_red.png')
orgRedImage = orgRedImage.resize((50,50),Image.ANTIALIAS)
redImage = ImageTk.PhotoImage(orgRedImage)
redImage.image = redImage

orgGoldImage = Image.open('card_gold.png')
orgGoldImage = orgGoldImage.resize((50,50),Image.ANTIALIAS)
goldImage = ImageTk.PhotoImage(orgGoldImage)
goldImage.image = goldImage

#make exit function
def exitGUI():
    window.destroy()

#setup card turn up button
def cardTurnUpClick(student):
    db.turnCardUp(student)
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()

#setup card turn down button
def cardTurnDownClick(student):
    db.turnCardDown(student)
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()

#setup card reset item
def resetCardsClick():
    db.resetAllCards()
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()

#setup add points item
def pointsAddClick():
    db.addPoints()
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()

#setup point reset item
def resetPointsClick():
    db.resetPoints()
    for widget in cardSpace.winfo_children():
        widget.destroy()
    fillWindow()
    
#set menu tear off to false
window.option_add('*tearOff', False)
#create menubar
menuBar = Menu(window)
window['menu'] = menuBar
#add menubar items
menu_file = Menu(menuBar)
menu_edit = Menu(menuBar)
menuBar.add_cascade(menu = menu_file, label = "File")
menuBar.add_cascade(menu = menu_edit, label = "Edit")
#add file_menu items
menu_file.add_command(label = "Exit", command = exitGUI)
#add edit_menu items
menu_edit.add_command(label = "Reset All Cards", command = resetCardsClick )
menu_edit.add_command(label = "Add Today's Points", command = pointsAddClick )
menu_edit.add_command(label = "Reset Weekly Points", command = resetPointsClick)

#make card space
cardSpace = Frame(window, bg = "azure")
cardSpace.grid(row = 0, column = 0)


#fill cardSpace with student cards
def fillWindow():
    #loops through returned student info values
    for line in (db.viewAll()):
        #create label text
        labelText = "ID: " + str(line[0]) + "\n" + \
                    "Name: " + str(line[1]) + "\n" + \
                    "Card Color: " + str(line[2]) 
        #create student card frame
        cardFrame = Frame(cardSpace, bg = "pale goldenrod", \
                              relief = 'ridge', \
                              borderwidth = 1)
        cardFrame.grid(padx = (5,0), pady = 5, row = 0, column = line[0])
        #add label with text to frame
        studentInfo = Label(cardFrame, text = labelText, \
                                bg = "pale goldenrod")
        studentInfo.grid()
        #add correct card color to frame
        if line[2] == 'green':
            photo = Label(cardFrame, image = greenImage.image, \
                                  bg = "pale goldenrod").grid()
        elif line[2] == 'yellow':
            photo = Label(cardFrame, image = yellowImage.image, \
                                  bg = "pale goldenrod").grid()
        elif line[2] == 'orange':
            photo = Label(cardFrame, image = orangeImage.image, \
                                  bg = "pale goldenrod").grid()
        elif line[2] == 'red':
            photo = Label(cardFrame, image = redImage.image, \
                                  bg = "pale goldenrod").grid()
        else:
            photo = Label(cardFrame, image = goldImage.image, \
                                  bg = "pale goldenrod").grid()
            
        #add card turn up button to frame
        button = Button(cardFrame, text = 'Turn Card Up', \
                                command = lambda name = str(line[1]): \
                                cardTurnUpClick(name))
        button.grid(pady = (5,0))
        #add card turn down button to frame
        button = Button(cardFrame, text = 'Turn Card Down', \
                                command = lambda name = str(line[1]): \
                                cardTurnDownClick(name))
        button.grid(pady = (5,0))
        #create point label and text
        pointText = "Weekly Points: " + str(line[3])
        studentPoints = Label(cardFrame, text = pointText, \
                                bg = "pale goldenrod")
        studentPoints.grid()
        


'''
#make button space
buttonSpace = Frame(window, bg = "azure")
buttonSpace.grid(row = 1, column = 1)

#make card reset button
resetCardsButton = Button(buttonSpace, text = 'Reset All Cards', \
                             command = resetCardsClick )
resetCardsButton.grid(row = 2, column = 5, pady = (20,5))

    
#make add points button
pointsAddButton = Button(buttonSpace, text = "Add Today's Points", \
                              command = pointsAddClick )
pointsAddButton.grid(row = 3, column = 5, pady = (0,5))


#make point reset button
resetPointsButton = Button(buttonSpace, text = "Reset Weekly Points", \
                                   command = resetPointsClick )
resetPointsButton.grid(row = 4, column = 5, pady = (0,5))
'''

def main(): 
    fillWindow()
    window.mainloop()

if __name__ == "__main__": main()

