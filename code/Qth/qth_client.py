import net
from usr import Qth


QTH_PRODUCT_KEY = "pe16Em"
QTH_PRODUCT_SECRET = "YVpLelJORnVnTjRB"


class QthClient(object):

    def __init__(self, pk=QTH_PRODUCT_KEY, ps=QTH_PRODUCT_SECRET):
        Qth.init()
        Qth.setProductInfo(pk, ps)
        Qth.setServer('mqtt://iot-south.quecteleu.com:1883')
        Qth.setEventCb(
            {
                "devEvent": self.eventCallback, 
                "recvTrans": self.recvTransCallback, 
                "recvTsl": self.recvTslCallback, 
                "readTsl": self.readTslCallback, 
                "readTslServer": self.recvTslServerCallback,
                "ota": {
                    "otaPlan":self.otaPlanCallback,
                    "fotaResult":self.fotaResultCallback
                }
            }
        )

    def start(self):
        Qth.start()
    
    def stop(self):
        Qth.stop()
    
    def sendTsl(self, mode, value):
        return Qth.sendTsl(mode, value)

    def isStatusOk(self):
        return Qth.state()
    
    def sendLbs():
        cell_info = -1
        cell_info = net.getCellInfo()
        if cell_info != -1 and cell_info[2]:
            first_tuple = cell_info[2]
            lbs_data = "$LBS,{},{},{},{},{},0*69;".format(first_tuple[0][2],first_tuple[0][3],first_tuple[0][5],first_tuple[0][1],first_tuple[0][7])
            Qth.sendOutsideLocation(lbs_data)

    def eventCallback(self, event, result):
        print("dev event:{} result:{}".format(event, result))
        if(2== event and 0 == result):
            Qth.otaRequest()

    def recvTransCallback(self, value):
        ret = Qth.sendTrans(1, value)
        print("recvTrans value:{} ret:{}".format(value, ret))

    def recvTslCallback(self, value):
        print("recvTsl:{}".format(value))
        for cmdId, val in value.items():
            print("recvTsl {}:{}".format(cmdId, val))
    def readTslCallback(self, ids, pkgId):
        print("readTsl ids:{} pkgId:{}".format(ids, pkgId))
        value=dict()
        for id in ids:
            if 1 == id:
                value[1]=180.25
            elif 2 == id:
                value[2]=30
            elif 3 == id:
                value[3]=True
        Qth.ackTsl(1, value, pkgId)

    def recvTslServerCallback(self, serverId, value, pkgId):
        print("recvTslServer serverId:{} value:{} pkgId:{}".format(serverId, value, pkgId))
        Qth.ackTslServer(1, serverId, value, pkgId)

    def otaPlanCallback(self, plans):
        print("otaPlan:{}".format(plans))
        Qth.otaAction(1)

    def fotaResultCallback(self, comp_no, result):
        print("fotaResult comp_no:{} result:{}".format(comp_no, result))
        
    def sotaInfoCallback(self, comp_no, version, url, md5, crc):
        print("sotaInfo comp_no:{} version:{} url:{} md5:{} crc:{}".format(comp_no, version, url, md5, crc))
        # 当使用url下载固件完成，且MCU更新完毕后，需要获取MCU最新的版本信息，并通过setMcuVer进行更新
        Qth.setMcuVer("MCU1", "V1.0.0", self.sotaInfoCallback, self.sotaResultCallback)

    def sotaResultCallback(comp_no, result):
        print("sotaResult comp_no:{} result:{}".format(comp_no, result))
