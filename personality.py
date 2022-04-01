import time
import random

def reqtime(tim = 0.05, text = ''):
    for x in text:
        time.sleep(tim)
        print(x, end='')
    return

def quesToBeAsked(prompt, response1,  response2,  response3):
    global score
    global line
    print()
    reqtime(0.07, prompt)
    print()
    reqtime(0.03, response1)
    print()
    reqtime(0.03, response2)
    print()
    reqtime(0.03, response3)
    print()
    print('Write your choice number ')
    
    while True:
        try:
            response = int(input())
            break
        except ValueError:
            print('Invalid input. Only use number as input')
            continue
    response = str(response)
    
    if (response not in response1) and (response not in response2) and (response not in response3):
        print('Huh')
        reqtime(text = '..... that was not even in the options anyway..???')
    else:
        if response in response1:
            reqtime(text = line[random.randint(0,13)])
            score += random.randint(1,2)
            print()
        if response in response2:
            reqtime(text = line[random.randint(0,13)])
            score += random.randint(3, 5)
            print()
        if response in response3:
            reqtime(text = line[random.randint(0,13)])
            score += random.randint(6, 9)
            print()

score = 0
check = True
line= ['WELL', 'Ahem! Ahem!','Pretty impressive','Did you just read my mind?','*stares in love*.',
           'No way....', 'Ooops  what was the ans again? i was busy stalking you', 'MY G.....', 'Was not expecting that',
           'Simputer for you', 'NEXT....', 'boooo', 'lalala....oh umh nevermind me singing', 'You are just too interesting','i think i am guessing it right'
           'Really???']
dramatic= [1,2,13,4,15,6,7,8,19,10,11,12,14]
clown = [16,18,39,20,21,22,24,13,]
notveryincluding = [25,23,27,9,28,29]
themain = [30,31,32,33,15,42,43,44,45,46,47,26,34]
fighter= [35,26,37,38,17,40,41,48,49,50]

input('lessgo..?')
reqtime(0.04," ")
print(" ")
reqtime(0.04,"WELCOME TO PERSONALITY QUIZ \nAnd unlike other quizzes this won't bore you -, -")
print(" ")
reqtime(0.04," ")
print(" ")
reqtime(0.04,"So, Every friend group has one of these....But which one is yours?")
print(" ")
reqtime(0.04," ")
print(" ")
reqtime(0.04,"Just be seated, let's find out :)")
print(" ")
reqtime(0.04," ")
print(" ")
reqtime(0.05, " Y O U  A R E  T H E . . . . .")
print()
print()
reqtime(0.04,"Lemme ask you some questions first")
reqtime(0.04," ")
print(" ")
reqtime(0.04,"Here you go...")
reqtime(0.04," ")
print(" ")
reqtime(0.04,"'Which animal do you prefer'\n '1. Cat'\n '2. Dog'\n '3. Kid '")
reqtime(0.04," ")
print(" ")
reqtime(0.2," loading ...................       " )
print(" ")
reqtime(0.04," JUST KIDDING, DON'T REPORT ME :P")
print(" ")
quesToBeAsked('What do you think you are?', '1. Introvert.', '2. Extrovert.', '3. In between these two.')
print()
quesToBeAsked('If you were asked to show your phone, what would you do', '1. Give it to them.', '2. Tell them incorrect password.', '3. Show it to them while keeping in your hands.')
print()
quesToBeAsked('If your crush wanted some help, what would you do?', '1. Help them.', '2. Confess before helping them.', '3. Reject in awkward 0_0')
print()
quesToBeAsked('If you had a fight with your fav person, what would you do?', "1. Apologize.",
             '2. Wait for them to apologize.', '3. Take a nap.')
print()
quesToBeAsked("Which kind of Helper you are?", '1. Simply help if asked.', '2. Not help. ', '3. Help only if they help/give-money in return.')
print()
quesToBeAsked("Do you find it hard to be open to others?", '1. Yes really.', '2. Not really. ', '3. Depends on the person i am talking to.')
print()
reqtime(text = 'Well then...')
print('it is....')
time.sleep(1)
print("YOU ARE ",end='')

while check == True:
    for a in dramatic:
        if a == score:
            print('THE DRAMATIC')
            print('''So, basically you are the one who turns every little situation into a mini cinema. Your biggest concern is your appearance, you love interacting. People love it when you are around, you have so much potential specially when it comes to *being ott*. You are the shine of your group ''')
            check = False
    for b in clown :
        if b == score:
            print('THE CLOWN')
            print('''You are always laughing even when they crack jokes on you. You are happy to be you, you love pulling legs and taunting around but not to offend them, you never throw jokes on someone's ordeal, which makes you the king of your group too. It is too bland to be in a group without you -, -.''')
            check = False

    for c in notveryincluding:
        if c == score:
            print('THE LEFT OUT')
            print('''Okay, umh if i had a chance to know you i believe i would not get disappointed but...you are the one who never really joins, you are usually really nice, but quiet.
But that does not bother you or them, you know they still love you. You are just too *speaks in mind language* ''')
            check = False
    for d in themain:
        if d == score:
            print('THE SPARK')
            print('''I SEE! So you are the main character of your group. Everyone treats you like a boss, but it's not because they are forced but because you are oftentimes right. You probably have some sharp jaw and crooked teeth.
You are like the parent, you appreciate each of the member and love it when they are around.''')
            check = False
    for e in fighter:
        if e == score:
            print('THE GANGSTA')
            print('''HAIL YOU! you are the one every one is afraid of. You literally roast people around if they harm any of your friend. Each of them obeys you, you are like their superior. Every one wants to be like you but damn they don't have sexy voice and charm like yours''')
            check = False

    if score >= 51:
        print("oops i took a nap, could you please do this again")
        time.sleep(1)
        print("errors?? glitches? i don't like your teeth thou")
        check = False


