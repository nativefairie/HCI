from Tkinter import *

canvas = Canvas(width=700, height=220)
canvas.pack(expand=YES, fill=BOTH)



canvas.create_rectangle(100, 200, 150, 30, width=0, fill='#FFFFFF')
canvas.create_rectangle(150, 200, 200, 30, width=0, fill='#DDDDDD')
canvas.create_rectangle(200, 200, 250, 30, width=0, fill='#CCCCCC')
canvas.create_rectangle(250, 200, 300, 30, width=0, fill='#BBBBBB')
canvas.create_rectangle(300, 200, 350, 30, width=0, fill='#999999')
canvas.create_rectangle(350, 200, 400, 30, width=0, fill='#888888')
canvas.create_rectangle(400, 200, 450, 30, width=0, fill='#777777')
canvas.create_rectangle(450, 200, 500, 30, width=0, fill='#666666')
canvas.create_rectangle(500, 200, 550, 30, width=0, fill='#555555')
canvas.create_rectangle(550, 200, 550, 30, width=0, fill='#454545')
canvas.create_rectangle(600, 200, 550, 30, width=0, fill='#333333')



mainloop()
