    ################################################################################
    ##########                                                            ##########
    ##########                 CVF_1205 Python Final_Lab                  ##########
    ##########                                                            ##########
    ################################################################################
import os
import re
import string



  
    ################################################################################
    ###################              Domain_Catcher            #####################
    ################################################################################

def domain_catcher():
    
    fhand = open(Datafile)
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From') : continue
        
        split = line.split()
        for words in split:
            if re.search ('@',words):
                space = str(" ")
                domain = words.split('@')[1]
                timestamp = open('tstamp.txt','a')
                stampwrite = timestamp.write(str(domain))
                sspace = timestamp.write(space)
                timestamp.close()
                    


    importtxt = open('tstamp.txt')
    for line3 in importtxt:
        importline = line3.split()
        names = (importline) 

    counts = dict()

    for name in names:
        counts[name] = counts.get(name, 0) + 1
    print ('\nPrinting dictionary contents:')
    print ('.............................................\n')
    print counts
        
    print ('\n\nCounting how many times users are listed:')
    print ('.............................................\n')



    l = list()
    for key, val in counts.items():
        l.append((val, key))
        l.sort(reverse=True)

    for val,key in l:
        print ('The User:'),key,('was found'),val,('time(s)\n')

    importtxt.close()     
    os.popen("del tstamp.txt")

    ################################################################################
    ###################                Hour_Catcher            #####################
    ################################################################################

def hour_catcher():
    #sample text to insert into a text document.
   
    
       


    #extracting the line starting with "Nov"
    fhand = open(Datafile)
    for line in fhand:
        line = line.rstrip()
        #if not line.startswith('Nov') : continue
        
        split = line.split()
        for words in split:
            if re.search (':..:',words):
                if len(words)==8:
                    stamp = words[0:3]
                    timestamp = open('tstamp.txt','a')
                    stampwrite = timestamp.write(str(stamp))
                    timestamp.close()
                    
               
    fhand = open('tstamp.txt')

    for time in fhand:
        
        x = re.findall("[0-9][0-9]",time)
        xwrite = str(x).strip('[]')
        xstamp = open('tstamp2.txt','a')
        xwritestamp = xstamp.write(xwrite)
        xstamp.close()

    fhand.close()


    fhand = open('tstamp2.txt')
    counts = dict()
    for line in fhand:
        words = line.split()
        print ('...................................')
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

    # Sort the dictionary by value
    lst = list()
    for key, val in list(counts.items()):
        lst.append((val, key))

    lst.sort(reverse=True)

    for key, val in lst:
        print('Hour found:'),val, ('How many times:'), key
               

    fhand.close()

    os.popen("del tstamp.txt")
    os.popen("del tstamp2.txt")



    ################################################################################
    ###################              Letter_Catcher            #####################
    ################################################################################



def letter_catcher():
    
    def split(words):
        return [char for char in words]


    x = open(Datafile)
    total = 0
    for letter in x:
        splitter = (split(letter))
        splitter = str(splitter)
        string = re.findall(('[a-z]'),splitter)
        letterstrip2 = str(string).strip("[]")
        letterstrip = str(letterstrip2).strip('')
        space = str("   ")
        letterkeep = letterstrip
        Lrecord = open('letterscan.txt','a')
        
        recorder = Lrecord.write(str(letterkeep))
        sspace = Lrecord.write(space)
        
        Lrecord.close()
        
        
    x.close()



    importtxt = open('letterscan.txt')
    for line3 in importtxt:
        importline = line3.split()
        names = (importline) 

    counts = dict()

    for name in names:
        total = total + 1
        counts[name] = counts.get(name, 0) + 1
    print ('\nPrinting dictionary contents:')
    print ('.............................................\n')
    print counts
        
    print ('\n\nCounting how many times letters are listed:')
    print ('.............................................\n')
    print ('\nThe total letters found'), total,('\n\n')


    l = list()
    for key, val in counts.items():
        l.append((val, key))
        l.sort(reverse=True)

    for val,key in l:
        calculation = (float(val)/(total))*100
        percent = str(calculation)
        print ('The letter:'),key,('was found'),val,('time(s)'), ('percentage:'), percent[:3],('%')

    importtxt.close()     
    os.popen("del letterscan.txt")


    ################################################################################
    ###################                User_Catcher            #####################
    ################################################################################



def user_catcher():
    
    fhand = open(Datafile)
    for line in fhand:
        line = line.rstrip()
    
        split = line.split()
   
        for words in split:
## searching for words with (:) symbol
            if re.search (':',words):
                space = str(" ")

                if words.startswith('su'):
                    cwords = words [:2]
                    sutext = open('sutext.txt','a')
                    swrite = sutext.write(str(cwords))
                    sspace = sutext.write(space)
                    sutext.close()

                
                if words.startswith ('sshd'):
                    c2words = words[:4]
                    sutext = open('sutext.txt','a')
                    swrite = sutext.write(str(c2words))
                    sspace = sutext.write(space)
                    sutext.close()
                    
    fhand.close()

    importtxt = open('sutext.txt')
    for line3 in importtxt:
        importline = line3.split()
        names = (importline) 

    counts = dict()

    for name in names:
        counts[name] = counts.get(name, 0) + 1
    print ('\nPrinting dictionary contents:')
    print ('.............................................\n')
    print counts
    
    print ('\n\nCounting how many times users are listed:')
    print ('.............................................\n')



    l = list()
    for key, val in counts.items():
        l.append((val, key))
        l.sort(reverse=True)

    for val,key in l:
         print ('The User:'),key,('was found'),val,('time(s)\n')

    importtxt.close()     
    os.popen("del sutext.txt")

    ################################################################################
    ###################              Email_Catcher             #####################
    ################################################################################

