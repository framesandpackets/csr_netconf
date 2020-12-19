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

#calling get_config to pull the running config from the device
config = csr_manager.get_config('running')

#creating and copying config as string to file
f = open('running_config.xml', 'w')
f.write(str(config))
f.close()

#parsing file with xml.dom.minidom and pretty printing the xml string to the file
dom = xml.dom.minidom.parse('running_config.xml')
pretty_xml_as_string = dom.toprettyxml()
f = open('running_config.xml', 'w')
f.write(pretty_xml_as_string)
f.close()

#closing session
csr_manager.close_session()
