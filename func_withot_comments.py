import serial.tools.list_ports
import serial
import time

def write_read(x, port, baudrate):
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=0.1)
        time.sleep(2)  # заменить значение на 5, если используется ESP
        ser.write(bytes(x, 'utf-8'))
        #time.sleep(2) раскомнтировать если используется ESP
        data = ser.readline()
        ser.close()
        return data.decode('utf-8')
    
    except Exception as e:
        print(f"Error in communication: {e}")
        return None

def search_corect_port(baudrate):
    ports = serial.tools.list_ports.comports()
    correct_ports = []

    for port, desc, hwid in sorted(ports):
        if "USB-SERIAL CH340" in desc or "USB Serial Port" in desc:
            try:
                response = write_read('5', port, baudrate)
                if response == '6':
                    correct_ports.append(port)
            except serial.SerialException as e:
                print(f"Failed to connect to port {port}: {e}")
    
    if len(correct_ports) != 0:
        return correct_ports
    else:
        return None

print(search_corect_port(9600))