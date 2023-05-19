import tkinter as tk

story = tk.Tk()
story.title("White Glass")

def show_frame(frame):
    frame.tkraise() # raises whatever frame you specify in the 'command' function of a button widget

def exit_button():
    quit()


f1 = tk.Frame(story) # Title screen
f2 = tk.Frame(story) # Details on what the game is about
f3 = tk.Frame(story) # Page where you choose your story option.
f4 = tk.Frame(story) # Apocalyptic Wasteland story
f5 = tk.Frame(story) # Superhuman experience
f6 = tk.Frame(story) # College Experience
f7 = tk.Frame(story) # Cabin Horror Experience
for frame in (f1, f2, f3, f4, f5, f6, f7):
    frame.grid(row=0, column=0, sticky="news")

intro = tk.Label(f1, text="WHITE GLASS", font=('times new roman', 32))
intro.grid(row=0,column=2)

start = tk.Button(f1, text="START", padx=100, pady=15, command=lambda:show_frame(f3))
start.grid(row=1, column=2)

exit = tk.Button(f1, text="EXIT", padx=100, pady=15, command=exit_button)
exit.grid(row=3, column=2)

details = tk.Button(f1, text="About", padx=100, pady=15, command=lambda:show_frame(f2))
details.grid(row=2, column=2)

# Details on what the game is about:
details_title = tk.Label(f2, text='About the game', font=("times new roman", 32))
details_title.pack()

details_description= tk.Label(f2, text=
"'White Glass' is a game that's loosely based on the Netflix show 'Black Mirror' and follows four 'choose your own adventure \n"
"themes that each contain multiple endings. We hope you enjoy your experience! ", font=('times new roman', 12))
details_description.pack()

return_to_screen = tk.Button(f2, text="Return to title screen", command=lambda:show_frame(f1))
return_to_screen.pack()

#------------
crossroads = tk.Label(f3, text="Choose your Theme", font=("ariel", 32), bg="yellow")
crossroads.pack()

choice_1 = tk.Button(f3, text="Apocalyptic Wasteland Experience", command=lambda:show_frame(story2))
choice_1.pack()

choice_2 = tk.Button(f3, text="Superhuman Experience", command=lambda:show_frame(story1))
choice_2.pack()

choice_3 = tk.Button(f3, text="College Experience", command=lambda:show_frame(story3))
choice_3.pack()

choice_4 = tk.Button(f3, text="Cabin Horror Experience", command=lambda:show_frame(story4))
choice_4.pack()







#------------------ Story 1 ------------------#

story1 = tk.Frame(story, bg='grey')


#------------------ Story 1 (Power 1 Selection) ------------------#

story1_power = tk.Frame(story)
story1_power1_choice1 = tk.Frame(story)
story1_power1_choice2 = tk.Frame(story)
story1_power1_choice3 = tk.Frame(story)
story1_power1_choice4 = tk.Frame(story)
story1_power1_choice5 = tk.Frame(story)
story1_power1_choice6 = tk.Frame(story)
story1_power1_choice7 = tk.Frame(story)
story1_power1_choice8 = tk.Frame(story)
story1_power1_choice9 = tk.Frame(story)
story1_power1_choice10 = tk.Frame(story)
story1_power1_choice11 = tk.Frame(story)

#------------------ Story 1 (Power 2 Selection) ------------------#

story2_power = tk.Frame(story)
story1_power2_choice1 = tk.Frame(story)
story1_power2_choice2 = tk.Frame(story)
story1_power2_choice3 = tk.Frame(story)
story1_power2_choice4 = tk.Frame(story)
story1_power2_choice5 = tk.Frame(story)
story1_power2_choice6 = tk.Frame(story)
story1_power2_choice7 = tk.Frame(story)
story1_power2_choice8 = tk.Frame(story)
story1_power2_choice9 = tk.Frame(story)

#------------------ Story 2 First Choice------------------#

story2 = tk.Frame(story)
story2_choice1_decision1 = tk.Frame(story)
story2_choice1_decision2 = tk.Frame(story)
story2_choice1_decision3 = tk.Frame(story)
story2_choice1_decision4 = tk.Frame(story)
story2_choice1_decision5 = tk.Frame(story)
story2_choice1_decision6 = tk.Frame(story)
story2_choice1_decision7 = tk.Frame(story)
story2_choice1_decision8 = tk.Frame(story)
story2_choice1_decision9 = tk.Frame(story)
story2_choice1_decision10 = tk.Frame(story)
story2_choice1_decision11 = tk.Frame(story)

#------------------ Story 2 Second Choice------------------#

story2_choice2_decision1 = tk.Frame(story)
story2_choice2_decision2 = tk.Frame(story)
story2_choice2_decision3 = tk.Frame(story)
story2_choice2_decision4 = tk.Frame(story)
story2_choice2_decision5 = tk.Frame(story)

#------------------Story 3 First Choice------------------#

story3 = tk.Frame(story)
story3_choice1_decision1 = tk.Frame(story)
story3_choice1_decision2 = tk.Frame(story)
story3_choice1_decision3 = tk.Frame(story)
story3_choice1_decision4 = tk.Frame(story)
story3_choice1_decision5 = tk.Frame(story)
story3_choice1_decision6 = tk.Frame(story)
story3_choice1_decision7 = tk.Frame(story)

#------------------Story 3 Second Choice------------------#

story3_choice2_decision1 = tk.Frame(story)
story3_choice2_decision2 = tk.Frame(story)
story3_choice2_decision3 = tk.Frame(story)
story3_choice2_decision4 = tk.Frame(story)
story3_choice2_decision5 = tk.Frame(story)

#------------------ Story 4 First Choice ------------------#

story4 = tk.Frame(story)
story4_choice1_decision1 = tk.Frame(story)
story4_choice1_decision2 = tk.Frame(story)
story4_choice1_decision3 = tk.Frame(story)
story4_choice1_decision4 = tk.Frame(story)
story4_choice1_decision5 = tk.Frame(story)
story4_choice1_decision6 = tk.Frame(story)
story4_choice1_decision7 = tk.Frame(story)
story4_choice1_decision8 = tk.Frame(story)
story4_choice1_decision9 = tk.Frame(story)
story4_choice1_decision10 = tk.Frame(story)

#------------------ Story 4 Second Choice ------------------#

story4_choice2_decision1 = tk.Frame(story)
story4_choice2_decision2 = tk.Frame(story)
story4_choice2_decision3 = tk.Frame(story)
story4_choice2_decision4 = tk.Frame(story)
story4_choice2_decision5 = tk.Frame(story)
story4_choice2_decision6 = tk.Frame(story)

