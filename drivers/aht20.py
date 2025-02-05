import utime
from machine import I2C


class I2CInterface(object):

    class I2CReadError(Exception):
        pass

    class I2CWriteError(Exception):
        pass

    def __init__(self, i2c, slaveaddr):
        if not isinstance(i2c, I2C):
            raise TypeError('`i2c` should be machine.I2C type')
        self.__i2c = i2c
        self.__slaveaddr = slaveaddr

    def read(self, addr, size=1, delay=0):
        """读寄存器

        :param addr: I2C 寄存器地址（bytes or bytearray）。
        :param size: 读取的字节长度。
        :param delay: 延时，数据转换缓冲时间(单位ms)，int类型。
        :return:
        """
        if size <= 0:
            raise ValueError('`size` should be greater than 0')
        data = bytearray(size)
        if self.__i2c.read(self.__slaveaddr, addr, len(addr), data, size, delay) != 0:
            raise self.I2CReadError("slave 0x{:X} read failed".format(self.__slaveaddr))
        return data

    def write(self, addr, data):
        """写寄存器

        :param addr: I2C 寄存器地址（bytes or bytearray）。
        :param data: 写入的数据，bytearray or bytes类型
        :return:
        """
        if not isinstance(data, (bytearray, bytes)):
            raise TypeError('`data` should be bytearray or bytes')
        if self.__i2c.write(self.__slaveaddr, addr, len(addr), data, len(data)) != 0:
            raise self.I2CWriteError("slave 0x{:X} write failed".format(self.__slaveaddr))


AHT20_CALIBRATION_CMD       = b"\xE1"   # Initialization command
AHT20_START_MEASURMENT_CMD  = b"\xAC"   # Trigger measurement
AHT20_RESET_CMD             = b"\xBA"   # reset
AHT20_STATUS_CMD            = b"\x71"    # get status byte


class Aht20(I2CInterface):

    def __init__(self, i2c, slaveaddr=0x38):
        super().__init__(i2c, slaveaddr)

    def getStatus(self):
        return self.read(AHT20_STATUS_CMD, 1)[0]

    def init(self):
        self.write(AHT20_CALIBRATION_CMD, b"\x08\x00")
        utime.sleep_ms(10)

    def reset(self):
        self.write(AHT20_RESET_CMD, b'')
        utime.sleep_ms(20)  # at last 20ms

    def trigger_measure(self):
        self.write(AHT20_START_MEASURMENT_CMD, b"\x33\x00")
        utime.sleep_ms(80)  # at last delay 80ms
        r_data = self.read(b'', size=6)
        if r_data[0] & (1 << 7):
            print("Conversion has error")
            return None
        data = r_data[1:6]
        humidity = (data[0] << 12) | (data[1] << 4) | ((data[2] & 0xF0) >> 4)
        humidity = (humidity / (1 << 20)) * 100.0
        temperature = ((data[2] & 0xf) << 16) | (data[3] << 8) | data[4]
        temperature = (temperature * 200.0 / (1 << 20)) - 50
        return humidity, temperature
