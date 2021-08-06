# handle ModuleNotFoundError: no module named 'bitwise' -> have to add to PYTHONPATH
import os 
import sys

working_dir = os.getcwd()
sys.path.append(working_dir)