for frame in (
              story1,
              story1_power,
              story1_power1_choice1,
              story1_power1_choice2,
              story1_power1_choice3,
              story1_power1_choice4,
              story1_power1_choice5,
              story1_power1_choice6,
              story1_power1_choice7,
              story1_power1_choice8,
              story1_power1_choice9,
              story1_power1_choice10,
              story1_power1_choice11,
              story1_power2_choice1,
              story1_power2_choice2,
              story1_power2_choice3,
              story1_power2_choice4,
              story1_power2_choice5,
              story1_power2_choice6,
              story1_power2_choice7,
              story1_power2_choice8,
              story1_power2_choice9,
              story2,
              story2_choice1_decision1,
              story2_choice1_decision2,
              story2_choice1_decision3,
              story2_choice1_decision4,
              story2_choice1_decision5,
              story2_choice1_decision6,
              story2_choice1_decision7,
              story2_choice1_decision8,
              story2_choice1_decision9,
              story2_choice1_decision10,
              story2_choice1_decision11,
              story2_choice2_decision1,
              story2_choice2_decision2,
              story2_choice2_decision3,
              story2_choice2_decision4,
              story2_choice2_decision5,
              story3,
              story3_choice1_decision1,
              story3_choice1_decision2,
              story3_choice1_decision3,
              story3_choice1_decision4,
              story3_choice1_decision5,
              story3_choice1_decision6,
              story3_choice1_decision7,
              story3_choice2_decision1,
              story3_choice2_decision2,
              story3_choice2_decision3,
              story3_choice2_decision4,
              story3_choice2_decision5,
              story4,
              story4_choice1_decision1,
              story4_choice1_decision2,
              story4_choice1_decision3,
              story4_choice1_decision4,
              story4_choice1_decision5,
              story4_choice1_decision6,
              story4_choice1_decision7,
              story4_choice1_decision8,
              story4_choice1_decision9,
              story4_choice1_decision10,
              story4_choice2_decision1,
              story4_choice2_decision2,
              story4_choice2_decision3,
              story4_choice2_decision4,
              story4_choice2_decision5,
              story4_choice2_decision6,
              ):
    frame.place(relheight=1.0,relwidth=1.0)

#------------------ Story 1 ------------------#

story1_title = tk.Label(story1, text = 'Dream (Fictional: Superpower) \n \n Please Choose a Super Power: >:)', bg = 'red')
story1_title.pack(fill='x')

#------------------ Story 1 Power 1 Decisions------------------#

power_btn1 = tk.Button(story1, text = 'Mind Reading', command=lambda:show_frame(story1_power))
power_btn1.place(x = 640, y = 600, width = 300, height = 60)

str1_power = tk.Label(story1_power, text = "\n  a random classmate of yours seems \n \n  moody entering class this morning, \n \n  you decided to read their mind and discover \n \n  their father is physically abusing their mother.", bg = 'red')
str1_power.pack(fill='x')

str1_power1_decision1 = tk.Button(story1_power, text = 'Leave them alone', command=lambda:show_frame(story1_power1_choice1))
str1_power1_decision1.place(x = 640, y = 600, width = 300, height = 60)

str1_power1_decision2 = tk.Label(story1_power1_choice1, text = ' \n your friend changest their personality \n \n (thinks of depression and failure) \n \n  and starts to change their style of clothing \n \n (darker or grey clothing)', bg = 'red')
str1_power1_decision2.pack(fill='x')

str1_power1_decision2_btn1 = tk.Button(story1_power1_choice1, text = 'Leave them alone',command=lambda:show_frame(story1_power1_choice2))
str1_power1_decision2_btn1.place(x = 640, y = 600, width = 300, height = 60)

str1_power1_decision2_btn2 = tk.Button(story1_power1_choice1, text = 'Confront them and share your ability',command=lambda:show_frame(story1_power1_choice4))
str1_power1_decision2_btn2.place(x = 1000, y = 600, width = 300, height = 60) # <===== Left Button Coordinates

story1_power1_decision3 = tk.Label(story1_power1_choice2, text = 'They start to think of suicide and wanting to end their life... \n where they show signs of depression.', bg = 'red')
story1_power1_decision3.pack(fill='x')

str1_power1_decision3_btn1 = tk.Button(story1_power1_choice2, text = 'Leave them alone', command=lambda:show_frame(story1_power1_choice3))
str1_power1_decision3_btn1.place(x = 640, y = 600, width = 300, height = 60) # <====== Right Button Coordinates

story1_power1_decision4 = tk.Label(story1_power1_choice3, text = 'They ended up killing themselves where their family and friend mourned for their death. \n you failed!', bg = 'red')
story1_power1_decision4.pack(fill='x')

story1_power1_decision4 = tk.Label(story1_power1_choice4, text = 'they were shock you knew about their issue and your power to read minds, \n thinking you were weird ', bg = 'red')
story1_power1_decision4.pack(fill='x')

story1_power1_decision4_btn1 = tk.Button(story1_power1_choice4, text = 'Insist of becoming friends', command=lambda:show_frame(story1_power1_choice5))
story1_power1_decision4_btn1.place(x = 820, y = 600, width = 300, height = 60) # <======== Middle Coordinates for 1 options only

story1_power1_decision5 = tk.Label(story1_power1_choice5, text = "Your new friend wants you to meet their mother so you can read her mind once in while \n so you can tell your new friend about her thoughts, and they can try to help her. \n They kept trying to keep in contact with to the point they are bothering during your own time, \n so you decided to ignore them.  \n They start stalking you seeing them around wherever you go, \n you decided the only way for you to get their attention was too put one of your lives one in danger \n where you forced to help them until you kill them, \n where you sent to prison for life on death row for man slaugther.", bg = 'red')
story1_power1_decision5.pack(fill='x')

story1_power1_decision6 = tk.Button(story1_power1_choice2, text = 'Confront them and share your ability', command=lambda:show_frame(story1_power1_choice6))
story1_power1_decision6.place(x = 1000, y = 600, width = 300, height = 60)

story1_power1_decision6 = tk.Label(story1_power1_choice6, text = 'they were shock you knew about their issue and \n your power to read minds, thinking you were weird', bg = 'red')
story1_power1_decision6.pack(fill='x')

story1_power1_decision6_btn1 = tk.Button(story1_power1_choice6, text = 'Try to become  friends with them', command=lambda:show_frame(story1_power1_choice7))
story1_power1_decision6_btn1.place(x = 820, y = 600, width = 300, height = 60)

story1_power1_decision7 = tk.Label(story1_power1_choice7, text = 'you end up becoming friends, where they take advantage of your super power and \n make you read someone minds', bg = 'red')
story1_power1_decision7.pack(fill='x')

story1_power1_decision7_btn1 = tk.Button(story1_power1_choice7, text = 'Help Them', command=lambda:show_frame(story1_power1_choice8))
story1_power1_decision7_btn1.place(x = 820, y = 600, width = 300, height = 60)

story1_power1_decision8 = tk.Label (story1_power1_choice8, text = " While trying to read someone minds to expose their secrets, \n you ended up reading your friends mind where you find out \n they are planning to use your friendship as tool for them. \n After listening to people's secret you start to lose yourself mentally, \n you start becoming crazy and mentally ill where you're sent to \n an asylum rotting for life while your friend lives in joy \n knowing they took advantage of your ability.  ", bg = 'red')
story1_power1_decision8.pack(fill='x')

#------------------ Story 1 Power1 Confront Button Layout ------------------#

str1_power2_decision1 = tk.Button(story1_power, text = 'Confront them and Share your ability', command=lambda:show_frame(story1_power1_choice9)) 
str1_power2_decision1.place(x = 1000, y = 600, width = 300, height = 60)

