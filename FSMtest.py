from FSM import WorkFlowFSM

print('Test Case 1:Check Import a class:')
workflowfsm = WorkFlowFSM()
print ('init state is %s,source state is %s'%(workflowfsm.FSM_get_init_state(),workflowfsm.FSM_get_source_state()))
print(workflowfsm.FSM_get_triger_and_desstate('chifan'))
