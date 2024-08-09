import time, threading, os, shutil, errno, sys

import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox, filedialog

global Ventana
def Create_Carp():
    global arcCreate

    carp = os.getcwd() + "/db_copias"
    try:
        os.mkdir(carp)
        pass
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        pass
    varUrl = carp + "/"

    for y in range(len(varUrl)):
        Url = varUrl.replace('\\','/')
        pass
    arcCreate = Url + "prediseñados.txt"
    try:
        p = open(str(arcCreate), "a")
        pass
    except OSError as q:
        if q.errno != errno.EEXIST:
            raise
        pass
    p.close

    k1 = bool()
    l1 = bool()
    def imagen(k1, li):
        with open(Url + 'ico.png', 'a+b') as k:
            k.write(b'')
            k.close()
            k1 = True

        if k1:
            k = open(Url + 'ico.png', 'w+b')
            k.write(b'')
            k.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x02\x00\x00\x00\x90\x91h6\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00\x7fIDAT8O\x8d\x90\xd1\r\xc0 \x08\x05\xdd\xc19\x1c\xa0#t+g\xa9\x1d\xaec\xf4\x11\x12D\x045\xb9\xf0\xf3\xee~H%\x17M\xbb_\x83^\xd3\xf3\r\x01\xe6zU\x834\xb0\xe9\x8a\xea\xda\x0c&\xb6\x87\xc0H\x1a\xd8\xd2P\xb0\xb5\xf9B\xa3\xe0\xd0\xc6\xdd\x07\xda\x96&\x0cf\x1b\x84\x81k\x03?\x88l\xe0\x04k\xdb\xbeua\x83\x1epsb\xf7\x00\x86i4\x98\x86\x00\x864 R\x99\xc4\xb6\x86\xa5Y%r\xf9\x01\x1e9'\xb2\xa8<lQ\x00\x00\x00\x00IEND\xaeB`\x82")
            k.close()

        with open(Url + 'ico32.ico', 'a+b') as l:
            l.write(b'')
            l.close()
            l1 = 1
            pass


        if l1:
            l = open(Url + 'ico32.ico', 'w+b')
            l.write(b'')
            l.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x02\x00\x00\x00\xfc\x18\xed\xa3\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x01vIDATHK\xad\x96=N\xc3@\x10F\x1dN\x80\x94#@\x1bC\x85D\xc7\x15\x10%\xd7@DT\x91+\x14\xc45(\x11WH\x87D\x85\\\xc3\x11\x908\x01\xf0-\xb3\x1a\x8f\xbd?\xde\x9d\xc9+V\xb3r\xf2\xbe\x1d;\xf1\xeeb\xb5\\5\x05\xdc\x9e\xad}%xx\xdb\xfa*\xc1\xc1s?\x13\xc0\xde\xcf\xef\x0f*$G\x87\xc7TD\x93`\xff\xb9j\x93\x01\xa4\x8ezC(I\xc6\xc0\x8e1\x19\x00{\xa1Z\x82\x18\xca`\xbb\xab\xdd\x951\xfdW\xaf\xb0\x03|\x0b+\x93v0\r\x80\xbd;\xef\xfc\xa4\x9e\xc7\xf55F\xb6\x83Q\x80\xd1\xfer\xbf\xc1xy\xd7q\x1f`\x08\xd8\x97\x1d#\xf5AD\x9e\x81\x02i\xa7\xfaf\xfb\xe4.p\x80e\xf9\xa1\x1d5=p\xd4\xd6\x0e\xa2v\xae\x81) c\xa7\x02\xb8\x00\xdd\xfd\xc9\xd81\x02\xff\xb7\xa0I-y;/\x1fh\x02\xca\xed\xa0:\xa0\xca\x0e\xea\x02j\xed\xa0"@a\x07\xa5\x01:;p\x01\xed\xb2\xdd\xbc\xba\xcf\xa5\xd0\xd9i{\x98\xef@ggf\x02\x8cv\xe0\x03\xa2w\xc9b\x1f\xb6O\x9a\x87X\xec\x92!@6a\xb4\xf3\xf2\xc1\xf4T\x81\x17\xdf\xe9\xce\x15j;V\x89\xb5\xfaIx\x8b\xf6k\x07\xa3\x0e\xf8\xc4\x11\xf61\xab\x06\xa1\x1d\x0c\x01\xa3\xd3\xd2\x7f\xfd~\xd1\x14\xee\x13\xf4\xf0B;\xf0\x01\x93\xd3\x12\x83V\xa8\x88&\xf1\x8f"\xaa&\\@\xca.\xe1$I\xc6\xcb,Nv\xbfy\xb5\x89\xa6\xf9\x03\xfc\xae4\xea\xb8\x0e\xe4\x98\x00\x00\x00\x00IEND\xaeB`\x82')
            l.close()
            pass
        pass

    imagen(k1, l1)
    pass
