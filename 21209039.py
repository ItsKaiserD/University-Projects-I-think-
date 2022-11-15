#Entrada
turing = str(input("Ingrese el codigo Turing: "))

#Procedimiento 1
año = int(turing[0:4:1])
mes = int(turing[4:6:1])
dia = int(turing[6:8:1])
competidores = int(turing[8])
saltos = int(turing[9])
puntaje = int(turing[10::1])

#Procedimiento 2
i = 1
while i <= saltos:
    if competidores == 2 and saltos == 1:
        promedio_1 = int(puntaje[10:10 + int(i):1]) // 2
        promedio_2 = int(puntaje[12:12 + int(i):1]) // 2
    if promedio_1 > promedio_2:
            ganador = "1"
            puntaje = promedio_1
    else:
        ganador = "2"
        puntaje = promedio_2
    if competidores == 3 and saltos == 1:
        promedio_1 = int(puntaje[10:10 + int(i):1]) // 2
        promedio_2 = int(puntaje[12:12 + int(i):1]) // 2
        promedio_3 = int(puntaje[14:14 + int(i):1]) // 2
    if promedio_1 > promedio_2 and promedio_1 > promedio_3:
        ganador = "1"
        puntaje = promedio_1
    elif promedio_2 > promedio_1 and promedio_2 > promedio_3:
        ganador = "2"
        puntaje = promedio_2
    else:
        ganador = "3"
        puntaje = promedio_3
    if competidores == 4 and saltos == 1:
        promedio_1 = int(puntaje[10:10 + int(i):1]) // 2
        promedio_2 = int(puntaje[12:12 + int(i):1]) // 2
        proemdio_3 = int(puntaje[14:14 + int(i):1]) // 2
        promedio_4 = int(puntaje[16:16 + int(i):1]) // 2
    if promedio_1 > promedio_2 and promedio_1 > promedio_3 and promedio_1 > promedio_4:
        ganador = "1"
        puntaje = promedio_1
    elif promedio_2 > promedio_1 and promedio_2 > promedio_3 and promedio_2 > promedio_4:
        ganador = "2"
        puntaje = promedio_2
    elif promedio_3 > promedio_1 and promedio_3 > promedio_2 and promedio_3 > promedio_4:
        ganador = "3"
        puntaje = promedio_3
    else:
        ganador = "4"
        puntaje = promedio_4
     if competidores == 5 and saltos == 1:
        promedio_1 = int(puntaje[10:10 + int(i):1]) // 2
        promedio_2 = int(puntaje[12:12 + int(i):1]) // 2
        promedio_3 = int(puntaje[14:14 + int(i):1]) // 2
        promedio_4 = int(puntaje[16:16 + int(i):1]) // 2
        promedio_5 = int(puntaje[18:18 + int(i):1]) // 2
    if promedio_1 > promedio_2 and promedio_1 > promedio_3 and promedio_1 > promedio_4 and promedio_1 > promedio_5:
        ganador = "1"
        puntaje = promedio_1
    elif promedio_2 > promedio_1 and promedio_2 > promedio_3 and promedio_2 > promedio_4 and promedio_2 > promedio_5:
        ganador = "1"
        puntaje = promedio_2
    elif promedio_3 > promedio_1 and promedio_3 > promedio_2 and promedio_3 > promedio_4 and promedio_3 > promedio_5:
        ganador = "3"
        puntaje = promedio_3
    elif promedio_4 > promedio_1 and promedio_4 > promedio_2 and promedio_4 > promedio_3 and promedio_4 > promedio_5:
        ganador = "4"
        puntaje = promedio_4
    else:
        ganador = "5"
        puntaje = promedio_5
    i += 1

#Salida
print("Año: ", año)
print("Mes: ", mes)
print("DIa: ", dia)
print("Competidores: ", competidores)
print("Saltos: ", saltos)
print("Ganador: "; ganador)
print("Promedio más alto: ", puntaje) 

