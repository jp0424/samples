#Justin Polido
#7/12/21
#Robot Vacuum

import random

#Assumptions for variables
#Maximum dirt that bin can handle is 750ml
#Maximum tanks for dirty water and cleaner is 300ml
#Maximum battery capacity is 3500mAh
#Rates are measured per cell
#Robot spends 0.6ml, and transfers to dirty water
#Vacuum dirt is a random value between 0-50ml (3 in3)
#Robot spends 13.5mAh for vacuum and 25mAh for mopping

NAME = "Herbert"
MAX_DIRT = 750
MAX_DIRT_WATER = 300
MAX_CLEANER = 300
MAX_BATTERY = 3500
RATE_SPRAY = 0.6
RATE_POW_VAC = 13.5
RATE_POW_MOP = 25

dirtBinLevel = 0
dirtyWaterLevel = 0
cleanerLevel = 0
batteryLevel = 0

#gridSet = {}

#Import Settings - will give an error if file is empty
def importSettings():
    #Test loop to check for file
    print("Reading Settings:")
    test = True
    while(test):
        try: #Try opening file if there is any, set test to False and loop back to exit
            fileOpen = open("settings.cfg", mode = 'r')
            test = False
            continue
        except: #If no file, create one with default values and rerun loop
            print("Initializing Settings:")
            fileOpen = open("settings.cfg", mode = 'w+')
            fileOpen.write("dirtBinLevel = 0\n"
                           "dirtyWaterLevel = 0\n"
                           "cleanerLevel = 0\n"
                           "batteryLevel = 3500\n")
   
    #Value extraction and assign to variable
    for line in fileOpen.readlines():
        if(line == '\n'):
            print("empty line")
        varName = ""
        varVal = None
        spIdx = line.find(' ')  #Get index of first space (will get variable name)
        numIdx = line.find(' ', spIdx+1)    #Get index of space after variable name
        varName = line[:spIdx]  #Get substring from start to spIdx and assign to varName
        varVal = int(float(line[numIdx+1:]))   #Get substring from numIdx+1 to end of string (numIdx is index of the next space - to exclude space, go to next index)
        #String is converted first to float to get a valid number along with decimals if any, then convert to integer to drop the decimal portion
        
        if varName == "dirtBinLevel":
            binVar = varVal
        elif varName == "dirtyWaterLevel":
            waterVar = varVal
        elif varName == "cleanerLevel":
            cleanerVar = varVal
        elif varName == "batteryLevel":
            batteryVar = varVal
    fileOpen.close()
    
    #Return a tuple of the value of variables
    return(binVar, waterVar, cleanerVar, batteryVar)

#Maintenance
#Bin Level
def binCheck(dirtBinLevel):
    if(dirtBinLevel/MAX_DIRT > 0.85):
        print(NAME + " needs cleaning.")
        print("Dirt bin level :-> " + str((dirtBinLevel/MAX_DIRT)*100) + "%")
        return False
    else:
        print("Dirt bin level :-> " + str((dirtBinLevel/MAX_DIRT)*100) + "%")
    return True
    
#Water Level
def waterCheck(dirtyWaterLevel):
    if(dirtyWaterLevel/MAX_DIRT_WATER > 0.85):
        print(NAME + " has full dirty water tank.")
        print("Dirty water level :-> " + str((dirtyWaterLevel/MAX_DIRT_WATER)*100) + "%")
        return False
    else:
        print("Dirty water level :-> " + str((dirtyWaterLevel/MAX_DIRT_WATER)*100) + "%")
    return True
    
#Cleaner Level
def cleanerCheck(cleanerLevel):
    if(cleanerLevel/MAX_CLEANER <= 0.15):
        print(NAME + " needs more cleaner.")
        print("Cleaner level :-> " + str((cleanerLevel/MAX_CLEANER)*100) + "% full")
        return False
    else:
        print("Cleaner level :-> " + str((cleanerLevel/MAX_CLEANER)*100) + "%")
    return True
    
