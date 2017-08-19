# FSM: Finite State Machine
FSM_TRANS_TABLE = [
    {'trigger': 'to_shuijiao', 'source': 'chifan', 'dest': 'shuijiao' },
    {'trigger': 'to_dadoudou', 'source': 'shuijiao', 'dest': 'dadoudou'},
    {'trigger': 'to_chifan', 'source': 'dadoudou', 'dest': 'chifan'}]

class FsmStateTrans:
    def __init__(self, srcstate, desstate, trigger):
        self.srcstate = srcstate #源状态
        self.desstate = desstate #目标状态
        self.trigger = trigger

class FsmState:
    def __init__(self, name):
        self.name = name
        self.trans = []
    def add_trans(self, trans): #funciton for add trans
        self.trans.append(trans)

def find_state_by_name(state_list, name):
    print('name is %s' %name)
    for cur_state in state_list:
        if cur_state.name == name
            return cur_state
    return None

STATE_LIST = []
for trans in FSM_TRANS_TABLE:
    transcase = FsmStateTrans(trans['source'], trans['dest'], trans['trigger'])
#    statecase = FsmState(trans['source']) #todo:avoid repeated state in FSM_TRANS_TABLE
    statecase = find_state_by_name(STATE_LIST, trans['source'])
    if statecase == None:

    statecase.add_trans(transcase)
    STATE_LIST.append(statecase)

for states in STATE_LIST:
    for trans in states.trans:
        print ('trans src is %s, trans des is %s,trig is %s' %(trans.srcstate, trans.desstate, trans.trigger))
