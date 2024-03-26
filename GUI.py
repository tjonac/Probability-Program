"""
Programa principal donde se ejecuta el GUI
"""
#Importaciones

from os import X_OK
import tkinter as tk
from tkinter import DoubleVar, PhotoImage, StringVar, Toplevel,ttk
from tkinter import font
from tkinter.constants import LEFT, TOP, X
from typing import Match
from PIL import Image,ImageTk
import glob
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import text
import numpy as np
from DiscretePF import *
from ContinuePF import *

def continue_window():
    def Normal_window():
        def finish(*_):
            aux = 0
            while aux == 0:
                try:
                    M = float(M_entry.get())
                    DE = float(DE_entry.get())
                    x = float(x_entry.get())
                    d = float(d_entry.get())
                    aux = 1
                except:
                    raise tk.messagebox.showerror("Error", "Verifique la entrada de datos.")

            M = float(M_entry.get())
            DE = float(DE_entry.get())
            x = float(x_entry.get())

            if float(d_entry.get()) % 1 == 0:
                d = int(d_entry.get())
            else:
                d = float(d_entry.get())    

            s = normal(M,DE,x,d)

            if s.Validate() == 1:
                s.graph()

                fixed_height = 413
                image = Image.open('Images\\Normal_Graph.png')
                height_percent = (fixed_height / float(image.size[1]))
                width_size = int((float(image.size[0]) * float(height_percent)))
                image = image.resize((width_size, fixed_height), Image.NEAREST)
                image.save('Images\\Normal_Graph.png')

                data01 = s.Evaluate()
                data02 = s.Estadisticos()

                text1.set(str(data01[0]))
                text2.set(str(data01[1]))
                text3.set(str(data02[0]))
                text4.set(str(data02[2]))


                grafica_image = tk.PhotoImage(file="Images\\Normal_Graph.png")     
                tk.Label(Normal_root,image=grafica_image).place(x=110,y=400)

            else:
                tk.messagebox.showerror("Error", "Verifique la entrada de datos.")


            Normal_root.mainloop()
        
        continue_root.destroy()
        Normal_root = tk.Toplevel(root)                 
        Normal_root.title("EzStatistics")                     
        Normal_root.geometry("800x850")
        Normal_root.config(bg="white")                
        Normal_root.iconbitmap("Images/Icon.ico")
        Normal_root.resizable(0, 0)

        tk.Label(Normal_root, text="Ingrese la media :", fg="black", font=("Arial",12)).place(x=50,y=125)
        tk.Label(Normal_root, text="Ingrese la desviación estándar:", fg="black", font=("Arial",12)).place(x=50,y=162)
        tk.Label(Normal_root, text="Ingrese el valor de x:", fg="black", font=("Arial",12)).place(x=50,y=200)
        tk.Label(Normal_root, text="Ingrese el número de decimales desados (0 a 8):", fg="black", font=("Arial",12)).place(x=50,y=237)
        tk.Label(Normal_root, text="P(X=x)", fg="black", font=("Arial",12)).place(x=50,y=275)
        tk.Label(Normal_root, text="P(X<=x)", fg="black", font=("Arial",12)).place(x=50,y=312)
        tk.Label(Normal_root, text="Media:", fg="black", font=("Arial",12)).place(x=350,y=275)
        tk.Label(Normal_root, text="Desviación estándar:", fg="black", font=("Arial",12)).place(x=350,y=312)

        text1 = StringVar()   #P(X=x)
        text2 = StringVar()   #P(X<=x)
        text3 = StringVar()   #Media
        text4 = StringVar()   #Desviación estándar


        tk.Entry(Normal_root, textvariable=text1, fg="black", font=("Arial",12), state="disabled").place(x=150,y=275)
        tk.Entry(Normal_root, textvariable=text2, fg="black", font=("Arial",12), state="disabled").place(x=150,y=312)
        tk.Entry(Normal_root, textvariable=text3, fg="black", font=("Arial",12), state="disabled").place(x=525,y=275)
        tk.Entry(Normal_root, textvariable=text4, fg="black", font=("Arial",12), state="disabled").place(x=525,y=312)

        M_entry = DoubleVar()
        ttk.Entry(Normal_root,textvariable=M_entry).place(x=525,y=125)
        DE_entry = DoubleVar()
        ttk.Entry(Normal_root,textvariable=DE_entry).place(x=525,y=162)
        x_entry = DoubleVar()
        ttk.Entry(Normal_root,textvariable=x_entry).place(x=525,y=200)
        d_entry = DoubleVar()
        ttk.Entry(Normal_root,textvariable=d_entry).place(x=525,y=237)

        tk.Button(Normal_root,text="Aceptar",command=finish).place(x=380,y=360)

        title_image = tk.PhotoImage(file="Images\\Normal.png")                   
        tk.Label(Normal_root,image=title_image).place(x=175,y=30)

        title_function = tk.PhotoImage(file="Images\\Normal_function.png")                   
        tk.Label(Normal_root,image=title_function).place(x=375,y=15)

        grafica_image = tk.PhotoImage(file="Images\\Base.png")                   
        tk.Label(Normal_root,image=grafica_image).place(x=110,y=400)     

        Normal_root.mainloop()
    
    def Exponential_window():
        def finish(*_):
            aux = 0
            while aux == 0:
                try:
                    M = float(M_entry.get())
                    x = float(x_entry.get())
                    d = float(d_entry.get())
                    aux = 1
                except:
                    raise tk.messagebox.showerror("Error", "Verifique la entrada de datos.")

            M = float(M_entry.get())
            x = float(x_entry.get())

            if float(d_entry.get()) % 1 == 0:
                d = int(d_entry.get())
            else:
                d = float(d_entry.get())    

            s = exponencial(M,x,d)

            if s.Validate() == 1:
                s.graph()

                fixed_height = 413
                image = Image.open('Images\Exponential_Graph.png')
                height_percent = (fixed_height / float(image.size[1]))
                width_size = int((float(image.size[0]) * float(height_percent)))
                image = image.resize((width_size, fixed_height), Image.NEAREST)
                image.save('Images\Exponential_Graph.png')

                data01 = s.Evaluate()
                data02 = s.Estadisticos()

                text1.set(str(data01[0]))
                text2.set(str(data01[1]))
                text3.set(str(data02[0]))
                text4.set(str(data02[2]))


                grafica_image = tk.PhotoImage(file="Images\Exponential_Graph.png")     
                tk.Label(Exponential_root,image=grafica_image).place(x=110,y=400)

            else:
                tk.messagebox.showerror("Error", "Verifique la entrada de datos.")


            Exponential_root.mainloop()
        
        continue_root.destroy()
        Exponential_root = tk.Toplevel(root)                 
        Exponential_root.title("EzStatistics")                     
        Exponential_root.geometry("800x850")
        Exponential_root.config(bg="white")                
        Exponential_root.iconbitmap("Images/Icon.ico")
        Exponential_root.resizable(0, 0)

        tk.Label(Exponential_root, text="Ingrese la media :", fg="black", font=("Arial",12)).place(x=50,y=125)
        tk.Label(Exponential_root, text="Ingrese el valor de x:", fg="black", font=("Arial",12)).place(x=50,y=162)
        tk.Label(Exponential_root, text="Ingrese el número de decimales desados (0 a 8):", fg="black", font=("Arial",12)).place(x=50,y=200)
        tk.Label(Exponential_root, text="P(X=x)", fg="black", font=("Arial",12)).place(x=50,y=237)
        tk.Label(Exponential_root, text="P(X<=x)", fg="black", font=("Arial",12)).place(x=50,y=275)
        tk.Label(Exponential_root, text="Media:", fg="black", font=("Arial",12)).place(x=350,y=237)
        tk.Label(Exponential_root, text="Desviación estándar:", fg="black", font=("Arial",12)).place(x=350,y=275)

        text1 = StringVar()   #P(X=x)
        text2 = StringVar()   #P(X<=x)
        text3 = StringVar()   #Media
        text4 = StringVar()   #Desviación estándar


        tk.Entry(Exponential_root, textvariable=text1, fg="black", font=("Arial",12), state="disabled").place(x=150,y=237)
        tk.Entry(Exponential_root, textvariable=text2, fg="black", font=("Arial",12), state="disabled").place(x=150,y=275)
        tk.Entry(Exponential_root, textvariable=text3, fg="black", font=("Arial",12), state="disabled").place(x=525,y=237)
        tk.Entry(Exponential_root, textvariable=text4, fg="black", font=("Arial",12), state="disabled").place(x=525,y=275)

        M_entry = DoubleVar()
        ttk.Entry(Exponential_root,textvariable=M_entry).place(x=525,y=125)
        x_entry = DoubleVar()
        ttk.Entry(Exponential_root,textvariable=x_entry).place(x=525,y=162)
        d_entry = DoubleVar()
        ttk.Entry(Exponential_root,textvariable=d_entry).place(x=525,y=200)

        tk.Button(Exponential_root,text="Aceptar",command=finish).place(x=380,y=360)

        title_image = tk.PhotoImage(file="Images\Exponential.png")                   
        tk.Label(Exponential_root,image=title_image).place(x=175,y=30)

        title_function = tk.PhotoImage(file="Images\Exponential_function.png")                   
        tk.Label(Exponential_root,image=title_function).place(x=460,y=15)

        grafica_image = tk.PhotoImage(file="Images\\Base.png")                   
        tk.Label(Exponential_root,image=grafica_image).place(x=110,y=400)     

        Exponential_root.mainloop()

    def Gamma_window():
        def finish(*_):
            aux = 0
            while aux == 0:
                try:
                    a = float(a_entry.get())
                    b = float(b_entry.get())
                    x = float(x_entry.get())
                    d = float(d_entry.get())
                    aux = 1
                except:
                    raise tk.messagebox.showerror("Error", "Verifique la entrada de datos.")

            a = float(a_entry.get())
            b = float(b_entry.get())
            x = float(x_entry.get())

            if float(d_entry.get()) % 1 == 0:
                d = int(d_entry.get())
            else:
                d = float(d_entry.get())    

            s = gamma(a,b,x,d)

            if s.Validate() == 1:
                s.graph()

                fixed_height = 413
                image = Image.open('Images\Gamma_Graph.png')
                height_percent = (fixed_height / float(image.size[1]))
                width_size = int((float(image.size[0]) * float(height_percent)))
                image = image.resize((width_size, fixed_height), Image.NEAREST)
                image.save('Images\Gamma_Graph.png')

                data01 = s.Evaluate()
                data02 = s.Estadisticos()

                text1.set(str(data01[0]))
                text2.set(str(data01[1]))
                text3.set(str(data02[0]))
                text4.set(str(data02[2]))


                grafica_image = tk.PhotoImage(file="Images\Gamma_Graph.png")     
                tk.Label(Gamma_root,image=grafica_image).place(x=110,y=400)

            else:
                tk.messagebox.showerror("Error", "Verifique la entrada de datos.")


            Gamma_root.mainloop()
        
        continue_root.destroy()
        Gamma_root = tk.Toplevel(root)                 
        Gamma_root.title("EzStatistics")                     
        Gamma_root.geometry("800x850")
        Gamma_root.config(bg="white")                
        Gamma_root.iconbitmap("Images/Icon.ico")
        Gamma_root.resizable(0, 0)

        tk.Label(Gamma_root, text="Ingrese el valor de alpha :", fg="black", font=("Arial",12)).place(x=50,y=125)
        tk.Label(Gamma_root, text="Ingrese el valor de beta:", fg="black", font=("Arial",12)).place(x=50,y=162)
        tk.Label(Gamma_root, text="Ingrese el valor de x:", fg="black", font=("Arial",12)).place(x=50,y=200)
        tk.Label(Gamma_root, text="Ingrese el número de decimales desados (0 a 8):", fg="black", font=("Arial",12)).place(x=50,y=237)
        tk.Label(Gamma_root, text="P(X=x)", fg="black", font=("Arial",12)).place(x=50,y=275)
        tk.Label(Gamma_root, text="P(X<=x)", fg="black", font=("Arial",12)).place(x=50,y=312)
        tk.Label(Gamma_root, text="Media:", fg="black", font=("Arial",12)).place(x=350,y=275)
        tk.Label(Gamma_root, text="Desviación estándar:", fg="black", font=("Arial",12)).place(x=350,y=312)

        text1 = StringVar()   #P(X=x)
        text2 = StringVar()   #P(X<=x)
        text3 = StringVar()   #Media
        text4 = StringVar()   #Desviación estándar


        tk.Entry(Gamma_root, textvariable=text1, fg="black", font=("Arial",12), state="disabled").place(x=150,y=275)
        tk.Entry(Gamma_root, textvariable=text2, fg="black", font=("Arial",12), state="disabled").place(x=150,y=312)
        tk.Entry(Gamma_root, textvariable=text3, fg="black", font=("Arial",12), state="disabled").place(x=525,y=275)
        tk.Entry(Gamma_root, textvariable=text4, fg="black", font=("Arial",12), state="disabled").place(x=525,y=312)

        a_entry = DoubleVar()
        ttk.Entry(Gamma_root,textvariable=a_entry).place(x=525,y=125)
        b_entry = DoubleVar()
        ttk.Entry(Gamma_root,textvariable=b_entry).place(x=525,y=162)
        x_entry = DoubleVar()
        ttk.Entry(Gamma_root,textvariable=x_entry).place(x=525,y=200)
        d_entry = DoubleVar()
        ttk.Entry(Gamma_root,textvariable=d_entry).place(x=525,y=237)

        tk.Button(Gamma_root,text="Aceptar",command=finish).place(x=380,y=360)

        title_image = tk.PhotoImage(file="Images\Gamma.png")                   
        tk.Label(Gamma_root,image=title_image).place(x=175,y=30)

        title_function = tk.PhotoImage(file="Images\Gamma_function.png")                   
        tk.Label(Gamma_root,image=title_function).place(x=375,y=15)

        grafica_image = tk.PhotoImage(file="Images\Base.png")                   
        tk.Label(Gamma_root,image=grafica_image).place(x=110,y=400)     

        Gamma_root.mainloop()

    root.iconify()                                    #Miniminiza root 
    continue_root = tk.Toplevel(root)                 #Crea la nueva ventana
    continue_root.title("EzStatistics")               #Titulo de la nueva ventana
    continue_root.geometry("800x800")                 #Tamaño de la nueva ventana
    continue_root.resizable(0, 0)                     #No permite cambaiar el tamaño de la ventana
    continue_root.iconbitmap("Images/Icon.ico")       #Icono del programa
    continue_root.config(bg="white")

    #<------------------------------Imagenes--------------------------------> 
    continue_title = tk.PhotoImage(file="Images\Continue_title.png")               #Se procesa la imagen
    tk.Label(continue_root,image=continue_title).place(x=150,y=50)                 #Se inserta la imagen

    Normal_Button_Image = PhotoImage(file = "Images\\Normal_button.png") 
    photoimage01 = Normal_Button_Image.subsample(3, 3) 

    Exponential_Button_Image = PhotoImage(file = "Images\Exponential_button.png") 
    photoimage02 = Exponential_Button_Image.subsample(3, 3)

    Gamma_Button_Image = PhotoImage(file = "Images\Gamma_button.png") 
    photoimage03 = Gamma_Button_Image.subsample(3, 3)

    #<-------------------------------Botones--------------------------------->
    tk.Button(continue_root, text = ' Normal', image = photoimage01, compound = LEFT,font =( 'Verdana', 15),bg="white", command=Normal_window).place(x=230,y=250)

    tk.Button(continue_root, text = ' Exponencial', image = photoimage02, compound = LEFT,font =( 'Verdana', 15),bg="white", command=Exponential_window).place(x=230,y=360)

    tk.Button(continue_root, text = ' Gamma', image = photoimage03, compound = LEFT,font =( 'Verdana', 15),bg="white", command=Gamma_window).place(x=230,y=475)


    



    continue_root.mainloop()


