# Package

# Its used to organize modules. 

# __init__.py file contains all imports of modules
# from Vodafone import Vodafone 



# Vodafone.py is simple python file under Phone folder
# Like we can add different phones with py file


# to execute import Vodafone for that you need to append the folder path
import sys
sys.path.append('...\Phone')
sys.path

import Phone # this time it will add the .pyc files for all the py files (compiled files)
Phone.Vodafone


