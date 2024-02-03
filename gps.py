import serial
import pynmea2

def read_gps_data(serial_port):
    try:
        with serial.Serial(serial_port, 9600, timeout=1) as ser:
            while True:
                data = ser.readline().decode('utf-8')
                if data.startswith('$GPGGA'):
                    msg = pynmea2.parse(data)
                    print(f'Latitude: {msg.latitude}  Longitude: {msg.longitude}')
    except KeyboardInterrupt:
        print("Exiting GPS reader")

if __name__ == "__main__":
    serial_port = '/dev/ttyS3'  # Use '/dev/ttyAMA0' if not working with '/dev/ttyS0'
    read_gps_data(serial_port)