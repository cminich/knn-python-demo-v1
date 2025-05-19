# Nearest Neighbor Demo 1
# This Python progam, that uses the pyGame-based cmu-graphics package, is
# used by Mr. Minich to help introductory computer programming students and 
# and curious laymen adults understand the nearest neighbor algorithm.
# This version of the demo program classifies favorite drinks by their
# sweetness and caffeine level features.

# Works Cited
# some help from ChatGPT here and there

###### global variables

app.background = 'lightGray'

# Categories                 0        1        2
app.categories = ['Soda', 'Juice', 'Coffee']

# Colors
app.colors = ['red', 'orange', 'brown']

# Data with features: sweetness (0-10) and caffeine (0-10)
# [ category index, sweetness, caffeine]

app.data = [
    # Soda (category 0)
    [0, 8, 6],   
    [0, 7, 7],
    [0, 9, 5],
    # Juice (category 1)
    [1, 9, 1],   
    [1, 8, 2],
    [1, 10, 0],
    # Coffee (category 2)
    [2, 2, 9],   
    [2, 3, 8],
    [2, 1, 10]
]

###### functions

# Computes distance between two feature points
def getDistance(p1, p2):
    dist = 0
    
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
        
    return dist ** 0.5

# Finds and returns the nearest neighbor in app.data for a given point
def classifyByNearestNeighbor(newPoint):
    closest = None
    minDist = 20000000000.0     
    # or    minDist = float('inf')

    # for each row in the app.data 2D list
    for row in app.data:
        category, sweet, caffeine = row
        dist = getDistance(newPoint, [sweet, caffeine])
        
        if (dist < minDist):
            minDist = dist
            closest = category

    return closest

# Draws the legend
def drawKey():
    
    for i in range(len(app.categories)):
        y = 25 + i * 20
        Circle(20, y, 6, fill=app.colors[i])
        Label(app.categories[i], 40, y, size=12, align='left')

# Converts from a point (x, y) on the canvas to a feature value (0-10)
def screenToFeature(x, y):
    # using CMU Graphics rounded library function rather than the Python round function
    return [rounded((x - 50) / 30), rounded((350 - y) / 30)]

# Converts from a feature value (0-10) to a point (x, y) on the canvas
def featureToScreen(sweetness, caffeine):
    return 50 + sweetness * 30, 350 - caffeine * 30

# Allows human user to click the mouse to add a new test point
def onMousePress(x, y):
    newFeatures = screenToFeature(x, y)
    
    # determine the category of the point's nearest neighbor
    catIndex = classifyByNearestNeighbor(newFeatures)
    
    # choose the appropriate color for this new point
    color = app.colors[catIndex]
    
    # find the correct (x, y) location and plot the new point
    cx, cy = featureToScreen(newFeatures[0], newFeatures[1])
    Circle(cx, cy, 8, fill=color, border='black')
    # TODO - figure out how to clear the previous label output
    Label('You picked ' + app.categories[catIndex], 200, 20, size=14, fill='black')

# Called once to start the program
def main():
    drawKey()

    # plot the test data sample points
    
    # for each row in the app.data dataset
    for row in app.data:
        catIndex, sweetness, caffeine = row
        color = app.colors[catIndex]
        cx, cy = featureToScreen(sweetness, caffeine)
        Circle(cx, cy, 6, fill=color)
        
    # Add axis labels
    Label("Sweetness", 200, 375)
    Label("Caffeine", 20, 200, rotateAngle=-90)

###### main program

main()
