# GLOSSARY

# ------------------------------------------------------------
# Packages
from tkinter import *


# ------------------------------------------------------------
# GUI
root = Tk()
root.title('Glossário de TI')
root.resizable(False, False)

# Determinação das medidas da janela
largura = 500
altura = 250

# Resolução do nosso sistema
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()

# Posição da janela
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

# Definir a geometry
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))


# ------------------------------------------------------------
# Function
def search():
    find = False
    with open('Glossary.txt', 'r', encoding="utf8") as archive:
        read = archive.readlines()
        try:
            for item in read:
                if item.split()[0] == entry_word.get().upper():
                    find = True
                    final.set(item.split()[1:])
                if not find:
                    final.set('Termo não encontrado')
        except Exception as e:
            final.set(e)


# ------------------------------------------------------------
# Widgets
final = StringVar()

frm = Frame(root)
label_title = Label(frm, text='Buscar Termo:', font='Arial 11')
entry_word = Entry(frm, width=35, font='Arial 11')
btn_search = Button(frm, text='Procurar', command=search, font='Arial 11')
label_result = Message(frm, textvariable=final, width=450, font='Arial 11')


# ------------------------------------------------------------
# Layouts
label_title.pack(pady=15)
entry_word.pack(pady=10)
btn_search.pack(pady=15)
label_result.pack()
frm.pack()

# ------------------------------------------------------------
# Screen Loop
root.mainloop()
