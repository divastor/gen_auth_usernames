#!python2

import urllib

def print_list(mylist):
    for i in (mylist):
        print(i)

def chopAndAdd(chop, add1, max_of_chop, add2=""):
    chopped=chop[0:max_of_chop]
    result=chopped
    max_chop=len(chop)-max_of_chop
    mylist=[]
    mylist.append(result+add1+add2)
    mylist.append(add1+add2+result)
    if(add2!=""):
        mylist.append(result+add2+add1)
        mylist.append(add2+add1+result)
    for i in chop[max_of_chop:]:
        result+=i
        mylist.append(result+add1+add2)
        mylist.append(add1+add2+result)
        if(add2!=""):
            mylist.append(result+add2+add1)
            mylist.append(add2+add1+result)
    return mylist

def gen_username(name, surname, father="", secondary="", n=6):
    mylist=chopAndAdd(name,surname[0], n)
    mylist+=chopAndAdd(surname,name[0], n)
    mylist+=chopAndAdd(surname,name[0:2], n)
    mylist+=chopAndAdd(name,surname[0:2], n)
    if(father!="" and father!="-" and father[0]!=" "):
        mylist+=chopAndAdd(name,surname[0], n,father[0])
        mylist+=chopAndAdd(surname,name[0], n,father[0])
    if(secondary!="" and secondary!="-" and secondary[0]!=" "):
        mylist+=chopAndAdd(name,surname[0], n,secondary[0])
        mylist+=chopAndAdd(surname,name[0], n,secondary[0])
    return mylist

def menu(name, surname, father, secondary):
    print("####################################")
    print("1. Edit Name")
    print("     current: "), name
    print("2. Edit Surname")
    print("     current: "), surname
    print("3. Edit Father's Name")
    print("     current: "), father
    print("4. Edit Secondary")
    print("     current: "), secondary
    print("5. See available usernames")
    print
    print("6. Exit")
    print("####################################")

#----------------------------------MAIN-----------------------------------------

#Initializing (Getting proper variables from user)  
print("NAME: ")
name = raw_input()
while(name=="" or name[0]==" " or name=="-"):
    print("Name must NOT be empty!")
    print("NAME: ")
    name = raw_input()
print("SURNAME: ")
surname = raw_input()
while(surname=="" or surname[0]==" " or surname=="-"):
    print("Surname must NOT be empty!")
    print("SURNAME: ")
    surname = raw_input()
print("FATHER: ")
father = raw_input()
print("SECONDARY NAME: ")
secondary = raw_input()

#Menu and Options
flag=0
while(flag==0):
    menu(name, surname, father, secondary)
    print(">"),
    choice=raw_input()
    if(choice=="1"):
        print("NAME: ")
        name = raw_input()
        while(name=="" or name[0]==" " or name=="-"):
            print("Name must NOT be empty!")
            print("NAME: ")
            name = raw_input()
    elif(choice=="2"):
        print("SURNAME: ")
        surname = raw_input()
        while(surname=="" or surname[0]==" " or surname=="-"):
            print("Surname must NOT be empty!")
            print("SURNAME: ")
            surname = raw_input()
    elif(choice=="3"):
        print("FATHER: ")
        father = raw_input()
    elif(choice=="4"):
        print("SECONDARY NAME: ")
        secondary = raw_input()
    elif(choice=="5"):
        n=6
        usernames = gen_username(name.lower(), surname.lower(), father.lower(), secondary.lower(), n)

        approved=[]
        domain = "http://users.auth.gr/"
        not_found = '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>404 Not Found</title>'
        for i in usernames:
            url=domain+i
            url_handler=urllib.urlopen(url)
            if(url_handler.read()[0:len(not_found)]!=not_found):
                approved.append(i)
            
        print_list(approved)
        print("\nPress ENTER to continue")
        raw_input()
    elif(choice=="6" or choice.lower()=="exit"):
        flag=1
        print("Bye!")
    else:
        print("Please choose one of the numbers 1-6!")
