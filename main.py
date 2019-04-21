import mysql.connector as ms
import tkinter as tk
from db_credentials import setu
from members import *
from books import *
from reg_window import *
from book_window import *
from borrow_window import *

#Upd8 books, member
#login - db - logout
#clock logo
#frontend


mukhya = tk.Tk()
mukhya.title("School of Computer Engineering : Library")
mukhya.geometry("900x600")
act_reg_win = tk.Button(mukhya, text="Register Member", command = start_reg_win)
act_addbook_win = tk.Button(mukhya, text="Add Books", command = start_addbook_win)
act_listAllbooks_win = tk.Button(mukhya, text="All books", command = start_listAllbooks_win)
act_searchBook_win = tk.Button(mukhya, text="Search Book", command = start_searchBook_win)
act_issueBook_win = tk.Button(mukhya, text="Issue Book", command = start_issueBook_win)
act_returnBook_win = tk.Button(mukhya, text="Return Book", command = start_returnBook_win)
act_listAll_members_win = tk.Button(mukhya, text="Search members", command = start_listAll_members)
#act_upd8Book_win = tk.Button(mukhya, text="Update Book Detail", command = start_upd8Book_win)
act_unreturned_books = tk.Button(mukhya, text="Issued Books", command = start_unreturnedBooks_win)




act_reg_win.pack()  #
act_addbook_win.pack() #
act_listAllbooks_win.pack() #
act_searchBook_win.pack() #
act_issueBook_win.pack()
act_listAll_members_win.pack()
act_returnBook_win.pack()
act_unreturned_books.pack()
#act_upd8Book_win.pack()
mukhya.mainloop()


#book = search_book('title','')
#print(book)
