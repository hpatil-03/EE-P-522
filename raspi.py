import socket
import time
import RPi.GPIO as GPIO
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins as an output and PWM
GPIO.setup(12, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
pwm = GPIO.PWM(12, 50)

# start PWM duty cycle 0
pwm.start(0)

#define all the functions
def dim():
    engine.say("dimming the lights!")
    engine.runAndWait()
    for dc in range(100, -1, -5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.1)

def inc():
    engine.say("brighten the lights!")
    engine.runAndWait()    
    for dc in range(0, 101, 5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.1)
        
def on():
    engine.say("turning on the lights!")
    engine.runAndWait()    
    pwm.ChangeDutyCycle(100)
    time.sleep(2)
    
def off():
    engine.say("turning off the lights!")
    engine.runAndWait()
    pwm.ChangeDutyCycle(0)
    
def blink():
    engine.say("blink mode on")
    engine.runAndWait()    
    start_time = time.time()
    while (time.time() - start_time) < 5:
        pwm.ChangeDutyCycle(100)
        time.sleep(0.3)
        pwm.ChangeDutyCycle(0)
        time.sleep(0.3)
        
def rgb():
    engine.say("RGB on")
    engine.runAndWait()
    start_time = time.time()
    while (time.time() - start_time) < 5:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        time.sleep(0.2)

        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(22, GPIO.LOW)

# Set up the socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific port
server_address = ('', 1234)  
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print('Waiting for connection...')
connection, client_address = sock.accept()


while True:
    # Receive the data from the client
    data = connection.recv(1024)
    if not data:
        break
    print('Received message: {}'.format(data.decode()))
    message = data.decode()


    # check for specific text in the message
    if "inc" ==message:
        inc()
    if "dim"==message:
        dim()
    if "on" ==message:
        on()
    if "off" ==message:
        off()
    if "blink" ==message:
        blink()
    if "rgb" ==message:
        rgb()          
   
