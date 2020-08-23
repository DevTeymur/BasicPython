import tkinter 

window=tkinter.Tk()
window.title('X/O')
window.geometry('300x350')
window.configure(bg='white')

def play_game():
    
    button_new_game.destroy()
    button_about.destroy()
    button_quit1.destroy()
    
    global count
    count=0
    
    def write1():
        global count
        if button1.cget('text')=='X' or button1.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button1['text']='X'
            else:
                button1['text']='O'
            count+=1
        check()
    
    def write2():
        global count
        if button2.cget('text')=='X' or button2.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button2['text']='X'
            else:
                button2['text']='O'
            count+=1
        check()
        
    def write3():
        global count
        if button3.cget('text')=='X' or button3.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button3['text']='X'
            else:
                button3['text']='O'
            count+=1
        check()
        
    def write4():
        global count
        if button4.cget('text')=='X' or button4.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button4['text']='X'
            else:
                button4['text']='O'
            count+=1
        check()
        
    def write5():
        global count
        if button5.cget('text')=='X' or button5.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button5['text']='X'
            else:
                button5['text']='O'
            count+=1
        check()
        
    def write6():
        global count
        if button6.cget('text')=='X' or button6.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button6['text']='X'
            else:
                button6['text']='O'
            count+=1
        check()
        
    def write7():
        global count
        if button7.cget('text')=='X' or button7.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button7['text']='X'
            else:
                button7['text']='O'
            count+=1
        check()
        
    def write8():
        global count
        if button8.cget('text')=='X' or button8.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button8['text']='X'
            else:
                button8['text']='O'
            count+=1
        check()
        
    def write9():
        global count
        if button9.cget('text')=='X' or button9.cget('text')=='O':
            pass
        else:
            if count%2==0:
                button9['text']='X'
            else:
                button9['text']='O'
            count+=1
        check()
    
    button1=tkinter.Button(window,font="arial-13",text='',command=write1)
    button1.place(width=100,height=100,x=0,y=0)
    
    button2=tkinter.Button(window,font="arial-13",text='',command=write2)
    button2.place(width=100,height=100,x=100,y=0)
    
    button3=tkinter.Button(window,font="arial-13",text='',command=write3)
    button3.place(width=100,height=100,x=200,y=0)
    
    button4=tkinter.Button(window,font="arial-13",text='',command=write4)
    button4.place(width=100,height=100,x=0,y=100)
    
    button5=tkinter.Button(window,font="arial-13",text='',command=write5)
    button5.place(width=100,height=100,x=100,y=100)
    
    button6=tkinter.Button(window,font="arial-13",text='',command=write6)
    button6.place(width=100,height=100,x=200,y=100)
    
    button7=tkinter.Button(window,font="arial-13",text='',command=write7)
    button7.place(width=100,height=100,x=0,y=200)
    
    button8=tkinter.Button(window,font="arial-13",text='',command=write8)
    button8.place(width=100,height=100,x=100,y=200)
    
    button9=tkinter.Button(window,font="arial-13",text='',command=write9)
    button9.place(width=100,height=100,x=200,y=200)
    
    note=tkinter.Label(window)
    note.place(width=100,height=50,x=0,y=300)

    def check():
        if button1.cget('text')=='X' and button2.cget('text')=='X' and button3.cget('text')=='X':
            button1.configure(bg='green1')
            button2.configure(bg='green1')
            button3.configure(bg='green1')
            button4.config(state='disabled')
            button5.config(state='disabled')
            button6.config(state='disabled')
            button7.config(state='disabled')
            button8.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='X wins')
        elif button4.cget('text')=='X' and button5.cget('text')=='X' and button6.cget('text')=='X':
            button4.configure(bg='green1')
            button5.configure(bg='green1')
            button6.configure(bg='green1')
            button1.config(state='disabled')
            button2.config(state='disabled')
            button3.config(state='disabled')
            button7.config(state='disabled')
            button8.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='X wins')
        elif button7.cget('text')=='X' and button8.cget('text')=='X' and button9.cget('text')=='X':
            button7.configure(bg='green1')
            button8.configure(bg='green1')
            button9.configure(bg='green1')
            button1.config(state='disabled')
            button2.config(state='disabled')
            button3.config(state='disabled')
            button4.config(state='disabled')
            button5.config(state='disabled')
            button6.config(state='disabled')
            note.config(text='X wins')
        elif button1.cget('text')=='X' and button4.cget('text')=='X' and button7.cget('text')=='X':
            button1.configure(bg='green1')
            button4.configure(bg='green1')
            button7.configure(bg='green1')
            button2.config(state='disabled')
            button5.config(state='disabled')
            button8.config(state='disabled')
            button3.config(state='disabled')
            button6.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='X wins')
        elif button2.cget('text')=='X' and button5.cget('text')=='X' and button8.cget('text')=='X':
            button2.configure(bg='green1')
            button5.configure(bg='green1')
            button8.configure(bg='green1')
            button1.config(state='disabled')
            button4.config(state='disabled')
            button7.config(state='disabled')
            button3.config(state='disabled')
            button6.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='X wins')
        elif button3.cget('text')=='X' and button6.cget('text')=='X' and button9.cget('text')=='X':
            button3.configure(bg='green1')
            button6.configure(bg='green1')
            button9.configure(bg='green1')
            button1.config(state='disabled')
            button4.config(state='disabled')
            button7.config(state='disabled')
            button2.config(state='disabled')
            button5.config(state='disabled')
            button8.config(state='disabled')
            note.config(text='X wins')
        elif button1.cget('text')=='X' and button5.cget('text')=='X' and button9.cget('text')=='X':
            button1.configure(bg='green1')
            button5.configure(bg='green1')
            button9.configure(bg='green1')
            button2.config(state='disabled')
            button3.config(state='disabled')
            button4.config(state='disabled')
            button6.config(state='disabled')
            button7.config(state='disabled')
            button8.config(state='disabled')
            note.config(text='X wins')
        elif button3.cget('text')=='X' and button5.cget('text')=='X' and button7.cget('text')=='X':
            button3.configure(bg='green1')
            button5.configure(bg='green1')
            button7.configure(bg='green1')
            button1.config(state='disabled')
            button2.config(state='disabled')
            button4.config(state='disabled')
            button6.config(state='disabled')
            button8.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='X wins')
        ##########################################################################################
        elif button1.cget('text')=='O' and button2.cget('text')=='O' and button3.cget('text')=='O':
            button1.configure(bg='green1')
            button2.configure(bg='green1')
            button3.configure(bg='green1')
            button4.config(state='disabled')
            button5.config(state='disabled')
            button6.config(state='disabled')
            button7.config(state='disabled')
            button8.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='O wins')
        elif button4.cget('text')=='O' and button5.cget('text')=='O' and button6.cget('text')=='O':
            button4.configure(bg='green1')
            button5.configure(bg='green1')
            button6.configure(bg='green1')
            button1.config(state='disabled')
            button2.config(state='disabled')
            button3.config(state='disabled')
            button7.config(state='disabled')
            button8.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='O wins')
        elif button7.cget('text')=='O' and button8.cget('text')=='O' and button9.cget('text')=='O':
            button7.configure(bg='green1')
            button8.configure(bg='green1')
            button9.configure(bg='green1')
            button1.config(state='disabled')
            button2.config(state='disabled')
            button3.config(state='disabled')
            button4.config(state='disabled')
            button5.config(state='disabled')
            button6.config(state='disabled')
            note.config(text='O wins')
        elif button1.cget('text')=='O' and button4.cget('text')=='O' and button7.cget('text')=='O':
            button1.configure(bg='green1')
            button4.configure(bg='green1')
            button7.configure(bg='green1')
            button2.config(state='disabled')
            button5.config(state='disabled')
            button8.config(state='disabled')
            button3.config(state='disabled')
            button6.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='O wins')
        elif button2.cget('text')=='O' and button5.cget('text')=='O' and button8.cget('text')=='O':
            button2.configure(bg='green1')
            button5.configure(bg='green1')
            button8.configure(bg='green1')
            button1.config(state='disabled')
            button4.config(state='disabled')
            button7.config(state='disabled')
            button3.config(state='disabled')
            button6.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='O wins')
        elif button3.cget('text')=='O' and button6.cget('text')=='O' and button9.cget('text')=='O':
            button3.configure(bg='green1')
            button6.configure(bg='green1')
            button9.configure(bg='green1')
            button1.config(state='disabled')
            button4.config(state='disabled')
            button7.config(state='disabled')
            button2.config(state='disabled')
            button5.config(state='disabled')
            button8.config(state='disabled')
            note.config(text='O wins')
        elif button1.cget('text')=='O' and button5.cget('text')=='O' and button9.cget('text')=='O':
            button1.configure(bg='green1')
            button5.configure(bg='green1')
            button9.configure(bg='green1')
            button2.config(state='disabled')
            button3.config(state='disabled')
            button4.config(state='disabled')
            button6.config(state='disabled')
            button7.config(state='disabled')
            button8.config(state='disabled')
            note.config(text='O wins')
        elif button3.cget('text')=='O' and button5.cget('text')=='O' and button7.cget('text')=='O':
            button3.configure(bg='green1')
            button5.configure(bg='green1')
            button7.configure(bg='green1')
            button1.config(state='disabled')
            button2.config(state='disabled')
            button4.config(state='disabled')
            button6.config(state='disabled')
            button8.config(state='disabled')
            button9.config(state='disabled')
            note.config(text='O wins')
        elif count==9:
            note.config(text="DRAW")
 
    
