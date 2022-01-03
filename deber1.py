import math
import calendar
from string import punctuation

class tipos_datos:
    def __init__(self,num_1,num_2 ):
        
    
        num_1 = int(input("ingrese un numero "))        
        num_2 = int (input("ingrese otro numero "))
        suma = num_1 + num_2
        resta = num_1 - num_2
        mult =num_1 * num_2
        divi =num_1 / num_2
        modulo =num_1 % num_2
        print("la suma es : ",suma)
        print("la resta es : ",resta)
        print("la multi. es : ",mult)
        print("la division es : ",divi)
        print("el modulo es : ",modulo)



    def ejercicio2(self,a,b):
        
        a = 5
        b = 9
        res = ( a **2) + (b **2)
        hipotenusa= math.sqrt(res)
        print("hiotenusa es : ",hipotenusa)

    def ejercicio(self):
        num_1=int(input("ingrese un numero : "))
        num_2=int(input("ingrese otro numero : "))
        num_3=int(input("ingrese otro valor : "))
        
        res=(num_2*num_2)-4*num_1*num_3

        if res <0:
            print("no hay solucion")
        else:
            a=(-num_2+math.sqrt(res))/(2*num_1)
            b=(-num_2-math.sqrt(res))/(2*num_1)

            print(a)
            print(b)    
        

        
    def ejercicio3(self,a1):
        
        a1= 8
        if a1 %2 ==0:
            print("0")
        else: 
            print("1")

    def ejercicio4(self,a1):
        
        a1= int(input("digite 4 numeros : "))
        b = a1
        dec = int (str(b),2)
        print (dec)

    def ejercicio5(self,num_1):
        
        num_1 = int(input("ingrese 4 numeros de 0 y 1 : "))
        b = num_1
        dec = int (str (b),2)
        if dec%2 ==0:
                    print("0")
        else:
                    print("1")
        print(dec)

    def ejercicio6(self,num_1):
        
        num_1= int(input("ingrese un numero : "))
        unidad = num_1%10
        decena = (num_1%100-num_1%10)// 10
        centena = (num_1%1000 - num_1%100)//100
        unidades = (num_1%10000 - num_1%1000)//1000

        print("unidad es : ",unidad)
        print("decena es : ",decena)
        print("centena es : ",centena)
        print("unidades de mil es : ",unidades)


