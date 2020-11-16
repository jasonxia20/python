import time
import random
print("Hi and welcome to the guessing game!")
time.sleep(2)
level = input("we have 5 different levels of 'difficulty' for you. Ultra Easy, Easy, Medium, Hard, Impossible or Custom (blank to exit). Choose your pick (write in all lowercase): ")
lives = 0
a = random.randint(1,2)
b = random.randint(1,5)
c = random.randint(1,15)
d = random.randint(1,25)
e = random.randint(1,1000000)
if level == "ultra easy":
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    a2 = eval(input("ok, let's start! choose a number between 1 and 2: "))
    if a2 == a:
        print("YOU GOT IT!!!1!!1!!!1!!!")
    elif a2 != a: 
        print("nope")
        lives += 1
        a3 = eval(input("choose a number between 1 and 2: "))
        if a3 == a:
            print("YOU GOT IT!!!1!!1!!!1!!!")
        elif a3 != a: 
            print("nope")
            lives += 1
            a4 = eval(input("choose a number between 1 and 2: "))
            if a4 == a:
                print("YOU GOT IT!!!1!!1!!!1!!!")
            elif a4 != a: 
                print("nope")
                lives += 1

    if lives == 3:
        print("lol no you lose. and on ultra easy mode too. Consider getting a brain before doing this again. And also, the number was", a)
        
if level == "easy":
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")    
    b2 = eval(input("ok, let's start! choose a number between 1 and 5: "))
    if b2 == b:
        print("YOU GOT IT!!!1!!1!!!1!!!")
    elif b2 != b: 
        print("nope")
        lives += 1
        b3 = eval(input("choose a number between 1 and 5: "))
        if b3 == b:
            print("YOU GOT IT!!!1!!1!!!1!!!")
        elif b3 != b: 
            print("nope")
            lives += 1
            b4 = eval(input("choose a number between 1 and 5: "))
            if b4 == b:
                print("YOU GOT IT!!!1!!1!!!1!!!")
            elif b4 != b: 
                print("nope")
                lives += 1

    if lives == 3:
        print("lol no you lose. the number was", b)

if level == "medium":
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    c2 = eval(input("ok, let's start! choose a number between 1 and 15: "))
    if c2 == c:
        print("YOU GOT IT!!!1!!1!!!1!!! I guess you are moderately good at guessing")
    elif c2 != c: 
        print("nope")
        lives += 1
        c3 = eval(input("choose a number between 1 and 15: "))
        if c3 == c:
            print("YOU GOT IT!!!1!!1!!!1!!! I guess you are moderately good at guessing")
        elif c3 != c: 
            print("nope")
            lives += 1
            c4 = eval(input("choose a number between 1 and 15: "))
            if c4 == c:
                print("YOU GOT IT!!!1!!1!!!1!!! I guess you are moderately good at guessing")
            elif c4 != c: 
                print("nope")
                lives += 1

    if lives == 3:
        print("lol no you lose. the number was", c)

if level == "hard":
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    d2 = eval(input("ok, let's start! choose a number between 1 and 25: "))
    if d2 == d:
        print("YOU GOT IT!!!1!!1!!!1!!! Cool, you know how to guess")
    elif d2 != d: 
        print("nope")
        lives += 1
        d3 = eval(input("choose a number between 1 and 25: "))
        if d3 == d:
            print("YOU GOT IT!!!1!!1!!!1!!! Cool, you know how to guess")
        elif d3 != d: 
            print("nope")
            lives += 1
            d4 = eval(input("choose a number between 1 and 25: "))
            if d4 == d:
                print("YOU GOT IT!!!1!!1!!!1!!! Cool, you know how to guess")
            elif d4 != d: 
                print("nope")
                lives += 1

    if lives == 3:
        print("lol no you lose. the number was", d)

if level == "impossible":
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    e2 = eval(input("ok, let's start! choose a number between 1 and 1000000: "))
    if e2 == e:
        print("Wtf. either you are really lucky, have ESP or are hacking. respect")
    elif e2 != e: 
        print("nope")
        lives += 1
        e3 = eval(input("choose a number between 1 and 1000000: "))
        if e3 == e:
            print("Wtf. either you are really lucky, have ESP or are hacking. respect")
        elif e3 != e: 
            print("nope")
            lives += 1
            e4 = eval(input("choose a number between 1 and 1000000: "))
            if e4 == e:
                print("Wtf. either you are really lucky, have ESP or are hacking. respect")
            elif e4 != e: 
                print("nope")
                lives += 1

    if lives == 3:
        print("lol no you lose. But seriously how the f**k are youb supposed to get this? the number was", e)

if level == "custom":
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")    
    start = eval(input("ok, custom it is! Choose the start margin for the guessing game: "))
    endd = eval(input("alright, now the end margin: "))
    custom = random.randint(start,endd)
    print("ok, let's start! choose a number between", start, "and", endd, end='')
    custom2 = eval(input(": "))
    if custom2 == custom:
        print("Cool, you got it")
    elif custom2 != custom: 
        print("nope")
        lives += 1
        print("choose a number between", start, "and", endd, end='')
        custom3 = eval(input(": "))
        if custom3 == custom:
            print("noice, you got it")
        elif custom3 != custom: 
            print("nope")
            lives += 1
            print("choose a number between", start, "and", endd, end='')
            custom4 = eval(input(": "))
            if custom4 == custom:
                print("Close one, but u got that")
            elif custom4 != custom: 
                print("nope")
                lives += 1

    if lives == 3:
        print("nope, sorry. the number was", custom)

if level == "":
    exit()
