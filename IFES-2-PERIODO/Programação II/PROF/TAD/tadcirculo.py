import math

# CONSTRUTOR: É POSSÍVEL TER MAIS DE UM CONSTRUTOR.
def criar(r,x,y):
  dic = {"raio":r,"cx":x,"cy":y}
  return dic

def criar_origem(r):
  dic = {"raio":r,"cx":0,"cy":0}
  return dic  

# ANALISADORAS
def getraio(circ):
  return circ["raio"]

def getx(circ):
  return circ["cx"]

def gety(circ):
  return circ["cy"]  

# MODIFICADORAS
def setraio(circ,novoraio):
  circ["raio"] = novoraio

def setx(circ,novox):
  circ["cx"] = novox

def sety(circ,novoy):
  circ["cy"] = novoy

def getarea(circ):
  return math.pi * circ["raio"]**2

def getperimetro(circ):
  return 2 * math.pi * circ["raio"]