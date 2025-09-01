#import modules
from time import time as t
from random import randrange as r
# ask how many questions user wants
question = int(input("How many question you want? : "))
max_num = int(input("How high the no sould be : "))
#set score start at zero
score = 0
answer_list = []
start = t()
#loop through number of questions
for q in range(question):
  num1 = r(1,max_num +1)
  num2 = r(1,max_num + 1)
  ans = num1 * num2
  
  u_ans = int(input(f'{num1} X {num2} = : '))
  if u_ans == ans:
    score += 1
  end = t()
  answer_list.append(f'{num1} X {num2} = {ans} and your answer : {u_ans} ')
print(f"Thank you for player \n you got {score} right out of {question} and ")
print(f'the percent you got {(round(score/question*100))}%  correct in {round(end-start,1)} seconds ({round(end - start)/question}) seconds per question ')


# create two random numbers and calc answer
# show user the question
for a in answer_list:
  print("\n",a)
# capture answer and modify user score
# output final score 
