AA = input("Ingrese el grupo de asensores a trabajar: ")
Z = int (input ("N° de ascensores para la edicicación: ")) #Numero de ascensores a trabajar.
V_n = int (input ("Ingrese el valor de la velocidad nominal del grupo de ascensores: "))
pn = int (input ("Ingrese la capacidad nominal de los ascensores: ")) #capacidad nominal de los ascensores.
Ar = int (input ("Ingrese el valor del area de ocupacion disponible: "))
B_i = int (input ("N° de personas por piso: ")) #Numero universal para todos los proyectos.
P_vd = (3.2//pn + 0.7*pn + 0.5) #Pasageros por viaje.
print (P_vd , "personas por viaje")

P_v = int (input ("Inserte el valor entero de la personas por viaje:"))
n_a = int (input ("N° de plantas a atender por ascensor, sin contar planta principal: ")) #Numero de piso totales.
#Si se dividen en secciones, tienes que tomar el piso mas alto de la seccion.
Zot = int (input ("N° de sotanos:"))
e_p = float (input ("Distancia entre los pisos de la edicicación: ")) #Distancia entre los pisos
H_a = (n_a * e_p )  #recorrido superior total de los ascensores. 
print ((H_a , "metros totales recorrido superior")) 
print ("distribuyendo la atencion de ascensores por secciones de atencion de piso, tenemos:")

n= int (input ("N° de pisos a atender por ascensor: "))
B_t= ((B_i * n) + (15*Zot)) #Valor de personas por piso por el factor de ocupacion, sumando los sotanos multiplicado por el numero de personas por sotano.
n_e = (n_a - n) #Total de pisos por atender, restando los atendidos, sin el recorrido expreso.
B = B_t #n_a va a variar segun sea el piso maximo a donde llegue las ascensores.
H_e = (n_e * e_p ) #Recorrido total en expreso.
H_s = (H_a - H_e) #Recorrido sobre la planta principal con servicio de ascensores. 
print (H_e , "Metros recorridos en expreso y ", H_s, "Metros recorridos sobre la planta principal." )

n_p = (n*(1-(((n-1)/n)**P_v))) #Numero de paradas probables.
print (n_p , "paradas probables")

Q = (((H_s// n_p))**0.5) 
print (Q ,"valor condicional de la velocidad nominal")

T_1 = float (input ("Ingrese los valores para el tiempo de recorrido, tomando en cosideracion la tabla 7:"))
T_2 = float (input ("Ingrese los valores para el tiempo de abordaje, tomando en consideracion la tabla 8:"))
if Q < V_n: #Condiciones para poder calcular el tiempo de viaje.
    TVC = (((2*H_a)/Q)+(V_n)+(H_a/V_n) + (T_1*(n_p+1)) + (T_2*P_v))
    print ("Segundos de viaje sobre las plantas: ", TVC, "s")
else: 
    TVC = ((2*H_a)/(V_n))+(((V_n/1)+T_1)*(n_p+1))-((H_s/(n_p*(V_n)))+((T_2)*(P_v)))
    print ("Segundos de viaje completo: ", TVC, "s")

Num = float (input ("Ingrese el valor entero del tiempo de viaje para el calculo del tiempo adicional: "))
TA= ((Num*((Zot*10)/100))) #Tiempo que tarda en recorrer los sotanos.
print ("Segundos de tiempo adicional: ", TA, "s")

TTV = float (TA + Num) #Tiempo total.
print (TTV , "Segundos es el tiempo que tarda en recorrer todo el circuito.")

I = float (TTV / Z)
print (I , "Segundos del intervalo probable.") #Intervelo probable, se tiene que cumplir la tabla 1. 

C = ((((((300*P_v)*Z)*100))/(TTV*B))) 
print (C , "es su capacidad de transporte.") #Capacidad de transrporte, se tiene que cumplir la tabla 1.
