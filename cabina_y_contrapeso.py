C_n = int(input("Ingrese capacidad nominal del ascensor: "))#N° de personas por ascensor
P_n = C_n*(75) #Peso nominal del ascensor
print("El peso nominal (Kg) del ascensor es:", P_n)

P_c = int(P_n/2) #Peso de la cabina
print("Peso (Kg) de la cabina es:", P_c)

P_cc = int(P_n*1.5) #valor del contra peso 
print("el contra peso de la cabina será:", P_cc)

print("Para calcular el radio de la polea del ascensor, tenemos:")

C_l = int(input("Ingrese el diametro del cable: "))
D = round(40*(C_l)) #diametro de la polea 
print("El diametro de la polea es:", D,"mm")
R = float((D/2)/1000)
print("El radio de la polea es:", R,"m")