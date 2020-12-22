from ncclient import manager, xml_


#calling manager.connect from ncclient module to connect to Cisco CSR1000v
#you need enter the specific values of your CSR device here
csr_manager = manager.connect(host='hostname/IP address',
                              port=830,
                              username='username',
                              password='password',
                              hostkey_verify=False,
                              device_params={'name':'csr'}
                              )

#template that matches save-config schema on CSR device
save_Running = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""

#command/reply being pushed/pulled to RPC API
CSR_Reply = csr_manager.dispatch(xml_.to_ele(save_Running))

#printig rpc-reply to terminial
print(CSR_Reply)

#closing session
csr_manager.close_session()