def about():
    win=tkinter.Tk()
    win.title('About')
    win.geometry('200x200')
    winl=tkinter.Label(win)
    winl.place(width=200,height=200,x=0,y=0)
    winl.config(text='Produced by Teymur \n\n 02.07.2020')
    winl.mainloop()
    
button_quit=tkinter.Button(window,font="arial-13",text='Quit',command=window.destroy)
button_quit.place(width=100,height=50,x=200,y=300)

button_play=tkinter.Button(window,font="arial-5",text='New Game',command=play_game)
button_play.place(width=100,height=50,x=100,y=300)

menu_l=tkinter.Label(window)
menu_l.place(width=300,height=50,x=0,y=0)
menu_l.config(text='MENU',bg='red1',font="arial-13")

button_new_game=tkinter.Button(window,font="arial-13",text='Play',command=play_game)
button_new_game.place(width=300,height=100,x=0,y=50)
button_new_game.configure(bg='yellow2',activebackground='chartreuse3')

button_about=tkinter.Button(window,font="arial-13",text='About',command=about)
button_about.place(width=300,height=100,x=0,y=150)
button_about.configure(bg='yellow2',activebackground='cornsilk1')

button_quit1=tkinter.Button(window,font="arial-13",text='Quit',command=window.destroy)
button_quit1.place(width=300,height=100,x=0,y=250)
button_quit1.configure(bg='yellow2',activebackground='crimson')

window.mainloop()