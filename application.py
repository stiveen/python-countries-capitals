    #!/usr/bin/python
# -​*- coding: utf-8 -*​-
from collections import OrderedDict
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import os
import sys
import smtplib
import getpass
todo={}
paises=[]
capitales=[]
def email():

    print "Send email by gmail"

    fromaddr = raw_input("Count from gmail: ")
    password = getpass.getpass("Password: ")
    toaddrs = raw_input("to: ")
    #asunto = raw_input("subject, from message: ")
    body = "Countries\t========\tCapitals\n"
    for msg in todo:
           body = body + str(msg).center(20) +str(todo[msg]).center(40) + "\n" 
    msg = MIMEMultipart()
    msg['From'] = fromaddr #This saves the mail of the sender
    msg['To'] = toaddrs  #This saves the mail of the receiver
    msg['Subject'] = "Countries and Capitals"  #This saves the subject
    msg.attach(MIMEText(body, 'plain')) #This saves the message

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr,password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "yes"
        raw_input("press enter")
    except (smtplib.SMTPAuthenticationError):
        limpiar()
        print "User name or password is incorrect introduce again"
        raw_input("press enter")
        limpiar()
        email()

        print "No se envio nada"

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
    print "CONTRIES"
    for i in paises:
        print i
    raw_input("Enter persione")
    limpiar()
    menu()

def capitals():
    print "CAPITALS"
    for i in capitales:
        print i
    raw_input("Enter persioner")
    limpiar()
    menu()

def alll():
    print "Contries"+"===================="+"Capitals"
    for i in todo:
        print i.ljust(10),"..............",todo[i].rjust(10)
    raw_input("Press enter to continue")
    limpiar()
    menu()

def allordered(): 

    print "          --All Ordered--          "
    print "==================================="
    print " COUNTRIES ".center(15)+" CAPITALS ".center(15)
    print "==================================="
    ordered = OrderedDict(sorted(todo.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print key.center(20) + value.center(10)
    raw_input("Press enter to continue")
    limpiar()
    menu()


def menu ():
    print"       >>>>>>Countries and capitals<<<<<<       "
    print"==============================================="
    print"          -----INSTRUCTIONS--------            "
    print"* To choose an option enter the number or name of the option"
    print
    print "1.country"
    print "2.countries"
    print "3.capitals"
    print "4.All"
    print "5.AllOrdered"
    print "6.Get out"
    opcion=raw_input("Enter option:")
    limpiar()

    if opcion == "1" or opcion == "country":
        contry()
    elif opcion == "2" or opcion == "countries":
        contries()
    elif opcion == "3" or opcion == "capitals":
        capitals()
    elif opcion == "4" or opcion == "all":
        alll()
    elif opcion == "5" or opcion == "allordered":
        allordered()
    elif opcion == "6":
        email()
    else:
        print "su dato no es valido vuelva a intentarlo"
    raw_input("Press enter to continue")
    limpiar()
    menu()
    
menu()