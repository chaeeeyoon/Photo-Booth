from flask import Flask, render_template
import RPi.GPIO as GPIO
import time 
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)
buzzer_pin = 4

pwm = GPIO.PWM(buzzer_pin,262)

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("main.html")

@app.route("/melody")
def play():
    t = threading.Thread(target=sound)
    t.start()
    return render_template("index.html")
    
def sound():
    melody = [262, 294, 330, 330, 349, 330, 294]
    melodytwo = [294, 330, 349, 349, 392, 349, 330]
    melodythree = [330, 349, 392, 392, 523, 440, 392, 330]
    melodyfour = [262, 294, 330, 330, 294, 262]    
    try:
        for i in melody:
            pwm.ChangeFrequency(i)
            time.sleep(0.3)
        time.sleep(1)
        for j in melodytwo:
            pwm.ChangeFrequency(j)
            time.sleep(0.3)
        time.sleep(1)
        for k in melodythree:
            pwm.ChangeFrequency(k)
            time.sleep(0.3)
        time.sleep(0.5)
        for l in melodyfour:
            pwm.ChangeFrequency(l)
            time.sleep(0.3)
    finally:
        pwm.stop()
        GPIO.cleanup()
    



if __name__=="__main__":
    app.run(host="0.0.0.0")

