from ncclient import manager
import xml.dom.minidom

#calling manager.connect from ncclient module to connect to Cisco CSR1000v
#you need enter the specific values of your CSR device here
csr_manager = manager.connect(host='hostname/IP address',
                              port=830,
                              username='username',
                              password='password',
                              hostkey_verify=False,
                              device_params={'name':'csr'}
                              )

#XML template of config to remove as a example I will be removing user.
EDIT_CONFIG = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<username operation='delete'>
    <name>test</name>
    <secret>
        <secret>test123</secret>
    </secret>
</username>
</native>
</config>
"""

#we are calling on the edit_config module of ncclient manager and giving it the target of the running config
config = csr_manager.edit_config(EDIT_CONFIG, target = 'running')

#printig rpc-reply to terminial
print(config)

#closing session
csr_manager.close_session()