story1_power1_decision9 = tk.Label(story1_power1_choice9, text = "They were shock you knew about their issue and your power to read minds, \n they would like you to be their friend \n since you help them report the issue to the police and they feel better. \n The police arrested their father, where the father was convicted with \n demostic violence later finding out he escaped from prison. \n Your friend starts to panick, they need your help, \n since their father was part of a military special force, \n where he was diagnosed with PTSD with a killers mentality. ", bg = 'red')
story1_power1_decision9.pack(fill='x')

story1_power1_decision9_btn1 = tk.Button(story1_power1_choice9, text = 'Leave them Alone', command=lambda:show_frame(story1_power1_choice10))
story1_power1_decision9_btn1.place(x = 640, y = 600, width = 300, height = 60) # <====== Left Button 

story1_power1_decision9_btn2 = tk.Button(story1_power1_choice9, text = 'Help them', command=lambda:show_frame(story1_power1_choice11))
story1_power1_decision9_btn2.place(x = 1000, y = 600, width = 300, height = 60) # <======= Right Button

story1_power1_decision10 = tk.Label(story1_power1_choice10, text = 'They ended up killing themselves where their family and friends mourned for their death. \n But the their father is still out there looking for you, \n just to get his revenge for imprisoning him', bg = 'red')
story1_power1_decision10.pack(fill='x')

story1_power1_decision11 = tk.Label(story1_power1_choice11, text = 'you decided to come over your friends house \n so you can discuss your plan with their mother. \n But already too late the father breaks into the house \n killing you, your friend, and their mother.', bg = 'red')
story1_power1_decision11.pack(fill='x')

#------------------ Story 1 Power 2 ------------------#

power_btn2 = tk.Button(story1, text = 'Strength', command=lambda:show_frame(story1_power2_choice1))
power_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story1_power2_decision1 = tk.Label(story1_power2_choice1, text = 'A random football coach approaches you based on your body structure \n since you seem pretty strong and fit.  \n They want you to join their sport', bg = 'red')
story1_power2_decision1.pack(fill='x')

#------------------ Story 1 Power 2 Options ------------------#

story1_power2_decision1_btn1 = tk.Button(story1_power2_choice1, text = 'Kindly Reject', command=lambda:show_frame(story1_power2_choice2))
story1_power2_decision1_btn1.place(x = 640, y = 600, width = 300, height = 60)

story1_power2_decision1_btn2 = tk.Button(story1_power2_choice1, text = 'Join the Sport', command=lambda:show_frame(story1_power2_choice7))
story1_power2_decision1_btn2.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 1 Power 2 Kindly Reject ------------------#

story1_power2_decision2 = tk.Label(story1_power2_choice2, text = 'The coach walks away and you proceed to go to class. \n After school, you come home seeing the football coach that asked you join the sport at your house.  \n He talked to both of your parents and convinced them to pressure you to join football. ', bg = 'red')
story1_power2_decision2.pack(fill='x')

story1_power2_decision2_btn1 = tk.Button(story1_power2_choice2, text = 'Ignore them', command=lambda:show_frame(story1_power2_choice3))
story1_power2_decision2_btn1.place(x = 640, y = 600, width = 300, height = 60)

story1_power2_decision2_btn2 = tk.Button(story1_power2_choice2, text = 'Join the Sport', command=lambda:show_frame(story1_power2_choice4))
story1_power2_decision2_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story1_power2_decision3 = tk.Label(story1_power2_choice3, text = "You seem like you can't handle the pressure, you start to lose yourself, \n and you start destroying your home breaking the walls & furniture. \n Your parents seen the distruction you've caused \n forcing  them to call the government specialist due to your strength. With government holding you captive, \n they will try to take advantage of your ability and use it as tool. \n So you decided to escape leaving no traces, \n where your idea is to runaway as far as you can so they won't catch you", bg = 'red')
story1_power2_decision3.pack(fill='x')

story1_power2_decision4 = tk.Label(story1_power2_choice4, text = "You didn't like the coach from what he did to you, so you decided to the opposite of his request. \n During practice you would frustrate him where you're forcing yourself not to try. \n The coach approaches you telling negative things about, \n where he is threatning your life since he wants to use you to revive his coaching career.", bg = 'red')
story1_power2_decision4.pack(fill='x')

story1_power2_decision4_btn1 = tk.Button(story1_power2_choice4, text = 'Talk Back', command=lambda:show_frame(story1_power2_choice5))
story1_power2_decision4_btn1.place(x = 640, y = 600, width = 300, height = 60)

story1_power2_decision4_btn2 = tk.Button(story1_power2_choice4, text = 'Leave Practice', command=lambda:show_frame(story1_power2_choice6))
story1_power2_decision4_btn2.place(x = 640, y = 600, width = 300, height = 60)

story1_power2_decision5 = tk.Label(story1_power2_choice5, text = 'you burst out of anger, where you pushed your football coach across \n the locker room where you break his bones and structure of his body. \n You break the locker room into pieces and living the whole place in wreckage. \n You come home, the polic are at your house looking for you... \n you are forced to runaway from home and live into another country.', bg = 'red')
story1_power2_decision5.pack(fill='x')

story1_power2_decision6 = tk.Label(story1_power2_choice6, text = 'you leave practice and your parents are very disappointed at you since they were promised you were going to become an NFL Player. So they decided to disown you, kicking you out of the house where you have to resort to getting an apartment, working for a minimum wage job, and going to school at the same time. You ended up doing videos of yourself lifting heavy and posting the videos on social media where you are gaining followers and getting paid to become an influencer in social media, motivating others to become fit.', bg = 'red')
story1_power2_decision6.pack(fill='x')

#------------------ Story 1 Power 2 Join the Sport ------------------#

story1_power2_decision7 = tk.Label(story1_power2_choice7, text = 'You become a varsity player, where you become really good at the sport and you start get Division 1 offers from well-known football schools. You ended with 20 offers from several Divison 1 football schools, but you seem pretty unsure if you want to continue football or pursue your academic career', bg = 'red')
story1_power2_decision7.pack(fill='x')

story1_power2_decision7_btn1 = tk.Button(story1_power2_choice7, text = 'Play Football', command=lambda:show_frame(story1_power2_choice8))
story1_power2_decision7_btn1.place(x = 640, y = 600, width = 300, height = 60)

story1_power2_decision7_btn2 = tk.Button(story1_power2_choice7, text = 'Purse Academia', command=lambda:show_frame(story1_power2_choice9))
story1_power2_decision7_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story1_power2_decision8 = tk.Label(story1_power2_choice8, text = "You become a recording breaking college football player, \n you win the heisman trophy, and a national champion. \n You get drafted as top pick and earn millions of dollars but your career didn't last, \n you decided to splurge your earnings where you're left with none. \n Where you become homeless living in a homeless shelter.", bg = 'red')
story1_power2_decision8.pack(fill='x')

story1_power2_decision9 = tk.Label(story1_power2_choice9, text = 'You decided to major in Kineseology, \n you earned your degree and started working for organizations to aid there players. \n You become really successful and earned enough to enjoy your life. ', bg = 'red')
story1_power2_decision9.pack(fill='x')

#------------------ Story 1  Power 1 Reset Buttons ------------------#

p1reset_button1 = tk.Button(story1_power1_choice3, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power))
p1reset_button1.place(x = 640, y = 600, width = 300, height = 60) # <======= Right Button Coordinates

