from tkinter import *

window = Tk()
window.title('School reg form')

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

birthDate_lbl = Label(window,text = 'Enter your birth date ===>').grid(row = 3, column = 0, padx = 10, pady = 10)
birthDate_entry = Entry(window,text = 'Enter your birth date ===>')

birthDate_entry.grid(row = 3, column = 1, padx = 10, pady = 10)

frm_3 = LabelFrame(window)
gender_lst = ['male','female']
r = StringVar()
r.set(gender_lst[0])

d = StringVar()
ethnicityLst = ['African Amercian','Hispanic/Latino','Asian','Caucasian','Native American/Alaskan','Hawaiian/Pacific Islander','Middle Eastern','Prefer not to answer','Other']
d.set(ethnicityLst[0])

gender_lbl = Label(frm_3,text = 'Enter your gender ===>').grid(row = 4, column = 0, padx = 10, pady = 10)
gender_drop = OptionMenu(frm_3,r,*gender_lst)

ethnicity_lbl = Label(frm_3,text = 'Enter your ethnicity ===>').grid(row = 5, column = 0, padx = 10, pady = 10)
ethnicity_drop = OptionMenu(frm_3,d,*ethnicityLst)

frm_3.grid(row = 4, column = 0, padx = 10, pady = 10)
gender_drop.grid(row = 4, column = 1, padx = 10, pady = 10)
ethnicity_drop.grid(row = 5, column = 1, padx = 10, pady = 10)

window.mainloop()