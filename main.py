from datetime import *
from tkinter import *
from dateutil import relativedelta

global clr_flag
global d_year
global d_months
global d_days
global years_value_label
global months_value_label
global weeks_value_label
global days_value_label
global hours_value_label
global minutes_value_label
global seconds_value_label


def clear_func():
    global clr_flag
    global d_year
    global d_months
    global d_days
    global years_value_label
    global months_value_label
    global weeks_value_label
    global days_value_label
    global hours_value_label
    global minutes_value_label
    global seconds_value_label
    b_day.delete(0, END)
    b_month.delete(0, END)
    b_year.delete(0, END)
    if clr_flag > 0:
        d_year.destroy()
        d_months.destroy()
        d_days.destroy()
        years_value_label.destroy()
        months_value_label.destroy()
        weeks_value_label.destroy()
        days_value_label.destroy()
        hours_value_label.destroy()
        minutes_value_label.destroy()
        seconds_value_label.destroy()


def cal_func():
    global clr_flag
    global d_year
    global d_months
    global d_days
    global years_value_label
    global months_value_label
    global weeks_value_label
    global days_value_label
    global hours_value_label
    global minutes_value_label
    global seconds_value_label
    clr_flag = 1
    if int(b_day.get()) <= 31:
        if int(b_month.get()) <= 12:
            if int(b_year.get()) >= 1901:
                last_two_digit = str(b_year.get())
                last_two_digit = last_two_digit[2:4]
                birth_date = str(b_day.get()+"/"+b_month.get()+"/"+last_two_digit)
                birth_date = datetime.strptime(birth_date, '%d/%m/%y')
                birth_date = birth_date.date()

                last_two_digit = str(t_year.get())
                last_two_digit = last_two_digit[2:4]
                today_date = str(t_day.get() + "/" + t_month.get() + "/" + last_two_digit)
                today_date = datetime.strptime(today_date, '%d/%m/%y')
                today_date = today_date.date()

                diff = relativedelta.relativedelta(today_date, birth_date)

                your_age = Label(root, text="Your age-", font=1, fg="blue")
                years = Label(root, text="Years", fg="blue")
                months = Label(root, text="Months", fg="blue")
                days = Label(root, text="Days", fg="blue")
                d_year = Label(root, text=diff.years, fg="black", font=1)
                d_months = Label(root, text=diff.months, fg="black", font=1)
                d_days = Label(root, text=diff.days, fg="black", font=1)

                f_blank = Label(root, text="   ")

                total_days = (today_date - birth_date).days
                total_weeks = total_days//7
                total_months = diff.months + (diff.years * 12)
                total_hours = total_days * 24
                total_minutes = total_hours * 60
                total_seconds = total_minutes * 60

                total_years_label = Label(root, text=f"Total Years: ", font=1, fg="blue")
                total_months_label = Label(root, text=f"Total Months: ", font=1, fg="blue")
                total_weeks_label = Label(root, text=f"Total Weeks: ", font=1, fg="blue")
                total_days_label = Label(root, text=f"Total Days: ", font=1, fg="blue")
                total_hours_label = Label(root, text=f"Total Hours: ", font=1, fg="blue")
                total_minutes_label = Label(root, text=f"Total Minutes: ", font=1, fg="blue")
                total_seconds_label = Label(root, text=f"Total Seconds: ", font=1, fg="blue")

                extra = Label(root, text="Extra: ", font=1, fg='blue')

                years_value_label = Label(root, text=diff.years, fg='black', font=1)
                months_value_label = Label(root, text=total_months, fg='black', font=1)
                weeks_value_label = Label(root, text=total_weeks, fg='black', font=1)
                days_value_label = Label(root, text=total_days, fg='black', font=1)
                hours_value_label = Label(root, text=total_hours, fg='black', font=1)
                minutes_value_label = Label(root, text=total_minutes, fg='black', font=1)
                seconds_value_label = Label(root, text=total_seconds, fg='black', font=1)

                your_age.grid(row=6, column=0, sticky='w')

                f_blank.grid(row=7, column=0, columnspan=1)

                years.grid(row=7, column=1)
                months.grid(row=7, column=2)
                days.grid(row=7, column=3)

                f_blank.grid(row=8, column=0)

                d_year.grid(row=8, column=1)
                d_months.grid(row=8, column=2)
                d_days.grid(row=8, column=3)

                extra.grid(row=9, column=0, sticky='w')

                total_years_label.grid(row=10, column=0, sticky='w')
                total_months_label.grid(row=11, column=0, sticky='w')
                total_weeks_label.grid(row=12, column=0, sticky='w')
                total_days_label.grid(row=13, column=0, sticky='w')
                total_hours_label.grid(row=14, column=0, sticky='w')
                total_minutes_label.grid(row=15, column=0, sticky='w')
                total_seconds_label.grid(row=16, column=0, sticky='w')

                years_value_label.grid(row=10, column=1)
                months_value_label.grid(row=11, column=1)
                weeks_value_label.grid(row=12, column=1)
                days_value_label.grid(row=13, column=1)
                hours_value_label.grid(row=14, column=1)
                minutes_value_label.grid(row=15, column=1)
                seconds_value_label.grid(row=16, column=1)
            else:
                clear_func()
        else:
            clear_func()
    else:
        clear_func()