#Battery Level
def batteryCheck(batteryLevel):
    if(batteryLevel/MAX_BATTERY < 0.15):
        print(NAME + " is tired.")
        print("Battery level :-> " + str((batteryLevel/MAX_BATTERY)*100) + "%")
        return False
    else:
        print("Battery level :-> " + str((batteryLevel/MAX_BATTERY)*100) + "%")
    return True
    
#System Check
def levelCheck(dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel):
    #Infinite loop of level checking until values are at the right level
    status = 0
    loopCheck = True
    while(loopCheck):
        #Check levels of each maintenance variable
        binBool = binCheck(dirtBinLevel)
        waterBool = waterCheck(dirtyWaterLevel)
        cleanerBool = cleanerCheck(cleanerLevel)
        batteryBool = batteryCheck(batteryLevel)
        #If any of the variable returns False, ask user for action
        #User input simulates emptying or filling up a tank (assume user inputs a valid number) - no error checking at this time
        #Loop back to start to check levels
        if (binBool == False):
            dirtBinLevel = int(input("Empty dirt bin. (0 min) > "))
            continue
        if (waterBool == False):
            dirtyWaterLevel = int(input("Empty dirty water. (0 min) > "))
            continue
        if (cleanerBool == False):
            cleanerLevel += int(input("Fill cleaner tank. (300 max) > "))
            continue
        #If low battery is encountered, go home and return -1 for status code to exit from calling function
        if (batteryBool == False):
            print(NAME, "has no energy.")
            status = -1
        loopCheck = False
    #Return values for updating
    print()
    return status, dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel
    
