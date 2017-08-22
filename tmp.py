import FSM
srcstate = FSM.FSM_get_source_state()
for tmp in srcstate:
    tmpdict = FSM.FSM_get_triger_and_desstate(tmp)
    for elmt in tmpdict:
        print('source is %s, trigger is %s, des is %s'%(tmp,elmt,tmpdict[elmt]))
