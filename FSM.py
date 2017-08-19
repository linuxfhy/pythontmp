# FSM: Finite State Machine
FSM_TRANS_TABLE = [
    {'trigger': 'to_shuijiao', 'source': 'chifan', 'dest': 'shuijiao' },
    {'trigger': 'to_dadoudou', 'source': 'shuijiao', 'dest': 'dadoudou'},
    {'trigger': 'to_chifan', 'source': 'dadoudou', 'dest': 'chifan'}]

class FsmStateTrans:
    def __init__(self, srcstate, desstate):
        self.srcstate = srcstate #源状态
        self.desstate = desstate #目标状态
class FsmState:
    def __init__(self, name):
        self.name = name
        self.trans = []
    def add_trans(self, trans): #funciton for add trans
        self.trans.append(trans)

statelist = []
for trans in FSM_TRANS_TABLE:
    transcase = FsmStateTrans(trans['source'], trans['dest'])
    statecase = FsmState(trans['source'])
    statecase.add_trans(transcase)
    statelist.append(statecase)

for states in statelist:
    for trans in states.trans:
        print ('trans src is %s, trans des is %s' %(trans.srcstate, trans.desstate))
