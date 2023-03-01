#tictac game no gui
#completed 11/24/2022

from random import randint

#TicTacBoard class
#Attributes:
#defaultBoard - uneditable board for initializing/resetting board
#inputCheck - list to contain entered user input at completed turn
#turn - tuple containing O/X turns
#t - variable for random selection from turn
#b - variable for editable board (list copy of defaultBoard)

#Methods:
# __init__ - constructor
# __del__ - destructor
# newBoard() - call for new game
# updateBoard(inputVal) - updates board using input from inputVal
# boardCheck() - checks board for winning combination
# nextTurn() - gets next turn after current turn
# displayBoard() - display current board condition when called
# createBoard() - create board from defaultBoard
class TicTacBoard:
    defaultBoard = [('7', '8', '9'),
                    ('4', '5', '6'),
                    ('1', '2', '3')]
    inputCheck = []
    turn = ('O', 'X')
    t = None
    b = []
    
    def __init__(self):
        #Generate turn and create board when instance is created
        self.t = self.turn[randint(0,1)]
        self.createBoard()
        
    def newBoard(self):
        #get random turn and assign to t (random select an index and get value from turn using index)
        #clear b (editable board) - list elements get deleted
        #recreate editable board - tuple elements appended from defaultBoard after list conversion
        #reset inputCheck
        #display clean board
        print('New Game')
        self.t = self.turn[randint(0,1)]
        self.b.clear()
        self.createBoard()
        self.inputCheck.clear()
        self.displayBoard()
        
    def updateBoard(self, inputVal):
        #if inputVal is not in inputCheck
        if(inputVal not in self.inputCheck):
            #append inputVal to inputCheck
            self.inputCheck.append(inputVal)
            #create an enumerated object with editable board (creates index for each list item)
            #i    j
            #0 [7,8,9]
            #1 [4,5,6]
            #2 [1,2,3]
            #for each item in editable board
            ##if inputVal is in list item
            ###get value of t (O/X)
            ###assign t to editable board where inputVal is equal to the list value
            ###self.b[i][j.index(inputVal)]
            ###i -> list row index
            ###j.index(inputVal) -> get index value of inputVal that is found in list item j
            for i, j in enumerate(self.b):
                if(inputVal in j):
                    self.b[i][j.index(inputVal)] = self.t
            #if inputCheck is at least 5, call boardCheck
            ##if boardCheck returns True (winning combination is found), return True to main
            #else continue if either condition is False
            if(len(self.inputCheck) >= 5 and self.boardCheck() == True):
                self.displayBoard()
                print()
                return True
            #if there are 9 items in inputCheck after boardCheck (no remaining turns left)
            ##display message to user and return False to main
            if(len(self.inputCheck) == 9):
                print('No moves left. Game is a draw.')
                self.displayBoard()
                print()
                return False
            #if no return is encountered, change turns and continue
            self.nextTurn()
        #else inform user of occupied square and continue
        else:
            print('Invalid turn. Square is occupied.')
        #display current board condition
        self.displayBoard()
    
    def boardCheck(self):
        #[00][01][02]
        #[10][11][12]
        #[20][21][22]
        #used simplified for loop and single if statement with 'and' condition
        ## if (item1 == item2) and (item2 == item3) -> return True 
        #first/second elements compared then second/third elements compared
        #all rows/columns/diagonals are checked when called
        #return True and exit function when equality condition is fully met (all 3 elements are equal)
        
        #horizontal print test -
        for row in range(3):
            #variable first index (row), constant second index (column)
            if(self.b[row][0] == self.b[row][1] and self.b[row][1] == self.b[row][2]):
                return True
            
        #vertical print test |
        for col in range(3):
            #constant first index (row), variable second index (column)
            if(self.b[0][col] == self.b[1][col] and self.b[1][col] == self.b[2][col]):
                return True
            
        #forward diagonal test \
        #downward diagonal elements
        if(self.b[0][0] == self.b[1][1] and self.b[1][1] == self.b[2][2]):
            return True

        #backward diagonal test /
        #upward diagonal elements
        if(self.b[2][0] == self.b[1][1] and self.b[1][1] == self.b[0][2]):
            return True

    def nextTurn(self):
        #get index value of t (O/X) from turn tuple
        turnIndex = self.turn.index(self.t)
        #flip index (if 1 -> get 0, if 0 -> get 1)
        #get new turn using flipped index and assign to t (turn[0,1] -> turn[O/X])
        if(turnIndex == 1):
            turnIndex = 0
            self.t = self.turn[turnIndex]
        elif(turnIndex == 0):
            turnIndex = 1
            self.t = self.turn[turnIndex]
        
    def displayBoard(self):
        print('Select item in grid or [N]ew/[Q]uit and Enter')
        print('-------------   {0} turn'.format(self.t))
        print('| {0} | {1} | {2} |'.format(self.b[0][0], self.b[0][1], self.b[0][2]))
        print('-------------')
        print('| {0} | {1} | {2} |'.format(self.b[1][0], self.b[1][1], self.b[1][2]))
        print('-------------')
        print('| {0} | {1} | {2} |   [N]ew'.format(self.b[2][0], self.b[2][1], self.b[2][2]))
        print('-------------   [Q]uit')

    def createBoard(self):
        #for each item in defaultBoard (a tuple)
        #convert tuple to a list and append to b (editable board)
        for board in self.defaultBoard:
            self.b.append(list(board))

    def __del__(self):
        print('Board removed')

#input validator function
def game(inputVal):
    #Tuple containing valid inputs
    boardInput = ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'Q', 'n', 'N')
    #Check if user input is in boardInput
    #Return True to main if valid -> assigned to inputTest
    #Inform invalid input. Will cause an infinite loop in main asking for user input
    ##because inputTest is False
    if inputVal in boardInput:
        return True
    else:
        print('Invalid input')

#main function
if (__name__ == '__main__'):
    #Create board instance and display board
    ticTacBoard = TicTacBoard()
    ticTacBoard.displayBoard()
    #Game loop
    while(True):
        #Continue asking user for input
        inputVal = input('Enter a value ')
        print()
        #Initialize inputTest
        #Pass user input to game function which will return a True if user input is valid
        ##or retain the initial False value if user input is not valid
        inputTest = False
        inputTest = game(inputVal)
        #If inputTest is True (user input is valid)
        if (inputTest == True):
            #Quit game if input is q or Q
            if (inputVal == 'q' or inputVal == 'Q'):
                break
            #Create new board if input is n or N
            elif (inputVal == 'n' or inputVal == 'N'):
                ticTacBoard.newBoard()
            #Pass user input to updateBoard function of board object which will return a True/False
            else:
                status = ticTacBoard.updateBoard(inputVal)
                #If game is a draw reset board for new game
                if (status == False):
                    ticTacBoard.newBoard()
                #If there is a winner show winning turn and reset board for new game
                elif (status == True):
                    print(ticTacBoard.t, 'wins')
                    ticTacBoard.newBoard()
    #Display on exit
    print('Game exit')
