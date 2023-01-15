questions = ["Q1) What is the Capital of Pakistan? \n a. Sialkot \t b. Karachi \n c. Lahore \t d. Islamabad", "Q2) What is the value of mathematics constant pi ?\n a. 3.14159 \t b. 22/7 \n c. 353/113 \t d. None of these", "Q3) Who is the winner of The FIFA World Cup ?\n a. Portugal \t b. France \n c. Argentina  \t d. Morocco", "Q4) On which Year Bangladesh get separated from Pakistan ?\n a. 1971 \t b. 1963 \n c. 1988. \t d. 1986", "Q5) Which Islamic State has Nuclear Power ?\n a. Qatar \t b. Egypt \n c. Pakistan \t d. Saudi Arab"]
points = 0
def func(ans):
    global points
    answer = input("Type the right answer:-  a, b, c, d: ").lower()
    if ans in answer:
        print("Your Answer is Correct!!! Moving on to the next Question\n\n")
        points += 1000
    else:
        print("Oops! This is the Wrong Answer")
        
print(questions[0])
func("d")
print(questions[1])
func("a")
print(questions[2])
func("c")
print(questions[3])
func("a")
print(questions[4])
func("c")

if points == 5000:
    print(f"Congratulation!!, You Win the Game, you get {points} points")
else:
    print(f"You can't win but you get {points} points")