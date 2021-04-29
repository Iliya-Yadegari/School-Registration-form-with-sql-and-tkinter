from tkinter import *

window = Tk()
window.title('School reg form')

frm_1 = LabelFrame(window,text = 'Additional documents for registration')
add_lbl = Label(frm_1,text = '• Original Certified Birth Certificate\n• Original Social Security Card\n• Current Immunization Form\n• Current Proofs of Residence (ex. power, water or gas bill)\n• Other').grid(row = 0, column = 0, padx = 10, pady = 10)

frm_1.grid(row = 0, column = 0, padx = 10, pady = 10)

frm_2 = LabelFrame(window,text = 'Name')
name_lbl = Label(frm_2,text = 'Enter your first name ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
name_entry = Entry(frm_2)
lastName_lbl = Label(frm_2,text = 'Enter your last name ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
lastName_entry = Entry(frm_2)

name_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
lastName_entry.grid(row = 2, column = 1, padx = 10, pady = 10)
frm_2.grid(row = 1, column = 0, padx = 10, pady = 10)

birthDate_lbl = Label(frm_2,text = 'Enter your birth date ===>').grid(row = 3, column = 0, padx = 10, pady = 10)
birthDate_entry = Entry(frm_2)

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

email_lbl = Label(frm_3,text = 'Enter your email ===>').grid(row = 6, column = 0, padx = 10, pady = 10)
email_entry = Entry(frm_3)

frm_3.grid(row = 4, column = 0, padx = 10, pady = 10)
gender_drop.grid(row = 4, column = 1, padx = 10, pady = 10)
ethnicity_drop.grid(row = 5, column = 1, padx = 10, pady = 10)
email_entry.grid(row = 6, column = 1, padx = 10, pady = 10)

frm_4 = LabelFrame(window)

m = IntVar()

entryYear_lbl = Label(frm_4,text = 'Enter your entry year ===>').grid(row = 6, column = 2, padx = 10, pady = 10)
entryYear_entry = Entry(frm_4)
grade_lbl = Label(frm_4,text = 'Enter your grade ===>').grid(row = 7, column = 2, padx = 10, pady = 10)
grade_entry = Entry(frm_4)
semester_lbl = Label(frm_4,text = 'Enter your semester ===>').grid(row = 8, column = 2, padx = 10, pady = 10)
semester_entry = Entry(frm_4)

radioBut_lbl = Label(frm_4,text = 'Have you previously applied to or attended this school?').grid(row = 9, column = 0, padx = 10, pady = 10)

Radiobutton(frm_4,text = 'Yes',variable = m,value = 1).grid(row = 10, column = 2, padx = 10, pady = 10)
Radiobutton(frm_4,text = 'no',variable = m,value = 1).grid(row = 10, column = 3, padx = 10, pady = 10)

entryYear_entry.grid(row = 6, column = 3, padx = 10, pady = 10)
grade_entry.grid(row = 7, column = 3, padx = 10, pady = 10)
semester_entry.grid(row = 8, column = 3, padx = 10, pady = 10)
frm_4.grid(row = 6, column = 2, padx = 10, pady = 10)

frm_5 = LabelFrame(window,text = 'Address')

streetAdd_lbl = Label(frm_5,text = 'Street Address ===>').grid(row = 0, column = 2, padx = 10, pady = 10)
streetAdd_entry = Entry(frm_5)
streetAdd2_lbl = Label(frm_5,text = 'Street Address Line 2 ===>').grid(row = 1, column = 2, padx = 10, pady = 10)
streetAdd2_entry = Entry(frm_5)
city_lbl = Label(frm_5,text = 'City ===>').grid(row = 2, column = 2, padx = 10, pady = 10)
city_entry = Entry(frm_5)
state_lbl = Label(frm_5,text = 'State/Province ===>').grid(row = 3, column = 2, padx = 10, pady = 10)
state_entry = Entry(frm_5)
homeNum_lbl = Label(frm_5,text = 'Home Phone Number ===>').grid(row = 4, column = 2, padx = 10, pady = 10)
homeNum_entry = Entry(frm_5)
cellNum_lbl = Label(frm_5,text = 'Cell Phone Number ==>').grid(row = 5, column = 2, padx = 10, pady = 10)
cellNum_entry = Entry(frm_5)

streetAdd_entry.grid(row = 0, column = 3, padx = 10, pady = 10)
streetAdd2_entry.grid(row = 1, column = 3, padx = 10, pady = 10)
city_entry.grid(row = 2, column = 3, padx = 10, pady = 10)
state_entry.grid(row = 3, column = 3, padx = 10, pady = 10)
homeNum_entry.grid(row = 4, column = 3, padx = 10, pady = 10)
cellNum_entry.grid(row = 5, column = 3, padx = 10, pady = 10)
frm_5.grid(row = 0, column = 2, padx = 10, pady = 10)

window.mainloop()