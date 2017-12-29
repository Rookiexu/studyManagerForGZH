class BanJi:
    def __init__(self, name, testName, testNo, pNum, zongfen, manfen, up95, up90, up85, up80, up75, up70, up65, up60,
                 up40, up0, quekao, Students):
        self.name = name #班级名字
        self.testNo = testNo  # 考试编号
        self.testName = testName  # 考试编号
        self.up0 = up0
        self.up40 = up40
        self.up60 = up60
        self.up65 = up65
        self.up70 = up70
        self.up75 = up75
        self.up80 = up80
        self.up85 = up85
        self.up90 = up90
        self.up95 = up95
        self.manfen = manfen
        self.zongfen = zongfen
        self.pNum = pNum
        self.quekao = quekao
        self.Students = Students

    def get_up0(self):
        return self.up0

    def set_up0(self, up0):
        self.up0 = up0

    def get_up40(self):
        return self.up40

    def set_up40(self, up40):
        self.up40 = up40

    def get_up60(self):
        return self.up60

    def set_up60(self, up60):
        self.up60 = up60

    def get_up65(self):
        return self.up65

    def set_up65(self, up65):
        self.up65 = up65

    def get_up70(self):
        return self.up70

    def set_up70(self, up70):
        self.up70 = up70

    def get_up75(self):
        return self.up75

    def set_up75(self, up75):
        self.up75 = up75

    def get_up80(self):
        return self.up80

    def set_up80(self, up80):
        self.up80 = up80

    def get_up85(self):
        return self.up85

    def set_up85(self, up85):
        self.up85 = up85

    def get_up90(self):
        return self.up90

    def set_up90(self, up90):
        self.up90 = up90

    def get_up95(self):
        return self.up95

    def set_up95(self, up95):
        self.up95 = up95

    def get_manfen(self):
        return self.manfen

    def set_manfen(self, manfen):
        self.manfen = manfen

    def set_quekao(self, quekao):
        self.quekao = quekao

    def get_quekao(self):
        return self.quekao

    def set_zongfen(self, zongfen):
        self.zongfen = zongfen

    def get_zongfen(self):
        return self.zongfen

    def get_pNum(self):
        return self.pNum

    def set_pNum(self, pNmu):
        self.pNum = pNmu

    def get_Students(self):
        return self.Students

    def set_Students(self, Students):
        self.Students = Students


class Student:
    def __init__(self, name: str, chengji: float, paiming: int, nianjipaiming: int):
        self.name = name
        self.chengji = chengji
        self.banjipaiming = paiming
        self.nianjipaiming = nianjipaiming

    def getInfo(self,i):
        if (i==0):
            return self.name
        elif (i == 1):
            return self.chengji
        elif (i == 2):
            return self.banjipaiming
        elif (i == 3):
            return self.nianjipaiming

