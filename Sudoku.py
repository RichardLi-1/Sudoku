#A Sudoku puzzle game where you fill a 9 x 9 grid with numbers.
#There are 3 x 3 subgrids that you fill in with numbers from 1-9.



#Importing
from graphics import*
from time import sleep
from random import randint
#from playsound import playsound

win=GraphWin("Sudoku", 600, 600) #Creates the window


rowText = Text(Point(300,300),'hi')
highlight = Image(Point(300, 300), 'highlight.gif')
mistakes = 0    #Counts the number of mistakes the user made




def showText(yCord,textShown): #Function that runs to display each line of numbers
    rowText = Text(Point(300,yCord),textShown)
    rowText.setSize(29)
    rowText.setTextColor('white')
    rowText.draw(win)

    textShown = ''
    yCord += 43


def skip():  #Function that waits for the user to press the skip/done button
    while True:
        click = win.getMouse()
        if click.getX() > 545 and click.getX() < 580 and click.getY() > 550 and click.getY() < 582:
            break


def refresh():   #Function that handles redrawing the numbers onto the board
        
        numberPressed = False
        rowText.undraw()
        yCord = 102
        textShown = '  '


        
        #Row 1
        #This section sifts through the numbers in each row and finds the ones that are supposed to be shown
        for i in range(9):
            if row1shown[i] == True:
                textShown += row1[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "

        showText(yCord, textShown)  #Triggers the showText function which will display the numbers found by the above section onto the board
        #This process repeats 8 more times for each row


        #Row2
        yCord += 43
        textShown = '  '
        for i in range(9):
            if row2shown[i] == True:
                textShown += row2[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "
        
        showText(yCord, textShown)


        #Row3
        yCord += 43
        textShown = '  '

        for i in range(9):
            if row3shown[i] == True:
                textShown += row3[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "

        showText(yCord, textShown)


        #Row4
        yCord += 43
        textShown = '  '

        for i in range(9):
            if row4shown[i] == True:
                textShown += row4[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "


        showText(yCord, textShown)


        #Row5
        yCord += 43
        textShown = '  '
        
        for i in range(9):
            if row5shown[i] == True:
                textShown += row5[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "

        showText(yCord, textShown)


        #Row6
        yCord += 43
        textShown = '  '

        for i in range(9):
            if row6shown[i] == True:
                textShown += row6[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "

        showText(yCord, textShown)
        yCord += 43
        textShown = '  '

        #Row7
        
        for i in range(9):
            if row7shown[i] == True:
                textShown += row7[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "

        showText(yCord, textShown)
        yCord += 43
        textShown = '  '

        #Row8
        
        for i in range(9):
            if row8shown[i] == True:
                textShown += row8[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "

        showText(yCord, textShown)
        yCord += 43
        textShown = '  '

        #Row9
        
        for i in range(9):
            if row9shown[i] == True:
                textShown += row9[(i+1)*3]
            else:
                textShown += "  "
            textShown += "  "

        showText(yCord, textShown)

        yCord = 102




#Loading

win.setBackground(color_rgb(205,173,135))           #Sets the background colour to the game theme colour


#Creates the big sudoku icon and buttons
icon = Image(Point(300,300),'sudoku.gif')
buttons = Image(Point(300,520),'buttons.gif')


#---Loading Screen---#
icon.draw(win)          #Draws the icon
sleep(1)

#Starts animation, the icon slightly shifts upwards
for i in range(10):
    sleep(0.04)
    icon.move(0,-1)

#Animation speeds up

for i in range(45):
    sleep(0.00001)
    icon.move(0,-1)

#Buttons get drawn and the animation slows
#Buttons and icons slowly move up, then stop
buttons.draw(win)

for i in range(5):
    sleep(0.02)
    icon.move(0,-1)
    sleep(0.02)
    buttons.move(0,-1)
    icon.move(0,-1)

#---Loading Complete---#


#playsound('music.wav', False)   #Plays the background music



#The main game; this loop manages mouse input on the main menu but also houses the How To screens, Credits, and the main game
while True:
    click = win.getMouse() #Waits for a click on the main menu

    #If the user pressed the play button
    if click.getX() > 215 and click.getX() < 385 and click.getY() > 450 and click.getY() < 507:
    
        while True:
            ##-----------------MAIN GAME-----------------##
            randomBoard = randint(1,3) #Randomly chooses which board to use for the game

            if randomBoard == 1:    #If the first board is chosen

                #Numbers for the first board
                row1 = "   5  3  4  6  7  8  9  1  2   "
                row2 = "   6  7  2  1  9  5  3  4  8   "
                row3 = "   1  9  8  3  4  2  5  6  7   "
                row4 = "   8  5  9  7  6  1  4  2  3   "
                row5 = "   4  2  6  8  5  3  7  9  1   "
                row6 = "   7  1  3  9  2  4  8  5  6   "
                row7 = "   9  6  1  5  3  7  2  8  4   "
                row8 = "   2  8  7  4  1  9  6  3  5   "
                row9 = "   3  4  5  2  8  6  1  7  9   "

                #Information for whether each number is visible or not
                row1shown = [True, True, False,False,True,  False,False, False ,False]
                row2shown = [True, False,False,True, True,  True, False, False ,False]
                row3shown = [False,True, True, False,False, False,False, True , False]
                row4shown = [True, False,False,True, False, True, False, False ,True]
                row5shown = [True, False,True, False,True,  False,False, False ,True]
                row6shown = [True, False,False,True, False, True, False, False ,True]
                row7shown = [False,True, False,False,True,  True, True,  True , False]
                row8shown = [False,False,True, True, False, False,False, False ,True]
                row9shown = [False,False,False,True, False, True, False, True , True]


            elif randomBoard == 2:   #If the second board is chosen
                row1 = "   4  3  1  6  7  9  5  2  8   "
                row2 = "   9  6  7  2  5  8  3  4  1   "
                row3 = "   5  8  2  1  4  3  9  6  7   "
                row4 = "   6  5  9  8  1  7  2  3  4   "
                row5 = "   3  2  8  5  6  4  1  7  9   "
                row6 = "   7  1  4  9  3  2  8  5  6   "
                row7 = "   8  7  3  4  2  1  6  9  5   "
                row8 = "   1  4  5  3  9  6  7  8  2   "
                row9 = "   2  9  6  7  8  5  4  1  3   "

                row1shown = [True, True, False,False,True,  False,True,  False ,True]
                row2shown = [True, True, False,True, True,  True, False, False ,True]
                row3shown = [False,True, True, False,False, False,False, True , False]
                row4shown = [True, False,False,True, False, True, False, True , True]
                row5shown = [True, False,True, True, True,  False,False, True , True]
                row6shown = [True, False,False,True, False, True, False, False ,True]
                row7shown = [False,True, True, True, True,  True, True,  True , False]
                row8shown = [True, False,False, True, False, True, False, False ,True]
                row9shown = [False,False,False, True, False, True, False, True , True]



            elif randomBoard == 3:  #If the third board is chosen
                row1 = "   8  6  1  7  9  4  3  5  2   "
                row2 = "   3  5  2  1  6  8  7  4  9   "
                row3 = "   4  9  7  2  5  3  1  8  6   "
                row4 = "   2  1  8  9  7  5  6  3  4   "
                row5 = "   6  7  5  3  4  1  9  2  8   "
                row6 = "   9  3  4  6  8  2  5  1  7   "
                row7 = "   5  2  6  8  1  9  4  7  3   "
                row8 = "   7  4  3  5  2  6  8  9  1   "
                row9 = "   1  8  9  4  3  7  2  6  5   "

                row1shown = [False,True, False,False,False, False,True,  True , False]
                row2shown = [True, False,False,True, True,  False,False, False ,False]
                row3shown = [False,True, True, False,False, False,False, True , True]
                row4shown = [True, False,False,True, False, True, False, False ,False]
                row5shown = [False,False,True, False,True,  False,False, False ,True]
                row6shown = [True, False,False,True, False, True, False, False ,True]
                row7shown = [True, True, False,False,True,  False,True,  True , False]
                row8shown = [False,False,False,True, False, False,False, False ,False]
                row9shown = [False,False,True, False,False, True, False, True , True]
            
            highlighted = False #Whether a square is currently highlighted or not
            gameOngoing = True  #Whether the game is ongoing or not, used to restart the game when the player wins or loses
            mistakes = 0        #Counts the mistakes the user made
            clickedRow = 0
            clickedColumn = 0

            #Draws the sudoku board and number buttons
            gameBackground = Image(Point(900,300), 'main game.gif')
            gameBackground.draw(win)
            
            


            #Transition; camera pans right from the main menu to the game
            for i in range(120):
                icon.move(-5,0)
                buttons.move(-5,0)
                gameBackground.move(-5,0)
                sleep(0.0001)

    
            refresh()   #Triggers the refresh function, which will draw the numbers onto the board
            
            #The loop for mouse input on the main game
            while gameOngoing == True:
                
                #Creates and draws the mistakes counter
                mistakesText = Text(Point(300,65), ('mistakes: ' + str(mistakes) + '/5'))
                mistakesText.setTextColor('white')
                mistakesText.setSize(11)
                mistakesText.setStyle('bold')
                mistakesText.draw(win)

                #If they didn't make 5 mistakes, the game continues
                if mistakes < 5:


                    click = win.getMouse()  #Waits for the user to click
                    

                    numberPressed = False

                    #If a box is currently highlighted, the program will react to the numbers being pressed
                    if highlighted == True:
                        #if they pressed the Y area of the numbers
                        if click.getY() > 508 and click.getY() < 547:
                            choice = 0
                            #if they pressed 1
                            if click.getX() > 125 and click.getX() < 160:
                                choice = 1

                            #if they pressed 2
                            elif click.getX() > 160 and click.getX() < 200:
                                choice = 2

                            #if they pressed 3
                            elif click.getX() > 200 and click.getX() < 240:
                                choice = 3
                            
                            #if they pressed 4
                            elif click.getX() > 240 and click.getX() < 280:
                                choice = 4

                            #if they pressed 5
                            elif click.getX() > 280 and click.getX() < 320:
                                choice = 5

                            #if they pressed 6
                            elif click.getX() > 320 and click.getX() < 360:
                                choice = 6

                            #if they pressed 7
                            elif click.getX() > 360 and click.getX() < 400:
                                choice = 7

                            #if they pressed 8
                            elif click.getX() > 400 and click.getX() < 440:
                                choice = 8

                            #if they pressed 9
                            elif click.getX() > 440 and click.getX() < 475:
                                choice = 9

                            else:
                                choice = 10 #This means that they pressed in the Y area of the numbers but didn't actually press a number
                                #This is so that the square will deselect when pressing here, just like all the other blank space


                            #If they selected a square in row 1 and pressed the correct number
                            if clickedRow == 1 and str(choice) == row1[clickedColumn*3]:
                                highlighted = False
                                row1shown[clickedColumn-1] = True
                                highlight.undraw()
                                refresh()

                            #If they selected a square in row 2 and pressed the correct number
                            elif clickedRow == 2 and str(choice) == row2[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row2shown[clickedColumn-1] = True
                                refresh()

                            #If they selected a square in row 3 and pressed the correct number
                            elif clickedRow == 3 and str(choice) == row3[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row3shown[clickedColumn-1] = True
                                refresh()

                            #If they selected a square in row 4 and pressed the correct number
                            elif clickedRow == 4 and str(choice) == row4[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row4shown[clickedColumn-1] = True
                                refresh()

                            #If they selected a square in row 5 and pressed the correct number
                            elif clickedRow == 5 and str(choice) == row5[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row5shown[clickedColumn-1] = True
                                refresh()

                            #If they selected a square in row 6 and pressed the correct number
                            elif clickedRow == 6 and str(choice) == row6[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row6shown[clickedColumn-1] = True
                                refresh()

                            #If they selected a square in row 7 and pressed the correct number
                            elif clickedRow == 7 and str(choice) == row7[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row7shown[clickedColumn-1] = True
                                refresh()

                            #If they selected a square in row 8 and pressed the correct number
                            elif clickedRow == 8 and str(choice) == row8[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row8shown[clickedColumn-1] = True
                                refresh()

                            #If they selected a square in row 9 and pressed the correct number
                            elif clickedRow == 9 and str(choice) == row9[clickedColumn*3]:
                                highlighted = False
                                highlight.undraw()
                                row9shown[clickedColumn-1] = True
                                refresh()

                            #If they pressed next to the numbers
                            elif choice == 10:
                                highlighted = False
                                highlight.undraw()
                            else:
                                mistakes += 1

                            numberPressed = True

                                

                        

                    
                    #If the press was not on a number
                    if numberPressed == False:
                        highlighted = True  #It was simplest to turn this true and change it back if the user did not press a square
                        #Otherwise the line would be repeated 9 times
                        if click.getX() > 110 and click.getX() < 150:   #If the user pressed in column 1
                                clickedColumn = 1
                                highlightX = 130 #This sets the X coordinate for the highlight square
                        elif click.getX() > 151 and click.getX() < 192: #If the user pressed in column 2
                                clickedColumn = 2
                                highlightX = 172
                        elif click.getX() > 193 and click.getX() < 235: #If the user pressed in column 3
                                clickedColumn = 3
                                highlightX = 213
                        elif click.getX() > 238 and click.getX() < 278: #If the user pressed in column 4
                                clickedColumn = 4
                                highlightX = 258
                        elif click.getX() > 280 and click.getX() < 320: #If the user pressed in column 5
                                clickedColumn = 5
                                highlightX = 300
                        elif click.getX() > 323 and click.getX() < 362: #If the user pressed in column 6
                                clickedColumn = 6
                                highlightX = 343
                        elif click.getX() > 366 and click.getX() < 404: #If the user pressed in column 7
                                clickedColumn = 7
                                highlightX = 385
                        elif click.getX() > 408 and click.getX() < 447: #If the user pressed in column 8
                                clickedColumn = 8
                                highlightX = 428
                        elif click.getX() > 450 and click.getX() < 490: #If the user pressed in column 9
                                clickedColumn = 9
                                highlightX = 470
                        else: #If the user pressed outside the board
                                highlighted = False #Reverts highlighted to false, so no change occured

                        if click.getY() > 82 and click.getY() < 121:                    #If the user pressed in row 1
                                clickedRow = 1
                                highlightY = 102
                        elif click.getY() > 124 and click.getY() < 164:                 #If the user pressed in row 2
                                clickedRow = 2
                                highlightY = 144
                        elif click.getY() > 167 and click.getY() < 205:                 #If the user pressed in row 3
                                clickedRow = 3
                                highlightY = 186
                        elif click.getY() > 210 and click.getY() < 249:                 #If the user pressed in row 4
                                clickedRow = 4
                                highlightY = 230
                        elif click.getY() > 251 and click.getY() < 291:                 #If the user pressed in row 5
                                clickedRow = 5
                                highlightY = 272
                        elif click.getY() > 294 and click.getY() < 333:                 #If the user pressed in row 6
                                clickedRow = 6
                                highlightY = 314
                        elif click.getY() > 338 and click.getY() < 376:                 #If the user pressed in row 7
                                clickedRow = 7
                                highlightY = 357
                        elif click.getY() > 380 and click.getY() < 419:                 #If the user pressed in row 8
                                clickedRow = 8
                                highlightY = 400
                        elif click.getY() > 422 and click.getY() < 460:                 #If the user pressed in row 9
                                clickedRow = 9
                                highlightY = 441
                        elif numberPressed == False:
                                highlighted = False                                     #Reverts highlighted to false, so no change occured



                        #This section is to check if the user pressed a number that is already shown
                        #If the number is already shown, the box will not highlight
                        if clickedRow == 1 and row1shown[clickedColumn-1] == True:      #if they press row 1 and it's a number that's already shown
                                highlighted = False                                     #Reverts highlighted to false, so no change occured
                        elif clickedRow == 2 and row2shown[clickedColumn-1] == True:    #if they press row 2
                                highlighted = False
                        elif clickedRow == 3 and row3shown[clickedColumn-1] == True:    #if they press row 3
                                highlighted = False
                        elif clickedRow == 4 and row4shown[clickedColumn-1] == True:    #if they press row 4
                                highlighted = False
                        elif clickedRow == 5 and row5shown[clickedColumn-1] == True:    #if they press row 5
                                highlighted = False
                        elif clickedRow == 6 and row6shown[clickedColumn-1] == True:    #if they press row 6
                                highlighted = False
                        elif clickedRow == 7 and row7shown[clickedColumn-1] == True:    #if they press row 7
                                highlighted = False
                        elif clickedRow == 8 and row8shown[clickedColumn-1] == True:    #if they press row 8
                                highlighted = False
                        elif clickedRow == 9 and row9shown[clickedColumn-1] == True:    #if they press row 9
                                highlighted = False

                        #If the user pressed an empty square, the highlight will be drawn there
                        else:
                                if highlighted == True:                                 
                                    highlight.undraw()
                                    highlight = Image(Point(highlightX, highlightY), 'highlight.gif')
                                    highlight.draw(win)


                    #If there isn't supposed to be a highlight, it undraws                
                    if highlighted == False:
                        highlight.undraw()


                    #Win Check: This section checks if the user has filled in every square
                    #If they have, a "you win" box will appear
                    #They can choose to play again or exit
                    
                    if row1shown == [True, True, True, True, True, True, True, True, True] and row2shown == [True, True, True, True, True, True, True, True, True]:
                        if row3shown == [True, True, True, True, True, True, True, True, True] and row4shown == [True, True, True, True, True, True, True, True, True]:
                            if row5shown == [True, True, True, True, True, True, True, True, True] and row6shown == [True, True, True, True, True, True, True, True, True]:
                                if row7shown == [True, True, True, True, True, True, True, True, True] and row8shown == [True, True, True, True, True, True, True, True, True]:
                                    if row9shown == [True, True, True, True, True, True, True, True, True]:

                                            youWin = Image(Point(300,300), 'you win.gif')
                                            youWin.draw(win)                            #Drawing you win box
                                            while True:
                                                click = win.getMouse()

                                                #If they press play again
                                                if click.getX() > 169 and click.getX() < 288 and click.getY() > 330 and click.getY() < 360:
                                                    youWin.undraw()
                                                    gameOngoing = False
                                                    break

                                                #If they press exit
                                                elif click.getX() > 313 and click.getX() < 432 and click.getY() > 330 and click.getY() < 360:
                                                    quit()


                #If the user made 5 mistakes, a "you lose" box will appear
                #They can again choose to play again or exit
                else:
                    youLose = Image(Point(300,300), 'you lose.gif')
                    youLose.draw(win)                                                   #Drawing you lose box


                    while True:
                        click = win.getMouse()
                        
                        #If they press play again
                        if click.getX() > 169 and click.getX() < 288 and click.getY() > 322 and click.getY() < 350:
                            youLose.undraw()
                            gameOngoing = False
                            break

                        #If they press exit
                        elif click.getX() > 313 and click.getX() < 432 and click.getY() > 322 and click.getY() < 350:
                            quit()

                mistakesText.undraw()
                
                
                
                




    #If they press the How To button
    if click.getX() > 490 and click.getX() < 580 and click.getY() > 520 and click.getY() < 553:

        #Drawing the first How To screen
        howTo1 = Image(Point(300,900), 'howto1.gif')
        howTo1.draw(win)

        #Transition; Camera pans down to the first How To screen
        for i in range(120):
                icon.move(0,-5)
                buttons.move(0,-5)
                howTo1.move(0,-5)
                sleep(0.001)

        skip()  #Waits for a press on the skip button


        #Drawing the second How To screen
        howTo2 = Image(Point(900,300), 'howto2.gif')
        howTo2.draw(win)

        #Transition; Camera pans right to the second How To screen
        for i in range(120):
                icon.move(-5,0)
                buttons.move(-5,0)
                howTo1.move(-5,0)
                howTo2.move(-5,0)
                sleep(0.001)

        skip()  #Waits for a press on the done button


        #Transition; Camera pans left and up back to the main menu
        for i in range(120):
                icon.move(5,5)
                buttons.move(5,5)
                howTo1.move(5,5)
                howTo2.move(5,5)
                sleep(0.001)


        #Undraws the how to screens
        howTo1.undraw()
        howTo2.undraw()


    #if they press the Credits button
    if click.getX() > 490 and click.getX() < 580 and click.getY() > 560 and click.getY() < 590:

        #Dims the screen and draws the credits box
        creditBackground = Image(Point(300,300), 'credits background.gif')
        creditBackground.draw(win)
        creditScreen = Image(Point(300,-150), 'credits.gif')
        creditScreen.draw(win)

        #Transition; Drops the credits box to the middle of the screen
        for i in range(90):
            creditScreen.move(0,5)
            sleep(0.00001)

        
        click = win.getMouse()  #Waits for any mouse input

        #Transition; Drops the credits box below the screen
        for i in range(90):
            creditScreen.move(0,5)
            sleep(0.00001)

        #Undraws the credit box and undims the screen
        creditScreen.undraw()
        creditBackground.undraw()