class iterativas :
    def ejercicio1(self):
        a1= int(input("ingrese los numeros : "))
        if a1>1:
            contador =0
            for i in range (2,a1):
                result = a1>i
            if contador ==0:
                print("primo")
            else:
                print("no es primo")

    def ejercicio(self):
        num=int(input("ingrese un numero : "))
        a= num//10000
        b=(num//1000)%10
        c=(num//100)%10
        d=(num//10)%10
        e=num%10
        if a==e and b==d:
            print("es capicua")
        else:
            print("no es capicua")    

        
    def ejercicio2(self):
        a1=int(input("ingrese los numeros : "))
        contador = len(str(a1))
        print(contador)

    def ejercicio3(self):
        a1= int (input("ingrese un numero : "))
        def factorial (a1):
            if a1==0:
                return 1
            else:
                    return a1.factorial(a1-1)
        print(math.factorial(a1))
            

    def ejercicio4(self):
        for a in range (10):
            print("tabla de mult: "+str(a+1))
            for b in range (12):
                print(str(+1)+"*"+str(b+1)+"="+str(a+1)* (b+1))
                print ("\n")
    def ejercicio (self):
        mult = int(input("ingrese un numero : "))
        cont=1
        if mult <=10:
            for a in range (12):
                print("tabla de multiplicar de : ",mult)
                res=mult*cont
                print(mult,"*",cont,"=",res)
        else:
            print("ingrese un numero menor a 10")

    def va_contraseña (sts):
        if len(sts)<2 or len(sts) >10 :
            print(("contrseña correcta "))
        elif not any([True if c in punctuation else False for c in sts]):
            print("intentelo de nuevo")
        else:
            print("contraseña incorrecta")
            return True
        return False

    intentos=0
    while True:
            contraseña=input("introduce la contraseña : ")
            intentos+=1
            if va_contraseña(contraseña):
                print("la contraseña es ".format(contraseña))
                break
            elif intentos >5:
                contraseña= None
                print("5 intentos maximo")
                break

    def ejercicio24(self):
            ed=[18,24,25,30,35,36]
            pe=[40,50,60,70,80]
            esta=[1.40,1.45,1.50,1.55,1.60,1.70]
            p_edad=(sum())/len()
            p_peso=(sum(pe))/len(pe)
            p_estatura=(sum(pe))/len(esta)
            c=0
            x=0
            while c<8:
                x+=(p_edad.count(18+c))
                c+=1  
            c=1
            mayores_36=0  
            while c<150:
                mayores_36+=(p_edad.count(36+c))
                c+=1
            c=0
            santos=0
            while c<36:
                santos=[i for i,x in enumerate(p_edad) if x>=18 and x<=35]
                c+=1
            suma=0
            c=0
            while c<len(santos):
                suma+=pe[santos[0+c]]
                c+=1
            print(santos)
            print("promedio edad :", p_edad)
            print("promedioa de peso : ", p_peso)
            print("promedio estatura : " ,p_estatura)
            print("un rango entrese 18 y 25 : ", x)
            print("personas mayores : " , mayores_36)
            print("promedio de pesos de todas las personas : " , suma/len(santos))

    def ejercicio26(self):
        for i in range(0,7):
            for j in range(0, i+1):
                print("|" + str(i) + "|" + str(j) + "|")

    def ejercicio27(self):
        c=0
        numerospos=0
        while True:
            numeros=int(input("Ingrese una serie de números positivos: "))
            if numeros==0:
                break
            elif numeros > 1:
                numerospos+=numeros
                c+=1
                prom1=numerospos/c
            print("serie promedio : " ,prom1 )  	

    def ejerciciio(self):
        ingresa = True
        lista = []
        while ingresa:
            valor = int(input("Ingresa un valor o 0 para finalizar, debe ser un valor entero: "))
            if valor == 0:
                break
            else:
                lista.append(valor) 
        print(lista)
        print(u'Menor %s' % min(lista)) 
        menor = lista[0] 
        mayor = lista[0] 
        for elemento in lista: 
            if elemento < menor: 
                menor = elemento
        for elemento in lista:
            if elemento > mayor:
                mayor = elemento
        print(u'Menor %s' % menor)
        print(u'Mayor %s ' % max(lista))
        print(u'Mayor %s ' % mayor)                


class control_datos():
    def  ejercicio1(self):
        seg=(input("ingrese un numero : "))
        dias = seg//(24*60*60)
        horas=seg%(24*60*60)

        horas=seg//(60*60)
        min = seg%(60*60)

        min=seg //(60)

        print("dia es :",dias)
        print("min es : ",min)
        print("hoa es : ",horas)

    
    def ejercicio(self):
            san=0
            año=0
            for a in self:
                san.append(int(a))
            fecha = input("Ingrese la fecha en formato (ddmmaaaa): ")
            (fecha)

            m = san
            n = san[6]
            o = san[5]
            p = san[4]

            if año % 4 != 0:
                print(" El año No es bisiesto")
            elif año % 4 == 0 and año % 100 != 0:
                print(" El año Es bisiesto")
            elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
                print("El año No es bisiesyo")
            elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
                print("El año Es bisiesto")


    def ejercicio(self):
        a= int (input("ingrese el año : "))
        b= int (input("ingrese el mes : "))
        print(calendar.month(a,b))


    def ejercicio(self):
        horas=int(input("ingrese las horas : "))
        min= int (input("ingrese los minutos : "))

        res= (horas*60*60)
        resl=(min*60)

        print("de hora a segundo : ",res)
        print("de min a segundo es : ",resl)    

    def ejercicio(self):
        producto=int(input("ingrese el valor : "))
        pagar=0
        if producto >1000:
            descuento = producto*0.20
            pagar = producto -descuento
            print(pagar)
        else:
            descuento=0
            print("no hay descuento ")    
        
    def ejercicio(self):
        
        A = int(input("Ingrese el primer numero entero positivo: "))

        if A > 0 :
            B = int(input("Ingrese el el segundor numero entero positivo: "))
        if B > 0 :
            C = int(input("Ingrese el Tercer numero entero positivo: "))
            if C > 0:
                if A > B and A > C:
                    print("\n El numero mayor es: ", A)
                    if B > C:
                        print("\n El segundo mayor es: ", B)
                    else:
                        print("\n El segundo mayor es: ", C)
                elif B > A and B > C:
                    print("\n EL numero mayor es: ", B)
                    if A > C:
                        print("\n El segundo mayor es: ", A)
                    else:
                        print("\n El segundo mayor es: ", C)
                elif C > A and C > B:   
                    print("\n EL numero mayor es: ", C)
                    if A > B:
                        print("\n El segundo mayor es: ", A)
                    else:
                        print("\n El segundo mayor es: ", B)
                else:
                    print("No se ha podido deteerminar el mayor de los 3 numeros")                
            else:
                    print("Por favor ingrese un numero entero positivo")  
        else:
                    print("Por favor ingrese un numero entero positivo")  
                    
                            
    def ejercicio(self):

        H_e = int(input("Ingrese de hora en formato de 12 en la que se estaciono: "))
        if H_e >= 0 and H_e <= 12:   
            M_e = int(input("Ingrese el o los minutos en la que se estaciono: "))   
        if M_e >= 0 and M_e < 60: 
            AM_PM_e  = input("SI usted se estaciono en la mañana ingrese la letra A y si ingreso pasado del medio dìa ingrese la letra P: ") 
            if AM_PM_e == "A" or AM_PM_e == "P" :
                H_s = int(input("Ingrese la hora en formato de 12 en la que sale del estacionamiento: "))
                if H_s >= 0 and H_s <= 12:
                    M_s= int(input("Ingrese la hora en la que sale del estacionamiento: ")) 
                    if M_s >= 0 and M_s < 60:
                        AM_PM_s = input("SI usted sale del estacionamiento en la mañana ingrese la letra A y si salio pasado del medio dìa ingrese la letra P: ")
                        if AM_PM_s == "A" or AM_PM_s == "P" :
                            if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "A" and AM_PM_s == "P" or AM_PM_e == "P" and AM_PM_s == "P":
                                if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "P" and AM_PM_s == "P":
                                    resta_H = H_e - H_s
                                    Total_H = resta_H * 4
                                    resta_M = M_e - M_s
                                    Total_M = resta_M/30
                                    Total_M_2 = 0
                                    if Total_M < 0 :
                                        Total_M_2 = 2.50
                                        Total_T = Total_H + Total_M_2
                                        print("El Valor a pagar es: Bs", Total_T)
                                elif AM_PM_e == "A" and AM_PM_s == "P":
                                    H_s+=12
                                    resta_H = H_e - H_s
                                    Total_H = resta_H * 4
                                    resta_M = M_e - M_s
                                    Total_M = resta_M/30
                                    Total_M_2 = 0
                                    if Total_M < 0 :
                                        Total_M_2 = 2.50
                                        Total_T = Total_H + Total_M_2
                                        print("El Valor a pagar es: Bs", Total_T)
                            else:
                                print("Los datos de entrada y salida no coinciden")
                        else:
                            print("Ingrese una Letra Valida")
                    else:
                        print("Ingrese unos minutos de salida valido")        
                else:
                    print("Ingrese una hora de salida valida")
            else:
                print("Ingrese una letra valida")    
        else:
            print("Ingrese una cantidad de minutos valido")   


        
    def ejercicio(self):
        masa=int(input("Escriba su peso  "))
        estatura=int(input("Escriba su estatura  "))
        peso = masa * 0.453591
        imc = peso /estatura
        if imc > 45 :
            print("SU IMC ES ",(imc), " sufre de Obesidad Hiper- Morbida")
        elif imc <=45 and (imc>=40):
            print("SU IMC ES " ,(imc), "  tiene Obesidad - Morbida ")
        elif imc <= 35 and imc >= 30:
            print("SU IMC ES " ,(imc), " tiene Pre- Morbida " )
        elif imc <=29 and imc >=25:
            print("SU IMC ES " ,(imc), " tiene Sobrepeso ")
        elif imc <=25 and imc >=18:
            print("SU IMC ES " ,(imc), " tiene Peso Normal ")
        elif imc == 17:
            print("SU IMC ES " ,(imc)," tiene Peso Bajo ")
        elif imc ==19:
            print("SU IMC ES " ,(imc), " tiene Infra Peso ")

    def ejercicio(self):
        a1 = float(input("Ingrese su peso en Libras: "))
        b1 = int(input("Ingrese su Altura en Centimetros: "))

        B = a1*0.453592
        A = b1 /100

        prom = B/(A * A)

        print(" peso en Kg es: ", B)
        print(" altura en Metros es: ", A)
        print(" promedio es: ", prom)

        if prom < 16 :
            print("Su categoria es Criterio de ingreso.")
        elif prom >= 16 and prom <= 16.9:
            print("Su categoria es infra peso.")
        elif prom >= 17 and prom <= 18.4:
            print("Su categoria es bajo peso.")
        elif prom >= 18.5 and prom <= 24.9:
            print("Su categoria es peso normal.")
        elif prom >= 25 and prom <= 29.9:
            print("Su categoria es sobrepeso.")
        elif prom >= 30 and prom <= 34.9:
            print("Su categoria es obesidad pre-mórbida.")
        elif prom >= 40 and prom <= 45:
            print("Su categoria es obesidad mórbida.")
        elif prom > 45 :
            print("Su categoria es obesidad híper-mórbida.")



    def ejercicio(self):
        d = int(input("Ingrese un dia correspondiente al 2014: "))
        if d > 0 and d < 31:
            m = int(input("Ingrese un numero de mes correspondiente al 2014: "))
            if m > 0 and m <=12 :
                dias_Mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                i = 0
                acum = 0
                while i <= m - 1:
                    acum = acum + dias_Mes[i]
                    i = i + 1
                total = acum + d
                print(" EL total de dias que han transcurrido desde el 1 de enero  hasta la fecha que solicito es: ", total)
                                    
            
                    
class acciones_fun():
    
       
    
     	

    def ejercicio1(self):
            c=0
            edades_mayores=0
            while True:
                
                edades=int((input("digite la edad :")))
                if edades=='':
                    break
                elif edades >= "18":
                    edades=int(edades)
                    edades_mayores+=edades
                    c+=1
                    prom=edades_mayores/c
            return prom

    def ejercicio2(self):
        base=int(input("ingrese la base: "))
        expo=int(input("ingrese el exponente: "))
        a=2
        result=base**a
        print(result)

    def ejercicio3(self):
        a=float(input("digite el datos del poligono :"))
        b=5*a
        return b

    def ejercicio4(self):
        def dis_millas_kilometro(millas):
            kilom=millas*1.60935
            return kilom
        ciudades=['']*12
        abc=['A','B','','C','D','','F','G','','H','I']
        indice=0
        while indice<=11:
            if indice==0 or indice==1 or indice==3 or indice==4 or indice==6 or indice==7 or indice==9 or indice==10:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese ciudad {abc[0+indice]}: ")
                indice+=1
            else:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese distancia entre ciudades en millas: ")
                indice+=1
        print(f"\nEntre {ciudades[0]} ; {ciudades[1]},  {dis_millas_kilometro(int(ciudades[2])):} Km de distancia\t")
        print(f"Entre {ciudades[3]} ; {ciudades[4]},  {dis_millas_kilometro(int(ciudades[5])):} Km de distancia\t")
        print(f"Entre {ciudades[6]} ; {ciudades[7]},  {dis_millas_kilometro(int(ciudades[8])):} Km de distancia\t")
        print(f"Entre {ciudades[9]} ; {ciudades[10]},  {dis_millas_kilometro(int(ciudades[11])):} Km de distancia\t")


    def calcula_pago(horas, valor, extra=False):
        if extra:
            total = round(horas * valor, 2)
        return total + ((total*35) / 100.0)
        return round(horas * valor, 2)

    def horas_extras(self):
        i = 1
        data = []
        datos = {}
       
        while i <= 5:
            empleado = input("Identificación del empleado: ")
            valor = float(input("Valor por hora, debe ser un valor numerico: "))
            horas = int(input("Horas laboradas, debe ser un valor entero: "))
            datos = {'identificacion': empleado, 'valor': valor, 'horas': horas}
            data.append(datos)  
            i += 1
        for d in data: 
            
            if int(d['horas']) <= 40:
                print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' %
                    (d['identificacion'], d['valor'], d['horas'], 0, (d['valor'], d['horas']), 0))
            else:
                
                print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' %
                    (d['identificacion'], d['valor'], d['horas'], d['horas'] - 40, (d['valor'], 40), (d['valor'], int(d['horas']) - 40, True)))    