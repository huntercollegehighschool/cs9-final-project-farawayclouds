"""
Name(s):Fara Hameed
Name of Project:
"""
import time
time.sleep(1)
print("Hello, player.")
time.sleep(1)
name = input("What is your character's name? ")
time.sleep(.5)
print("Welcome to the kingdom of Brophowyth, Your Majesty", name)
time.sleep(2)
print("Your Majesty, your kingdom is in shambles. Your father King Luther stole from his people and our treasury and spent all our money on useless wine and women. The kingdom is deep in debt and the people are unhappy with the high taxes. The upper class hates you and your father for greedily hoarding your wealth. We are doomed unless you can perform miracles.")
time.sleep(8)
print("A messenger runs down the corridor to where you sit in the throne room.")
time.sleep(2)
print("'Your Majesty! There is big trouble!'")
time.sleep(2)
print("'Our neighboring kingdoms are asking you to pay up all the Brophowythian debts your father created, but we have no money! What should we do?'")
time.sleep(3)
r1 = input("What should you do? type a to raise taxes, type b to order your army to beat up the neighboring kingdom ")

if "a" in r1:
  print("You decide to raise taxes to raise enough money. However, you fear the retaliation of the public.") 
  import page1
elif "b" in r1:
  print("You decide to gather your army and have them attack your neigbors, hoping that they will cancel your debts. A couple of days later, you recieve news that your army has been crushed, and the enemy has declared war; they are approaching rapidly.")
  import page2
else: 
  print("You didn't follow the rules. Start over.")