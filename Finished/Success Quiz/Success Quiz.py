print('Welcome to the success quiz!\nHow successful will YOU be in 10 years??\n')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.lower()=='yes':
    answer=input('Question 1: What are your current plans? As in general life. ')
    if answer.lower()=='suck dick':
        score += -10
        print('Hmm interesting...')
    else:
        score += 25
        print('Hmm interesting...')
 
 
    answer=input('Question 2: Do you follow Cutiey on literally every social media? Yes or No? ')
    if answer.lower()=='yes':
        score += 69
        print('Great, awesome, amazing..')
    else:
        score += -420
        print('Damn... Hurts')
 
    answer=input('Question 3: Are you a weeb, gay, or just plain weird?')
    if answer.lower()=='Yes':
        score += -25
        print('Jesus christ off yourself...')
    if answer.lower()=='Yeah':
        score += -15
        print('Jesus christ off yourself...')
    if answer.lower()=='Mhm':
        score += -199
        print('Jesus christ off yourself...')
    else:
        score += 5
        print('Hell yeah good for you!')
 
print('Thank you for Playing Cutieys success quiz!\n\n you got',score," \n\nwith 10-40% being a fucking loser joke waste of space and 40-100% being epicly awesome millionair, if your results are significantly negative than u may be a gay weeb... message me ur results :D")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')