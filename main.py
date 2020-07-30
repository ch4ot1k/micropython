import utime
from machine import Pin, PWM, Timer


def main():
	led = Pin(10, Pin.OUT)
	servo = PWM(Pin(5), freq=50)
	# servo = Pin(4, mode = Pin.OUT)
	# pwm = Timer(1, freq=40)
	# pwm_ch = pwm.channel(1,mode=Timer.PWM,freq = 40, duty_cycle=3000)
	# pwm_ch.period(2000000)
	switch = False
	#
	# def tick(timer):
	# 	global switch, led
	#
	# 	if switch:
	# 		pwm.duty_cycle(3000)
	# 		led.on()
	# 	else:
	# 		pwm.duty_cycle(5000)
	# 		led.on()
	# 	switch = not switch
	#
	# pwm_ch.irq(handler = tick, trigger = Timer.TIMEOUT)
	while True:
		if switch:
			servo.duty(40)
			led.off()
		else:
			led.on()
			servo.duty(115)
		utime.sleep_ms(1000)
		switch = not switch

if __name__ == '__main__':
	main()

# from ota_update.main.ota_updater import OTAUpdater
#
#
# def download_and_install_update_if_available():
# 	o = OTAUpdater('https://github.com/ch4ot1k/micropython')
# 	o.download_and_install_update_if_available('Veltkamp-5G', 'veltkamper')
#
#
# def start():
#
# 	from main.flash_led import main
#
# 	main()
#
# def boot():
# 	download_and_install_update_if_available()
# 	start()
#
# boot()