Create_Carp()

#----------------------------Variables Globales
Titulo = str("Sistema de Copias")             #
Pre = str("Prediseñado")                      #
Dat = str("Datos")                            #
Sb = "$"                                      #
Blist = arcCreate                             #
#-----------------------------Estilo de Letras#
Font = str("Bauhaus 93")                      #
Arial = ("Arial", 11)                         #
Arial_Black = ("Arial Black", 11)             #

#---------------------------------------------#
#---------------Funcionalidad--------------------------------------------------------------------------------------
def in_name():
    global Ventana_2
    Ventana_2 = Toplevel(Ventana)
    Ventana_2.title("Nombre a Guardar")
    Ventana_2.configure(width=300, height=100)
    marco_2 = Frame(Ventana_2, borderwidth = 2)
    marco_2.place(relwidth=2, relheight=2)
    Nombre_Lable_2 = Label(marco_2, text = "Introdusca su nombre: ", font=(Arial_Black, 12), anchor = "center").place(x=20, y=1)
    Nombre_Enter_2 = Entry(marco_2, justify = "center", textvariable = Nombre).place(x = 20, y = 23, width = 260, height=23)
    Nombre_Button_2 = Button(marco_2, text = "Guardar Nombre", command = safe_list).place(x = 20, y = 55)
    pass

def safe_list():
    Ventana_2.destroy()
    N_in = str(Nombre.get().lower())
    D_in = str(Directorio.get())
    A_in = str(Adonde.get())
    T_in = str(Tiempo.get())
    R_in = str(Repetir.get())
    Lista_base.append(N_in+ Sb+ D_in+ Sb+ A_in+ Sb+ T_in+ Sb+ R_in)
    write_user()
    crear()
    pass

def crear():
    Lista_base.sort()
    global Lista_val
    Lista_val = [""]
    for items in Lista_base:
        arreglo = items.split(Sb)
        Lista_val.append(arreglo[0])
        pass
    ruleta_user = Spinbox(marco, value=(Lista_val), textvariable = User_items).place(x = 5, y = 65, width = 115)
    pass

def cargar():
    arc = open(Blist, "r")
    line = arc.readline()
    if line:
        while line:
            if line[-1]=='\n':
                line = line[:-1]
                Lista_base.append(line)
                line = arc.readline()
    arc.close()
    crear()
    pass

def write_user():
    arc = open(Blist, "w")
    Lista_base.sort()
    for items in Lista_base:
        arc.write("")
        esc = str(items + '\n')
        arc.write(esc)
        pass
    arc.close()
    pass

def insert():
    insert = User_items.get()
    for items in Lista_base:
        arreglo = items.split(Sb)
        if insert == arreglo[0]:
            inicio = messagebox.showinfo("Bienvenido","Inicio correcto a " + arreglo[0])
            time.sleep(0.5)
            Directorio.set(arreglo[1])
            Adonde.set(arreglo[2])
            Tiempo.set(arreglo[3])
            Repetir.set(arreglo[4])
            pass
        pass
    crear()
    pass

