from tkinter import *
from base import *

class Menu(Frame):
    def __init__(self,master):
        super(Menu,self).__init__(master)
        self.creat_widgets()
        self.place()
        self.pack()



    def creat_widgets(self):
        f0 = Frame(root, width=1100, height=1000)
        f1 = Frame(f0, width=550, height=500)
        f2 = Frame(f0, width=550, height=500)
        f0.pack()
        f1.pack(side=LEFT)
        f2.pack(side=RIGHT)

        self.metka_vvod_x = Label(f1, text = "Введите значения x: ", font = 'Arial 20')
        self.metka_vvod_x.place(relx =0, rely =0)

        self.metka_vvod_y = Label(f1, text="Введите значения y: ", font = 'Arial 20')
        self.metka_vvod_y.place(relx = 0, rely = 0.2)

        self.pole_vvod_x = Entry(f1, bd = 5, font = 'Arial 20'  )
        self.pole_vvod_x.place(relx =0.4 ,rely = 0 )

        self.pole_vvod_y = Entry(f1, bd=5, font = 'Arial 20' )
        self.pole_vvod_y.place(relx = 0.4, rely = 0.2)

        self.metka_vvod_xerr = Label(f2, text="Введите погрешность по x: ", font = 'Arial 20')
        self.metka_vvod_xerr.place(relx = 0,  rely = 0)

        self.metka_vvod_yerr = Label(f2, text="Введите погрешноть по y: ", font = 'Arial 20')
        self.metka_vvod_yerr.place(relx = 0,  rely = 0.2)

        self.pole_vvod_xerr = Entry(f2, bd=4, font = 'Arial 20')
        self.pole_vvod_xerr.place(relx = 0.54,  rely = 0)

        self.pole_vvod_yerr = Entry(f2, bd=4, font = 'Arial 20')
        self.pole_vvod_yerr.place(relx = 0.54,  rely = 0.2)

        self.bttn = Button(f0, text = "Ввести", font = 'Arial 20', bd = 5)
        self.bttn["command"] = self.button_vvod
        self.bttn.place(relx = 0.35,  rely = 0.9, relwidth = 0.3)

        self.metka_text_ox = Label(f1, text="Надпись на оси Ox: ", font='Arial 20')
        self.metka_text_ox.place(relx=0, rely=0.3)
        self.pole_text_ox = Entry(f1, bd=4, font='Arial 20')
        self.pole_text_ox.place(relx=0, rely=0.4)

        self.metka_graphic = Label(self, text = "Вид аппроксимации: ")
        self.metka_graphic.place()

        self.v_graphic = StringVar() #Создаем переключатель
        self.v_graphic.set(None)

        Radiobutton(self, text = "Линейная", variable = self.v_graphic, value = "Линейная").place()
        Radiobutton(self, text = "Квадратичная", variable = self.v_graphic, value = "Квадратичная").place()

    def write_x_to_file(self):
        x = self.pole_vvod_x.get()
        file_obj = open('File_with_znach.txt', 'w')
        file_obj.write(x)
        file_obj.close()

    def write_y_to_file(self):
        y = self.pole_vvod_y.get()
        file_obj = open('File_with_znach.txt', 'a')
        file_obj.write("\n")
        file_obj.write(y)
        file_obj.close()

    def write_xerr_to_file(self):
        xerr = self.pole_vvod_xerr.get()
        file_obj = open('File_with_pogreshnosti.txt', 'w')
        file_obj.write(xerr)
        file_obj.close()

    def write_yerr_to_file(self):
        yerr = self.pole_vvod_yerr.get()
        file_obj = open('File_with_pogreshnosti.txt', 'a')
        file_obj.write("\n")
        file_obj.write(yerr)
        file_obj.close()

    def write_text_ox_to_file(self):
        text_ox = self.pole_text_ox.get()
        file_obj = open('File_with_text.txt', 'w')
        file_obj.write(text_ox)
        file_obj.close()

    def button_vvod(self):
        self.write_x_to_file()
        self.write_y_to_file()
        self.write_xerr_to_file()
        self.write_yerr_to_file()
        self.write_text_ox_to_file()
        graphic()





root = Tk()
root.title("Меню")
root.geometry('1100x1000+150+200')
app = Menu(root)
root.mainloop()



