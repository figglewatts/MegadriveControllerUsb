import serial

upFlag = 0b00000001
downFlag = 0b00000010
leftFlag = 0b00000100
rightFlag = 0b00001000
aFlag = 0b00010000
bFlag = 0b00100000
cFlag = 0b01000000
startFlag = 0b10000000

ser = serial.Serial('COM4', 9600)
name = ser.name
print "Now listening on %s for serial data" % name

while True:
	readByte = ord(ser.read())
	if readByte == upFlag:
		print "UP pressed"