def email_catcher():
    
    print ('''\n---------------------------------------------------\n''')
    print ('These are the emails found.\n')



    fhand = open(Datafile)
    for line in fhand:
        line = line.rstrip()
       
        
        split = line.split()
        
        for words in split:
            if re.search ('@',words):
                print words 

                
    fhand.close()   
    print ('\n\n---------------------------------------------------\n')
    #searching for emails and formatting them for importing
    email = open(Datafile)

    for line2 in email:
        ecount = line2.split()
        for words in ecount:
            if re.search ('@',words):
                Elist = open('sample2.txt','a')
                Space = str(' ')
                Wlist = Elist.write(words)
                Slist = Elist.write(Space)
                Elist.close()
               

    email.close()

    emailt = open(Datafile)

    for line in emailt:
        tcount = line
        for dword in tcount:
            if not re.search('@',dword): continue
            if re.search ('@',dword):
                #if line.startswith(''):
                datetime = tcount[:6]
                dtlist = open('tdate.txt','a')
                dspace = str(' ')
                dlist = dtlist.write (str(datetime))
                Sdlist = dtlist.write(Space)
                dtlist.close()
               

    emailt.close()


    #adding index values to emails
    importtxt = open('sample2.txt')
    for line3 in importtxt:
        importline = line3.split()
        names = (importline)



    importdate = open('tdate.txt')
    for line4 in importdate:
        importd = line4.split()
        x = re.findall('([0-9]+)',line4)
        
        dname = x
           

        

    counts = dict()

    for name in names :
        counts[name] = counts.get(name, 0) + 1
    print ('Counting how many times each email was listed from most to least:\n')
    print counts

    fhand = open(Datafile)
    for line in fhand:
        line = line.rstrip()
        split = line.split()
        combine = split[0]+split[1]+' '
        datestring = open('datestring.txt','a')
        datestring2 = datestring.write (str(combine))
        datestring.close()

    fhand.close() 


    print('\n------------------------------------------------\n')
    print ('Searching for date occurrence and sorting in reverse order\n')
    strhand = open('datestring.txt')
    countstr = dict()
    for strline in strhand:
        strline = strline.translate(None, string.punctuation)
        wordstr = strline.split()
       
    for wordst in wordstr:
        if wordst not in countstr:
            countstr[wordst] = 1
        else:
            countstr[wordst] += 1
    # Sort the dictionary by value
    slst = list()

    for key, val in countstr.items():
        slst.append( (val, key) )
        slst.sort(reverse=True)
    for key, val in slst[:] :
        print val,('was found'), key

    strhand.close()     
    importtxt.close()
    importdate.close()

    os.popen("del sample2.txt")
    os.popen ("del sample.txt")
    os.popen ("del tdate.txt")
    os.popen ("del datestring.txt")



print ('\n...................................................................................................')
print ('\n.                                                                                                 .')
print ('\n.                                                                                                 .')
print ('\n.                                                                                                 .')
print ('\n.     pppppppp      yyy    yyy        ttt         hhh    hhh         oooo         nnn         nn  .')
print ('\n.    ppp     pp     yyy  yyy     ttttttttttt     hhh    hhh      ooo    ooo      nn  nn      nn   .')
print ('\n.   pppppppp         yyy            ttt         hhhhhhhhhh     ooo       ooo    nn     nn   nn    .')
print ('\n.  ppp              yyy            ttt         hhh    hhh      ooo    ooo      nn       nn nn     .')
print ('\n. ppp              yyy            ttt         hhh    hhh         oooo         nn         nnn      .')
print ('\n.                                                                                                 .')
print ('\n.                                                                                                 .')
print ('\n.                                                                                                 .')
print ('\n...................................................................................................')

q = 0
while q == 0:
    try:    
        print('\nCVF 1205 Python Finals\n')
        print('####################################################################\n')
        print('#    1. Domain Catcher      2. Hour Catcher     3. Email Catcher   #\n')
        print('#    4. User Catcher        5. Letter Catcher                      #\n')
        print('####################################################################\n')
        print('To quit type q\n\n')
        userinput = raw_input('\n\nPlease select a number: \n\n')
        prog =  str(userinput)

        if userinput == 'q':
            print ('\n\n.......Program closing.............\n')
            q = 1
            quit()

        
        if prog == "1":
            userinput2 = raw_input('Please select a file name to use: \n\n\n\n\n')
            Datafile = str(userinput2)
            if userinput2 == 'q':
                q = 1
                print ('\n\n.......Program closing.............\n')
                quit()
            domain_catcher()

        elif prog == "2":
            userinput2 = raw_input('Please select a file name to use: \n')
            Datafile = str(userinput2)
            if userinput2 == 'q':
                q = 1
                print ('\n\n.......Program closing.............\n')
                quit()
            hour_catcher()

        elif prog == "3":
            userinput2 = raw_input('Please select a file name to use: \n')
            Datafile = str(userinput2)
            if userinput2 == 'q':
                q = 1
                print ('\n\n.......Program closing.............\n')
                quit()
            email_catcher()
            
        elif prog == "4":
            userinput2 = raw_input('Please select a file name to use: \n')
            Datafile = str(userinput2)
            if userinput2 == 'q':
                q = 1
                print ('\n\n.......Program closing.............\n')
                quit()
            user_catcher()
            
        elif prog == "5":
            userinput2 = raw_input('Please select a file name to use: \n')
            Datafile = str(userinput2)
            if userinput2 == 'q':
                q = 1
                print ('\n\n.......Program closing.............\n')
                quit()
            letter_catcher()

        else:
            print('\n......................................')
            print ('(((Please enter a selection 1-5)))')
            print('......................................\n')
    except:
        print("\n\nError!!! ((((_____Can't find the file._____))))\n\n")



    
