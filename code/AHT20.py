from machine import I2C 
from utime import sleep_ms
from usr import EventMesh

class aht20(object):
    def __init__(self):
        self.i2c = I2C(I2C.I2C1,I2C.STANDARD_MODE)
        self.slave_addr = 0x38# AHT20 slave address
        self.RESET_CMD = b'\xBA'# reset command
        self.INIT_CMD = b'\xE1'# initialize command
        self.MEASURE_CMD = b'\xAC\x33\x00'# measure command

    def reset(self):
        self.i2c.write(self.slave_addr,b'\x00',0,self.RESET_CMD,len(self.RESET_CMD))
        sleep_ms(20)# wait 20ms

    def init(self):#initialize aht20
        self.i2c.write(self.slave_addr,b'\x00',0,self.INIT_CMD,len(self.INIT_CMD))

    def read(self):
        # Send measurement cmd to trigger data acquirement.
        self.i2c.write(self.slave_addr,b'\x00',0,self.MEASURE_CMD,len(self.MEASURE_CMD))

        #read data
        #wait for data ready (at least 80ms)
        sleep_ms(80)
        r_data = bytearray([0x00]*6)
        self.i2c.read(self.slave_addr,b'\x00',0,r_data,6,80)
        busy = 0#r_data[0]>>7
        if not busy:
            RH_reg_data = (r_data[1]<<12) | (r_data[2]<<4) | (r_data[3]>>4)
            RH = RH_reg_data/(1<<20) * 100

            temp_reg_data = ((r_data[3]&0x0F)<<16) | (r_data[4]<<8) | r_data[5]
            temp = temp_reg_data/(1<<20) * 200 - 50

            return RH,temp
        else:
            return ()

def update_temphumi(args):
    aht20_obj = aht20()
    aht20_obj.init()
    sleep_ms(1000)
    #while True:
    res = aht20_obj.read()
    if res:
        #print("RH: %.2f%%" % res[0])
        #print("Temp: %.2f" % res[1])
        #print("------------")
        EventMesh.publish("update_monitordate",res)
        EventMesh.publish("update_main_screen_date",res)
        return res
    else:
        print("aht20 read error")
        return (0,0)
    #sleep_ms(1000)