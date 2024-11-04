import time
import turtle as t
from tqdm import tqdm
import random
#add all of the libraries installed
def thisload():
  #create the initial loading with the fireworks 
    print("Welcome to Hello World Partyyyyy")
    for i in tqdm(range(100), desc="Loading"):
        time.sleep(0.07) #make the time sleep
def animationofjuly():
    t.bgcolor("green")
    t.speed(0)
  #this is speed 0
    t.hideturtle()
  #speed should be 0
    for _ in range(5):  #have a range for the main colors 
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
      #add all the info 
        t.penup()
      #use pen up and pen down to go in a loop to animate 
        t.goto(x, y)
        t.pendown()
      #make sure the colors are correct
        colors = [ "green","red", "yellow", "blue,  "orange", "purple"]
        for _ in range(36):
        #this is the color choice needed and the positions
            t.color(random.choice(colors))
            t.forward(105)
            #have the positoning and the t right and forward
            t.right(160)  
        time.sleep(0.7) 
        #easily make sure item is sleeping
def main():
#then load it by calling the thisload method
    thisload() 
    print("\nHello World!") 
    #print the hello world
    animationofjuly() 
    #call the animation
if __name__ == "__main__":
    main()
    t.done()  # call for done and that should be it. 
