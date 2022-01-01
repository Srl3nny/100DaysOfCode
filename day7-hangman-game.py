import random

#to clear the screen
from replit import clear

words = ["pen","bird","mouse"]
word = random.choice(words)

size = len(word)

logo = '''
8   8                                          8""""8                    
8   8 eeeee eeeee eeeee eeeeeee eeeee eeeee    8    " eeeee eeeeeee eeee 
8eee8 8   8 8   8 8   8 8  8  8 8   8 8   8    8e     8   8 8  8  8 8    
88  8 8eee8 8e  8 8e    8e 8  8 8eee8 8e  8    88  ee 8eee8 8e 8  8 8eee 
88  8 88  8 88  8 88 "8 88 8  8 88  8 88  8    88   8 88  8 88 8  8 88   
88  8 88  8 88  8 88ee8 88 8  8 88  8 88  8    88eee8 88  8 88 8  8 88ee 

'''

stage = [    
"""    
_______    
  |       |    
  |       0    
  |      [|]    
  |       |     
  |      / \     
============    
""",
"""    
_______    
  |       |    
  |       0    
  |      [|]    
  |       |     
  |        \     
============    
""",
"""    
_______    
  |       |    
  |       0    
  |      [|]    
  |       |     
  |           
============    
""",
"""    
_______    
  |       |    
  |       0    
  |       |]    
  |       |     
  |           
============    
""",
"""    
_______    
  |       |    
  |       0    
  |       |    
  |       |     
  |           
============    
""",
"""    
_______    
  |       |    
  |       0    
  |           
  |            
  |           
============    
""",
"""    
_______    
  |       |    
  |           
  |           
  |            
  |           
============    
"""
]

life = 6
print(logo)
display = []
for i in range(size):
    display +='-'
while True:
    #print(word)
    letter = input("Guess a letter:\n").lower()
    if letter in word:
        for i in range(size):
            if word[i] == letter:
                display[i] = letter
    else:
        life -= 1
    clear()
    if life == 0:
        print(stage[life])
        print("You loose")
        break
    print(stage[life])
    print(display)
    if "-" not in display:
        print("You Win!!")
        break























