import tkinter as tk


def show_frame(frame):
    frame.tkraise()

    name = user_entry.get()
    start = 'hello'+' '+ name +' '+'you are presented with 4 different situations, \n each situations are adventures where you can choose your own path with a twisted ending. \n \n Hope you enjoy it \n \n choose wisely which path you want to take \n if you want to have a good ending :)'
    theme_title.configure(text = start, font = ('comic sans ms', 32), bg = 'red', fg = 'black')


story = tk.Tk()
story.state('zoomed')
story.title('No Title Yet')

story.rowconfigure(0, weight = 1)
story.columnconfigure(0, weight = 1)

user_frame = tk.Frame(story, bg = 'black')
theme_frame = tk.Frame(story, bg = 'black')

#------------------ Story 1 ------------------#

story1 = tk.Frame(story, bg = 'black')

#------------------ Story 1 (Power 1 Selection) ------------------#

story1_power = tk.Frame(story, bg = 'black')
story1_power1_choice1 = tk.Frame(story, bg = 'black')
story1_power1_choice2 = tk.Frame(story, bg = 'black')
story1_power1_choice3 = tk.Frame(story, bg = 'black')
story1_power1_choice4 = tk.Frame(story, bg = 'black')
story1_power1_choice5 = tk.Frame(story, bg = 'black')
story1_power1_choice6 = tk.Frame(story, bg = 'black')
story1_power1_choice7 = tk.Frame(story, bg = 'black')
story1_power1_choice8 = tk.Frame(story, bg = 'black')
story1_power1_choice9 = tk.Frame(story, bg = 'black')
story1_power1_choice10 = tk.Frame(story, bg = 'black')
story1_power1_choice11 = tk.Frame(story, bg = 'black')

#------------------ Story 1 (Power 2 Selection) ------------------#

story2_power = tk.Frame(story, bg = 'black')
story1_power2_choice1 = tk.Frame(story, bg = 'black')
story1_power2_choice2 = tk.Frame(story, bg = 'black')
story1_power2_choice3 = tk.Frame(story, bg = 'black')
story1_power2_choice4 = tk.Frame(story, bg = 'black')
story1_power2_choice5 = tk.Frame(story, bg = 'black')
story1_power2_choice6 = tk.Frame(story, bg = 'black')
story1_power2_choice7 = tk.Frame(story, bg = 'black')
story1_power2_choice8 = tk.Frame(story, bg = 'black')
story1_power2_choice9 = tk.Frame(story, bg = 'black')
#------------------ Story 2 ------------------#

story2 = tk.Frame(story, bg = 'black')

#------------------ Story 3 ------------------#

story3 = tk.Frame(story, bg = 'black')

#------------------ Story 4 ------------------#

story4 = tk.Frame(story, bg = 'black')



for frame in (user_frame,
              theme_frame,
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
              story3,
              story4):
    frame.place(relheight = 1.0, relwidth = 1.0)



#------------------ User Frame Code ------------------#

user_title = tk.Label(user_frame, text = 'Welcome :) \n \n Please Enter your name', bg = 'red', font = ("times new roman", 32), fg = 'white')
user_title.pack(fill='x')

user_entry = tk.Entry(user_frame)
user_entry.place(x = 900, y = 900, width = 150, height = 20)

user_btn = tk.Button(user_frame, text='Enter', command=lambda:show_frame(theme_frame))
user_btn.place(x = 900, y = 920, width = 150)

#------------------ Theme Frame Code ------------------#

theme_title = tk.Label(theme_frame, text = 'Theme Frame', bg = 'yellow')
theme_title.pack(fill='x')

theme_btn1 = tk.Button(theme_frame, text = 'Dream (Fictional: Superpower)', command=lambda:show_frame(story1))
theme_btn1.place(x = 640, y = 600, width = 300, height = 60)

theme_btn2 = tk.Button(theme_frame, text = 'Simulation (Apocalyptic: Wasteland)', command=lambda:show_frame(story2))
theme_btn2.place(x = 1000, y = 600, width = 300, height = 60)

theme_btn3 = tk.Button(theme_frame, text = 'Experiencing a College Life ', command=lambda:show_frame(story3))
theme_btn3.place(x = 640, y = 720, width = 300, height = 60)

theme_btn4 = tk.Button(theme_frame, text=' "Horror" (Cabin in the Woods) ', command=lambda:show_frame(story4))
theme_btn4.place(x = 1000, y = 720, width = 300, height = 60)


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

p1return_button1 = tk.Button(story1_power1_choice3, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p1return_button1.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button2 = tk.Button(story1_power1_choice5, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p1return_button2.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button3 = tk.Button(story1_power1_choice8, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p1return_button3.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button4 = tk.Button(story1_power1_choice10, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p1return_button4.place(x = 1000, y = 600, width = 300, height = 60)

p1return_button5 = tk.Button(story1_power1_choice11, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
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

p2return_button1 = tk.Button(story1_power2_choice3, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p2return_button1.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button2 = tk.Button(story1_power2_choice5, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p2return_button2.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button3 = tk.Button(story1_power2_choice6, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p2return_button3.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button4 = tk.Button(story1_power2_choice8, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p2return_button4.place(x = 1000, y = 600, width = 300, height = 60)

p2return_button4 = tk.Button(story1_power2_choice9, text = 'Return to Theme', command=lambda:show_frame(theme_frame))
p2return_button4.place(x = 1000, y = 600, width = 300, height = 60)

#------------------ Story 2 ------------------#

story2_title = tk.Label(story2, text = 'story 2', bg = 'white')
story2_title.pack(fill='x')

#------------------ Story 3 ------------------#

story3_title = tk.Label(story3, text = 'red', bg = 'white')
story3_title.pack(fill='x')

#------------------ Story 4 ------------------#

story4_title = tk.Label(story4, text = 'this is frame1', bg = 'white')
story4_title.pack(fill='x')

show_frame(theme_frame)

story.mainloop()