def eliminar():
    delete = User_items.get()
    quito = bool(0)
    for items in Lista_base:
        arreglo = items.split(Sb)
        if delete == str(arreglo[0]):
            Lista_base.remove(items)
            Lista_val.remove(arreglo[0])
            quito = 1
            messagebox.showinfo("Eliminar","Elemento "+ delete +" eliminado" )
        pass
    write_user()
    crear()
    pass

def del_form():
    Nombre.set("")
    Directorio.set("")
    Adonde.set("")
    Tiempo.set(0)
    Repetir.set(0)
    pass

def active1():
    Buscar1 = filedialog.askdirectory()
    time.sleep(0.5)
    Directorio.set(Buscar1)

def active2():
    Buscar2 = filedialog.askdirectory()
    time.sleep(0.5)
    Adonde.set(Buscar2)
#------------------Validacion de datos del usuario-----------------------------------------------------------------------------------------------------------------------
def verif():
    global a
    a = bool(False)
    if Directorio.get() == str(""):
        showerror(title='Error', message='Introdusca una direccion, por favor.')
        a = 0
        pass
    elif Adonde.get() == str(""):
        showerror(title='Error', message='Introdusca una direccion, por favor.')
        a = 0
        pass
    elif Tiempo.get() == 0:
        showerror(title='Error', message='Introdusca un tiempo diferente de cero para hacer las copias, por favor.')
        a = 0
        pass
    elif Tiempo.get() >= 60:
        showerror(title='Error', message='Introdusca un tiempo menor que 59 minutos para hacer las copias, por favor.')
        Tiempo.set(0)
        a = 0
        pass
    else:
        a = 1
        pass
#-----------------Fin de Validacion-----------------------------------------------------------------------------------------------------------------------------------------------------------
    if a:
        in_name()
        pass
    pass

def Copiar(seg, dir1, dir2, RE):
    global Aviso
    Iniciar_button.configure(state= 'disabled')

    for x in range(RE+RE+RE):
        copiando = "copia: " + repr(x)
        start_copia = shutil.copytree(dir1, dir2, ignore = None, dirs_exist_ok=True)
        Aviso = Label(marco, text = copiando , font=(Arial_Black, 12), relief="raised" , anchor = "center", bg= "pale green", fg = "#CDC")
        Aviso.place(x = 201, y = 250, width = 388, height=40)
        time.sleep(RE)
        ven = Ventana.winfo_exists()
        if ven == False:
            hilo_copiar.join()
            Q = not ven
            time.sleep(2)
            print("hola salida")
            sys.exit(Q)
            pass

        var = Aviso.winfo_exists()
        if var == True:
            time.sleep(RE)
            Aviso.destroy()
            pass
        pass

    Iniciar_button.configure(state= 'active')
    time.sleep(2)
    Iniciar_button.configure(state= 'normal')
    pass
#---------------Sistema funcionalidad------------------------------------------------------------------------------
def inicio():
    dir1 = Directorio.get()
    dir2 = Adonde.get()
    seg = int(Tiempo.get())
    veri1 = bool(False)
    veri2 = bool(False)
    inicio_fun = bool(True)
    for vara1 in dir1:
        if vara1 == "/":
            veri1 = 1
    for vara2 in dir2:
        if vara2 == "/":
            veri2 = 1
    ruta1 = os.path.isdir(dir1)
    ruta2 = os.path.isdir(dir2)
    if (dir2 or dir1) == "/":
        inicio_fun = 0
    if inicio_fun:
        if (ruta1 and ruta2) and (veri1 and veri2):
            if Repetir.get() == True:
                RE = int(1.1)*seg
                pass
            else:
                RE = int(2)
                pass
            global hilo_copiar
            hilo_copiar = threading.Thread(target = Copiar, args = (seg, dir1, dir2, RE,))
            hilo_copiar.start()

        else:
            showerror(title='Error', message='Introdusca una direccion valida o exista')
        pass
    pass
