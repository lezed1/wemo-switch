from ouimeaux.environment import Environment
from RPi import GPIO


### Configure these VV ###

switch_pin = 27
led_pin = 4
wemo_lamp_name = "Lamp"

### Configure these ^^ ###


try:
    ## WeMo

    def on_switch(switch):
        print("Switch found!", switch.name)

    def on_motion(motion):
        print("Motion found!", motion.name)

    env = Environment(on_switch, on_motion)
    env.start()
    env.discover(seconds=5)

    lamp_wemo_switch = env.get_switch(wemo_lamp_name)
    lamp_wemo_switch.set_state(True)


    ## GPIO

    state = False

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(led_pin, GPIO.OUT)


    ## Puttin it together!

    def switch_handler(channel):
        global state
        lamp_wemo_switch.set_state(state)
        state = not state
        GPIO.output(led_pin, state)
        print("Got button press! (on channel {})".format(channel))


    GPIO.add_event_detect(switch_pin, GPIO.RISING, callback=switch_handler, bouncetime=750)


    input("Ready to go! Press enter to end")

finally:
    GPIO.cleanup()
