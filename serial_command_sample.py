import serial
import time
import base64
import struct




class SerialQueueB64:
    def __init__(self, on_decode) -> None:
        self.mainstring = b"" 
        self.decoded_string = ""
        self.on_decode = on_decode

    
    def __str__(self) -> str:
        return self.mainstring[::-1]

    def pop3(self):
        """
        get b64 symbols (encoded by ascii) from the first 3 byte
        """
        if (len(self.mainstring) < 3) :
            return
        rid_string = self.mainstring[-3:]
        self.mainstring = self.mainstring[:-3]

        encoded_str = base64.b64encode(rid_string).decode('ascii')
        self.decoded_string += encoded_str[::-1]

        self.on_decode(self.decoded_string);
        print(self.mainstring)
    def push(self, stuff):
        """
        put byte string in the queue
        """
        self.mainstring += stuff[::-1]
        # self.mainstring += stuff


class SerialQueueBIN:
    def __init__(self, on_decode) -> None:
      self.mainstring = b""
      self.decoded_pipe = []
      self.on_decode = on_decode

    
    def __str__(self) -> str:
        return str(self.decoded_pipe)

    def pop(self):
        """
        get symbols (encoded by bit representation) from the mainstring
        """
        if len(self.mainstring) == 0:
            return
        for c in self.mainstring:
            bin_str = bin(c)
            self.decoded_pipe.append(bin_str)

        self.mainstring = b""
        self.on_decode(self.__str__())

    def push(self, stuff):
        """
        put byte string in the queue
        """
        self.mainstring += stuff[::-1]
        # self.mainstring += stuff


    

def base64DecodeFloatDebug(b64) :
    # validation of param, which base64 must have the 6-letter.
    if len(b64) != 6 or type(b64) != type(''):
        return -1
    b64 = b64[::-1]
    b64 = "AA" + b64
    s = bytearray(base64.b64decode(b64)[-4:])
    print(s)
    s.reverse()
    p =  struct.unpack('f', s)
    print(p)



py_serial = serial.Serial(port='COM5', baudrate=9600,)
serial_buffer_queue = SerialQueueB64(on_decode=print)

base64DecodeFloatDebug("7Rhj/A")

# code firing section

# code=b'S[3f8e147b]'
code=b'r'
print(code)

time.sleep(2)
# print("original_code" ,code)
py_serial.write(code)
time.sleep(1) 

# code=b'X'
# print(code)

# time.sleep(2)
# # print("original_code" ,code)
# py_serial.write(code)
# time.sleep(1) 

while True:
    # time.sleep(0.5)
    # put the serial buffer-ed strings in the queue.
    if (py_serial.readable()):
        response = py_serial.read_all()
        serial_buffer_queue.push(response)
    


    ## for b64 queue
    # pop 3 byte inside buffer then convert them to 4 base64 char s.  
    # then save 4 base64 chars to base64 buffer.
    serial_buffer_queue.pop3()

    # ### for bin queue
    # # pop all byte then convert them into the bin form.
    # serial_buffer_queue.pop()
    # print(serial_buffer_queue.decoded_string)


