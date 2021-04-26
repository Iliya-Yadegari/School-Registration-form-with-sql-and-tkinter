from tkinter import *


window = Tk()


frm_1 = LabelFrame(window,text = 'Additional documents for registration')
add_lbl = Label(frm_1,text = '• Original Certified Birth Certificate\n• Original Social Security Card\n• Current Immunization Form\n• Current Proofs of Residence (ex. power, water or gas bill)\n• Other').grid(row = 0, column = 0, padx = 10, pady = 10)

frm_1.grid(row = 0, column = 0, padx = 10, pady = 10)

frm_2 = LabelFrame(window,text = 'Name')
name_lbl = Label(window,text = 'Enter your first name ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
name_entry = Entry(frm_2)
lastName_lbl = Label(frm_2,text = 'Enter your last name ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
lastName_entry = Entry(frm_2)

name_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
lastName_entry.grid(row = 2, column = 1, padx = 10, pady = 10)
frm_2.grid(row = 1, column = 0, padx = 10, pady = 10)


window.mainloop()