#pip install pyqrcode
#pip install pypng

import time
import pyqrcode
import png
from pyqrcode import QRCode


def Menu():
    print("QR Code Generator App")
    s = input("Please enter your URL: ") #Hold the URL as a string
    url = pyqrcode.create(s) #Store the QR code
    url.png(s+".png", scale=6) #Create & save the file as a png
    print("QR Code has been saved as " + s + ".png")
    print("Thank you for using our app!")
    time.sleep(2)
    quit()

Menu()