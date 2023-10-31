import random
from art import logo, vs
from game_data import data
from replit import clear

def format_game_data(account):
  """Takes the account data and returns a printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Use an if statement to check if the user guess is correct."""""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_game_data(account_a)}")
  print(vs)
  print(f"Against B: {format_game_data(account_b)}")
  
  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_answer_correct = check_answer(user_guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  
  if is_answer_correct:
    score += 1
    print(f"You're right! Your current score is: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score is: {score}")