def discrete_window():

    def Binomial_window():
        def finish(*_):
            aux = 0
            while aux == 0:
                try:
                    n = float(n_entry.get())
                    x = float(x_entry.get())
                    p = float(p_entry.get())
                    d = float(d_entry.get())
                    aux = 1
                except:
                    raise tk.messagebox.showerror("Error", "Verifique la entrada de datos.")

            if float(n_entry.get()) % 1 == 0:
                n = int(n_entry.get())
            else:
                n = float(n_entry.get())

            if float(x_entry.get()) % 1 == 0:
                x = int(x_entry.get())
            else:
                x = float(x_entry.get())

            if float(d_entry.get()) % 1 == 0:
                d = int(d_entry.get())
            else:
                d = float(d_entry.get())    
            p = float(p_entry.get())

            s = binomial(n,x,p,d)

            if s.Validate() == 1:
                s.graph()

                fixed_height = 413
                image = Image.open('Images\Binomial_Graph.png')
                height_percent = (fixed_height / float(image.size[1]))
                width_size = int((float(image.size[0]) * float(height_percent)))
                image = image.resize((width_size, fixed_height), Image.NEAREST)
                image.save('Images\Binomial_Graph.png')

                data01 = s.Evaluate()
                data02 = s.Estadisticos()

                text1.set(str(data01[0]))
                text2.set(str(data01[1]))
                text3.set(str(data02[0]))
                text4.set(str(data02[2]))


                grafica_image = tk.PhotoImage(file="Images\Binomial_Graph.png")     
                tk.Label(Binomial_root,image=grafica_image).place(x=110,y=400)

            else:
                tk.messagebox.showerror("Error", "Verifique la entrada de datos.")


            Binomial_root.mainloop()
        
        discrete_root.destroy()
        Binomial_root = tk.Toplevel(root)                 
        Binomial_root.title("EzStatistics")                     
        Binomial_root.geometry("800x850")
        Binomial_root.config(bg="white")                
        Binomial_root.iconbitmap("Images/Icon.ico")
        Binomial_root.resizable(0, 0)

        tk.Label(Binomial_root, text="Ingrese el total de datos :", fg="black", font=("Arial",12)).place(x=50,y=125)
        tk.Label(Binomial_root, text="Ingrese el valor de x:", fg="black", font=("Arial",12)).place(x=50,y=162)
        tk.Label(Binomial_root, text="Ingrese el valor de p:", fg="black", font=("Arial",12)).place(x=50,y=200)
        tk.Label(Binomial_root, text="Ingrese el número de decimales desados (0 a 8):", fg="black", font=("Arial",12)).place(x=50,y=237)
        tk.Label(Binomial_root, text="P(X=x)", fg="black", font=("Arial",12)).place(x=50,y=275)
        tk.Label(Binomial_root, text="P(X<=x)", fg="black", font=("Arial",12)).place(x=50,y=312)
        tk.Label(Binomial_root, text="Media:", fg="black", font=("Arial",12)).place(x=350,y=275)
        tk.Label(Binomial_root, text="Desviación estándar:", fg="black", font=("Arial",12)).place(x=350,y=312)

        text1 = StringVar()   #P(X=x)
        text2 = StringVar()   #P(X<=x)
        text3 = StringVar()   #Media
        text4 = StringVar()   #Desviación estándar


        tk.Entry(Binomial_root, textvariable=text1, fg="black", font=("Arial",12), state="disabled").place(x=150,y=275)
        tk.Entry(Binomial_root, textvariable=text2, fg="black", font=("Arial",12), state="disabled").place(x=150,y=312)
        tk.Entry(Binomial_root, textvariable=text3, fg="black", font=("Arial",12), state="disabled").place(x=525,y=275)
        tk.Entry(Binomial_root, textvariable=text4, fg="black", font=("Arial",12), state="disabled").place(x=525,y=312)

        n_entry = DoubleVar()
        ttk.Entry(Binomial_root,textvariable=n_entry).place(x=525,y=125)
        x_entry = DoubleVar()
        ttk.Entry(Binomial_root,textvariable=x_entry).place(x=525,y=162)
        p_entry = DoubleVar()
        ttk.Entry(Binomial_root,textvariable=p_entry).place(x=525,y=200)
        d_entry = DoubleVar()
        ttk.Entry(Binomial_root,textvariable=d_entry).place(x=525,y=237)


        tk.Button(Binomial_root,text="Aceptar",command=finish).place(x=380,y=360)

        title_image = tk.PhotoImage(file="Images/Binomial.png")                   
        tk.Label(Binomial_root,image=title_image).place(x=175,y=30)

        title_function = tk.PhotoImage(file="Images/Binomial_function.png")                   
        tk.Label(Binomial_root,image=title_function).place(x=375,y=30)

        grafica_image = tk.PhotoImage(file="Images/Base.png")                   
        tk.Label(Binomial_root,image=grafica_image).place(x=110,y=400)     

        Binomial_root.mainloop()

    def Hypergeometric_window():
        def finish(*_):
            aux = 0
            while aux == 0:
                try:
                    N = float(N_entry.get())
                    k = float(k_entry.get())
                    n = float(n_entry.get())
                    x = float(x_entry.get())
                    d = float(d_entry.get())
                    aux = 1
                except:
                    raise tk.messagebox.showerror("Error", "Verifique la entrada de datos.")

            if float(N_entry.get()) % 1 == 0:
                N = int(N_entry.get())
            else:
                N = float(N_entry.get())

            if float(k_entry.get()) % 1 == 0:
                k = int(k_entry.get())
            else:
                k = float(k_entry.get())

            if float(n_entry.get()) % 1 == 0:
                n = int(n_entry.get())
            else:
                n = float(n_entry.get())

            if float(x_entry.get()) % 1 == 0:
                x = int(x_entry.get())
            else:
                x = float(x_entry.get())

            if float(d_entry.get()) % 1 == 0:
                d = int(d_entry.get())
            else:
                d = float(d_entry.get())    

            s = Hipergeometrica(N,k,n,x,d)

            if s.Validate() == 1:
                s.graph()

                fixed_height = 413
                image = Image.open('Images\Hypergeometric_Graph.png')
                height_percent = (fixed_height / float(image.size[1]))
                width_size = int((float(image.size[0]) * float(height_percent)))
                image = image.resize((width_size, fixed_height), Image.NEAREST)
                image.save('Images\Hypergeometric_Graph.png')

                data01 = s.Evaluate()
                data02 = s.Estadisticos()

                text1.set(str(data01[0]))
                text2.set(str(data01[1]))
                text3.set(str(data02[0]))
                text4.set(str(data02[2]))


                grafica_image = tk.PhotoImage(file="Images\Hypergeometric_Graph.png")     
                tk.Label(Hypergeometric_root,image=grafica_image).place(x=110,y=420)

            else:
                tk.messagebox.showerror("Error", "Verifique la entrada de datos.")


            Hypergeometric_root.mainloop()
        
        discrete_root.destroy()
        Hypergeometric_root = tk.Toplevel(root)                 
        Hypergeometric_root.title("EzStatistics")                     
        Hypergeometric_root.geometry("800x850")
        Hypergeometric_root.config(bg="white")                
        Hypergeometric_root.iconbitmap("Images/Icon.ico")
        Hypergeometric_root.resizable(0, 0)

        tk.Label(Hypergeometric_root, text="Ingrese el valor de N:", fg="black", font=("Arial",12)).place(x=50,y=125)
        tk.Label(Hypergeometric_root, text="Ingrese el valor de k:", fg="black", font=("Arial",12)).place(x=50,y=162)
        tk.Label(Hypergeometric_root, text="Ingrese el valor de n:", fg="black", font=("Arial",12)).place(x=50,y=200)
        tk.Label(Hypergeometric_root, text="Ingrese el valor de x:", fg="black", font=("Arial",12)).place(x=50,y=237)
        tk.Label(Hypergeometric_root, text="Ingrese el número de decimales desados (0 a 8):", fg="black", font=("Arial",12)).place(x=50,y=275)
        tk.Label(Hypergeometric_root, text="P(X=x)", fg="black", font=("Arial",12)).place(x=50,y=312)
        tk.Label(Hypergeometric_root, text="P(X<=x)", fg="black", font=("Arial",12)).place(x=50,y=350)
        tk.Label(Hypergeometric_root, text="Media:", fg="black", font=("Arial",12)).place(x=350,y=312)
        tk.Label(Hypergeometric_root, text="Desviación estándar:", fg="black", font=("Arial",12)).place(x=350,y=350)

        text1 = StringVar()   #P(X=x)
        text2 = StringVar()   #P(X<=x)
        text3 = StringVar()   #Media
        text4 = StringVar()   #Desviación estándar


        tk.Entry(Hypergeometric_root, textvariable=text1, fg="black", font=("Arial",12), state="disabled").place(x=150,y=312)
        tk.Entry(Hypergeometric_root, textvariable=text2, fg="black", font=("Arial",12), state="disabled").place(x=150,y=350)
        tk.Entry(Hypergeometric_root, textvariable=text3, fg="black", font=("Arial",12), state="disabled").place(x=525,y=312)
        tk.Entry(Hypergeometric_root, textvariable=text4, fg="black", font=("Arial",12), state="disabled").place(x=525,y=350)

        N_entry = DoubleVar()
        ttk.Entry(Hypergeometric_root,textvariable=N_entry).place(x=525,y=125)
        k_entry = DoubleVar()
        ttk.Entry(Hypergeometric_root,textvariable=k_entry).place(x=525,y=162)
        n_entry = DoubleVar()
        ttk.Entry(Hypergeometric_root,textvariable=n_entry).place(x=525,y=200)
        x_entry = DoubleVar()
        ttk.Entry(Hypergeometric_root,textvariable=x_entry).place(x=525,y=237)
        d_entry = DoubleVar()
        ttk.Entry(Hypergeometric_root,textvariable=d_entry).place(x=525,y=275)


        tk.Button(Hypergeometric_root,text="Aceptar",command=finish).place(x=380,y=385)

        title_image = tk.PhotoImage(file="Images/Hypergeometric.png")                   
        tk.Label(Hypergeometric_root,image=title_image).place(x=100,y=30)

        title_function = tk.PhotoImage(file="Images/Hypergeometric_function.png")                   
        tk.Label(Hypergeometric_root,image=title_function).place(x=530,y=15)

        grafica_image = tk.PhotoImage(file="Images/Base.png")                   
        tk.Label(Hypergeometric_root,image=grafica_image).place(x=110,y=420)     

        Hypergeometric_root.mainloop()

    def Poisson_window():

        def finish(*_):                                     #Función que procesa los datos de entrada y los valida
            aux = 0
            while aux == 0:                                 #Loop para comprobar que el usuario dé datos validos
                try:                                        #Intenta transformar los datos a flotantes para verificar que la entrada sea un número real
                    M = float(M_entry.get())
                    x = float(x_entry.get())
                    d = float(d_entry.get())
                    aux = 1
                except:                                     #Si la entrada no es un número real da un mensaje de error
                    raise tk.messagebox.showerror("Error", "Verifique la entrada de datos.")
                    
            if float(x_entry.get()) % 1 == 0:               #Convierte los datos enteros a int y el resto a flotante
                x = int(x_entry.get())
            else:
                x = float(x_entry.get())
            if float(d_entry.get()) % 1 == 0:
                d = int(d_entry.get())
            else:
                d = float(d_entry.get())    
                
            s = Poisson(float(M_entry.get()),x,d)           #Asocia la clase Poisson a la variable s con las entradas del usuario
            if s.Validate() == 1:                           #Utiliza el metodo validate de la clase Poisson para verificar que los datos sean adecuados
                s.graph()                                   #Utiliza el metodo de graph de la clase Poisson para obtener una grafica de los datos con al funcion de Poisson
 
                #Se redimensiona la grafica
                fixed_height = 413                          
                image = Image.open('Images\Poisson_Graph.png')
                height_percent = (fixed_height / float(image.size[1]))
                width_size = int((float(image.size[0]) * float(height_percent)))
                image = image.resize((width_size, fixed_height), Image.NEAREST)
                image.save('Images\Poisson_Graph.png')

                #Se utiliza el metodo Evaluate y Estadisticos de la clase Poisson para obtener los valores deseados
                data01 = s.Evaluate()
                data02 = s.Estadisticos()

                #Da el valor correspondiente a las variables para que sean mostradas en la interfaz
                text1.set(str(data01[0]))
                text2.set(str(data01[1]))
                text3.set(str(data02[0]))
                text4.set(str(data02[2]))

                #Se procesa y coloca la imagen de la grafica
                grafica_image = tk.PhotoImage(file="Images\Poisson_Graph.png")     
                tk.Label(Poisson_root,image=grafica_image).place(x=110,y=405)

            else:
                tk.messagebox.showerror("Error", "Verifique la entrada de datos.")            #Si los datos no son adecuados da un mensaje de error


            Poisson.mainloop()                                                                #Asegura que las variables locales no se destruyan
        
        discrete_root.destroy()
        Poisson_root = tk.Toplevel(root)                 
        Poisson_root.title("EzStatistics")                     
        Poisson_root.geometry("800x850")
        Poisson_root.config(bg="white")                
        Poisson_root.iconbitmap("Images/Icon.ico")
        Poisson_root.resizable(0, 0)

        tk.Label(Poisson_root, text="Ingrese la media :", fg="black", font=("Arial",12)).place(x=50,y=175)
        tk.Label(Poisson_root, text="Ingrese el valor de x:", fg="black", font=("Arial",12)).place(x=50,y=212)
        tk.Label(Poisson_root, text="Ingrese el número de decimales desados (0 a 8):", fg="black", font=("Arial",12)).place(x=50,y=250)
        tk.Label(Poisson_root, text="P(X=x)", fg="black", font=("Arial",12)).place(x=50,y=287)
        tk.Label(Poisson_root, text="P(X<=x)", fg="black", font=("Arial",12)).place(x=50,y=323)
        tk.Label(Poisson_root, text="Media:", fg="black", font=("Arial",12)).place(x=350,y=287)
        tk.Label(Poisson_root, text="Desviación estándar:", fg="black", font=("Arial",12)).place(x=350,y=323)

        text1 = StringVar()
        text2 = StringVar()
        text3 = StringVar()
        text4 = StringVar()


        tk.Entry(Poisson_root, textvariable=text1, fg="black", font=("Arial",12), state="disabled").place(x=150,y=287)
        tk.Entry(Poisson_root, textvariable=text2, fg="black", font=("Arial",12), state="disabled").place(x=150,y=323)
        tk.Entry(Poisson_root, textvariable=text3, fg="black", font=("Arial",12), state="disabled").place(x=525,y=287)
        tk.Entry(Poisson_root, textvariable=text4, fg="black", font=("Arial",12), state="disabled").place(x=525,y=323)

        M_entry = DoubleVar()
        ttk.Entry(Poisson_root,textvariable=M_entry).place(x=525,y=175)
        x_entry = DoubleVar()
        ttk.Entry(Poisson_root,textvariable=x_entry).place(x=525,y=212)
        d_entry = DoubleVar()
        ttk.Entry(Poisson_root,textvariable=d_entry).place(x=525,y=250)


        tk.Button(Poisson_root,text="Aceptar",command=finish).place(x=380,y=365)

        title_image = tk.PhotoImage(file="Images/Poisson.png")                   
        tk.Label(Poisson_root,image=title_image).place(x=140,y=50)

        title_function = tk.PhotoImage(file="Images/Poisson_function.png")                   
        tk.Label(Poisson_root,image=title_function).place(x=475,y=50)

        grafica_image = tk.PhotoImage(file="Images/Base.png")                   
        tk.Label(Poisson_root,image=grafica_image).place(x=110,y=405)     

        Poisson_root.mainloop()


    root.iconify()                                    #Miniminiza root 
    discrete_root = tk.Toplevel(root)                 #Crea la nueva ventana
    discrete_root.title("EzStatistics")               #Titulo de la nueva ventana
    discrete_root.geometry("800x800")                 #Tamaño de la nueva ventana
    discrete_root.resizable(0, 0)                     #No permite cambaiar el tamaño de la ventana
    discrete_root.iconbitmap("Images/Icon.ico")       #Icono del programa
    discrete_root.config(bg="white")                  #Fondo de la ventana

    #<------------------------------Imagenes-------------------------------->
    discrete_title = tk.PhotoImage(file="Images\Discrete_title.png")             
    tk.Label(discrete_root,image=discrete_title).place(x=150,y=50) 

    Binomial_Button_Image = PhotoImage(file = "Images\Binomial_button.png") 
    photoimage01 = Binomial_Button_Image.subsample(3, 3) 

    Hypergeometric_Button_Image = PhotoImage(file = "Images\Hypergeometric_button.png") 
    photoimage02 = Hypergeometric_Button_Image.subsample(3, 3)

    Poisson_Button_Image = PhotoImage(file = "Images\Poisson_button.png") 
    photoimage03 = Poisson_Button_Image.subsample(3, 3)

    #<-------------------------------Botones--------------------------------->
    tk.Button(discrete_root, text = 'Binomial', image = photoimage01, compound = LEFT,font =( 'Verdana', 15),bg="white", command=Binomial_window).place(x=230,y=250)

    tk.Button(discrete_root, text = 'Hipergeométrica', image = photoimage02, compound = LEFT,font =( 'Verdana', 15),bg="white", command=Hypergeometric_window).place(x=230,y=350)

    tk.Button(discrete_root, text = 'Poisson', image = photoimage03, compound = LEFT,font =( 'Verdana', 15),bg="white", command=Poisson_window).place(x=230,y=475)
    
    discrete_root.mainloop()                                                       #El programa no saldrá de esta función, los widgets (variable locales) no se destruirán



