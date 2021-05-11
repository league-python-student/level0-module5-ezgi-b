"""
Go to the recipe to run the demonstration before starting this program
"""

def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(800, 600)
    
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
    global x
    global ex
    global speed
    speed = 1
    x = 100
    ex = 700

def draw():
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.
    background(200, 90, 200)
    global x
    global ex
    global speed
    for i in range(40):
        ellipse(x, 300, i*10, i*10)
    if x>= 800 or x<=0:
        speed = -1*speed
    x += speed
    
    for i in range(40):
        ellipse(ex, 300, i*10, i*10)
    ex -= speed

    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.
        
    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */

         
    # When the rings reach the left side of the sketch, reverse the direction again
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
        
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