p1reset_button2 = tk.Button(story1_power1_choice5, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power))
p1reset_button2.place(x = 640, y = 600, width = 300, height = 60)

p1reset_button3 = tk.Button(story1_power1_choice8, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power))
p1reset_button3.place(x = 640, y = 600, width = 300, height = 60)

p1reset_button4 = tk.Button(story1_power1_choice10, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power))
p1reset_button4.place(x = 640, y = 600, width = 300, height = 60)

p1reset_button5 = tk.Button(story1_power1_choice11, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power))
p1reset_button5.place(x = 640, y = 600, width = 300, height = 60)

#------------------ Story 1  Power 1 Return to Theme ------------------#

p1return_button1 = tk.Button(story1_power1_choice3, text = 'Return to Theme', command=lambda:show_frame(f3))
p1return_button1.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button2 = tk.Button(story1_power1_choice5, text = 'Return to Theme', command=lambda:show_frame(f3))
p1return_button2.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button3 = tk.Button(story1_power1_choice8, text = 'Return to Theme', command=lambda:show_frame(f3))
p1return_button3.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button4 = tk.Button(story1_power1_choice10, text = 'Return to Theme', command=lambda:show_frame(f3))
p1return_button4.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button5 = tk.Button(story1_power1_choice11, text = 'Return to Theme', command=lambda:show_frame(f3))
p1return_button5.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 1  Power 2 Reset Buttons ------------------#

p2reset_button1 = tk.Button(story1_power2_choice3, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power2_choice1))
p2reset_button1.place(x = 640, y = 600, width = 300, height = 60)

p2reset_button2 = tk.Button(story1_power2_choice5, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power2_choice1))
p2reset_button2.place(x = 640, y = 600, width = 300, height = 60)

p2reset_button3 = tk.Button(story1_power2_choice6, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power2_choice1))
p2reset_button3.place(x = 640, y = 600, width = 300, height = 60)

p2reset_button4 = tk.Button(story1_power2_choice8, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power2_choice1))
p2reset_button4.place(x = 640, y = 600, width = 300, height = 60)

p2reset_button5 = tk.Button(story1_power2_choice9, text = 'Reset from the Beginning', command=lambda:show_frame(story1_power2_choice1))
p2reset_button5.place(x = 640, y = 600, width = 300, height = 60)

#------------------ Story 1  Power 2 Return to Theme ------------------#

p2return_button1 = tk.Button(story1_power2_choice3, text = 'Return to Theme', command=lambda:show_frame(f3))
p2return_button1.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button2 = tk.Button(story1_power2_choice5, text = 'Return to Theme', command=lambda:show_frame(f3))
p2return_button2.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button3 = tk.Button(story1_power2_choice6, text = 'Return to Theme', command=lambda:show_frame(f3))
p2return_button3.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button4 = tk.Button(story1_power2_choice8, text = 'Return to Theme', command=lambda:show_frame(f3))
p2return_button4.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button4 = tk.Button(story1_power2_choice9, text = 'Return to Theme', command=lambda:show_frame(f3))
p2return_button4.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 2 ------------------#

story2_title = tk.Label(story2, text = "Your friend has been working on a simulation game that will be revolutional to the gaming industry. \n They invited you over their companies facility, so you can try their new game. \n You're very thrilled to try it out and so the game begins, you spawn in an Apocalyptic Wasteland, and your main goal is to survive.", bg = 'red')
story2_title.pack(fill='x')

#------------------ Story 2 First Choice ------------------#

story2_title_btn1 = tk.Button(story2, text = "Look for Weapons, and Survivors", command=lambda:show_frame(story2_choice1_decision1))
story2_title_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c1_d1 = tk.Label(story2_choice1_decision1, text = "You found a pistol with a little bit of ammo and discovered a survivor who use to work for a hospial, \n they are very skilled with aiding people. \n You guys are getting chased by a hoard of zombies....", bg = 'red')
story2_c1_d1.pack(fill='x')

story2_c1_d1_btn1 = tk.Button(story2_choice1_decision1,  text = "Run Away", command=lambda:show_frame(story2_choice1_decision2))
story2_c1_d1_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c1_d1_btn2 = tk.Button(story2_choice1_decision1, text = 'Kill the Zombies', command=lambda:show_frame(story2_choice1_decision7))
story2_c1_d1_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c1_d2 = tk.Label(story2_choice1_decision2, text = 'You guys escape the zombies, but \n you guys are very tired but in need for Food and Water', bg = 'red')
story2_c1_d2.pack(fill='x')

story2_c1_d2_btn1 = tk.Button(story2_choice1_decision2, text = 'Split up and search for Food and Water', command=lambda:show_frame(story2_choice1_decision3))
story2_c1_d2_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c1_d2_btn2 = tk.Button(story2_choice1_decision2, text = 'Go together and search for Food and Water', command=lambda:show_frame(story2_choice1_decision8))
story2_c1_d2_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c1_d3 = tk.Label(story2_choice1_decision3, text = 'You and the survivor come back with food and water. \n But the survivor came back infected, where you have to make a choice...', bg = 'red')
story2_c1_d3.pack(fill='x')

story2_c1_d3_btn1 = tk.Button(story2_choice1_decision3, text = 'Kill the survivor', command=lambda:show_frame(story2_choice1_decision4))
story2_c1_d3_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c1_d3_btn2 = tk.Button(story2_choice1_decision3, text = 'Aid the survivor', command=lambda:show_frame(story2_choice1_decision9))
story2_c1_d3_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c1_d4 = tk.Label(story2_choice1_decision4, text = 'Now that you killed the survivor with the food and water you found. \n You also, found a walky talky while scavenging, \n you receive a transmission from the walky talky. \n The device gave you directions where to head for shelter and protection.', bg = 'red')
story2_c1_d4.pack(fill='x')

story2_c1_d4_btn1 = tk.Button(story2_choice1_decision4, text = 'Rest for the Night', command=lambda:show_frame(story2_choice1_decision5))
story2_c1_d4_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c1_d4_btn2 = tk.Button(story2_choice1_decision4, text = 'Search for Vehicle', command=lambda:show_frame(story2_choice1_decision10))
story2_c1_d4_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c1_d5 = tk.Label(story2_choice1_decision5, text = 'You rested for the night and consumed some food so you can gain your enevery the next day. \n Once the sun rised, you found a hidden hatch that led to a room...', bg = 'red')
story2_c1_d5.pack(fill='x')

story2_c1_d5_btn1 = tk.Button(story2_choice1_decision5, text = 'Search for a Vehicle', command=lambda:show_frame(story2_choice1_decision6))
story2_c1_d5_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c1_d5_btn2 = tk.Button(story2_choice1_decision5, text = 'Go inside the hatch', command=lambda:show_frame(story2_choice1_decision11))
story2_c1_d5_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c1_d6 = tk.Label(story2_choice1_decision6, text = 'You find a vehicle, and gassed up the vehicle at the nearest gas station. \n You followed the coordinates that you receive from the transmission. \n But once you arrived at the destination, \n you are surprised with the military and their guns pointed at you, \n where they fired their weapons and you died. \n Game Over!!', bg = 'red')
story2_c1_d6.pack(fill='x')

story2_c1_d7 = tk.Label(story2_choice1_decision7, text = 'You lost ammo and died.....', bg = 'red')
story2_c1_d7.pack(fill='x')

