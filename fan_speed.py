#!/usr/bin/python3
#coding:utf8
# Auto fan control
# AutoFanControl_PNP.service


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    # Get CPU temperature
    with open('/sys/class/thermal/thermal_zone0/temp') as tmpFile:
        cpu_temp_raw = tmpFile.read()

    cpu_temp = round(float(cpu_temp_raw) / 1000, 1)
    print(cpu_temp)

    if cpu_temp > 40:
        GPIO.setup(18, GPIO.OUT)
        print('TRUN ON :',cpu_temp)
        
    elif cpu_temp < 35:
        time.sleep(20)
        GPIO.setup(18, GPIO.IN)
        print('TRUN OFF :',cpu_temp)

    time.sleep(5)

GPIO.cleanup()

