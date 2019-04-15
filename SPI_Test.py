import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 0b11

try:
    while True:
        resp = spi.readbytes(3)
        if (resp[0] != 255):
            print(resp)
            value = resp[1] + resp[2]
            print(value)
            byte1 = bin(resp[0])[2:].rjust(8,'0')
            byte2 = bin(resp[1])[2:].rjust(8,'0')
            byte3 = bin(resp[2])[2:].rjust(8,'0')
            bits = byte1 + byte2 + byte3
            print(bits)
            time.sleep(0.1)
except KeyboardInterrupt:
    spi.close()