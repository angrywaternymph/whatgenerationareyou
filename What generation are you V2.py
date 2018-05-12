
# coding: utf-8

# In[ ]:


counter = 0

while (counter <= 20) == True:
    age = int(input("Enter your age in this space: "))
    type(age)
    print("You are", age, "years old.")
    if age < 0:  # nonexistant
        print("Oh, fuck off.")
    elif 0 <= age <= 6:
        print("You're too young to be using the internet.  Also, Google Pornhub.")
    elif 7 <= age <= 23:  # Generation Z
        print("Generation Z. Get off my lawn!")
    elif 24 <= age <= 41:  # Generation Y / Millenials
        print("Millenials: The greatest generation!  Now where's my vape pen...")
    elif 42 <= age <= 52:  # Generation X
        print("Generation X: You assholes willed Ready Player One into existence.")
    elif 52 <= age <= 72:  # Baby Boomers
        print("Baby Boomers: You are everything I hate about this country.")
    else:  # pre-boomers    
        print("Eh.  Roasting the elderly isn't much fun.  Glad you made it this far!")
    counter = counter + 1
    if counter <= 20:
        continue
    if counter > 20:
        break
        
else:
    age = int(input("Enter your age in this space: "))    
    type(age)
    print("Nah, I'm done.")

