import subprocess as sb

import tkinter as tk

def onclick():
    #test = sb.Popen(["ping","-W","2","-c", "1", "192.168.1.70"], stdout=sb.PIPE)
    test = sb.Popen(["iwlist", "wlan0","scan"], stdout=sb.PIPE)
   
    output = test.communicate()[0]
    tb.insert("1.0",output)
    



def Connect():
    test = sb.Popen(["iwconfig", "wlan0","essid","Swa"], stdout=sb.PIPE)
    test2 = sb.Popen(["dhclient","-v","wlan0"], stdout=sb.PIPE)
    output = test2.communicate()[0]
    tb.insert("1.0",output)


win=tk.Tk()
win.title('Kali linux 2019.4 wifi conector')
lb=tk.Label(win,text='Wifi connector')
show=tk.Button(win,text='Show available networks',command=onclick)

connect=tk.Button(win,text='connect',command=Connect)
tb=tk.Text(win,)
tb.place(x=1,y=1)

connect.pack()
tb.pack()
show.pack()
lb.pack()
win.mainloop()







