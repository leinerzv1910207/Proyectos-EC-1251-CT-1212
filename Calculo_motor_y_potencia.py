W_e = int(3600) #revoluciones del motor
W_ee = float(((W_e/60)*2)*3.14)
V_n = int(input("Ingrese la velocidad nominal del ascensor: ")) #velocidad nominal del ascensor

R = float(input("Ingrese el valor del radio del cable (m): ")) #radio de la polea

W_s = round(V_n/R)
print("La velocidad angular de la polea es:", W_s,"rad/s")

N_e = round(W_ee/W_s) #N° de engranajes
print("El N° de engranajes es:", N_e) 

print("la pontencia hacia la polea estara dada por:")

P_c = 2925 #peso del contra peso
P_n = 1950 #peso del ascensor
g = 10 #aceleracion de gravedad
a = 1 #aceleracion establecida en la Ley venezolana
T = int(((P_c*(g-a))+(P_n*(g+a)))/2)
print("La tension de la polea:", T, "N")

print("Para conocer la potencia que nos de un 80%, de eficiencia en la caja de cambio, tenemos")

P_s = round(T*(R*W_s)*(10**(-3))) #potencia de salida del motor
print("La pontencia de salida de la caja de cambio es:", P_s, "kW")

P_e = round(P_s/0.8) #potencia del motor necesaria para trabajar con 80% de eficiencia
print("La pontencia de entrada a la caja de cambio es:", P_e,"kW")

POR = round((P_s/P_e)*100)
print("la eficiencia de la caja es del:", POR, "%")

print("Para obtener la potencia del motor, para que funcione con un 90%, de eficiencia, tenemos")

P_m = round(P_e/0.9)
print("La potencia del motor es igual a:", P_m,"kW")
print("La potencia de salida del motor es igual a:", P_e,"kW")

PORM = round((P_e/P_m)*100)
print("la eficiencia del motor es del:", PORM,"%")