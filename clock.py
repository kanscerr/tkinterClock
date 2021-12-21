#importing necessary features
from time import strftime
from tkinter import *
from playsound import playsound

#defining the display of tkinter window
root= Tk()
root.geometry("750x500")

root.title("Clock")

root.configure(bg= "#080808")

#function to play timer audio
def sound_timer():
    playsound('C:/Users/KIIT/Downloads/alarm.wav')
    alarmdone= Button(root, text= 'TIMER WENT OFF', command= del03).place(relx= 0.5, rely= 0.1, anchor= S)
    root.after(3000, del03)

#to hide the message after a given time
def del03():
    t_text2= Label(root, padx= 90, pady= 5, bg= "#080808").place(relx= 0.5, rely= 0.1, anchor= S) 

#function to play alarm audio
def sound_alarm():
    playsound('C:/Users/KIIT/Downloads/alarm.wav')
    alarmdone= Button(root, text= 'ALARM WENT OFF', command= del04).place(relx= 0.5, rely= 0.1, anchor= S)
    root.after(3000, del04)

#to hide the message after a given time
def del04():
    t_text2= Label(root, padx= 90, pady= 5, bg= "#080808").place(relx= 0.5, rely= 0.1, anchor= S) 
    
#setting up clock time
def loop1(): 
    global a
    global b 
    global c

    a= strftime('%H')
    b= strftime('%M')
    c= strftime('%S')
    m= strftime('%p')

    mn01= Label(root, text= b, font= ("Ariel", 28), bg= "#000000", fg= "white", padx= 30, pady= 30).place(relx= 0.5, rely= 0.5, anchor= CENTER)
    dot01= Label(root, text= ':', font= 9000, bg= "#080808", fg= "white", padx= 10, pady= 10).place(relx= 0.34, rely= 0.5, anchor= W)
    sc01= Label(root, text= c, font= ("Ariel", 28), bg= "#000000", fg= "white", padx= 30, pady= 30)
    sc01.place(relx= 0.86, rely= 0.5, anchor= E)
    dot02= Label(root, text= ':', font= 9000, bg= "#080808", fg= "white", padx= 5, pady=5).place(relx= 0.65, rely= 0.5, anchor= E)
    hr01= Label(root, text= a, font= ("Ariel", 28), bg= "#000000", fg= "white", padx= 30, pady= 30).place(relx= 0.14, rely= 0.5, anchor= W) 
    meridian= Label(root, text= m, font= 9000, bg= "#080808", fg= "white", padx= 10, pady= 10).place(relx= 0.93, rely= 0.42, anchor= E)

    sc01.after(1000, loop1)

    #for alarm
    def del02():
        t_text2= Label(root, padx= 90, pady= 5, bg= "#080808").place(relx= 0.5, rely= 0.1, anchor= S) 
        alarm_compare()

    def alarmresult():
        global x 
        global y 
        global z
        x= alarm_hr.get()
        y= alarm_mn.get()
        z= alarm_sc.get()
        global t_text
        t_text= Button(root, text= 'Your alarm has been set', command= del02).place(relx= 0.5, rely= 0.1, anchor= S)
        root.after(3000, del02)

    def alarm():
        global alarm_hr
        global alarm_mn
        global alarm_sc
        alarm_hr= IntVar()
        alarm_mn= IntVar()
        alarm_sc= IntVar()
        a_hr= Entry(root, textvariable= alarm_hr, width= 3)
        a_hr.place(relx= 0.07, rely= 0.75, anchor= NW)
        a_mn= Entry(root, textvariable= alarm_mn, width= 3)
        a_mn.place(relx= 0.13, rely= 0.75, anchor= NW)
        a_sc= Entry(root, textvariable= alarm_sc, width= 3)
        a_sc.place(relx= 0.18, rely= 0.75, anchor= NW)
        a_dot01= Label(root, text= ":", bg= "#080808", fg= "white", padx= 2, pady=0.5).place(relx= 0.115, rely= 0.75, anchor= NW)
        a_dot02= Label(root, text= ":", bg= "#080808", fg= "white", padx= 2, pady=0.5).place(relx= 0.170, rely= 0.75, anchor= NW)
        a_ok= Button(root, text='OK', bg= "#080808", fg= "white", padx= 10, command= alarmresult).place(relx= 0.135, rely= 0.87, anchor= NW)

    #for timer
    def del01():
        t_text2= Label(root, padx= 90, pady= 5, bg= "#080808").place(relx= 0.5, rely= 0.1, anchor= S)   
        timer_compare()

    def timerresult():
        global e 
        global f 
        global g 
        e= timer_hr.get()
        f= timer_mn.get()
        g= timer_sc.get()
        global t_text
        t_text= Button(root, text= 'Your timer has been set', command= del01).place(relx= 0.5, rely= 0.1, anchor= S)
        root.after(3000, del01)

    def timer():
        global timer_hr
        global timer_mn
        global timer_sc
        timer_hr= IntVar()
        timer_mn= IntVar()
        timer_sc= IntVar()
        t_hr= Entry(root, textvariable= timer_hr, width= 3)
        t_hr.place(relx= 0.82, rely= 0.75, anchor= NE)
        t_mn= Entry(root, textvariable= timer_mn, width= 3)
        t_mn.place(relx= 0.87, rely= 0.75, anchor= NE)
        t_sc= Entry(root, textvariable= timer_sc, width= 3)
        t_sc.place(relx= 0.92, rely= 0.75, anchor= NE)
        t_hr01= Label(root, text= "hr", padx= 0.2, pady=2, fg= "white", bg= "#080808").place(relx= 0.838, rely= 0.75, anchor= NE)
        t_mn01= Label(root, text= "mn", padx= 0.2, pady= 2, bg= "#080808", fg= "white").place(relx= 0.895, rely= 0.75, anchor= NE)
        t_sc01= Label(root, text= "sc", padx= 0.2, pady= 2, bg= "#080808", fg= "white").place(relx= 0.94, rely= 0.75, anchor= NE)
        t_ok= Button(root, text='OK', bg= "#080808", fg= "white", padx= 10, command= timerresult).place(relx= 0.845, rely= 0.87, anchor= NE) 

    alarm= Button(root, text= 'Alarm', bg= '#000000', fg= 'white', padx= 10, command= alarm).place(relx= 0.12, rely= 0.66, anchor= NW)
    timer= Button(root, text= 'Timer', bg= '#000000', fg= 'white', padx= 10, command= timer).place(relx= 0.88, rely= 0.66, anchor= NE)

#final alarm formula
def alarm_compare():
    root.after(1000, alarm_compare)
    if z==int(c):
        if y== int(b):
            if x== int(a):
                sound_alarm()
              
#final timer formula             
def timer_compare():   
    def timer_compare2():
        if int(a)==r:
            if int(b)==q:
                if int(c)==p:
                    sound_timer()
        root.after(1000, timer_compare2)
    p= int(c)+g-3
    if p>=60:
        p=p-60 
    q= int(b)+f
    if q>=60:
        q=q-60
    r= int(a)+e 
    timer_compare2()

loop1()

#event loop
root.mainloop()