#---------------Fin de Funciones-----------------------------------------------------------------------------------

#---------------------------Ventana Principal-------------------------------------------------------------------------------------------------------
Ventana = Tk()

Ventana.title(Titulo)
Ventana.configure(background = "white")
#Ventana.configure(background = "red")
Ventana.maxsize(595, 395)
Ventana.minsize(595, 395)
Ventana.iconphoto(True, PhotoImage(file='db_copias/ico.png'))
marco = Frame(Ventana, borderwidth = 2,)
marco.place(relwidth=1, relheight=1)
#--------------- Logo ---------------------------------------------------------------------------------------------
def Logo():
    mlogo= Canvas(Ventana, width=17, height=17, bg="white")
    mlogo_segun = mlogo.create_oval( 2, 2, 15, 15, fill = "blue")

    logo = Canvas(Ventana, width = 196, height = 297, bg = "#160013")
    logo.pack()
    logo.place(x = 4, y = 90)
#------------------------------------------------------------------------------------------------------------------
    logo_segun = logo.create_oval( 24, 78, 171, 226, fill = "#e900c2", activefill = "sky blue", width = 0)
    logo_prin = logo.create_oval( 25, 78, 171, 225, fill = "#220023", width = 0)
    logo.configure(highlightbackground = "#2c0674")
    def logo_line():
        linea1 = logo.create_line( 25, 225, 171, 78, fill = "#004781", activefill = "#1900fc", width = 3)
        linea2 = logo.create_line( 45, 215, 161, 98, fill = "#004581", activefill = "#1400c5", width = 3)
        linea3 = logo.create_line( 65, 205, 151, 118, fill = "#004381", activefill = "#0e008a", width = 3)
        linea4 = logo.create_line( 45+40, 225-30, 141, 98+40, fill = "#004081", activefill = "#080053", width = 3)
        pass
    logo_line()
    pass
Logo()
#---------------Variables Intro -----------------------------------------------------------------------------------
Nombre = StringVar()
Directorio = StringVar()
Adonde = StringVar()
Tiempo = IntVar()
Repetir = BooleanVar()
User_items = StringVar()
Lista_base = []

#---------------Herramientas---------------------------------------------------------------------------------------

