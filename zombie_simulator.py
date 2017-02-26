#Name: Simple Zombie Simulator
#Program for a game simulating a random spread of letters across a grid
#Date created: 23 August 2014
#Date I began to update the program using new programming knowledge: 15 July 2015
#Date I began to separate the program into logical modules: 18 December 2015
#Most recently updated: 18 December 2015

def openingLines():
    #explanation of the program
    print("u is for the uninfected")
    print("z is for the zombies")
    print()
    print("Use \"/end\" to end the program or \"/restart\" to restart it.")
    print()

def creatingVariables():
    #making a variable for each coordinate
    a = [0, 0]
    b = [1, 0]
    c = [2, 0]
    d = [3, 0]
    e = [4, 0]

    f = [0, 1]
    g = [1, 1]
    h = [2, 1]
    i = [3, 1]
    j = [4, 1]

    k = [0, 2]
    l = [1, 2]
    m = [2, 2]
    n = [3, 2]
    o = [4, 2]

    p = [0, 3]
    q = [1, 3]
    r = [2, 3]
    s = [3, 3]
    t = [4, 3]

    u = [0, 4]
    v = [1, 4]
    w = [2, 4]
    x = [3, 4]
    y = [4, 4]

    #adding the variables to a tuple for ease of use
    return (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y)

def assigningInitialZombies(plots):
    #making a random number of the grid spaces zombies and checking if the total number of zombies is more than 0
    import random
    zombies = 0
    for space in plots:
        numberOutOf100 = random.randint(1, 100)
        if numberOutOf100 <= 10:
            value = "z"
            zombies += 1
        else:
            value = "u"
        space.append(value)
    if zombies >= 1:
        valuesAssigned = True
    return valuesAssigned

def showGrid(plots):
    #simplifies using plots to create the grid
    def block(num):
        return (plots[num])[2]
    #showing the grid
    print("%s,%s,%s,%s,%s" % (block(20), block(21), block(22), block(23), block(24)))
    print("%s,%s,%s,%s,%s" % (block(15), block(16), block(17), block(18), block(19)))
    print("%s,%s,%s,%s,%s" % (block(10), block(11), block(12), block(13), block(14)))
    print("%s,%s,%s,%s,%s" % (block(5), block(6), block(7), block(8), block(9)))
    print("%s,%s,%s,%s,%s" % (block(0), block(1), block(2), block(3), block(4)))

def choosingCoordinates(square, plots):
    #checking the grid for which direction to infect using coordinates
    import random
    adjoining = []
    for squareTwo in plots:
        #checking if the current square is one of the squares next to the zombie square
        if((squareTwo[0] == square[0] + 1 and squareTwo[1] == square[1])
        or(squareTwo[0] == square[0] - 1 and squareTwo[1] == square[1])
        or (squareTwo[1] == square[1]  + 1 and squareTwo[0] == square[0])
        or (squareTwo[1] == square[1] - 1 and squareTwo[0] == square[0])):
            if squareTwo[2] == "u":
                adjoining.append(squareTwo)
    #if there are available uninfected people for the zombie to infect, then it chooses a random direction to infect
    if len(adjoining) > 0:
        pickedSquare = random.choice(adjoining)
        pickedSquare[2] = "z"
        #adding "new" to make sure the square is not called up to infect others on this turn
        pickedSquare.append("new")

def checkingBeforeInfecting(plots):
    #checks that the square hasn't been infected on the same turn before using it to infect other squares
    for square in plots:
        #picking out the square we're looking at and seeing if it's a zombie or not
        #if it is, we go to checking the coordinates
            if square[2] == "z":
                if "new" not in square:
                    choosingCoordinates(square, plots)

def removeNew(plots):
    #removing the value used to keep newly created zombies from infecting others on the same turn they were created
        #print(">before:", plots) debugging line for optimising removing new
        for place in plots:
            if "new" in place:
                place.remove("new")
        #print(">after:", plots) ditto

def endingOption():
    #options for exit and restart given
    import sys
    first = input()
    if first == "/end":
        sys.exit()
    elif first == "/restart":
        main()

def main():
    openingLines()
    #opening the loops for assigning a value to the plots and checking if at least one is assigned as a zombie
    valuesAssigned = False
    while valuesAssigned == False:
        plots = creatingVariables()
        #print(">first: ", plots) debugging line for checking that assigning zombies worked
        valuesAssigned = assigningInitialZombies(plots)
        #print(">second: ", plots) ditto
    showGrid(plots)
    endingOption()
    
    #infecting squares
    checkingAndInfecting = True
    while checkingAndInfecting == True:
        checkingBeforeInfecting(plots)
        showGrid(plots)
        removeNew(plots)
        endingOption()

main()
