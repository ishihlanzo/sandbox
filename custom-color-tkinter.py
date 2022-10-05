# made by ø
# made for Thiefaine
from tkinter import *

root = Tk()


def hightlight():
    user_entry = "Bonjurt".lower()
    result = "bonjour".lower()

    if len(user_entry) != len(result):
        print("Veuilliez mettre un mot contenant le bon nombre de lettre !")
        return
    new_word = []
    for i in range(len(user_entry)) :
        if user_entry[i] == result[i] :
            new_word.append((user_entry[i], "#07fc03"))
        if (user_entry[i] in result) and (user_entry[i] != result[i]):
            new_word.append((user_entry[i], "#fcca03"))
        if user_entry[i] not in result :
            new_word.append((user_entry[i], "white"))

    for i in range(len(new_word)):
        Label(root, text=new_word[i][0], bg=new_word[i][1], font=("Minecraft", 30)).grid(row=0, column=i)

hightlight()
root.mainloop()
