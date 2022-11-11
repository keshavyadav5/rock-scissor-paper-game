import random
print('''\t\t WELCOME TO ROCK PAPPER SCISSOR GAME
                    rock vs paper->paper win
                    rock vs scissor->rock win
                    paper vs scissor->scissor win
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ''')
try:
    while True:
        ccount=0
        ucount=0
        l=["rock","scissor","paper"]
        uc=int(input('''
    Do You Want To Play Game...:>
    1 Yes
    2 No | Exit
		'''))
        if uc==1:
            for i in range(1,6):
                userInput=int(input('''
	1 rock
	2 scissor
	3 paper
	 	    '''))
                if userInput==1:
                    uchoice="rock"
                elif userInput==2:
                    uchoice="scissor"
                elif userInput==3:
                    uchoice="paper"
                else:
                    print('Opps!, there is only 3 options 1,2 & 3')
                    break
                Cchoice=random.choice(l)
                if uchoice==Cchoice:
                    print("Your choice:",uchoice)
                    print("computer choice:",Cchoice)
                    print("Match Draw")
                    ccount=ccount+1
                    ucount=ucount+1
                elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or(uchoice=="scissor" and Cchoice=="paper"):
                    print("Your choice:",uchoice)
                    print("computer choice:",Cchoice)
                    print("You Win")
                    ucount=ucount+1
                else:
                    print("Your choice:",uchoice)
                    print("computer choice:",Cchoice)
                    print("Computer Win")
                    ccount=ccount+1
            print()
            if ucount==ccount:
                print("At final Match Draw")
                print("Your count:",ucount)
                print("computer count:",ccount)
            elif ucount>ccount:
                print("!!!**Congratulation**!!! You win the game")
                print("Your count:",ucount)
                print("computer count:",ccount)
            else:
                print("**At final Computer win**")
                print("Your count:",ucount)
                print("computer count:",ccount)
        else:
            print('\n\n\t\t!!!"""**Good Bye**"""!!!')
            break
except Exception as e:
	print("\t\t**Error Occured**")
	print(e)
