import FSM
print('Test Case 1:Check get source state ,trigger, destination state:')
srcstate = FSM.FSM_get_source_state()
for tmp in srcstate:
    tmpdict = FSM.FSM_get_triger_and_desstate(tmp)
    for elmt in tmpdict:
        print('source is %s, trigger is %s, des is %s'%(tmp,elmt,tmpdict[elmt]))

print('Test Case 2:Check get init state')
init_state = FSM.FSM_get_init_state();
print('init state is %s'%(init_state))
