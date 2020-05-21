# Welcome to your Focus Day Project. Replace this comment with something that introduces the user to your project. Be sure to mention the Focus Day and your initials and graduation year. (ie This game is for Pool Volume Day and is written by ML '23.)
# Also, be sure to use comments throughout your program. Use good programming practices, including organization, documentation and citation. Yes, you need to cite your sources! (You can do so using comments at the bottom of your code.)
# Harry Potter Day, sorting hat
def sortinghat(houses):
    G=0
    S=0
    H=0
    R=0
print("Welcome to the sorting hat")
print("I will ask you some questions and sort you into the right house.")
print("Let's begin!")
print("A Blue, B Red, C Green, D Yellow")
def answers(A,B,C,D): #what should A,B,C,D be defined as here?
    A=1
    B=1
    C=1
    D=1
print("A blue, B red, C green, D yellow")
Q1=input(str("Which color suits your personality the most?"))
if Q1==A:
    R+1
elif Q1==B:
    G+1
elif Q1==C:
    S+1
elif Q1==D:
    H+1
print("A snake, B lion, C badger, D eagle ")
Q2=input(str("Which of the animals below is your favorite? "))
if Q2==A:
    S+1
elif Q2==B:
    G+1
elif Q2==C:
    H+1
elif Q3==D:
    R+1
print("A fire, B air, C water, D earth")
Q3=input(str("Which element relates with you the most? "))
if Q3==A:
    G+1
elif Q3==B:
    R+1
elif Q3==C:
    S+1
elif Q3==D:
    S+1
print("A analytical, B ambitous, C giving, D honest")
Q4=input(str("Which of the following words describes you the most? "))
if Q4==A:
   R+1
elif Q4==B:
    S+1
elif Q4==C:
    H+1
elif Q4==D:
    G+1
print("A talented, B clever, C brave, D determind")
Q5=input(str("Which of the qualities do you think is the key to success? "))
if Q5==A:
    H+1
elif Q5==B:
    R+1
elif Q5==C:
    G+1
elif Q5==D:
    S+1
print("A Luna Lovegood, B Draco Malfory, C Harry Potter, D Newton Scamander ")
Q6=input(str("Which of the characters above you admire the most? "))
if Q6==A:
    R+1
elif Q6==B:
    S+1
elif Q6==C:
    G+1
elif Q6==D:
    H+1
print("Final question! A Transifiguration, B Potions, C defense agianst dark arts, D Herbology")
Q7=input(str("Which course are you most interested in? "))
if Q7==A:
    G+1
elif Q7==B:
    H+1
elif Q7==C:
    S+1
elif Q7==D:
    R+1
print("Here is the result")
while G>R and G>S and G>H:
    print("You got sorted into Griffindor")
while R>G and R>S and R>H:
    print("You got sorted into Ravenclaw")
while H>G and H>S and G>R:
    print("You got sorted into Hufflepuff")
while S>G and S>H and S>R:
    print("You got sorted into Slytherin")
else:
    print("Seems like you are qualified for all houses.")
result=input("Which house do you want to go to")
print("You are going to 'result'")









    

