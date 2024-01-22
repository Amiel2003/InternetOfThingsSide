import serial
import time

ser = serial.Serial('/dev/ttyS3', baudrate=9600, timeout=1)

number = "+639532511515"  # Change with your number

def send_message():
    ser.write(b'AT+CMGF=1\r\n')
    time.sleep(0.2)
    ser.write(('AT+CMGS="' + number + '"\r\n').encode('utf-8'))
    time.sleep(0.2)
    sms = "Hello, from Ocier's GSM module!"
    ser.write((sms + "\x1A").encode('utf-8'))  # \x1A is ASCII code for CTRL+Z
    time.sleep(0.2)
    print(read_serial())

def read_serial():
    timeout = 0
    while ser.in_waiting == 0 and timeout < 20000:
        time.sleep(0.013)
        timeout += 13
    if ser.in_waiting > 0:
        return ser.read(ser.in_waiting).decode('utf-8')
    else:
        print("No data received from SIM800LV2")
        return None

if __name__ == "__main__":
    ser.flush()
    print("System Started...")
    time.sleep(1)
    print("Sending message")
    send_message()