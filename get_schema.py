from ncclient import manager

#calling manager.connect from ncclient module to connect to Cisco CSR1000v
#you need enter the specific values of your CSR device here
csr_manager = manager.connect(host='hostname/IP address',
                              port=830,
                              username='username',
                              password='password',
                              hostkey_verify=False,
                              device_params={'name':'csr'}
                              )

#calling get_schema to pull the .yaml schema from CSR
#ENTER SCHEMA NAME HERE:
#for demo purposes here I have Cisco-IOS-XE-ospf schema selected, you can pull all schemas on CSR by using get_capabilties.py script in repo
schema = csr_manager.get_schema('Cisco-IOS-XE-ospf')
f = open("schema.yaml", 'a+')
f.write(str(schema))
f.close()

#closing netconf session
csr_manager.close_session()
