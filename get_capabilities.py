from ncclient import manager

#calling manager.connect from ncclient module to connect to Cisco CSR1000v
#you need enter the specific values of your CSR device here
csr_manager = manager.connect(host='hostname/ip',
                              port=830,
                              username='username',
                              password='password',
                              hostkey_verify=False,
                              device_params={'name':'csr'}
                              )

#for loop to print the list of capabilities of the Cisco CSR1000v
for csr_capability in csr_manager.server_capabilities:
    print(csr_capability)

#closing netconf session
csr_manager.close_session()
