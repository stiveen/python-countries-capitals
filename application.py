"""This program saves and capitalse countries and shows"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-
from collections import OrderedDict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import getpass
TODO = {}
PAISES = []
CAPITALES = []
def email():
    """This feature allows you mail a message to one person or recipient"""
    print "Send email by gmail"
    try:
        fromaddr = raw_input("Count from gmail: ")
        password = getpass.getpass("Password: ")
        toaddrs = raw_input("to: ")
        #asunto = raw_input("subject, from message: ")
        body = "Countries\t========\tCapitals\n"
        for msg in TODO:
            body = body + str(msg).center(20) +str(TODO[msg]).center(40) + "\n"
        msg = MIMEMultipart()
        msg['From'] = fromaddr #This saves the mail of the sender
        msg['To'] = toaddrs  #This saves the mail of the receiver
        msg['Subject'] = "Countries and Capitals"  #This saves the subject
        msg.attach(MIMEText(body, 'plain')) #This saves the message
    except TypeError:
        print "Try again"

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "yes"
        raw_input("press enter")
    except Exception as inst:
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

def question():
    """Generates a question for function call in the contry"""
    val3 = raw_input("You want to enter another country and capital?y/n\n")
    val3 = val3.lower()
    if val3 == "y":
        contry()
    elif val3 == "n":
        menu()
    else:
        print "Your character is not valid try again"
        limpiar()
        question()

def contry():
    """In this function the countries and capitals are entered and stored in lists and dictionary"""
    var = True
    while var == True:
        val1 = raw_input("Enter a country:")
        val1 = val1.capitalize()
        if str(val1).isdigit() == False or " " in val1:
            PAISES.append(val1)
            var = False
        else:
            print "Your data is not valid try again"
            var = True
    vor = True
    while vor == True:
        val2 = raw_input("Enter a capitals:")
        val2 = val2.capitalize()
        if str(val2).isdigit() == False or " " in val2:
            CAPITALES.append(val2)
            vor = False
        else:
            print "Your data is not valid try again"
            vor = True
    TODO[val1] = val2
    limpiar()
    question()

def contries():
    """It is a function that shows the countries admitted"""
    print "CONTRIES"
    for i in PAISES:
        print i
    raw_input("Enter persione")
    limpiar()
    menu()

def capitals():
    """It is a function that shows capital entered lal"""
    print "CAPITALS"
    for i in CAPITALES:
        print i
    raw_input("Enter persioner")
    limpiar()
    menu()

def alll():
    """It is a function that shows countries and capital entered"""
    print "Contries"+"===================="+"Capitals"
    for i in TODO:
        print i.ljust(10), "..............", TODO[i].rjust(10)
    raw_input("Press enter to continue")
    limpiar()
    menu()

def allordered():
    """It is a function that shows countries and capital sorted alphabetically capitals only"""
    print "          --All Ordered--          "
    print "==================================="
    print " COUNTRIES ".center(15)+" CAPITALS ".center(15)
    print "==================================="
    ordered = OrderedDict(sorted(TODO.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print key.center(20) + value.center(10)
    raw_input("Press enter to continue")
    limpiar()
    menu()


def menu():
    """It is a function that displays the menu and
    lets you access the option to show you the menu"""
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
    opcion = raw_input("Enter option:")
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
