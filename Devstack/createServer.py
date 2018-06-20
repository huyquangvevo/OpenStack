import time
from credentials import get_nova_credentials_v2
from novaclient.client import Client

try:
    credentials = get_nova_credentials_v2()
    nova_client = Client(**credentials)

    image = nova_client.images.find(name='cirros')
    flavor = nova_client.flavors.find(name='m1.tiny')
    net = nova_client.networks.find(label='private')
    nics = [{'net-id':net.id}]
    instance = nova_client.servers.create(name="vm2",image=image,flavor=flavor,key_name='keypair-1',nics=nics)
    print("Sleeping for 5s after create command")
    time.sleep(5)
    print("list of VMS")
    print(nova_client.servers.list())
finally:
    print("Execution Completed")
    
