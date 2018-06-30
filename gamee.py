# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:12:34 2017

@author: Chirag Bajaj
"""
#r=rock
#p=paper
#s=scissor
#l=lizard
#sp=spock
class _Getch:
    """
    Gets a single character from standard input.  Does not echo to
    the screen.
    """
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            try:
                self.impl = _GetchMacCarbon()
            except(AttributeError, ImportError):
                self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class _GetchMacCarbon:
    """
    A function which returns the current ASCII key that is down;
    if no ASCII key is down, the null string is returned.  The
    page http://www.mactech.com/macintosh-c/chap02-1.html was
    very helpful in figuring out how to do this.
    """
    def __init__(self):
        import Carbon
        Carbon.Evt #see if it has this (in Unix, it doesn't)

    def __call__(self):
        import Carbon
        if Carbon.Evt.EventAvail(0x0008)[0]==0: # 0x0008 is the keyDownMask
            return ''
        else:
            #
            # The event contains the following info:
            # (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            #
            # The message (msg) contains the ASCII char which is
            # extracted with the 0x000000FF charCodeMask; this
            # number is converted to an ASCII character with chr() and
            # returned
            #
            (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            return chr(msg & 0x000000FF)

getch = _Getch()
import random
def main():
    game=['r','p','s','l','sp']
    print("KEM CHO? " )
    n=input()
    m="majama"
    me=0
    chirag=0
    if n==m:
        print("Great,so let us continue!!!"'\n')
        print("Select a language"'\n'"1.English"'\n'"2.Hindi"'\n'"3.Bhojpuri")
        x=input()
        print('\n')
        if x=='1':
            
            
            print("Rules are as follows"'\n')
            print("Scissor cuts paper"'\n'"Paper crushes rock"'\n')
            print("Rock crushes lizard"'\n'"Lizard poisons spock"'\n')
            print("Spock smashes scissors"'\n'"Scissor decapicates lizard"'\n')
            print("Lizard eats paper"'\n'"Paper disproves spock"'\n')
            print("Spock vapourises rock"'\n'"Rock crushes scissor"'\n')
            print("BEWARE! Your opponent is chirag!"'\n')
            print("r=rock,p=paper,s=scissor,l=lizard,sp=spock"'\n')
            print("How much points you want to play?"'\n')
            print("1. Five,2. Ten,3. Fifteen"'\n')
            y=input()
            if y=='1':
                while (me<5 and chirag<5):
                    print("Your turn")
                    a=input()
                    c=random.randint(0,4)
                    b=game[c]
                    print("My turn "'\n'+b+'\n')
                    if (a=='s' and b=='p') or (a=='s' and b=='l'):
                        me+=1
                    elif(a=='p' and b=='r') or (a=='p' and b=='sp'):
                        me+=1
                    elif(a=='r' and b=='l') or (a=='r' and b=='s'):
                        me+1
                    elif(a=='l' and b=='sp') or (a=='l' and b=='p'):
                        me+=1
                    elif(a=='sp' and b=='s') or (a=='sp' and b=='r'):
                        me+=1
                    elif a==b:
                        a=a
                    else:
                        chirag+=1
                    print("Current score is"'\n')
                    print("You-"+str(me)+"Chirag-"+str(chirag)+'\n')
                        
                    
            elif y=='2':
                while (me<10 and chirag<10):
                    print("Your turn")
                    a=input()
                    c=random.randint(0,4)
                    b=game[c]
                    print("My turn "'\n'+b+'\n')
                    if (a=='s' and b=='p') or (a=='s' and b=='l'):
                        me+=1
                    elif(a=='p' and b=='r') or (a=='p' and b=='sp'):
                        me+=1
                    elif(a=='r' and b=='l') or (a=='r' and b=='s'):
                        me+1
                    elif(a=='l' and b=='sp') or (a=='l' and b=='p'):
                        me+=1
                    elif(a=='sp' and b=='s') or (a=='sp' and b=='r'):
                        me+=1
                    elif a==b:
                        a=a
                    else:
                        chirag+=1
                    print("Current score is"'\n')
                    print("You-"+str(me)+"Chirag-"+str(chirag)+'\n')
                    
            elif y=='3':
                while (me<15 and chirag<15):
                    print("Your turn")
                    a=input()
                    c=random.randint(0,4)
                    b=game[c]
                    print("My turn "'\n'+b+'\n')
                    if (a=='s' and b=='p') or (a=='s' and b=='l'):
                        me+=1
                    elif(a=='p' and b=='r') or (a=='p' and b=='sp'):
                        me+=1
                    elif(a=='r' and b=='l') or (a=='r' and b=='s'):
                        me+1
                    elif(a=='l' and b=='sp') or (a=='l' and b=='p'):
                        me+=1
                    elif(a=='sp' and b=='s') or (a=='sp' and b=='r'):
                        me+=1
                    elif a==b:
                        a=a
                    else:
                        chirag+=1
                    print("Current score is"'\n')
                    print("You-"+str(me)+"Chirag-"+str(chirag)+'\n')
        elif x=='2':
            me=0
            chirag=0
            print("Anusashan ka palan karna anivarya hai"'\n')
            print("Kaichi cuts Kagaz"'\n'"Kagaz crushes Pathar"'\n')
            print("Pathar crushes Chipkali"'\n'"Chipkali poisons Chirag"'\n')
            print("Chirag smashes Kaichi"'\n'"Kaichi decapicates Chipkali"'\n')
            print("Chipkali eats Kagaz"'\n'"Kagaz disproves Chirag"'\n')
            print("Chirag vapourises Pathar"'\n'"Pathar crushes Kaichi"'\n')
            print("BEWARE! Your opponent is chirag!"'\n')
            print("r=Pathar,p=Kagaz,s=Kaichi,l=Chipkali,sp=Chirag"'\n')
            print("Kitne anko ka khelna chahenge?"'\n')
            print("1. Pach,2. Dus,3. Pandrah"'\n')
            y=input()
            if y=='1':
                while (me<5 and chirag<5):
                    print("Your turn")
                    a=input()
                    c=random.randint(0,4)
                    b=game[c]
                    print("My turn "'\n'+b+'\n')
                    if (a=='s' and b=='p') or (a=='s' and b=='l'):
                        me+=1
                    elif(a=='p' and b=='r') or (a=='p' and b=='sp'):
                        me+=1
                    elif(a=='r' and b=='l') or (a=='r' and b=='s'):
                        me+1
                    elif(a=='l' and b=='sp') or (a=='l' and b=='p'):
                        me+=1
                    elif(a=='sp' and b=='s') or (a=='sp' and b=='r'):
                        me+=1
                    elif a==b:
                        a=a
                    else:
                        chirag+=1
                    print("Current score is"'\n')
                    print("You-"+str(me)+"Chirag-"+str(chirag)+'\n')
            elif y=='2':
                while (me<10 and chirag<10):
                    print("Your turn")
                    a=input()
                    c=random.randint(0,4)
                    b=game[c]
                    print("My turn "'\n'+b+'\n')
                    if (a=='s' and b=='p') or (a=='s' and b=='l'):
                        me+=1
                    elif(a=='p' and b=='r') or (a=='p' and b=='sp'):
                        me+=1
                    elif(a=='r' and b=='l') or (a=='r' and b=='s'):
                        me+1
                    elif(a=='l' and b=='sp') or (a=='l' and b=='p'):
                        me+=1
                    elif(a=='sp' and b=='s') or (a=='sp' and b=='r'):
                        me+=1
                    elif a==b:
                        a=a
                    else:
                        chirag+=1
                    print("Current score is"'\n')
                    print("You-"+str(me)+"Chirag-"+str(chirag)+'\n')
                    
            elif y=='3':
                while (me<15 and chirag<15):
                    print("Your turn")
                    a=input()
                    c=random.randint(0,4)
                    b=game[c]
                    print("My turn "'\n'+b+'\n')
                    if (a=='s' and b=='p') or (a=='s' and b=='l'):
                        me+=1
                    elif(a=='p' and b=='r') or (a=='p' and b=='sp'):
                        me+=1
                    elif(a=='r' and b=='l') or (a=='r' and b=='s'):
                        me+1
                    elif(a=='l' and b=='sp') or (a=='l' and b=='p'):
                        me+=1
                    elif(a=='sp' and b=='s') or (a=='sp' and b=='r'):
                        me+=1
                    elif a==b:
                        a=a
                    else:
                        chirag+=1
                    print("Current score is"'\n')
                    print("You-"+str(me)+"Chirag-"+str(chirag)+'\n')
                    
        if x=='3':
            print("Budbak ho ka"'\n'"Humse panga loge"'\n'"U Luzz")
            _Getch()
    else:
        print("byeee")
    if (chirag>me):
        print("Chirag wins!!!")
    elif(me>chirag):
        print("You win!!!")
    
main()
