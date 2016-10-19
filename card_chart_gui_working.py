from tkinter import *
from tkinter import ttk
import student_db as db
from PIL import ImageTk, Image

class GUIWindow():
    def __init__(self, master):
        

        #title window
        master.title("Student Card Chart GUI")
        #size window
        master.geometry("1080x720")
        master.resizable(False,False)
        #color window
        master.configure(background = "azure")

        #setup card images
        self.orgGreenImage = Image.open('card_green.png')
        self.orgGreenImage = self.orgGreenImage.resize((50,50),Image.ANTIALIAS)
        self.greenImage = ImageTk.PhotoImage(self.orgGreenImage)
        self.greenImage.image = self.greenImage

        self.orgYellowImage = Image.open('card_yellow.png')
        self.orgYellowImage = self.orgYellowImage.resize((50,50),Image.ANTIALIAS)
        self.yellowImage = ImageTk.PhotoImage(self.orgYellowImage)
        self.yellowImage.image = self.yellowImage

        self.orgOrangeImage = Image.open('card_orange.png')
        self.orgOrangeImage = self.orgOrangeImage.resize((50,50),Image.ANTIALIAS)
        self.orangeImage = ImageTk.PhotoImage(self.orgOrangeImage)
        self.orangeImage.image = self.orangeImage

        self.orgRedImage = Image.open('card_red.png')
        self.orgRedImage = self.orgRedImage.resize((50,50),Image.ANTIALIAS)
        self.redImage = ImageTk.PhotoImage(self.orgRedImage)
        self.redImage.image = self.redImage

        self.orgGoldImage = Image.open('card_gold.png')
        self.orgGoldImage = self.orgGoldImage.resize((50,50),Image.ANTIALIAS)
        self.goldImage = ImageTk.PhotoImage(self.orgGoldImage)
        self.goldImage.image = self.goldImage

        #set menu tear off to false
        master.option_add('*tearOff', False)
        #create menubar
        self.menuBar = Menu(master)
        master['menu'] = self.menuBar
        #add menubar items
        self.menu_file = Menu(self.menuBar)
        self.menu_edit = Menu(self.menuBar)
        self.menuBar.add_cascade(menu = self.menu_file, label = "File")
        self.menuBar.add_cascade(menu = self.menu_edit, label = "Edit")
        #add file_menu items
        self.menu_file.add_command(label = "Exit", command = self.exitGUI)
        #add edit_menu items
        self.menu_edit.add_command(label = "Add New Student", command = lambda master = master: self.addStudent(master))
        self.menu_edit.add_command(label = "Delete Student", command = lambda master = master: self.deleteStudent(master))
        self.menu_edit.add_command(label = "Reset All Cards", command = self.resetCardsClick )
        self.menu_edit.add_command(label = "Add Today's Points", command = self.pointsAddClick )
        self.menu_edit.add_command(label = "Reset Weekly Points", command = self.resetPointsClick)

        #make card space
        self.cardSpace = Frame(master, bg = "azure")
        self.cardSpace.grid(row = 0, column = 0)

    #setup exit item
    def exitGUI(self):
        self.destroy()

    #setup card space refresh
    def refreshCardSpace(self):
        for widget in self.cardSpace.winfo_children():
            widget.destroy()
        self.fillWindow()

    #setup card turn up button
    def cardTurnUpClick(self,student):
        db.turnCardUp(student)
        self.refreshCardSpace()

    #setup card turn down button
    def cardTurnDownClick(self,student):
        db.turnCardDown(student)
        self.refreshCardSpace()

    #setup card reset item
    def resetCardsClick(self):
        db.resetAllCards()
        self.refreshCardSpace()

    #setup add points item
    def pointsAddClick(self):
        db.addPoints()
        self.refreshCardSpace()

    #setup point reset item
    def resetPointsClick(self):
        db.resetPoints()
        self.refreshCardSpace()

    #setup add student item
    def addStudent(self, master):
        #create new window
        self.addWindow = Toplevel(master)
        #size and color window
        self.addWindow.geometry("160x100")
        self.addWindow.configure(background = 'azure')
        #create entry label
        self.addLabel = Label(self.addWindow, bg = 'azure', \
                              text = "Enter New Student's Name: ")
        self.addLabel.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        #create entry field
        self.addEntry = Entry(self.addWindow)
        self.addEntry.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
        #create add and cancel buttons
        self.addButton = Button(self.addWindow, text = "Add Student", command = self.addClick)
        self.addButton.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.addCancel = Button(self.addWindow, text = "Cancel", command = self.addCancelClick)
        self.addCancel.grid(row = 2, column = 1, padx = 5, pady = 5)

    #setup add student function
    def addClick(self):
        self.newName = self.addEntry.get()
        db.newStudent(self.newName)
        self.addWindow.destroy()
        self.refreshCardSpace()

    #setup cancel function
    def addCancelClick(self):
        self.addWindow.destroy()

    #setup delete student function
    def deleteStudent(self, master):
        self.deleteWindow = Toplevel(master)
        self.deleteWindow.geometry("200x150")
        self.deleteWindow.configure(background = 'azure')
        #create entry label
        self.deleteLabel = Label(self.deleteWindow, bg = 'azure', \
                              text = "Enter Name of Student to Delete: ")
        self.deleteLabel.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        #create entry field
        self.deleteEntry = Entry(self.deleteWindow)
        self.deleteEntry.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
        #create delete and cancel buttons
        self.deleteButton = Button(self.deleteWindow, text = "Delete Student", command = self.deleteClick)
        self.deleteButton.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.deleteCancel = Button(self.deleteWindow, text = "Cancel", command = self.deleteCancelClick)
        self.deleteCancel.grid(row = 2, column = 1, padx = 5, pady = 5)

    #setup add student function
    def deleteClick(self):
        self.deleteName = self.deleteEntry.get()
        if db.removeStudent(self.deleteName) == False:
            self.deleteFail = Label(self.deleteWindow, bg = 'azure', \
                                    text = "Student Name Not Found...")
            self.deleteFail.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
        else:
            self.deleteWindow.destroy()
            self.refreshCardSpace()

    #setup cancel function
    def deleteCancelClick(self):
        self.deleteWindow.destroy()
        
        


    #fill cardSpace with student cards
    def fillWindow(self):
        #loops through returned student info values
        for line in (db.viewAll()):
            #create label text
            self.labelText = "Name: " + str(line[1]) + "\n" + \
                        "Card Color: " + str(line[2]) 
            #create student card frame
            self.cardFrame = Frame(self.cardSpace, bg = "pale goldenrod", \
                                  relief = 'ridge', borderwidth = 1)
            self.cardFrame.grid(padx = (5,0), pady = 5, row = 0, column = line[0])
            #add label with text to frame
            self.studentInfo = Label(self.cardFrame, text = self.labelText, \
                                    bg = "pale goldenrod")
            self.studentInfo.grid()
            #add correct card color to frame
            if line[2] == 'green':
                photo = Label(self.cardFrame, image = self.greenImage.image, \
                                      bg = "pale goldenrod").grid()
            elif line[2] == 'yellow':
                photo = Label(self.cardFrame, image = self.yellowImage.image, \
                                      bg = "pale goldenrod").grid()
            elif line[2] == 'orange':
                photo = Label(self.cardFrame, image = self.orangeImage.image, \
                                      bg = "pale goldenrod").grid()
            elif line[2] == 'red':
                photo = Label(self.cardFrame, image = self.redImage.image, \
                                      bg = "pale goldenrod").grid()
            else:
                photo = Label(self.cardFrame, image = self.goldImage.image, \
                                      bg = "pale goldenrod").grid()
                
            #add card turn up button to frame
            self.turnUpButton = Button(self.cardFrame, text = 'Turn Card Up', \
                                    command = lambda name = str(line[1]): \
                                    self.cardTurnUpClick(name))
            self.turnUpButton.grid(pady = (5,0))
            #add card turn down button to frame
            self.turnDownButton = Button(self.cardFrame, text = 'Turn Card Down', \
                                    command = lambda name = str(line[1]): \
                                    self.cardTurnDownClick(name))
            self.turnDownButton.grid(pady = (5,0))
            #create point label and text
            self.pointText = "Weekly Points: " + str(line[3])
            self.studentPoints = Label(self.cardFrame, text = self.pointText, \
                                    bg = "pale goldenrod")
            self.studentPoints.grid()
        


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
    root = Tk()
    window = GUIWindow(root)
    window.fillWindow()
    root.mainloop()

if __name__ == "__main__": main()