#Clean
def clean(dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel):
    #Assign parameters to temporary local variables
    dbLvl = dirtBinLevel
    dwLvl = dirtyWaterLevel
    clLvl = cleanerLevel
    btLvl = batteryLevel
    
    #For test only
    #rowCount = 10
    #colCount = 10
    
    #Navigation grid using floor types
    navGridA = [['tl','tl','tl','ca','ca','ca','hw','hw','hw','hw','tl','hw','tl','ca'],
                ['tl','tl','tl','ca','ca','ca','hw','hw','hw','ca','hw','tl','ca','hw'],
                ['tl','tl','tl','ca','ca','ca','hw','hw','hw','tl','tl','tl','hw','tl'],
                ['H','tl','tl','ca','ca','ca','hw','hw','hw','tl','ca','hw','ca','hw']]

    #Grid layout 1F
    #+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    #|tl|tl|tl|ca|ca|ca|hw|hw|hw|hw|tl|hw|tl|ca|
    #+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    #|tl|tl|tl|ca|ca|ca|hw|hw|hw|ca|hw|tl|ca|hw|
    #+--+--+--+--+--+--+--+--+--+--+--+--+--+--+    *tl<--ca
    #|tl|tl|tl|ca|ca|ca|hw|hw|hw|tl|tl|tl|hw|tl|    tl-->hw^
    #+--+--+--+--+--+--+--+--+--+--+--+--+--+--+    ^tl<--tl
    #|H |tl|tl|ca|ca|ca|hw|hw|hw|tl|ca|hw|ca|hw|    H--->hw^
    #+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    
    #Navigation grid stairs
    #navGridB = [['x','x','x','x','x'],
    #            ['ca','ca','ca','ca','x'],
    #            ['x','x','x','ca','x'],
    #            ['x','ca','ca','ca','x'],
    #            ['x','ca','x','x','x'],
    #            ['x','ca','x','ca','ca'],
    #            ['x','ca','x','ca','x'],
    #            ['x','ca','ca','ca','x']]
    
    #Grid layout Stairs
    #+--+--+--+--+--+
    #|x |x |x |x |x |
    #+--+--+--+--+--+
    #|ca|ca|ca|ca|x | -> start from leftmost ca
    #+--+--+--+--+--+
    #|x |x |x |ca|x |
    #+--+--+--+--+--+
    #|x |ca|ca|ca|x |
    #+--+--+--+--+--+
    #|x |ca|x |x |x |
    #+--+--+--+--+--+
    #|x |ca|x |ca|ca| -> exit here
    #+--+--+--+--+--+
    #|x |ca|x |ca|x |
    #+--+--+--+--+--+
    #|x |ca|ca|ca|x |
    #+--+--+--+--+--+
    
    #Navigation grid 2F
    #navGridC = [['hw','hw','hw','hw','hw'],
    #            ['hw','hw','hw','hw','hw'],
    #            ['hw','hw','hw','hw','hw'],
    #            ['hw','hw','hw','hw','hw'],
    #            ['hw','hw','hw','hw','hw'],
    #            ['ca','ca','ca','ca','ca'],
    #            ['ca','ca','ca','ca','ca'],
    #            ['ca','ca','ca','ca','ca'],
    #            ['ca','ca','ca','ca','ca']]
    
    #Grid layout 2F
    #+--+--+--+--+--+
    #|hw|hw|hw|hw|hw|
    #+--+--+--+--+--+
    #|hw|hw|hw|hw|hw|
    #+--+--+--+--+--+
    #|hw|hw|hw|hw|hw|
    #+--+--+--+--+--+
    #|hw|hw|hw|hw|hw|
    #+--+--+--+--+--+
    #|hw|hw|hw|hw|hw|
    #+--+--+--+--+--+
    #|ca|ca|ca|ca|ca| -> start at leftmost ca (do not clean) then start at bottom left
    #+--+--+--+--+--+   cell
    #|ca|ca|ca|ca|ca|
    #+--+--+--+--+--+
    #|ca|ca|ca|ca|ca|
    #+--+--+--+--+--+
    #|ca|ca|ca|ca|ca|
    #+--+--+--+--+--+

    cellTotal = 0
    for row in navGridA:
        cellTotal += len(row)   #Get total number of cells in whole grid

    #For test only
    #cellTotal = rowCount*colCount
    
    #Number of cells robot has cleaned (initialize 1 to include home terminal)
    workedCell = 0
    
    #For test only
    #for i in range(rowCount):
    #    column = []
    #    for j in range(colCount):
    #        column.append('-')
    #    navGridA.append(column)
    
    #Print cells before cleaning
    #for row in navGridA:
    #    print(row)
    
    #Home terminal location
    HOME_X = len(navGridA)-1
    HOME_Y = 0
    
    #For test only
    #Home terminal is always on lower left corner
    #navGridA[HOME_X][HOME_Y] = 'H'
    
    #Set x/y index to home terminal location x - left/right y - up/down
    xIdx = HOME_X
    yIdx = HOME_Y
    
    #For each cell in each column, get the value of the cell (floor type)
    ##Call cleanCell and pass floor type along with maintenance variables
    ##cleanCell will process the maintenance values based on floor type
    ##cleanCell will return a tuple of the maintenance variables
    ##returned maintenance variables from cleanCell will be reassigned back to the maintenance variables
    #Cleaned cells are replaced with '0'
    cleanSignal = True
    while(cleanSignal):
        status = 0
        rowIdx = len(navGridA) #Get maximum rows
        colIdx = len(navGridA[0]) #Get maximum columns (should be the same for all rows)
        for row in range(rowIdx-1, -1,-1):
            #If index of row is odd (actual row location is even ie. second row is index 1)
            #Herbert will travel from left to right
            #Pre clean level to check to catch abnormal levels
            print("Pre clean level check")
            status, dbLvl, dwLvl, clLvl, btLvl = levelCheck(dbLvl, dwLvl, clLvl, btLvl)
            print("Dirt bin real level:", dbLvl,
                  "\nDirty water real level:", dwLvl,
                  "\nCleaner real level:", clLvl,
                  "\nBattery real level:", btLvl,"\n")
            if (status != -1):
                if row%2 != 0:
                    for col in range(colIdx):
                        cellValue = navGridA[row][col]
                        dbLvl, dwLvl, clLvl, btLvl = cleanCell(cellValue, dbLvl, dwLvl, clLvl, btLvl)
                        if(navGridA[row][col] != 'H'):
                            navGridA[row][col] = '0'
                        workedCell += 1
                #If index of row is even (actual row location is odd ie. third row is index 2)
                #Herbert will travel from right to left
                elif row%2 == 0 :
                    for col in range(colIdx-1, -1, -1):
                        cellValue = navGridA[row][col]
                        dbLvl, dwLvl, clLvl, btLvl = cleanCell(cellValue, dbLvl, dwLvl, clLvl, btLvl)             
                        if(navGridA[row][col] != 'H'):
                            navGridA[row][col] = '0'
                        workedCell += 1
            elif (status == -1):
                print(NAME,"is low on battery. Charge or check power if", NAME, "is stationed.")
                return (dbLvl, dwLvl, clLvl, btLvl)
            #Post clean level to check to catch abnormal levels
            status, dbLvl, dwLvl, clLvl, btLvl = levelCheck(dbLvl, dwLvl, clLvl, btLvl)
            print("Post clean level check")
            print("Dirt bin real level:", dbLvl,
                  "\nDirty water real level:", dwLvl,
                  "\nCleaner real level:", clLvl,
                  "\nBattery real level:", btLvl,"\n")
        cleanSignal = False
    if(workedCell == cellTotal):
        print(NAME, "has finished cleaning\n")

    #For test only to check if all cells are covered
    #for row in navGridA:
    #    print(row)
    return (dbLvl, dwLvl, clLvl, btLvl)

