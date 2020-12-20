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

#XML filter! filtering the get request from the CSR for all usernames configured on the device. All XML tags can be
#found by pulling config with get_config.py and parsing the running_config.xml file
filter = """
<filter>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<username>
<name>
</name>
</username>
</native>
</filter>
"""

#calling get_config to pull the running config from the device, adding XML filter to the get request
config = csr_manager.get_config('running', filter)

#creating and copying config as string to file
f = open('filtered_running_config.xml', 'w')
f.write(str(config))
f.close()

#parsing file with xml.dom.minidom and pretty printing the xml string to the file
dom = xml.dom.minidom.parse('filtered_running_config.xml')
pretty_xml_as_string = dom.toprettyxml()
f = open('filtered_running_config.xml', 'w')
f.write(pretty_xml_as_string)
f.close()

#closing session
csr_manager.close_session()
