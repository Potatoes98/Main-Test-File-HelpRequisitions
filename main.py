import os
import time
import math
import random
import sys
from modules.util import *

files = [f for f in os.listdir("people") if os.path.isfile(os.path.join("people", f))]

mainText = []
extraText = []