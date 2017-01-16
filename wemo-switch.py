import RPi.GPIO as GPIO


## Configure these VV ##

switch_pin = 27
led_pin = 4

## Configure these ^^ ##


state = False

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

def switch_handler(channel):
    global state
    state = not state
    GPIO.output(led_pin, state)
    print("Got button press! (on channel {})".format(channel))


GPIO.add_event_detect(switch_pin, GPIO.RISING, callback=switch_handler, bouncetime=750)

input("Press enter to end")

GPIO.cleanup()
