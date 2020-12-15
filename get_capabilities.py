from ncclient import manager

csr_manager = manager.connect(host='192.168.0.150',
                              port=830,
                              username='michael',
                              password='pass1',
                              hostkey_verify=False,
                              device_params={'name':'csr'}
                              )

for csr_capability in csr_manager.server_capabilities:
    print(csr_capability)

csr_manager.close_session()
