import random as rand
import turtle as trtl
import leaderboard as lb

painter = trtl.Turtle()
painter.speed(0)
score_writer = trtl.Turtle()

leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name: ")


font_setup = ("Arial", 20, "normal")

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle()

leaderboard_file_name = 'a122_leaderboard.txt'

#-----game functions-----

def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global painter

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, painter, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, painter, score)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def turtle_shape():
  painter.shapesize(2)
  painter.color('green') 
  painter.shape('circle')

score = 0


def change_position(x,y):
  if timer_up == False:
    score_writer.clear()
    score_writer.penup()
    score_writer.goto(-200, 200)
    random_x = rand.randint(-200,200)
    random_y = rand.randint(-150,150)
    painter.penup()
    painter.goto(random_x,random_y)
    painter.pendown()
    global score
    score +=1
    score_writer.pendown()
    score_writer.write(score, font=font_setup)


turtle_shape()
painter.onclick(change_position)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()