story2_c1_d8 = tk.Label(story2_choice1_decision8, text = "You guys were able gather enough food for each other until, \n it wasn't enough where you guys starved to death together.", bg = 'red')
story2_c1_d8.pack(fill='x')

story2_c1_d9 = tk.Label(story2_choice1_decision9, text = 'The Survivor ended up becoming a zombie, and kills you.', bg = 'red')
story2_c1_d9.pack(fill='x')

story2_c1_d10 = tk.Label(story2_choice1_decision10, text = "You found a vehicle, but you are very tired, \n you died of starvation since you didn't rest and decided \n to leave your belongings instead you went to go look for a vehicle. ", bg = 'red')
story2_c1_d10.pack(fill='x')

story2_c1_d11 = tk.Label(story2_choice1_decision11, text = 'Once you go inside the hatch, there was locked door and a camera pointed at you... \n where you are welcomed with a colony of survivors ready \n to go out and fight against the the horde of zombies and \n the government who has been spawning the creatures. \n You fight with the colony and eventually beating the game. \n GOOD JOB!', bg = 'red')
story2_c1_d11.pack(fill='x')

#------------------ Story 2 First Choice Reset ------------------#

story2_reset1 = tk.Button(story2_choice1_decision6, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset1.place(x = 640, y = 600, width = 300, height = 60)

story2_reset2 = tk.Button(story2_choice1_decision7, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset2.place(x = 640, y = 600, width = 300, height = 60)

story2_reset3 = tk.Button(story2_choice1_decision8, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset3.place(x = 640, y = 600, width = 300, height = 60)

story2_reset4 = tk.Button(story2_choice1_decision9, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset4.place(x = 640, y = 600, width = 300, height = 60)

story2_reset5 = tk.Button(story2_choice1_decision10, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset5.place(x = 640, y = 600, width = 300, height = 60)

story2_reset6 = tk.Button(story2_choice1_decision11, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset6.place(x = 640, y = 600, width = 300, height = 60)

#------------------ Story 2 First Choice Return Theme ------------------#

story2_return1 = tk.Button(story2_choice1_decision6, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return1.place(x = 1000, y = 600, width = 300, height = 60)

story2_return2 = tk.Button(story2_choice1_decision7, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return2.place(x = 1000, y = 600, width = 300, height = 60)

story2_return3 = tk.Button(story2_choice1_decision8, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return3.place(x = 1000, y = 600, width = 300, height = 60)

story2_return4 = tk.Button(story2_choice1_decision9, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return4.place(x = 1000, y = 600, width = 300, height = 60)

story2_return5 = tk.Button(story2_choice1_decision10, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return5.place(x = 1000, y = 600, width = 300, height = 60)

story2_return6 = tk.Button(story2_choice1_decision11, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return6.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 2 Second Choice ------------------#

story2_title_btn2 = tk.Button(story2, text = "Look for Food and Shelter", command=lambda:show_frame(story2_choice2_decision1))
story2_title_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c2_d1 = tk.Label(story2_choice2_decision1, text = 'While serching for food, you found seeds \n where you can start your own farm and produce an unlimited supply of food. \n You produce plenty where you can go venture and get supplies \n such as weapons and gear to protect yourself, \n also look for survivors.', bg = 'red')
story2_c2_d1.pack(fill='x')

story2_c2_d1_btn1 = tk.Button(story2_choice2_decision1, text = 'Go Venture', command=lambda:show_frame(story2_choice2_decision2))
story2_c2_d1_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c2_d1_btn2 = tk.Button(story2_choice2_decision1, text = 'Stay and Farm', command=lambda:show_frame(story2_choice2_decision4))
story2_c2_d1_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c2_d2 = tk.Label(story2_choice2_decision2, text = 'While venturing, you found weapons and gear to protect yourself. \n Also, you discover two survivors who are need of food, \n so you take them with you to your place and provided them with your supplies. \n Days goes by and found more survivors and gear \n where you started a village/community that provides and protects anyone you find, \n but one night you guys are ambushed with a big horde of zombies \n where you to need to find a way to protect everyone.', bg = 'red')
story2_c2_d2.pack(fill='x')

story2_c2_d2_btn1 = tk.Button(story2_choice2_decision2, text = 'Get Everyone and Prepare to Depart', command=lambda:show_frame(story2_choice2_decision3))
story2_c2_d2_btn1.place(x = 640, y = 600, width = 300, height = 60)

story2_c2_d2_btn2 = tk.Button(story2_choice2_decision2, text = 'Stay and Defend', command=lambda:show_frame(story2_choice2_decision5))
story2_c2_d2_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story2_c2_d3 = tk.Label(story2_choice2_decision3, text = 'You and your community left to go far from the place where you find another shelter from an abandon military base \n  where you are supplied with hightech weaponry \n to fight against the horde of zombies and purify the world from the infection.', bg = 'red')
story2_c2_d3.pack(fill='x')

story2_c2_d4 = tk.Label(story2_choice2_decision4, text = "While farming, you're place was attacked by zombies, \n where you had nothing to defend yourself. You Died. Game Over!", bg = 'red')
story2_c2_d4.pack(fill='x')

story2_c2_d5 = tk.Label(story2_choice2_decision5, text = 'While defending you lost a lot of people, \n weapons and gear were very limited, \n and the horde overwhelmed your people where you guys are stuck. Game Over!', bg = 'red')
story2_c2_d5.pack(fill='x')

#------------------ Story 2 Second Choice Reset ------------------#

story2_reset1_c2 = tk.Button(story2_choice2_decision3, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset1_c2.place(x = 640, y = 600, width = 300, height = 60)

story2_reset2_c2 = tk.Button(story2_choice2_decision4, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset2_c2.place(x = 640, y = 600, width = 300, height = 60)

story2_reset3_c2 = tk.Button(story2_choice2_decision5, text = 'Reset to the Beginning', command=lambda:show_frame(story2))
story2_reset3_c2.place(x = 640, y = 600, width = 300, height = 60)


#------------------ Story 2 Second Choice Return Theme ------------------#

story2_return1_c2 = tk.Button(story2_choice2_decision3, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return1_c2.place(x = 1000, y = 600, width = 300, height = 60)

story2_return2_c2 = tk.Button(story2_choice2_decision4, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return2_c2.place(x = 1000, y = 600, width = 300, height = 60)

story2_return3_c2 = tk.Button(story2_choice2_decision5, text = 'Return to Theme', command=lambda:show_frame(f3))
story2_return3_c2.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 3 ------------------#

story3_title = tk.Label(story3, text = 'You wake up for first day of school, \n feeling tired from the days you stayed up playing video games. \n Due to our current circumstances of COVID-19, classes are recorded through zoom.. \n you have a choice to attend or dismiss class..', bg = 'red')
story3_title.pack(fill='x')

#------------------ Story 3 First Decision ------------------#

story3_c1 = tk.Button(story3, text = 'Attend', command=lambda:show_frame(story3_choice1_decision1))
story3_c1.place(x = 640, y = 600, width = 300, height = 60)

story3_c1_d1 = tk.Label(story3_choice1_decision1, text = 'Since you attended class you were introduced \n to a club where you can engage with the campus community. \n Especially, you are able to meet new friends and help each for the assignment. \n Class just finished, you have choice to do homework right away or play video games \n since you have a break for a a while until the next class', bg = 'red')
story3_c1_d1.pack(fill='x')

story3_c1_d1_btn1 = tk.Button(story3_choice1_decision1, text = 'Do Homework', command=lambda:show_frame(story3_choice1_decision2))
story3_c1_d1_btn1.place(x = 640, y = 600, width = 300, height = 60)

story3_c1_d1_btn2 = tk.Button(story3_choice1_decision1, text = 'Play Video Games', command=lambda:show_frame(story3_choice1_decision5))
story3_c1_d1_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c1_d2 = tk.Label(story3_choice1_decision2, text = 'You did homework right away, and started to get ahead of the class \n where you have enough time for yourself to learn other things or relax. \n One of your classmates decided to ask you for help \n you have a choice to help them or ignore them ', bg = 'red')
story3_c1_d2.pack(fill='x')

story3_c1_d2_btn1 = tk.Button(story3_choice1_decision2, text = 'Help them', command=lambda:show_frame(story3_choice1_decision3))
story3_c1_d2_btn1.place(x = 640, y = 600, width = 300, height = 60)

story3_c1_d2_btn2 = tk.Button(story3_choice1_decision2, text = 'Ignore them', command=lambda:show_frame(story3_choice1_decision4))
story3_c1_d2_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c1_d3 = tk.Label(story3_choice1_decision3, text = 'Since you help them, you guys become really successful together \n throughout your college career and became bestfriends. \n You guys worked really well in your field of study \n where you guys started an organization, became investors, and built a company. \n Succesful Ending!', bg = 'red')
story3_c1_d3.pack(fill='x')

story3_c1_d4 = tk.Label(story3_choice1_decision4, text = 'Since you decided to stay independent and stick to your plans, n\ also ignoring people when they need your help. n\ You graduated very successful, but you end up meeting the people you ignored n\ where they become more successful than you.Last thing you know, n\ they are the project cordinatoor that you are working with. ', bg = 'red')
story3_c1_d4.pack(fill='x')

story3_c1_d5 = tk.Label(story3_choice1_decision5, text = "You decided to play video games, \n you decided to do homework later since you want to relax and enjoy your break. \n your guardian ask you to do chores, since you are home and they see you not doing anything...", bg = 'red')
story3_c1_d5.pack(fill='x')

story3_c1_d5_btn1 = tk.Button(story3_choice1_decision5, text= 'Help', command=lambda:show_frame(story3_choice1_decision6))
story3_c1_d5_btn1.place(x = 640, y = 600, width = 300, height = 60)

story3_c1_d5_btn2 = tk.Button(story3_choice1_decision5, text = 'Lie', command=lambda:show_frame(story3_choice1_decision7))
story3_c1_d5_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c1_d6 = tk.Label(story3_choice1_decision6, text = "You decided to help your guardian with your chores and task to do around the house, \n but you tend to be tired while doing homework, \n so you decided to do your homework last minute where you didn't produce a good work. Later you graduate with a degree, \n but how you preform your task hinders your success in your field. \n Where you are just stuck as a regular employee \n who is in a contract with the company.", bg = 'red')
story3_c1_d6.pack(fill='x')

story3_c1_d7 = tk.Label(story3_choice1_decision7, text = 'Since you lied that you were busy and played video games, \n you started to make YouTube videos since you do pretty well at videogames \n and you would like to share your skills to the gaming community. \n You become an influencer to many people in the gaming community \n where you decided to drop out of school and pursue becoming an influencer', bg = 'red')
story3_c1_d7.pack(fill='x')

#------------------ Story 3 First Decision Reset ------------------#

story3_c1_reset1 = tk.Button(story3_choice1_decision3, text = "Reset to the Beginning",  command=lambda:show_frame(story3))
story3_c1_reset1.place(x = 640, y = 600, width = 300, height = 60)

story3_c1_reset2 = tk.Button(story3_choice1_decision4, text = "Reset to the Beginning",  command=lambda:show_frame(story3))
story3_c1_reset2.place(x = 640, y = 600, width = 300, height = 60)

story3_c1_reset3 = tk.Button(story3_choice1_decision6, text = "Reset to the Beginning",  command=lambda:show_frame(story3))
story3_c1_reset3.place(x = 640, y = 600, width = 300, height = 60)

story3_c1_reset4 = tk.Button(story3_choice1_decision7, text = "Reset to the Beginning",  command=lambda:show_frame(story3))
story3_c1_reset4.place(x = 640, y = 600, width = 300, height = 60)

#------------------ Story 3 First Decision Return ------------------#

story3_c1_return1 = tk.Button(story3_choice1_decision3, text = "Return to Theme",  command=lambda:show_frame(f3))
story3_c1_return1.place(x = 1000, y = 600, width = 300, height = 60)

story3_c1_return2 = tk.Button(story3_choice1_decision4, text = "Return to Theme",  command=lambda:show_frame(f3))
story3_c1_return2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c1_return3 = tk.Button(story3_choice1_decision6, text = "Return to Theme",  command=lambda:show_frame(f3))
story3_c1_return3.place(x = 1000, y = 600, width = 300, height = 60)

story3_c1_return4 = tk.Button(story3_choice1_decision7, text = "Return to Theme",  command=lambda:show_frame(f3))
story3_c1_return4.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 3 Second Decision ------------------#

story3_c2 = tk.Button(story3, text = 'Dismiss', command=lambda:show_frame(story3_choice2_decision1))
story3_c2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c2_d1 = tk.Label(story3_choice2_decision1, text = "You decided to dismiss class \n since you want to catch up with your sleep and you a very tired, \n  you won't be acquiring any knowledge. \n your guardian ask you to do chores, \n since you are home and they see you not doing anything...", bg = 'red')
story3_c2_d1.pack(fill='x')

story3_c2_d1_btn1 = tk.Button(story3_choice2_decision1, text = 'Lie', command=lambda:show_frame(story3_choice2_decision2))
story3_c2_d1_btn1.place(x = 640, y = 600, width = 300, height = 60)

story3_c2_d1_btn2 = tk.Button(story3_choice2_decision1, text = 'Help', command=lambda:show_frame(story3_choice2_decision4))
story3_c2_d1_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c2_d2 = tk.Label(story3_choice2_decision2, text = "You lied to your guardian that you're in break for class, and decided \n to play video games and plan to do homework later tonight. \n Now you're very hungry, you want have a choice \n to order from Uber or make your own meal", bg = 'red')
story3_c2_d2.pack(fill='x')

story3_c2_d2_btn1 = tk.Button(story3_choice2_decision2, text = "Uber", command=lambda:show_frame(story3_choice2_decision3))
story3_c2_d2_btn1.place(x = 640, y = 600, width = 300, height = 60)

story3_c2_d2_btn2 = tk.Button(story3_choice2_decision2, text = "Make your own Meal", command=lambda:show_frame(story3_choice2_decision5))
story3_c2_d2_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c2_d3 = tk.Label(story3_choice2_decision3, text = 'After receiving your order and finished eating, \n you seem very tired so you decided to rest for the day. \n You kept repeating the same routine to the point \n where you dropped out of school, \n and decided to work for a minimum wage job.', bg = 'red')
story3_c2_d3.pack(fill='x')

story3_c2_d4 = tk.Label(story3_choice2_decision4, text = 'You decided to help your guardian while your chores, \n but you continued to miss class. \n You started to fail each class since you are always busy \n so you became a part time student \n where the duration of you receiving your degree will be longer.', bg = 'red')
story3_c2_d4.pack(fill='x')

story3_c2_d5 = tk.Label(story3_choice2_decision5, text = 'You have your own meal, where you feel refresh and consumed enough energy in order to motivate yourself to do your school. \n But your guardian was very upset at you since they figured you lied to them, \n so they decided to take away your fun. \n Where you are forced to continue school \n without having any enjoyment until you graduate', bg = 'red')
story3_c2_d5.pack(fill='x')

#------------------ Story 3 Second Decision Reset ------------------#

story3_c2_reset1 = tk.Button(story3_choice2_decision3, text = 'Reset to the Beginning', command=lambda:show_frame(story3))
story3_c2_reset1.place(x = 640, y = 600, width = 300, height = 60)

story3_c2_reset2 = tk.Button(story3_choice2_decision4, text = 'Reset to the Beginning', command=lambda:show_frame(story3))
story3_c2_reset2.place(x = 640, y = 600, width = 300, height = 60)

story3_c2_reset3 = tk.Button(story3_choice2_decision5, text = 'Reset to the Beginning', command=lambda:show_frame(story3))
story3_c2_reset3.place(x = 640, y = 600, width = 300, height = 60)

#------------------ Story 3 Second Decision Return ------------------#

story3_c2_return1 = tk.Button(story3_choice2_decision3, text = 'Return to Theme', command=lambda:show_frame(f3))
story3_c2_return1.place(x = 1000, y = 600, width = 300, height = 60)

story3_c2_return2 = tk.Button(story3_choice2_decision4, text = 'Return to Theme', command=lambda:show_frame(f3))
story3_c2_return2.place(x = 1000, y = 600, width = 300, height = 60)

story3_c2_return3 = tk.Button(story3_choice2_decision5, text = 'Return to Theme', command=lambda:show_frame(f3))
story3_c2_return3.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 4 ------------------#

story4_title = tk.Label(story4, text = "You and 4 other friends are willing \n to go for a vacation in the woods for 2 and a half weeks so \n you guys can experience the wild life. You guys stayed in a Cabin, \n where you and 4 other friends have your own seperate rooms and \n you guys are making plans for the next couple weeks. \n You guys were enjoying yourself until, \n one night one of your friends discovers a tunnel \n where there was someone staying underneath the cabin.", bg = 'red')
story4_title.pack(fill='x')

#------------------ Story 4 First Choice ------------------#

story4_c1 = tk.Button(story4, text = "Rest for the Night", command=lambda:show_frame(story4_choice1_decision1))
story4_c1.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_d1 = tk.Label(story4_choice1_decision1, text = 'You guys rested for the night, until the next morning \n you find a dead moose in front of the house \n that has been chopped up into pieces', bg = 'red')
story4_c1_d1.pack(fill='x')

story4_c1_d1_btn1 = tk.Button(story4_choice1_decision1, text = 'Ignore', command=lambda:show_frame(story4_choice1_decision2))
story4_c1_d1_btn1.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_d1_btn2 = tk.Button(story4_choice1_decision1, text = 'Investigate', command=lambda:show_frame(story4_choice1_decision4))
story4_c1_d1_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_d2 = tk.Label(story4_choice1_decision2, text = "You guys ignored and assumed it was nature doing its own cycle of life \n where it couldn't have been different predators looking for food. \n You guys were swimming at the lake enjoying yourself, \n you guys arrived at the cabin and the place was open where it seems \n like someone went inside the place and took some of your belongings.", bg = 'red')
story4_c1_d2.pack(fill='x')

story4_c1_d2_btn1 = tk.Button(story4_choice1_decision2, text = 'Ignore', command=lambda:show_frame(story4_choice1_decision3))
story4_c1_d2_btn1.place(x = 820, y = 600, width = 300, height = 60)

story4_c1_d3 = tk.Label(story4_choice1_decision3, text = 'You guys assumed it was predator looking for food and they decided \n to go inside since the some of your friends left there window open. \n Until one night, you guys woke up hanged upside down \n inside the cave that your friend discovered. \n Where you guys are tortured and killed by a Serial Killer that lived underneath \n the cabin for years using it as bait for him to get his victims.', bg = 'red')
story4_c1_d3.pack(fill='x')

story4_c1_d4 = tk.Label(story4_choice1_decision4, text = "The dead moose was cut into pieces using sharp tools \n which it didn't came from other predators. \n You discovered foot prints around the area...", bg = 'red')
story4_c1_d4.pack(fill='x')

story4_c1_d4_btn1 = tk.Button(story4_choice1_decision4, text = 'Ignore', command=lambda:show_frame(story4_choice1_decision5))
story4_c1_d4_btn1.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_d4_btn2 = tk.Button(story4_choice1_decision4, text = 'Investigate', command=lambda:show_frame(story4_choice1_decision6))
story4_c1_d4_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_d5 = tk.Label(story4_choice1_decision5, text = "You decided to ignore the foot prints that could've led to something \n that you could've discovered...Until one morning, \n you and your friends wake up with no limbs suffering. \n RIP BOZO", bg = 'red')
story4_c1_d5.pack(fill='x')

story4_c1_d6 = tk.Label(story4_choice1_decision6, text = 'You followed the footprints where it led to a storage, \n full of sharps tools that used recently with blood stains on them.', bg = 'red')
story4_c1_d6.pack(fill='x')

story4_c1_d6_btn1 = tk.Button(story4_choice1_decision6, text = 'Ignore', command=lambda:show_frame(story4_choice1_decision7))
story4_c1_d6_btn1.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_d6_btn2 = tk.Button(story4_choice1_decision6, text = 'Investigate', command=lambda:show_frame(story4_choice1_decision8))
story4_c1_d6_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_d7 = tk.Label(story4_choice1_decision7, text = "You decided to ignore tools that could be use as a clue \n to investigate the paranormal activities around the camping grounds.... \n Until you walk back to your cabin, you are accompanied by an unknown figure \n where he hunts down each one of your friends, \n until he kills all you and your friends...", bg = 'red')
story4_c1_d7.pack(fill='x')

story4_c1_d8 = tk.Label(story4_choice1_decision8, text = "You started to see clues and gained knowledge who owned the place, until you hear footprints getting near..You hide so you won't get spotted, stunned and frieghtened, you see who committed the incident.. it was one of your friends that insisted you guys to go campingWith your heartbeating fast, you have to make a choice", bg = 'red')
story4_c1_d8.pack(fill='x')

story4_c1_d8_btn1 = tk.Button(story4_choice1_decision8, text = 'Run', command=lambda:show_frame(story4_choice1_decision9))
story4_c1_d8_btn1.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_d8_btn2 = tk.Button(story4_choice1_decision8, text = 'Wait and Confron your friend later', command=lambda:show_frame(story4_choice1_decision10))
story4_c1_d8_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_d9 = tk.Label(story4_choice1_decision9, text = 'You decided to run for your life, \n where your friend started to chase you and throws a tamohawk \n while doing a 360 and kills you for the final kill cam', bg = 'red')
story4_c1_d9.pack(fill='x')

story4_c1_d10 = tk.Label(story4_choice1_decision10, text = "You decided to confront your friend about him entering the storage \n without being shocked or freightened from the items... \n your friend throws a flashbang, \n goes on the roof the cabin and 360 no scopes you for the final kill cam \n while recording it for an audition to join an ESports team.", bg = 'red')
story4_c1_d10.pack(fill='x')

#------------------ Story 4 First Choice Reset------------------#

story4_c1_reset1 = tk.Button(story4_choice1_decision3, text = 'Reset to Beginning', command=lambda:show_frame(story4))
story4_c1_reset1.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_reset2 = tk.Button(story4_choice1_decision5, text = 'Reset to Beginning', command=lambda:show_frame(story4))
story4_c1_reset2.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_reset3 = tk.Button(story4_choice1_decision7, text = 'Reset to Beginning', command=lambda:show_frame(story4))
story4_c1_reset3.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_reset4 = tk.Button(story4_choice1_decision9, text = 'Reset to Beginning', command=lambda:show_frame(story4))
story4_c1_reset4.place(x = 640, y = 600, width = 300, height = 60)

story4_c1_reset5 = tk.Button(story4_choice1_decision10, text = 'Reset to Beginning', command=lambda:show_frame(story4))
story4_c1_reset5.place(x = 640, y = 600, width = 300, height = 60)

#------------------ Story 4 First Choice Return------------------#

story4_c1_return1 = tk.Button(story4_choice1_decision3, text = 'Return to Theme', command=lambda:show_frame(f3))
story4_c1_return1.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_return2 = tk.Button(story4_choice1_decision5, text = 'Return to Theme', command=lambda:show_frame(f3))
story4_c1_return2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_return3 = tk.Button(story4_choice1_decision7, text = 'Return to Theme', command=lambda:show_frame(f3))
story4_c1_return3.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_return4 = tk.Button(story4_choice1_decision9, text = 'Return to Theme', command=lambda:show_frame(f3))
story4_c1_return4.place(x = 1000, y = 600, width = 300, height = 60)

story4_c1_return10 = tk.Button(story4_choice1_decision10, text = 'Return to Theme', command=lambda:show_frame(f3))
story4_c1_return10.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 4 Second Choice ------------------#

story4_c2 = tk.Button(story4, text = 'Investigate Tunnel', command=lambda:show_frame(story4_choice2_decision1))
story4_c2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c2_d1 = tk.Label(story4_choice2_decision1, text = "You guys investigated the tunnel, finding Witchcraft items \n that was dated centuries ago. \n One of your friends finds book \n that had latin writing and some English.", bg = 'red')
story4_c2_d1.pack(fill='x')

story4_c2_d1_btn1 = tk.Button(story4_choice2_decision1, text = "Read the Book", command=lambda:show_frame(story4_choice2_decision2))
story4_c2_d1_btn1.place(x = 640, y = 600, width = 300, height = 60)

story4_c2_d1_btn2 = tk.Button(story4_choice2_decision1, text = "Leave the Area", command=lambda:show_frame(story4_choice2_decision3))
story4_c2_d1_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c2_d2 = tk.Label(story4_choice2_decision2, text = "one of you friends decided to read book, \n where it shared a quick history of the cabin \n then an unknown voice told them to read the Latin part of the book... \n After reading the Latin part of the book, it was really quite, \n you guys are waiting for something to happen... \n You guys exit the Tunnel, \n the Cabin is being attacked by Trolls who are seeking for revenge \n where they capture you guys and become slaves \n to them since you woke them with a spell that disturbed their slumber.", bg = 'red')
story4_c2_d2.pack(fill='x')

story4_c2_d3 = tk.Label(story4_choice2_decision3, text = "You guys left the area all of sudden \n the entrance to the cave was closed, and you guys are stuck. ", bg = 'red')
story4_c2_d3.pack(fill='x')

story4_c2_d3_btn1 = tk.Button(story4_choice2_decision3, text = "Break the Entrance", command=lambda:show_frame(story4_choice2_decision4))
story4_c2_d3_btn1.place(x = 640, y = 600, width = 300, height = 60)

story4_c2_d3_btn2 = tk.Button(story4_choice2_decision3, text = "Read the Book", command=lambda:show_frame(story4_choice2_decision2))
story4_c2_d3_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c2_d4 = tk.Label(story4_choice2_decision4, text = 'The Entrance was broken, where you guys.. \n are debating to stay or leave the Cabin', bg = 'red')
story4_c2_d4.pack(fill='x')

story4_c2_d4_btn1 = tk.Button(story4_choice2_decision4, text = "Leave the Cabin", command=lambda:show_frame(story4_choice2_decision5)) 
story4_c2_d4_btn1.place(x = 640, y = 600, width = 300, height = 60)

story4_c2_d4_btn2 = tk.Button(story4_choice2_decision4, text = "Stay in the Cabin", command=lambda:show_frame(story4_choice2_decision6))
story4_c2_d4_btn2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c2_d5 = tk.Label(story4_choice2_decision5, text = "You and your friends started to pack up your things and leave the Cabin, but before leaving \n the tires were popped recently by someoneOne of your friend were missing, \n until suddenly he appears out of nowhere holding an intervention fully suited. \n He started to climb the Cabins roof and started to move in a weird motion,  \n doing small tricks with his gear until he jumps off... \n fakes to throw a sniper magazine and shoots all of you guys for the best kill cam.", bg = 'red')
story4_c2_d5.pack(fill='x')

story4_c2_d6 = tk.Label(story4_choice2_decision6, text = "You guys stayed in the Cabin, and paranormal activities started to occur... \none of your friends called the 'Ghostbusters' where they took care of \n the issue and the next day you guys decided to leave and go home.. \n HAPPY ENDING :)", bg = 'red')
story4_c2_d6.pack(fill='x')

#------------------ Story 4 Second Choice Reset------------------#

story4_c2_reset1 = tk.Button(story4_choice2_decision2, text = "Reset to Beginning", command=lambda:show_frame(story4))
story4_c2_reset1.place(x = 640, y = 600, width = 300, height = 60)

story4_c2_reset2 = tk.Button(story4_choice2_decision5, text = "Reset to Beginning", command=lambda:show_frame(story4))
story4_c2_reset2.place(x = 640, y = 600, width = 300, height = 60)

story4_c2_reset3 = tk.Button(story4_choice2_decision6, text = "Reset to Beginning", command=lambda:show_frame(story4))
story4_c2_reset3.place(x = 640, y = 600, width = 300, height = 60)

#------------------ Story 4 Second Choice Return------------------#

story4_c2_return1 = tk.Button(story4_choice2_decision2, text = "Return to Theme", command=lambda:show_frame(f3))
story4_c2_return1.place(x = 1000, y = 600, width = 300, height = 60)

story4_c2_return2 = tk.Button(story4_choice2_decision5, text = "Return to Theme", command=lambda:show_frame(f3))
story4_c2_return2.place(x = 1000, y = 600, width = 300, height = 60)

story4_c2_return3 = tk.Button(story4_choice2_decision6, text = "Return to Theme", command=lambda:show_frame(f3))
story4_c2_return3.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Finished ------------------#


show_frame(f1)

story.mainloop()
