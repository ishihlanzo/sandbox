import pyglet,tkinter

pyglet.font.add_file('file.ttf')

root = tkinter.Tk()
MyLabel = tkinter.Label(root,text="test",font=('font name',25))
MyLabel.pack()
root.mainloop()