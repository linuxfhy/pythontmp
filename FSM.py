# FSM: Finite State Machine
FSM_TRANS_TABLE = [
    {'trigger': 'to_睡觉', 'source': '吃饭', 'dest': '睡觉' },
    {'trigger': 'to_打豆豆', 'source': '睡觉', 'dest': '打豆豆'},
    {'trigger': 'to_吃饭', 'source': '打豆豆', 'dest': '吃饭'}]

class FsmStateTrans:
    def __init__(self, srcstate, desstate, trigger):
        self.srcstate = srcstate
        self.desstate = desstate
        self.trigger = trigger

class FsmState:
    def __init__(self, name):
        self.name = name
        self.trans = []
    def add_trans(self, trans):
        self.trans.append(trans)

def find_state_by_name(state_list, name):
    for cur_state in state_list:
        if cur_state.name == name:
            return cur_state
    return None

def find_trans_by_state(state_list, srcstate, desstate):
    for cur_state in state_list:
        for cur_trans in cur_state.trans:
            if cur_trans.srcstate == srcstate and cur_trans.desstate == destate:
                return cur_trans
    return None

def get_triger_and_desstate(state_list, srcstate):
    tmpdict = {}
    for cur_state in state_list:
        for trans in cur_state.trans:
            tmpdict[trans.trigger] = trans.desstate
    return tmpdict


#Code for init
STATE_LIST = []
for trans in FSM_TRANS_TABLE:
    statecase = find_state_by_name(STATE_LIST, trans['source'])
    if statecase == None:
        statecase = FsmState(trans['source'])
    transcase = find_trans_by_state(STATE_LIST, trans['source'], trans['dest'])
    if transcase == None:
        transcase = FsmStateTrans(trans['source'], trans['dest'], trans['trigger'])
    statecase.add_trans(transcase)
    STATE_LIST.append(statecase)

#CODE FOR TEST:
for cur_trans in FSM_TRANS_TABLE:
    result_dict = get_triger_and_desstate(STATE_LIST, cur_trans['source'])
for tmp_dict in result_dict:
    print ('result_dict[%s] = %s'%(tmp_dict, result_dict[tmp_dict]))

