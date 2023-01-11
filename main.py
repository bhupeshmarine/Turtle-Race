import turtle as t
import random
screen = t.Screen()


colours = ["Blue", "orange", "Red", "black", "Green", "wheat", "yellow"]

all_t = []
x = -75
for j in range(0, 6):
  new_turtle = t.Turtle("turtle")
  new_turtle.penup()
  new_turtle.color(colours[j])
  new_turtle.goto(-250, x)
  all_t.append(new_turtle)
  x += 25

race_is_on = True
user_input = screen.textinput(title= "Put your bet", prompt= "On what colour you want to bet?")

while race_is_on:
  for items in all_t:
    dist = random.randint(0, 10)
    items.forward(dist)
    if items.xcor() >= 250:
      race_is_on = False
      if user_input.lower() == items.color()[0]:
        print(f"You won winnner is {items.color()[0]} turtle")
      else:
        print(f"You lost winnner is {items.color()[0]} turtle")
      
  
  


########### Challenge 4 - Random Walk ########

  
  

