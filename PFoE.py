#coding:utf-8

class PFoE:
    def likelihood(self, sensorA, sensorB):

    def setEvent(self,sensor,action):

    def writeData(self):

    def addData(self):

    def readData(self):

    def getAction(self,Sensor):

if __name__=='__main__':
    test = PFoE()
    """in case of teaching"""
    while(True):
        test.setEvent([1,1,0,0],0)

    test.writeData('data1')
    #test.addData('data1')

    """in case of replay"""
    test.readData('data1')
    while(True):
        test.setEvent([1,0,0,1],0)
        a = test.getAction()
