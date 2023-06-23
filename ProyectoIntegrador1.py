from tkinter import *
from tkinter.ttk import *
window = Tk()
from utils import *
from logic import *

def from_diagnostico():
    clausulas = []

    # Enfermedades

    clausulas.append(expr("(FaltaAire(x) & Sibilancias(x) & DificultadSueño(x)) ==> Enfermo(x,Asma)"))
    clausulas.append(expr("(DolorPecho(x) & OpresionPecho(x)) ==> Enfermo(x,Asma)"))


    clausulas.append(expr("(TosSangre(x) & PerdidaApetito(x)) ==> Enfermo(x, CancerDePulmon)"))
    clausulas.append(expr("(GangliosInflamados(x) & InfeccionesRespiratoriasFrecuentes(x)) ==> Enfermo(x, CancerDePulmon)"))
    clausulas.append(expr("(DificultadSueño(x) & DolorMuscular(x)) ==> Enfermo(x, Cansancio)"))

    clausulas.append(expr("(Temperatura(x) & Diarrea(x)) ==> Enfermo(x, Neumonía)"))
    clausulas.append(expr("(Escalofrios(x) & Diarrea(x)) ==> Enfermo(x, Neumonía)"))
    clausulas.append(expr("(TosFlema(x) & DificultadRespirar(x)) ==> Enfermo(x, Neumonía)"))
    clausulas.append(expr("(Nauseas(x) & Vomitos(x)) ==> Enfermo(x, Neumonía)"))

    clausulas.append(expr("DolorIntensoEnGarganta(x) & PerdidaApetito(x) ==> Enfermo(x,InfeccionDeGarganta)"))
    clausulas.append(expr("Debilidad(x) & Temperatura(x) ==> Enfermo(x,InfeccionDeGarganta)"))
    clausulas.append(expr("DolorTragar(x) & BloqueoGarganta(x)==> Enfermo(x,InfeccionDeGarganta)"))

    # Tratamiento de enfermedades 
    clausulas.append(expr("Enfermo(x,Asma) ==> Tratamiento(EvitarTabaco,x)"))
    clausulas.append(expr("Enfermo(x,Asma) ==> Tratamiento(RealizarDeporte,x)"))
    clausulas.append(expr("Enfermo(x,Asma) ==> Tratamiento(UtilizarFarmacos,x)"))
    clausulas.append(expr("Enfermo(x,Asma) ==> Tratamiento(EvitarAlergenos,x)"))

    clausulas.append(expr("Enfermo(x,CancerDePulmon) ==> Tratamiento(Quimioterapia,x)"))
    clausulas.append(expr("Enfermo(x,CancerDePulmon) ==> Tratamiento(LobectomiaPulmonar,x)"))
    clausulas.append(expr("Enfermo(x,CancerDePulmon) ==> Tratamiento(DejarDeFumar,x)"))

    clausulas.append(expr("Enfermo(x,Neumonía) ==> Tratamiento(TomarAntibióticos,x)"))
    clausulas.append(expr("Enfermo(x,Neumonía) ==> Tratamiento(TomarAnalgesicos,x)"))
    clausulas.append(expr("Enfermo(x,Neumonía) ==> Tratamiento(TomarMedicamentoTos,x)"))

    clausulas.append(expr("Enfermo(x,InfeccionDeGarganta) ==> Tratamiento(Reposo,x)"))
    clausulas.append(expr("Enfermo(x,InfeccionDeGarganta) ==> Tratamiento(Paracetamol,x)"))
    clausulas.append(expr("Enfermo(x,InfeccionDeGarganta) ==> Tratamiento(Antiobiótico,x)"))
    clausulas.append(expr("Enfermo(x,InfeccionDeGarganta) ==> Tratamiento(Suero,x)"))

    #------------------------------------------------------------------------------------------------------------------
    # BASE DE CONOCIMIENTO 
    #------------------------------------------------------------------------------------------------------------------
    kb= PropDefiniteKB()
    for clausula in clausulas:
        kb.tell(expr(clausula))

    #------------------------------------------------------------------------------------------------------------------
    # TEST
    #------------------------------------------------------------------------------------------------------------------
    name=n_value.get()
    if t1_value.get() == 'si':
        kb.tell(expr("FaltaAire({})".format(name)))

    if t2_value.get() == 'si':
        kb.tell(expr("Sibilancias({})".format(name)))
        
    if t3_value.get() == 'si':
        kb.tell(expr("DificultadSueño({})".format(name)))
        
    if t4_value.get() == 'si':
        kb.tell(expr("DolorPecho({})".format(name)))
        kb.tell(expr("OpresionPecho({})".format(name)))

    if t5_value.get() == 'si':
        kb.tell(expr("Temperatura({})".format(name)))

    if t6_value.get() == 'si':
        kb.tell(expr("Escalofrios({})".format(name)))
        
    if t7_value.get() == 'si':
        kb.tell(expr("TosSangre({})".format(name)))

    if t8_value.get() == 'si':
        kb.tell(expr("TosFlema({})".format(name)))
        
    if t9_value.get() == 'si':
        kb.tell(expr("Nauseas({})".format(name)))
        kb.tell(expr("Vomitos({})".format(name)))

    if t10_value.get() == 'si':
        kb.tell(expr("Diarrea({})".format(name)))
        
    if t11_value.get() == 'si':
        kb.tell(expr("DolorIntensoEnGarganta({})".format(name)))
        
    if t12_value.get() == 'si':
        kb.tell(expr("Debilidad({})".format(name)))
        
    if t13_value.get() == 'si':
        kb.tell(expr("DolorTragar({})".format(name)))

    if t14_value.get() == 'si':
        kb.tell(expr("BloqueoGarganta({})".format(name)))
        
    if t15_value.get() == 'si':
        kb.tell(expr("DificultadRespirar({})".format(name)))
        
    if t16_value.get() == 'si':
        kb.tell(expr("GangliosInflamados({})".format(name)))
        
    if t17_value.get() == 'si':
        kb.tell(expr("InfeccionesRespiratoriasFrecuentes({})".format(name)))
        
    if t18_value.get() == 'si':
        kb.tell(expr("DolorMuscular({})".format(name)))
        
    if t19_value.get() == 'si':
        kb.tell(expr("PerdidaApetito({})".format(name)))
    #------------------------------------------------------------------------------------------------------------------
    # DIAGNÓSTICO DEL PACIENTE 
    #------------------------------------------------------------------------------------------------------------------

    print("\n",name," tu diágnostico es: ")
    answer = fol_fc_ask(kb,expr("Enfermo({},x)".format(name)))
    answer = list(answer)

    if len(answer) > 0: 
        for i in answer:
            print(i[x])
    else: 
        print("\nNo contamos con suficiente información para hacerte un diagnóstico")

    #-----------------------------------------------------------------------------------------------------------------
    # TRATAMIENTO DEL PACIENTE
    #-----------------------------------------------------------------------------------------------------------------

    print("\nTu tratamiento es: ")

    trat = fol_fc_ask(kb,expr("Tratamiento(x,{})".format(name)))
    trat = list(trat)

    if len(trat)>0:
        for i in trat:
            print(i[x])
    else:
        print("No hay tratamiento para tu diagnóstico")
        
    print("\n¡Gracias por utilizar el sistema experto de enfermedades respiratorias!")
    print("\nEsperemas haberte ayudado. Que tengas lindo día.")

