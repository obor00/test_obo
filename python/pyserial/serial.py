import serial

devtty="/dev/tty0"

# open post
timeout = 10
sertty = serial.Serial( idevtty, timeout )

sertty.reset_input_buffer()
sertty.reset_output_buffer()

with open ('toto', 'wb') as fp:
    while True:
        wcar = sertty.inWaiting()
        if wcar > 0:
            abuffer = sertty.read( wcar )
            fp.write( abuffer )
        else:
            time.sleep(1/1000.0)

