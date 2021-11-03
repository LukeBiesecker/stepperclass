import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ] #sequence of steps to make one full rotation.
        
state = 0 #current position in the stator sequence
class Stepper:
  def __init__(self, angle, zero):
    self.angle = angle
    self.zero = zero
    

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  #dir = +/-1(cww/cw)
  global state
  for hstep in range(8):
    state += dir
    if state >7: state = 0
    elif state<0: state = 7
    for pin in range(4):    # 4 pins that need to be energized
      GPIO.output(pins[pin], sequence[state][pin])
    delay_us(1000)

def movesteps(steps, dir):
  #move the actuation sequence a given number of half steps
  for step in steps:
    halfstep(dir)
def goangle(steps, dir):
  movesteps

#need a variable for the current angle 
#need to make his whole thing a class so that i can instantiate it in the main code

try:
  movesteps(1000,1)
except:
  pass
GPIO.cleanup() 
#512 steps in a rotation so resolution is 360/512