#######################################################################################################################
# Create the Label widgets
e1 = Label(window, text="¡Buen día! Bienvenido al sistema experto de enfermedades respiratorias\n",font=("Century Gothic",14), background="#9CCFEC")
e2 = Label(window, text="A continuación te haremos un cuestionario para hacerte un diagnostico preliminar...\n",font=("Century Gothic",12), background="#9CCFEC")
e3 = Label(window, text='¿Cuál es tu nombre?', font=("Century Gothic",12),background="#9CCFEC", anchor="w")
n1 = Label(window, text='', font=("Century Gothic",12), background="#9CCFEC", anchor="w")
n2 = Label(window, text='', font=("Century Gothic",12), background="#9CCFEC", anchor="w")
e4 = Label(window, text='Responda las siguientes preguntas con si o no\n', font=("Century Gothic",12), background="#9CCFEC")
p1 = Label(window, text='¿En los últimos meses has sentido falta de aire?',font=("Century Gothic",10), background="#9CCFEC")
p2 = Label(window, text='¿Tienes sibilancias al respirar? ',font=("Century Gothic",10), background="#9CCFEC")
p3 = Label(window, text='¿Tienes problemas para dormir causados por falta de aliento o tos?',font=("Century Gothic",10), background="#9CCFEC")
p4 = Label(window, text='¿Sientes dolor y opresión en el pecho?',font=("Century Gothic",10), background="#9CCFEC")
p5 = Label(window, text='¿Tienes fiebre?',font=("Century Gothic",10), background="#9CCFEC")
p6 = Label(window, text='¿Tienes escalofríos? ', font=("Century Gothic",10), background="#9CCFEC")
p7 = Label(window, text='¿Has tenido algún episodio de tos con sangre o expectoración de sangre?', font=("Century Gothic",10), background="#9CCFEC")
p8 = Label(window, text='¿Has tenido tos con flema o expectoración de pus?', font=("Century Gothic",10), background="#9CCFEC")
p9 = Label(window, text='¿Has experimentado náuseas y/o vómitos?', font=("Century Gothic",10), background="#9CCFEC")
p10 = Label(window, text='¿Tienes diarrea? ', font=("Century Gothic",10), background="#9CCFEC")
p11= Label(window, text='¿Sientes dolor intenso en la garganta?',font=("Century Gothic",10), background="#9CCFEC")
p12 = Label(window, text='¿Sientes debilidad?',font=("Century Gothic",10), background="#9CCFEC")
p13 = Label(window, text='¿Sientes dolor a la hora de tragar alimentos, líquidos o tu misma saliva?',font=("Century Gothic",10), background="#9CCFEC")
p14 = Label(window, text='¿Sientes bloqueo en la garganta?',font=("Century Gothic",10), background="#9CCFEC")
p15 = Label(window, text='¿Sientes dificultad para respirar?',font=("Century Gothic",10), background="#9CCFEC")
p16 = Label(window, text='¿Tienes los ganglios inflamados?',font=("Century Gothic",10), background="#9CCFEC")
p17 = Label(window, text='En los últimos meses, ¿te enfermas seguido de enfermedades respiratorias? ',font=("Century Gothic",10), background="#9CCFEC")
p18 = Label(window, text='¿Tiene dolor muscular?',font=("Century Gothic",10), background="#9CCFEC")
p19 = Label(window, text='¿Tiene perdida de apetito?',font=("Century Gothic",10), background="#9CCFEC")
p20 = Label(window, text="\n", background="#9CCFEC")
# Create the Text Widgets
n_value = StringVar()
n =  Entry(window, textvariable = n_value, font=("Century Gothic",12),justify=CENTER)
t1_value = StringVar()
t1 =  Entry(window, textvariable = t1_value, font=("Century Gothic",10),justify=CENTER)
t2_value = StringVar()
t2 =  Entry(window, textvariable = t2_value, font=("Century Gothic",10),justify=CENTER)
t3_value = StringVar()
t3 =  Entry(window, textvariable = t3_value, font=("Century Gothic",10),justify=CENTER)
t4_value = StringVar()
t4 =  Entry(window, textvariable = t4_value, font=("Century Gothic",10),justify=CENTER)
t5_value = StringVar()
t5 =  Entry(window, textvariable = t5_value, font=("Century Gothic",10),justify=CENTER)
t6_value = StringVar()
t6 =  Entry(window, textvariable = t6_value, font=("Century Gothic",10),justify=CENTER)
t7_value = StringVar()
t7 =  Entry(window, textvariable = t7_value, font=("Century Gothic",10),justify=CENTER)
t8_value = StringVar()
t8 =  Entry(window, textvariable = t8_value, font=("Century Gothic",10),justify=CENTER)
t9_value = StringVar()
t9 =  Entry(window, textvariable = t9_value, font=("Century Gothic",10),justify=CENTER)
t10_value = StringVar()
t10 =  Entry(window, textvariable = t10_value, font=("Century Gothic",10),justify=CENTER)
t11_value = StringVar()
t11 =  Entry(window, textvariable = t11_value, font=("Century Gothic",10),justify=CENTER)
t12_value = StringVar()
t12 =  Entry(window, textvariable = t12_value, font=("Century Gothic",10),justify=CENTER)
t13_value = StringVar()
t13 =  Entry(window, textvariable = t13_value, font=("Century Gothic",10),justify=CENTER)
t14_value = StringVar()
t14 =  Entry(window, textvariable = t14_value, font=("Century Gothic",10),justify=CENTER)
t15_value = StringVar()
t15 =  Entry(window, textvariable = t15_value, font=("Century Gothic",10),justify=CENTER)
t16_value = StringVar()
t16 =  Entry(window, textvariable = t16_value, font=("Century Gothic",10),justify=CENTER)
t17_value = StringVar()
t17 =  Entry(window, textvariable = t17_value, font=("Century Gothic",10),justify=CENTER)
t18_value = StringVar()
t18 =  Entry(window, textvariable = t18_value, font=("Century Gothic",10),justify=CENTER)
t19_value = StringVar()
t19 =  Entry(window, textvariable = t19_value, font=("Century Gothic",10),justify=CENTER)

