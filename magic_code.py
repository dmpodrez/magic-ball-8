import random

answers = [
    "It is certain",
    "It is decided",
    "No doubts",
    "Definitely yes",
    "You can be sure of it",
    "I think - yes",
    "Most likely",
    "Good prospects",
    "Signs point to - yes",
    "Yes",
    "Unclear, try again",
    "Ask later",
    "Better not to tell you",
    "Cannot predict now",
    "Focus and ask again",
    "According to my data - no",
    "Very doubtful",
    "Prospects aren't very good",
    "My answer is - no",
    "Don't even think about it",
]

def random_num():
  number = random.randint(0,19)
  return number

print('Hello World, I am the magic ball, and I know the answer to any of your questions.')
print('What is your name ?')
name = input()
print('Hello,', name)

def magic(num):
  print('Ask question')
  while True:
    question = input()
    print(answers[num])
    print('Do you want to ask again ?')
    answer = input()
    if answer.lower() == 'yes':
      num = random_num()
      magic(num)
    else:
      print('Have a nice day', name)
      break

num = random_num()
magic(num)
       
       





