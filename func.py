import serial.tools.list_ports
import serial
import time


# Вспомогательная функция для отправки и чтения данных
def write_read(x, port,baudrate):
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=0.1)
        time.sleep(2)#заменить значение на 5, если используется ESP
        ser.write(bytes(x, 'utf-8'))  # Отправляем данные
        ##time.sleep(2) раскомнтировать если используется ESP
        data = ser.readline()  # Читаем ответ
        ser.close()
        return data.decode('utf-8')  # Декодируем и убираем лишние пробелы
    
    except Exception as e:
        print(f"Error in communication: {e}")
        return None

# Поиск порта с Arduino 
def search_corect_port(baudrate):
    ports = serial.tools.list_ports.comports()
    correct_ports = []

    for port, desc, hwid in sorted(ports):
        if "USB-SERIAL CH340" in desc or "USB Serial Port" in desc:  # Ищем порт с CH340 или USB Serial Port в случае ESP
            #print(f"Checking port: {port}")
            try:
                # Подключение к Arduino
                #print(f"Connected to Arduino on port: {port}")
                # Отправляем '5' и проверяем ответ
                response = write_read('5', port,baudrate)
                if response == '6':  # Проверяем, что ответ равен '6'
                    #print(f"Correct Arduino found on port: {port}")
                    correct_ports.append(port) # Сохраняем правильный порт в список
                      # Выходим из цикла, так как правильный порт найден
            except serial.SerialException as e:
                print(f"Failed to connect to port {port}: {e}")
    # Результат поиска
    if len(correct_ports)!=0:
        return correct_ports
    else:
        return None

print(search_corect_port(9600)) # не перепутать скорость 