#---------------Titulo --------------------------------------------------------------------------------------------
Titulo_label = Label(marco, text = Titulo, font=(Font, 14),  anchor = "center", bg="Black")
#---------------columna 0 Prediseñados-----------------------------------------------------------------------------
Pre_label = Label(marco, text = Pre, font=(Font, 12), relief = "raised", anchor = "center")
#releta donde de encuentran los usuarios guardados
ruleta_user = Spinbox(marco, textvariable=User_items)
ruleta_add = Button(marco, text = "Ins", command = insert,  relief="ridge", borderwidth=1, activebackground="#b7faff", activeforeground="white", font=(Arial_Black, 9))#insertar en el input
ruleta_del = Button(marco, text = "Quit", command = eliminar, relief="ridge", borderwidth=1, activebackground="#ffc5b7", activeforeground="white", font=(Arial_Black, 9))
#---------------columna 1 Datos-----------------------------------------------------------------------------------
#Titulo
Dat_label = Label(marco, text = Dat, relief = "raised", anchor = "center", font=(Font, 12))
#Direccion a enviar
Arc_label = Label(marco, text = " - Direccion del archivo a Copiar", font=Arial, relief = "raised", anchor = "nw")
Dir_label1 = Label(marco, text = "Dirección: ", font=Arial_Black, )
#Entrada para buscar o crear
Dir_Enter = Entry(marco, justify = "left", textvariable = Directorio, highlightcolor="blue violet", highlightthickness=1)
#Boton para buscar archivo, o direccion
Dir_Button = Button(marco, text = "Buscar", width = 10, command = active1, relief="ridge", borderwidth=1)
#---------------Seccion 2-----------------------------------------------------------------------------------------
#Direccion a donde Copiar
Cop_label = Label(marco, text = " - Dirección a donde Copiar", font=Arial, anchor = "nw")
Cop_Label_Enter = Label(marco, text = "Dirección: ", font=Arial_Black, anchor = "nw")
#Entrada a donde Copiar
Cop_Enter = Entry(marco, justify = "left", textvariable = Adonde, highlightcolor="blue violet", highlightthickness=1)
Cop_Button = Button(marco, text = "Buscar", width = 10, command= active2, relief="ridge", borderwidth=1)
#---------------Seccion 3------------------------------------------------------------------------------------------
#Tiempo de espera para Copiar
Tem_label = Label(marco, text = " - Tiempo espera para Copiar", font=Arial, anchor = "nw")
Tem_label_Enter = Label(marco, text = "Hacer copias cada: ", font=("Arial Black", 11), anchor = "nw")
#Entrada de minutos para las copias, la entrada multiplicarla: var x 60
Tem_Enter = Spinbox(marco, from_= 0, to= 59, textvariable = Tiempo, width= 30, highlightcolor="blue violet", highlightthickness=1)
Tem_label_Min = Label(marco, text = "Minutos", font=("Arial Black", 11))
#---------------Seccion 4------------------------------------------------------------------------------------------
#Repetir el procedimiento tantas veces por dia
Re_check = Checkbutton(marco, text = "Repetir", var = Repetir)
#---------------Seccion 5------------------------------------------------------------------------------------------
#Opciones
Borrar_button = Button(marco, text = "Borrar", command= del_form,  relief="ridge", borderwidth=1, activebackground="#ffc5b7", activeforeground="white", font=(Arial_Black, 9))
Guardar_button = Button(marco, text = "Guardar", command= verif, relief="ridge", borderwidth=1, activebackground="#b7faff", activeforeground="white", font=(Arial_Black, 9))
Iniciar_button = Button(marco, text = "Iniciar", command= inicio, relief="ridge", borderwidth=1, activebackground="#f5c3f7", activeforeground="white", font=(Arial_Black, 9))
#---------------Seccion 6------------------------------------------------------------------------------------------
#Pie de Pagina
Label_Autor = Label(marco, text = "Elaborado por MKHERED", font =(Font, 12), anchor = "center", relief = "raised")
#---------------posicion de los objetos XD-------------------------------------------------------------------------
def posicion():
    Titulo_label.place(x=1, y=1, width = 588, height = 30)
    Pre_label.place(x=1, y=31, width = 200, height = 30)
    ruleta_user.place(x = 5, y = 65, width = 115)
    ruleta_add.place(x= 120, y = 64, width = 40, height = 22)
    ruleta_del.place(x = 160, y = 64, width = 40, height = 22)
    Dat_label.place(x = 201, y = 31, width = 388, height = 30)
    Arc_label.place(x = 201, y = 61, width = 388, height = 265)
    Dir_label1.place(x = 203, y = 81, width = 90)
    Dir_Enter.place(x = 291, y = 85, width = 220)
    Dir_Button.place(x = 515, y = 83, width = 70, height=23)
    Cop_label.place(x = 202, y = 110)
    Cop_Label_Enter.place(x=202, y = 130, width = 90)
    Cop_Enter.place(x = 291, y = 134, width = 220)
    Cop_Button.place(x = 515, y =132, width = 70, height=23)
    Tem_label.place(x = 202, y = 156)
    Tem_label_Enter.place(x=202, y = 177, width = 165)
    Tem_Enter.place(x = 370, y = 180, width = 45)
    Tem_label_Min.place(x = 415, y = 177 )
    Re_check.place(x = 220, y = 200)
    Borrar_button.place(x = 207, y = 298, width = 118)
    Guardar_button.place(x = 207 + 128, y = 298, width = 118)
    Iniciar_button.place(x = 207 + 128 + 128, y = 298, width = 118)
    Label_Autor.place(x = 201, y = 326, width = 388, height = 63)
    pass

posicion()
cargar()
Ventana.mainloop()
