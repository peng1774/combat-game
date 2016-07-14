import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
  def setup(self):
    self.player = Character()
    self.monsters = [
      Goblin(),
      Troll(),
      Dragon()
    ]
    self.monster = self.get_next_monster()
    
  def get_next_monster(self):
    try:
      return self.monsters.pop(0)
    except IndexError:
      return None
    
  def player_get_hit(self):
    self.player.hit_points -= 1
  def monster_get_hit(self):
    self.monster.hit_points -= 1
    
  def monster_turn(self):
    if self.monster.attack():
      print('{} attacks you!'.format(self.monster))
      if input('dodge? Y/N  > ').lower() == 'y':
        if self.player.dodge():
          print('dodge succssed')
        else:
          print('you got hit!')
          self.player_get_hit()
      else:
        print('{} hit you for 1 point'.format(self.monster))
        self.player_get_hit() 
    else: 
      print('{} is not attacking this turn.'.format(self.monster))
      
      
  def player_turn(self):
    player_choice = input('[A]attack [R]rest [Q]quit? > ').lower()
    if player_choice == 'a':
      print('you are attacking!')
      if self.player.attack():
        if self.monster.dodge():
          print('{} has dodged your attack.'.format(self.monster))
        else:
          if self.player.leveled_up():
            self.monster.hit_points -= 2
            print('you hit it 2 points!')
          else:
            self.monster.hit_points -= 1   
            print('you hit it 1 point!')
      else:
        print('you missed!')
    # if they rest:
    elif player_choice == 'r':
      self.player.rest()     
    elif player_choice == 'q':
      print('bye bye')
      sys.exit()
    else:
      print('invalid input, try again.')
      self.player_turn()
    
  def cleanup(self):
    if self.monster.hit_points <= 0:
      self.player.experience += self.monster.experience
      print('you have taken downn {}, and got {} exp.'.format(self.monster,self.monster.experience))
      self.monster = self.get_next_monster()
      
  def __init__(self):
    self.setup()
    
    while self.player.hit_points and (self.monster or self.monsters):
      print('='*20 )
      print(self.player)
      self.monster_turn()
      print('-'*20)
      self.player_turn()
      print('-'*20)
      self.cleanup()
      #print('\n' +'='*20)
      
    if self.player.hit_points:
      print("You win!")
    elif self.monsters or self.monster:
      print("You lose!")
    sys.exit()
    
    
Game()