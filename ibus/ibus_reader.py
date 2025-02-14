import serial  # type: ignore

class ibus_reader:
    def __init__(self, port='/dev/ttyAMA0', baudrate=115200):
        self.ser = serial.Serial(port, baudrate)
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        # Initialize attributes
        self.linear_x = 0.0
        self.linear_y = 0.0
        self.yellow_sw = 0
        self.red_sw = 0
        self.long_sw = 0

    def read_channel(self, frame, start_index):
        return int.from_bytes(frame[start_index:start_index+2], byteorder='little')

    def read_serial_data(self):
        frame = bytearray()
        received_data = self.ser.read()
        int_received = int.from_bytes(received_data, byteorder='little')

        if int_received == 32:  # Header byte
            frame.extend(received_data)
            frame.extend(self.ser.read(31))  # Read the rest of the frame

            self.linear_y = self.read_channel(frame, 2)
            self.linear_x = self.read_channel(frame, 6)
            self.yellow_sw = self.read_channel(frame, 10)
            self.red_sw = self.read_channel(frame, 12)
            self.long_sw = self.read_channel(frame, 14)
    
    def system_troubleshoot(self):
        print(f'linear_y:{self.linear_y} linear_x: {self.linear_x} yellow_sw: {self.yellow_sw} red_sw: {self.red_sw} long_sw: {self.long_sw}')