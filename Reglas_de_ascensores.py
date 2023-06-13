z = int(input("N° de ascensores para la edicicación: ")) #numero de ascensores a trabajar
V_n = int(input("Ingrese el valor de la velocidad nominal del grupo de ascensores: "))
pn = int(input("Ingrese la capacidad nominal de personas, de los ascensores: "))
Ar = int(input("Ingrese el area de ocupacion disponible: "))
B_i = int(input("N° de pasajeros por piso: "))
#print(B_t, "Estimacion de personas a utilazar los ascensores. ")

P_v = ((3.2//pn) + (0.7*pn) + 0.5) #pasajeros por viaje
print(P_v, "personas por viaje")

n_a = int(input("N° de plantas a incluir, sin contar planta principal: ")) #pisos totales

#si se dividen en secciones, tienes que tomar el piso mas alto de la seccion

Zot = int(input("N° de sotanos: "))
e_p = float(input("Distancia entre los pisos de la edicicación: "))
H_a = (n_a * e_p) #recorrido superior total de los ascensores
print(H_a , "metros totales del recorrido superior")
print("distribuyendo la atencion de ascensores por secciones de atencion de piso, tenemos")
 
n = int(input("N° de pisos a atender por ascensor: "))
B_t = ((B_i * 2 * n) + (15*3)) #Valor de personas por piso por el factor de ocupacion, sumando los sotanos multiplicado por el numero de personas
n_e = (n_a - n) #total de pisos por atender, restando los atendidos, sin el recorrido expreso.
B = B_t #n_a va a variar segun sea el piso maximo donde llegue los ascensores
H_e = (n_e * e_p) #Total de pisos por atender, restando los atendidos, sin el recorrido expreso
H_s = (H_a - H_e) #Recorrido sobre la planta principal con servicio de ascensores
print(H_e , "Metros recorridos en expreso y ", H_s, "Metros recorridos sobre la planta principal")

n_p = (n*(1-(((n-1)/n)**P_v))) #Numero de paradas probables
print(n_p, "Paradas probables")
print("tomaremos la entrada libre para los pasajeros de 1000m**2")

Q = ((H_s//n_p)**0.5)
print(Q , "valor condicional de la velocidad nominal")

T_1 = float(input("Ingrese el tiempo de recorrido, tomando en consideracion la tabla 7: "))
T_2 = float(input("Ingrese el tiempo de abordaje, tomando en consideracion la tabla 8: "))
if Q > V_n: #condiciones para calcular tiempo de viaje.
	TVC = ((((2*H_a)/(V_n))) - ((H_s/V_n)) + ((2*V_n)/(1)) + (((2*H_s)/((n_p*(Q)))*(n_p-1)) + (T_1*(n_p+1) + (T_2)*(P_v) )))
	print(TVC , "Segundos de viaje sobre las plantas. ")
else:
	TVC = ((((2*H_a)/(V_n)))-((H_s/V_n)) + ((2*V_n)/(1)) + (((2*H_s)/((n_p*(Q))*n_p-1)) + (T_1*(n_p+1) + (T_2)*(P_v) )))
	print(TVC , "Segundos del viaje completo")

Num = int(input("Ingrese el valor entero del tiempo de viaje para el calculo del tiempo adicional: "))
TA = ((Num*((Zot*10)/100))) #Tiempo que tarda en recorrer los sotanos.
print(TA, "Segundos de tiempo adicional")

TTV = float(TA + Num) # tiempo total de viaje
print(TTV, "Es el tiempo que tarda en recorrer todo el circuito. ")

I = float (TTV/z)
print(I, "Segundos del intervalo probable. ") #El intervalo probable,  se tiene que cumplir la tabla 1

C = ((((((300*P_v)*z)*100)/TTV*B)))
print(C, "es us capacidad de transporte.") #Capacidad de transporte, se tiene que cumplir la 
											#tabla 1