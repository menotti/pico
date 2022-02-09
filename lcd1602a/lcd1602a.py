import machine
import utime

def pulseE():
    e.value(1)
    utime.sleep_us(40)
    e.value(0)
    utime.sleep_us(40)
    
def longDelay(t):
    utime.sleep_ms(t)
    
def shortDelay(t):
    utime.sleep_us(t)
    
def send2LCD4(BinNum):
    d4.value((BinNum & 0b00000001)>>0)
    d5.value((BinNum & 0b00000010)>>1)
    d6.value((BinNum & 0b00000100)>>2)
    d7.value((BinNum & 0b00001000)>>3)
    pulseE()
    
def send2LCD8(BinNum):
    send2LCD4(BinNum>>4)
    send2LCD4(BinNum)
    
def setCursor(line, pos):
    b = 0
    if line==1:
        b=0
    elif line==2:
        b=40
    returnHome()
    for i in range(0, b+pos):
        moveCursorRight()
        
def returnHome():
    rs.value(0)
    send2LCD8(0b00000010)
    rs.value(1)
    longDelay(2)
    
def moveCursorRight():
    rs.value(0)
    send2LCD8(0b00010100)
    rs.value(1)
    
def setupLCD():
    global rs, e, d4, d5, d6, d7
    rs = machine.Pin(16, machine.Pin.OUT)
    e  = machine.Pin(17, machine.Pin.OUT)
    d4 = machine.Pin(18, machine.Pin.OUT)
    d5 = machine.Pin(19, machine.Pin.OUT)
    d6 = machine.Pin(20, machine.Pin.OUT)
    d7 = machine.Pin(21, machine.Pin.OUT)
    rs.value(0)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0010)
    send2LCD8(0b00101000)
    send2LCD8(0b00001100)
    send2LCD8(0b00000110)
    send2LCD8(0b00000001)
    longDelay(2)
    rs.value(1)
    
def displayString(row, col, input_string):
    setCursor(row,col)
    for x in input_string:
        send2LCD8(ord(x))
        utime.sleep_ms(100)

setupLCD()
displayString(1 ,0, "Hello World!")
displayString(2, 0, "Raspberry # Pico")