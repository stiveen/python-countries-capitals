import sys
import os 
todo={}
paises=[]
capitales=[]

def limpiar():
    "This function serves to clean in windows and ubuntu"
    os.system("cls")
    os.system("clear")

def question ():
    val3=raw_input("You want to enter another country and capital? y/n\n")
    val3=val3.lower()
    if val3 == "y":
        contry()
    elif val3 == "n":
        menu()
    else:
        print "Your character is not valid try again"
        limpiar()
        question()

def contry():
    var= True
    while var== True:
        val1=raw_input("Enter a country:")
        if val1.isalpha() == True:
            paises.append(val1)
            var =False
        else:
            print "su dato no es valido intentelo de nuevo"
            var = True
    vor = True
    while vor == True:
        val2=raw_input("Enter a capitals:")
        if val2.isalpha() == True:
            capitales.append(val2)
            vor = False
        else:
            print "su dato no es valido intentelo de nuevo"
            vor = True
    limpiar()
    question()
    menu()

def contries():
    for i in paises:
        print i
    raw_input("presione enter")
    limpiar()
    menu()

def capitals():
    for i in capitales:
        print i
    raw_input("presione enter")
    limpiar()
    menu()

def menu ():
    print"       >>>>>>Countries and capitals<<<<<<       "
    print"==============================================="
    print"          -----INSTRUCTIONS--------            "
    print"*write the word what you want for any option"
    print
    print "1.Country"
    print "2.Countries"
    print "3.Capitals"
    print "4.All"
    print "5.All Ordered"
    print "6.Get out"

    menu=raw_input("ingrese una opcion:")
    limpiar()
    if menu == "1":
        contry()
    elif menu == "2":
        contries()
    elif menu == "3":
        capitals()
    elif menu == "4":
        xx
    elif menu == "5":
        xxxxx
    elif menu == "6":
        xxxxx
    else:
        "no"
    
menu()
