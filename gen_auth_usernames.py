#!python2
import datetime
import urllib

def print_list(mylist, string=""):
    if(string==""):
        for i in (mylist):
            print(i)
        return
    else:
        for i in (mylist):
            string+="\n"+i
        return string
        
def chopAndAdd(chop, max_of_chop, add1="" , add2=""):
    chopped=chop[0:max_of_chop]
    result=chopped
    max_chop=len(chop)-max_of_chop
    mylist=[]
    mylist.append(result+add1+add2)
    if(add1!=""):
        mylist.append(add1+add2+result)
    if(add2!=""):
        mylist.append(result+add2+add1)
        mylist.append(add2+add1+result)
    for i in chop[max_of_chop:]:
        result+=i
        mylist.append(result+add1+add2)
        if(add1!=""):
            mylist.append(add1+add2+result)
        if(add2!=""):
            mylist.append(result+add2+add1)
            mylist.append(add2+add1+result)
    return mylist

def gen_username(name, surname, father="", secondary="", n=6):
    mylist=chopAndAdd(name, n)
    mylist+=chopAndAdd(surname, n)
    mylist+=chopAndAdd(name, n, surname[0])
    mylist+=chopAndAdd(surname, n, name[0])
    mylist+=chopAndAdd(surname, n, name[0:2])
    mylist+=chopAndAdd(name, n, surname[0:2])
    if(father!="" and father!="-" and father[0]!=" "):
        mylist+=chopAndAdd(name, n, surname[0], father[0])
        mylist+=chopAndAdd(surname, n, name[0], father[0])
    if(secondary!="" and secondary!="-" and secondary[0]!=" "):
        mylist+=chopAndAdd(name, n, surname[0], secondary[0])
        mylist+=chopAndAdd(surname, n, name[0], secondary[0])
    mylist = list(set(mylist))
    mylist.sort()
    return mylist

def menu(name, surname, father, secondary):
    print("############################################")
    print("1. Edit Name")
    print("     current: "), name
    print("2. Edit Surname")
    print("     current: "), surname
    print("3. Edit Father's Name")
    print("     current: "), father
    print("4. Edit Secondary Name")
    print("     current: "), secondary
    print("5. Run script and see available usernames")
    print
    print("6. Write to file")
    print
    print("7. Exit")
    print("############################################")
    return

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
n=6

#Menu and Options
flag=0
approved=[]
while(flag==0):
    
    menu(name, surname, father, secondary)
    choice=raw_input(">")

    #Edit Name
    if(choice=="1"):
        approved=[]
        print("NAME: ")
        name = raw_input()
        while(name=="" or name[0]==" " or name=="-"):
            print("Name must NOT be empty!")
            print("NAME: ")
            name = raw_input()
    #Edit Surname
    elif(choice=="2"):
        approved=[]
        print("SURNAME: ")
        surname = raw_input()
        while(surname=="" or surname[0]==" " or surname=="-"):
            print("Surname must NOT be empty!")
            print("SURNAME: ")
            surname = raw_input()

    #Edit Father's Name
    elif(choice=="3"):
        approved=[]
        print("FATHER: ")
        father = raw_input()

    #Edit Secondary Name
    elif(choice=="4"):
        approved=[]
        print("SECONDARY NAME: ")
        secondary = raw_input()

    #Run Script
    elif(choice=="5"):
        usernames = gen_username(name.lower(), surname.lower(), father.lower(), secondary.lower(), n)
        date=datetime.datetime.now()
        
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

    #Write results to file
    elif(choice=="6"):
        if(len(approved)>0):
            bar="\n----------------------------------------------------------------------\n"
            dataToWrite = "gen_auth_usernames.py  --  Downloaded from: https://github.com/divastor/gen_auth_usernames"+bar+"NAME: "+name+"\nSURNAME: "+surname+"\nFATHER: "+father+"\nSECONDARY NAME: "+bar+"DATE RECORDED: "+date.strftime("%Y-%m-%d %H:%M")+"\nLIST OF USERNAMES: \n"
            dataToWrite=print_list(approved, dataToWrite)
            dataToWrite+=bar
            try:
                filename=raw_input("What would you like to be the file's name? (Leave empty for default):\n")
                if filename=="":
                    filename=name.lower()+"_"+surname.lower()+".txt"
                else:
                    filename+=".txt"
                    
                fhandler=open(filename, "w+")
                fhandler.write(dataToWrite)
                fhandler.close()
                print "Results saved in file "+filename
                raw_input("Press ENTER to continue")
            except:
                print "Something went wrong while trying to write to file! Check your permissions!"
                raw_input("Press ENTER to continue")
        else:
            print "You must run option 5 first!"
            raw_input("Press ENTER to continue")

    #Exit
    elif(choice=="7" or choice.lower()=="exit"):
        flag=1
        print("Bye!")
    else:
        print("Please choose one of the numbers 1-7!")
