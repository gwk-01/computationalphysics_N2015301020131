import time
from tkinter import*
tk = Tk()
canvas = Canvas(tk,width=400,height=200)
canvas.pack()
canvas.create_text(10,100,text="高伟康") 
for x in range(0,60):
    canvas.move(1,10,0)  
    tk.update()          
    time.sleep(0.1)   
tk.mainloop()    