def cleanCell(cellValue, dbLvl, dwLvl, clLvl, btLvl):
    if cellValue == "hw" or cellValue == "tl":  #If cellValue is for hardwood or tile
        #Pass dirtyWater, cleaner, and battery levels to cleanMop and return processed values back to the same variables
        print("Mopping")
        dwLvl, clLvl, btLvl = cleanMop(dwLvl, clLvl, btLvl)
    elif cellValue == "ca": #If cellValue is for carpet
        #Pass dirtBin and battery to cleanVac and return processed values back to the same variables
        print("Vacuuming")
        dbLvl, btLvl = cleanVac(dbLvl, btLvl)
    #Return updated variables back to calling function
    return (dbLvl, dwLvl, clLvl, btLvl)

def cleanVac(dirtBinLevel, batteryLevel):
    dirtBinLevel += random.randint(0, 50) #Random value for vacuumed dirt
    batteryLevel -= RATE_POW_VAC
    return (dirtBinLevel, batteryLevel)

def cleanMop(dirtyWaterLevel, cleanerLevel, batteryLevel):
    dirtyWaterLevel += RATE_SPRAY
    cleanerLevel -= RATE_SPRAY
    batteryLevel -= RATE_POW_MOP
    return (dirtyWaterLevel, cleanerLevel, batteryLevel)

def goHome():
    print(NAME,"is going home")
    #Simulate direct movement to terminal
    print(NAME,"is home. Clean",NAME,"before use.")

#Save Settings
def saveSettings(dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel):
    print("Saving settings")
    fileOpen = open("settings.cfg", mode='w')
    fileOpen.writelines("dirtBinLevel = " + str(dirtBinLevel) + "\n"
                   "dirtyWaterLevel = " + str(dirtyWaterLevel) + "\n"
                   "cleanerLevel = " + str(cleanerLevel) + "\n"
                   "batteryLevel = " + str(batteryLevel))
    fileOpen.close()


#========================================================================================
#Main Program
#Call import settings and assign returned tuple to their variables
print(NAME + " is starting up")
print(NAME + " is checking settings\n")
dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel = importSettings()

#Check levels before cleaning
status, dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel = levelCheck(dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel)

#If battery is low from initial check (-1) stay in terminal
#Else start cleaning
if(status != -1):
    #print("Herbert cleans here")
    dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel = clean(dirtBinLevel, dirtyWaterLevel, cleanerLevel, batteryLevel)
    goHome()
elif(status == -1):
    print(NAME,"is low on battery. Charge or check power if", NAME, "is stationed.")
    goHome()

#Save settings
print(NAME + " is saving settings")
#Assume Herbert is cleaned and will be fully charged for next use
saveSettings(0, 0, cleanerLevel, 3500)
print(NAME + " is sleeping")