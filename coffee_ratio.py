#!/usr/bin/env python3
"""
Final Project for Code in Place 2021
Simple coffee ratio calculator to get total brew water weight
"""

__author__ = "Tim Oh"
__version__ = "0.1.0"
__license__ = "MIT"

from colorama import Fore, Back, Style

def main():
  
  # print title message 
  print()
  print(Fore.YELLOW + Style.BRIGHT + 'Simple Cofeee Brew Ratio Calculator ' + '☕️')
  print()

  # take in the input of amount of coffee you will use and store it in a variable.
  while True:
    coffee_ground_weight = float(input(Fore.GREEN + Style.BRIGHT + 'Enter your coffee beans in grams (e.g. if 18g, input 18)' + ' : '))
    calculate_ratio(coffee_ground_weight)

# helper f(x) to take in grams of coffee ground and return the total brew water weight.
def calculate_ratio(coffee_ground_weight):
    
  # variable for taking in the input of ratio you want
  desired_ratio = float(input(Fore.RED + Style.BRIGHT + 'Your ratio (e.g. if (1/15) input 15) *SCA recommends (1/16.7)* : '))
  
  # formula to calculate the total brew water needed
  total = (coffee_ground_weight) / (1/(desired_ratio))
  
  # return the total brew water weight to the function caller from main()
  return print(Fore.CYAN + Style.BRIGHT + 'Your total brew water is 💦 : ' + str('%.2f' %total) + ' grams!\n')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()