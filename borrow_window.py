import tkinter as tk
from tkinter import *
from tkinter import messagebox
from books import *
from borrows import issue_book, return_book1, getAllUnreturnedBooks, getUnreturnedBooks
from members import *
from book_window import start_searchBook_win

def clearTable(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)


## Issueing a book
def start_issueBook_win():
    def trig_issue_book():
        status = issue_book(mem_name.get(), to_be_issued_book_accn.get())
        if status == -1:
            messagebox.showinfo("Error","Member doesnt exist")
            issue_win.destroy()
        elif status == -2:
            messagebox.showinfo("Error","Book is not available")
            issue_win.destroy()
        else:
            messagebox.showinfo("Success","Book issued Successfully")
            issue_win.destroy()

    issue_win = tk.Tk()
    issue_win.title("Issue a book")
    issue_win.geometry("900x600")

    Label(issue_win, text="Member Name:").grid(row=0,column=1);
    Label(issue_win, text="Accession Number:").grid(row=1,column=1);
    mem_name = Entry(issue_win)
    to_be_issued_book_accn = Entry(issue_win)

    Button(issue_win, text='Issue Book', command = trig_issue_book).grid(row=3,column=1, sticky=W, pady=4)
    Button(issue_win, text='Cancle', command = issue_win.destroy).grid(row=3,column=2,sticky=W, pady=4)
    Button(issue_win, text='Search Book', command = start_searchBook_win).grid(row=1,column=4, sticky=W, pady=4)

    to_be_issued_book_accn.grid(row=1,column=2)
    mem_name.grid(row=0,column=2)


#books issued by particular member search


def start_returnBook_win():
    return_win = tk.Tk()
    return_win.title("Return Book")
    return_win.geometry("900x600")

    def trig_return_book():
        mem_id = get_memid(mem_name.get())
        if mem_id == -1:
            messagebox.showinfo("Error","Member doesnot Exist, (\nCheck Spelling)")
            return_win.destroy()
            start_returnBook_win()
        else:
            return_book1(mem_id, to_be_returned_book_accn.get(), remarks.get())
            #check if
            messagebox.showinfo("Success","Book returned Successfully")
            return_win.destroy()


    Label(return_win, text="Member Name:").grid(row=1,column=1)
    Label(return_win, text="accession Number:").grid(row=2,column=1)
    Label(return_win, text="Remarks").grid(row=3,column=1)

    mem_name = Entry(return_win)
    to_be_returned_book_accn = Entry(return_win)
    remarks  = Entry(return_win)

    Button(return_win, text="Return Book", command = trig_return_book).grid(row = 4, column=1, sticky=W, pady=4)
    Button(return_win, text="Cancle", command = return_win.destroy).grid(row = 4, column=2, sticky=W, pady=4)
    mem_name.grid(row=1,column=2)
    to_be_returned_book_accn.grid(row=2,column=2)
    remarks.grid(row=3,column=2)


def start_unreturnedBooks_win():
    book_win = tk.Tk()
    #book_win.overrideredirect(1)
    book_win.title("Issued Book")
    book_win.geometry("960x600")
    v=IntVar()
    flag=True;
    def searchThem():
        clearTable(tree)
        print(tkvar.get())

        if(tkvar.get() == 'Member'):
            skey = "full_name"
        elif(tkvar.get() == 'Title'):
            skey = "title"
        elif(tkvar.get() == 'Accession no'):
            skey = "book_accession_number"

        unreturnedBooks = getUnreturnedBooks(skey, searchField.get())
        if unreturnedBooks == -1:
            messagebox.showinfo("","Zero books issued for your search query")
            book_win.destroy()
        else:
            for book in unreturnedBooks:
                tree.insert('',0, text='', value = book)


    def selectItem(a):
        def trig_return_book():
                print(focus)
                val = focus['values']
                print(val)
                msg = "Return Book: "+val[1]+" issued by: "+val[2]
                x = messagebox.askyesno("Return Book",msg)
                print(x)

                if(x):
                    mem_id = get_memid(val[2])
                    return_book1(mem_id, val[0],'')
                    book_win.destroy()

        CurItem = tree.focus()
        #print(tree.item(CurItem))
        Button(book_win, text='Return Book', command=trig_return_book).pack()
        focus = tree.item(CurItem)




    tkvar = StringVar(book_win)
    Label(book_win, text="Search Book By :").pack()
    searchField = Entry(book_win)
    searchBy = ['Member','Title','Accession No']
    tkvar.set('Title')
    popupMenu = OptionMenu(book_win, tkvar, *searchBy)
    searchField.pack()
    popupMenu.pack()

    Button(book_win, text='Search',command=searchThem).pack()
    Button(book_win, text='Exit', command = book_win.destroy)



    tree = ttk.Treeview(book_win)
    tree["column"] = ("acn", "title","issued to","issue date","Mobile No.")
    tree.column("acn", width=100)
    tree.column("title", width=150)
    tree.column("issued to", width=120)
    tree.column("issue date", width=110)
    tree.column("Mobile No.", width=110)
    tree.heading("acn", text="Accession No.")
    tree.heading("title", text="Title")
    tree.heading("issued to", text="Issued to")
    tree.heading("issue date", text="Issue Date")
    tree.heading("Mobile No.", text="Mobile No.")
    tree.pack()

    if(flag):
        AllUnreturnedBooks = getAllUnreturnedBooks();
        for book in AllUnreturnedBooks:
            tree.insert('',0, text='', value = book)
    flag=False;

    tree.bind('<ButtonRelease-1>', selectItem)

    mainloop()