# Create the Button Widget
b1 = Button(window, text="INICIAR",command=from_diagnostico)

# grid method is used for placing
# the widgets at respective positions
# in table like structure
window.configure(background="#9CCFEC")
e1.grid(row=0, column=0)
e2.grid(row=1, column=0)
n1.grid(row=2, column=0)
e3.grid(row=3, column=0)
n2.grid(row=4, column=0)
e4.grid(row=5, column=0)
p1.grid(row=6, column=0)
p2.grid(row=7, column=0)
p3.grid(row=8, column=0)
p4.grid(row=9, column=0)
p5.grid(row=10, column=0)
p6.grid(row=11, column=0)
p7.grid(row=12, column=0)
p8.grid(row=13, column=0)
p9.grid(row=14, column=0)
p10.grid(row=15, column=0)
p11.grid(row=16, column=0)
p12.grid(row=17, column=0)
p13.grid(row=18, column=0)
p14.grid(row=19, column=0)
p15.grid(row=20, column=0)
p16.grid(row=21, column=0)
p17.grid(row=22, column=0)
p18.grid(row=23, column=0)
p19.grid(row=24, column=0)
p20.grid(row=25, column=0)

n.grid(row=3, column=1)
t1.grid(row=6, column=1)
t2.grid(row=7, column=1)
t3.grid(row=8, column=1)
t4.grid(row=9, column=1)
t5.grid(row=10, column=1)
t6.grid(row=11, column=1)
t7.grid(row=12, column=1)
t8.grid(row=13, column=1)
t9.grid(row=14, column=1)
t10.grid(row=15, column=1)
t11.grid(row=16, column=1)
t12.grid(row=17, column=1)
t13.grid(row=18, column=1)
t14.grid(row=19, column=1)
t15.grid(row=20, column=1)
t16.grid(row=21, column=1)
t17.grid(row=22, column=1)
t18.grid(row=23, column=1)
t19.grid(row=24, column=1)

b1.grid(row=26, column=0)

# Start the GUI
window.mainloop()