root = Tk()
root.title("Age Calculator")

# From Part of Code -------------------------------------------------------------------------------------
today_label = Label(root, text="Today's Date: ", fg="blue", font=2)

t_dd = Label(root, text='DD: ', font=1)
t_mm = Label(root, text='MM: ', font=1)
t_yy = Label(root, text='YY: ', font=1)

t_day = Entry(root, width=5, font=1)
t_month = Entry(root, width=5, font=1)
t_year = Entry(root, width=5, font=1)

day = str(date.today().day)
month = str(date.today().month)
year = str(date.today().year)

t_day.insert(0, day)
t_month.insert(0, month)
t_year.insert(0, year)

today_label.grid(row=0, column=0, columnspan=1)

t_dd.grid(row=1, column=0, columnspan=2)
t_day.grid(row=1, column=1)

t_mm.grid(row=1, column=2)
t_month.grid(row=1, column=3, sticky='w')

t_yy.grid(row=1, column=4)
t_year.grid(row=1, column=5)
# --------------------------------------------------------------------------------------------------------
# Input Birthdate of user
birth_date_label = Label(root, text='Date of Birth: ', fg='blue', font=2)

b_dd = Label(root, text='DD: ', font=1)
b_mm = Label(root, text='MM: ', font=1)
b_yy = Label(root, text='YY: ', font=1)

blank_1 = Label(root, text="         ")

b_day = Entry(root, width=5, font=1)
b_month = Entry(root, width=5, font=1)
b_year = Entry(root, width=5, font=1)

birth_date_label.grid(row=2, column=0)

b_dd.grid(row=3, column=0, columnspan=2)
b_day.grid(row=3, column=1)

b_mm.grid(row=3, column=2)
b_month.grid(row=3, column=3, sticky='w')

b_yy.grid(row=3, column=4)
b_year.grid(row=3, column=5)

blank_1.grid(row=1, column=6)

# --------------------------------------------------------------------------------------------------------
# Create Buttons
clear_button = Button(root, text="Clear", command=clear_func, padx=10, pady=5, font="Arial", fg="black", bg="lime")
cal_button = Button(root, text="Calculate", command=cal_func, padx=10, pady=5, font="Arial", fg="black", bg="lime")

blank = Label(root, text="")

clear_button.grid(row=5, column=1)
blank.grid(row=4, column=0)
cal_button.grid(row=5, column=3, columnspan=2)

# ----------------------------------------------------------------------------------------------------

root.mainloop()
