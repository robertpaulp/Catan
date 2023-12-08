import math
import pygame
import random
import sys
import numpy as np

sys.path.append("../../")

from constants import *

# --- Card class ---
class Card:
	def __init__(self):
		self.resource = None