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
        self.trans = {}

def find_state_by_name(state_list, name):
    for cur_state in state_list:
        if cur_state.name == name:
            return cur_state
    return None

def find_trans_by_state(state_list, srcstate, desstate):
    for cur_state in state_list:
        for trigger in cur_state.trans:
            if cur_state.name == srcstate and cur_trans.trans[trigger] == desstate:
                return True
    return False

def get_source_state(state_list):
    src_list = []
    for cur_state in state_list:
        src_list.append(cur_state.name)
    return src_list

def get_triger_and_desstate(state_list, srcstate):
    for cur_state in state_list:
        if cur_state.name == srcstate:
            return cur_state.trans
    return None

def get_destination_state(sate_list, srcstate, trigger):
    for cur_state in state_list:
        if cur_state.name == srcstate:
            return cur_state.trans[trigger]
    return None


#Code for init
STATE_LIST = []
for trans in FSM_TRANS_TABLE:
    statecase = find_state_by_name(STATE_LIST, trans['source'])
    if statecase == None:
        statecase = FsmState(trans['source'])
    have_trans = find_trans_by_state(STATE_LIST, trans['source'], trans['dest'])
    if have_trans == False:
        statecase.trans[trans['trigger']] = trans['dest']
    STATE_LIST.append(statecase)

#CODE FOR TEST:
for cur_trans in FSM_TRANS_TABLE:
    result_dict = get_triger_and_desstate(STATE_LIST, cur_trans['source'])
    for dict_elmt in result_dict:
        print("srcstate is %s, trigger is %s, des state is %s"%(cur_trans['source'], dict_elmt, result_dict[dict_elmt]))