#<-----------Configuración de la ventana principal root---------->
root = tk.Tk()
root.title("EzStatistics")                 #Titulo de la ventana
root.geometry("800x800")                   #Dimensiones de la venta (anchoxaltura)
root.resizable(0, 0)                       #No permite cambaiar el tamaño de la ventana
root.iconbitmap("Images/Icon.ico")         #Icono del programa
root.config(bg="white")                    #Fondo de la ventana


#<--------------------------Imagenes----------------------------->
root_title = tk.PhotoImage(file="Images/root_label.png")          #Se procesa la imagen
tk.Label(root,image=root_title).place(x=150,y=50)                 #Se inserta la imagen

Var_continua = ImageTk.PhotoImage(file="Images\Continue_Image.png")  #Se procesa la imagen
tk.Label(root,image=Var_continua).place(x=100,y=350)                 #Se inserta la imagen

Var_discreta = ImageTk.PhotoImage(file="Images\Discrete_Image.png")  #Se procesa la imagen
tk.Label(root,image=Var_discreta).place(x=450,y=350)                 #Se inserta la imagen
#<----------------------------Botones----------------------------->
tk.Button(root, text="Variable continua", compound="top",command=continue_window).place(x=170,y=550)
tk.Button(root, text="Variable discreta", compound="top",command=discrete_window).place(x=520,y=550)



root.mainloop()                          #Hace un ciclo infinito para que el programa no se cierre