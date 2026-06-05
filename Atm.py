import os
import json
from System_atm import System

class Atm(System):
  def atm(self):
    inputMenu=self.headAtm()
    if (inputMenu==1):
      self.login()
    elif (inputMenu==2):
      self.daftar()
    elif (inputMenu==3):
      print('Exit')
      print('TERIMAKASIH')
    else:
      print("MENU TIDAK TERSEDIA")
    
os.system('clear')
start = Atm()
start.atm()
