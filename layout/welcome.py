# -*- coding: utf-8 -*-
"""
Welcome module

this module can be called from main to show a welcome when the app is launched.

Created on Thu Oct 23 15:55:48 2025

@author: thomas brockmans
"""


def display_welcome():
    
    bike_art = r"""
    __o
  _`\<,_
 (*)/ (*)
    """
    
    welcome_message = "VELOG. bike ride logging application"
    
    print(bike_art)
    print(welcome_message)
    print()
    

if __name__ == '__main__':
    display_welcome()