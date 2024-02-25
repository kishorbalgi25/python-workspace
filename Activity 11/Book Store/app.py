from tkinter import *
from database import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.dataBase = DataBase()
        self.title("BookStore")

        # Labels and Entrys.
        self.titleLabel = Label(self, text="Title")
        self.titleLabel.grid(row=0, column=0)
        self.titleVar = StringVar()
        self.titleEntry = Entry(self, textvariable=self.titleVar)
        self.titleEntry.grid(row=0, column=1)
        self.authorLabel = Label(self, text="Author")
        self.authorLabel.grid(row=0, column=2)
        self.authorVar = StringVar()
        self.authorEntry = Entry(self, textvariable=self.authorVar)
        self.authorEntry.grid(row=0, column=3)
        self.yearLabel = Label(self, text="Year")
        self.yearLabel.grid(row=1, column=0)
        self.yearVar = StringVar()
        self.yearEntry = Entry(self, textvariable=self.yearVar)
        self.yearEntry.grid(row=1, column=1)
        self.isbnLabel = Label(self, text="ISBN")
        self.isbnLabel.grid(row=1, column=2)
        self.isbnVar = StringVar()
        self.isbnEntry = Entry(self, textvariable=self.isbnVar)
        self.isbnEntry.grid(row=1, column=3)
        
        # List of the items and the scrollbar.
        self.itemsList = Listbox(self, height=6, width=35)
        self.itemsList.grid(row=2, column=0, rowspan=6,columnspan=2)
        self.itemsListScrollbar = Scrollbar(self)
        self.itemsListScrollbar.grid(row=2, column=2, rowspan=6)
        self.itemsList.configure(yscrollcommand=self.itemsListScrollbar.set)
        self.itemsListScrollbar.configure(command=self.itemsList.yview)
        self.itemsList.bind("<<ListboxSelect>>", self.getSelectedRow)
        
        # Actions Buttons.
        self.viewButton = Button(self, text="View All", width=12, command=self.viewDataCommand)
        self.viewButton.grid(row=2, column=3)
        self.addButton = Button(self, text="Add Entry", width=12, command=self.insertDataCommand)
        self.addButton.grid(row=4, column=3)
        self.updateButton = Button(self, text="Update Entry", width=12, command=self.updateDataCommand)
        self.updateButton.grid(row=5, column=3)
        self.deleteButton = Button(self, text="Delete Entry", width=12, command=self.deleteDataCommand)
        self.deleteButton.grid(row=6, column=3)
        self.closeButton = Button(self, text="Close", width=12, command=self.closeApplication)
        self.closeButton.grid(row=7, column=3)

        self.mainloop()

    def closeApplication(self):
        self.destroy()

    def insertInputValues(self, item):
        self.titleEntry.delete(0, END)
        self.titleEntry.insert(END, item[1])
        self.authorEntry.delete(0, END)
        self.authorEntry.insert(END, item[2])
        self.yearEntry.delete(0, END)
        self.yearEntry.insert(END, item[3])
        self.isbnEntry.delete(0, END)
        self.isbnEntry.insert(END, item[4])

    def getSelectedRow(self, event):
        try:
            global selectedRow
            index = self.itemsList.curselection()
            selectedRow = self.itemsList.get(index[0])
            self.insertInputValues(selectedRow)
        except IndexError:
            pass

    def viewDataCommand(self):
        query = self.dataBase.viewData()
        self.itemsList.delete(0, END)
        for row in query:
            self.itemsList.insert(END, row)

    def searchDataCommand(self):
        title = self.titleVar.get()
        author = self.authorVar.get()
        year = self.yearVar.get()
        isbn = self.isbnVar.get()

        searchQuery = self.dataBase.searchData(title, author, year, isbn)
        self.itemsList.delete(0, END)
        for row in searchQuery:
            self.itemsList.insert(END, row)

    def insertDataCommand(self):
        title = self.titleVar.get()
        author = self.authorVar.get()
        year = self.yearVar.get()
        isbn = self.isbnVar.get()

        self.dataBase.insertData(title, author, year, isbn)

        self.itemsList.delete(0, END)
        self.itemsList.insert(END, (title, author, year, isbn))

    def deleteDataCommand(self):
        itemId = selectedRow[0]
        self.dataBase.deleteData(itemId)

    def updateDataCommand(self):
        id = selectedRow[0]
        title = self.titleVar.get()
        author = self.authorVar.get()
        year = self.yearVar.get()
        isbn = self.isbnVar.get()

        print((id, title, author, year, isbn))
        self.dataBase.updateData(id, title, author, year, isbn)

App()