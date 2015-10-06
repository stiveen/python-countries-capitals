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
        val1= val1.title()
        if str(val1).isalpha() == True or " " in val1:
            paises.append(val1)
            var =False
        else:
            print "Your data is not valid try again"
            var = True
    vor = True
    while vor == True:
        val2=raw_input("Enter a capitals:")
        val2= val2.title()
        if str(val2).isalpha() == True or " " in val2:
            capitales.append(val2)
            vor = False
        else:
            print "Your data is not valid try again"
            vor = True
    todo[val1]=val2        
    limpiar()
    question()

def contries():
    for i in paises:
        print i
    raw_input("Enter persione")
    limpiar()
    menu()

def capitals():
    for i in capitales:
        print i
    raw_input("Enter persioner")
    limpiar()
    menu()

def alll():
    print "Contries"+"--"+"Capitals"
    for i in todo:
        print i,"--", todo[i]
    raw_input("Press enter to continue")
    limpiar()
    menu()

def menu ():
    print"       >>>>>>Countries and capitals<<<<<<       "
    print"==============================================="
    print"          -----INSTRUCTIONS--------            "
    print"*write the word what you want for any option"
    print
    print "1.country"
    print "2.countries"
    print "3.capitals"
    print "4.All"
    print "5.All Ordered"
    print "6.Get out"

    menu=raw_input("ingrese una opcion:")
    limpiar()
    if menu == "1" or menu == "country":
        contry()
    elif menu == "2" or menu == "countries":
        contries()
    elif menu == "3" or menu == "capitals":
        capitals()
    elif menu == "4" or menu == "All":
        alll()
    elif menu == "5":
        xxxxx
    elif menu == "6":
        xxxxx
    else:
        "no"
menu()