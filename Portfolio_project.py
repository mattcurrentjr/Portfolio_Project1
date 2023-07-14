#This is my first portfolio project. I want to make an Pokemon style battle game where only 2 players get to play. 
#They have a choice of 3 different weapons. Each weapon will have a weight and a power rating. 
#Weight affects how often you get to attack and power affects how much damage you do to the opponent
#I want both players to start at 100HP and lose HP based on random chance and on which weapon they chose.
#I want all three weapon options to be fair choices, with one not being more overpowered than the other. This will not be a rock, paper, scissors style game.
#I want to import the random module to have random chance involved.
#A higher power weapon typically does more damage, but takes longer to fire (heavier and reloading)
#A lighter weapon does less damage, but you tend to get more chances to shoot. There is also a chance to miss the target completely.
#The user's only input is picking their name and their weapon. The rest is chance.

import random

class Weapon:
  def __init__(self, name, type1, weight, speed):
    self.name = name
    self.type1 = type1
    self.weight = weight
    self.speed = speed

  def __repr__(self):
    if self.weight > 50:
      return "You are viewing the {name}; it's a {type1} weapon that is in the heavy weapons category with lots of firepower, but slower speed.".format(name=self.name, type1=self.type1)
    else:
      return "You are viewing the {name}; it's a {type1} weapon that is in the light weapons category with less firepower, but allows more movement for your character.".format(name=self.name, type1=self.type1)

class Player:

  def __init__(self, name, health, score, weapon, catchphrase):
    self.name = name
    self.score = score
    self.health = health
    self.catchphrase = catchphrase
    self.weapon = weapon

  def __repr__(self):
    return "{catchphrase}! My name is {name} and I'm ready to win!".format(catchphrase=self.catchphrase, name=self.name)

  # def select_weapon(self):
  #   selection = input("Welcome to weapon selection. You can pick a Tommy Gun [1] or a Gatling Gun[2]. Press 1 or 2 for your selection..")
  #   self.weapon = selection

  def gain_health(self, amount):
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health
    print("{name} now has {health} health.".format(name = self.name,health = self.health))

  def lose_health(self, amount):
        self.health -= amount
        # print("{name} now has {health} health.".format(name = self.name, health = self.health))
  
  def attack(self, other_player):
    if self.weapon == tommy_gun:
      damage_check = 5
      print("{self} attacked {other_player} for {damage} damage!".format(self=self.name, other_player = other_player.name, damage = damage_check))
      print('')
      other_player.lose_health(damage_check)
    if self.weapon == gatling_gun:
      damage_check = 10
      print("{self} attacked {other_player} for {damage} damage!".format(self=self.name, other_player = other_player.name, damage = damage_check))
      print('')
      other_player.lose_health(damage_check)
    if self.weapon == twelve_shotgun:
      damage_check = 7
      print("{self} attacked {other_player} for {damage} damage!".format(self=self.name, other_player = other_player.name, damage = damage_check))
      print('')
      other_player.lose_health(damage_check)

#--------------------------------------------------------------------------------
# #Actual user interaction beginning

player_one_name = input("what is Player One's name? ")
player_two_name = input("what is Player Two's name? ")


tommy_gun = Weapon('Tommy Gun', 'machine gun', 20, 80)
gatling_gun = Weapon('Gatling Gun', 'Heavy Laser Weapon', 80, 20)
twelve_shotgun = Weapon('12 Gauge Shotgun', 'shotgun', 45, 50 )


player_one_weapon = input("Which weapon do you want? Your choices are Tommy Gun [1], Gatling Gun [2], or a 12 Gauge Shotgun[3]: ")
player_two_weapon = input("Which weapon do you want? Your choices are Tommy Gun [1], Gatling Gun [2], or a 12 Gauge Shotgun[3]: ")

# weapons = [tommy_gun, gatling_gun]

if player_one_weapon == '1':
  player_one_weapon = tommy_gun
elif player_one_weapon == '2':
  player_one_weapon = gatling_gun
elif player_one_weapon == '3':
  player_one_weapon = twelve_shotgun
else:
  print('Looks like you didn\'t hit the 1, 2, or 3 keys!')

if player_two_weapon == '1':
  player_two_weapon = tommy_gun
elif player_two_weapon == '2':
  player_two_weapon = gatling_gun
elif player_two_weapon == '3':
  player_two_weapon = twelve_shotgun
else:
  print('Looks like you didn\'t hit the 1, 2, or 3 keys!')

Player1 = Player(player_one_name, 100, 0, player_one_weapon, "Let's goooooo")
print(Player1)
input('enter to continue')
Player2 = Player(player_two_name, 100, 0, player_two_weapon,"Huahhhh")
print(Player2)
input('enter to continue')

#possible future state to pick weapons using OOP
# matt_weapon = Player1.select_weapon()
# joe_weapon = Player2.select_weapon()

#'random' calculations for missing shots as well as damage ratios
chance = random.randint(0,100)

while Player1.health >0 and Player2.health > 0:
  print(Player1.name + 's health is: '+ str(Player1.health))
  print(Player2.name + 's health is: '+ str(Player2.health))
  print('')
  input('Press enter when '+ Player1.name + ' is ready to attack!')
  print('')
  chance = random.randint(0,100)
  if chance < 20:
    print(Player1.name + ' missed ' + Player2.name + '!!')
    print('!!!!!!')
    print('!!!!!!')
  else:
    Player1.attack(Player2)
  if Player1.health <=0:
    print(Player1.name + ' has died!')
    print(Player2.name+ ' is the winner!!')
    break
  if Player2.health <=0:
    print(Player2.name + ' has died!')
    print(Player1.name + ' is the winner!!')
    break
  print(Player1.name + 's health is: '+ str(Player1.health))
  print(Player2.name + 's health is: '+ str(Player2.health))
  print('')
  input('Press enter when '+ Player2.name + ' is ready to attack!')
  print('')
  if chance < 20:
    print(Player2.name + ' missed ' + Player1.name + '!!')
    print('!!!!!!')
    print('!!!!!!')
  else:
    Player2.attack(Player1)
  if Player1.health <=0:
    print(Player1.name + ' has died!')
    print(Player2.name+ ' is the winner!!')
    break
  if Player2.health <=0:
    print(Player2.name + ' has died!')
    print(Player1.name + ' is the winner!!')
    break



