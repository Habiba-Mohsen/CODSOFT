import time 
print("---Welcome to the world of TRIVIA!---")
playing = input("Do you want to start playing? ")
if playing.lower() !="yes":
    quit()
name= input("Enter your name: ")
print(f"hello {name} , let's play!")
score=0
time.sleep(1)
print("RULES: \n Type in the answer to each of the following questions \n Make sure to check your spelling to get the answer correct \n    Let's dive in the world of trivia, BUDDY!")
time.sleep(1)
print("## QUESTION ONE ##")
time.sleep(0.5)
Q1= input ("What is the Capital of France? ")
if Q1.lower()=="paris" :
    time.sleep(1)
    print("Correct!")
    score=score+1
else: 
    time.sleep(1)
    print("Wrong!")
    score=score
    time.sleep(1)
    print("Correct Answer: Paris")
print("## QUESTION TWO ##")
time.sleep(0.5)
Q2= input ( "What is the longest river in the world? ")
if Q2.lower()=="the nile river" :
    time.sleep(1)
    print("Correct!")
    score=score+1
else: 
    time.sleep(1)
    print("Wrong!")
    score=score
    time.sleep(1)
    print("Correct Answer: The Nile River")
print("## QUESTION THREE ##")
time.sleep(0.5)
Q3= input ("Which country is both an island and a continent? ")
if Q3.lower()=="australia" :
    time.sleep(1)
    print("Correct!")
    score=score+1
else: 
    time.sleep(1)
    print("Wrong!")
    time.sleep(1)
    print("Correct Answer: Australia")
    score=score
print("## QUESTION FOUR ##")
time.sleep(0.5)
Q4= input ("Which country is known as the Land of the Rising Sun? ")
if Q4.lower()=="japan" :
    time.sleep(1)
    print("Correct!")
    score=score+1
else: 
    time.sleep(1)
    print("Wrong!")
    score=score
    print("Correct Answer:Japan")
print("## QUESTION FIVE ##")
time.sleep(0.5)
Q5= input ("What is the tallest mountain in the world? ")
if Q5.lower()=="mount everest" :
    time.sleep(1)
    print("Correct!")
    score=score+1
else: 
    time.sleep(1)
    print("Wrong!")
    score=score
    time.sleep(1)
    print("Correct Answer: Mount Everest")
time.sleep(1)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(f"HUZZAH! you made it with score {score} out of 5")
performance=(score/5)*100 
time.sleep(1)
print(f"-----your performance is {performance}% ----- ")
