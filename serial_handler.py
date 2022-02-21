import serial


class SerialHandler:
    def __init__(self, port, baudrate=115200):
        self.port = serial.Serial()
        self.port.port = port
        self.port.baudrate = 115200
        self.port.timeout = 0

    def open(self):
        self.port.open()
        return self.port.is_open

    def close(self):
        self.port.close()
        return not self.port.is_open

    def write(self, msg):
        self.port.write(msg)

    def read(self, num_bytes=256):
        return self.port.read(num_bytes)
