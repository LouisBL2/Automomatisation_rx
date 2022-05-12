#importer les modules necessaire pour napalm, netmiko ou paramiko. Ou bien des finction d'autres fichiers
import time
from jinja2 import pass_context
import paramiko

router_list = [   ## Question 17,18,19

{
    "name" : "R1",
    "ip" : "172.16.100.126",
    "username" :"cisco", 
    "password" : "cisco" 

},

    {
    "name" : "R2",
    "int adm":"g0/0.99",
    "ip" : "172.16.100.190",
    "username" :"cisco", 
    "password" : "cisco" 
},
    {
    "name" : "R3",
    "int adm":"g0/0.99",
    "ip" : "172.16.100.254",
    "username" :"cisco", 
    "password" : "cisco" 
}

]

device = {
    "ip" : "172.16.100.126",
    "username" :"cisco", 
    "password" : "cisco" 

}

#envoyer la commande show ip interface sur un equipement 
def question_11(remote_conn, nbytes):
    remote_conn.send("show ip int brief\n")
    time.sleep(.5) #wait for command execution
    output = remote_conn.recv(nbytes) #Get output data from the channel
    print(output.decode("utf-8"))

#envoyer des commandes afin de creeer une interface lo1
def question_15(remote_conn, nbytes):
    commands = [
    'conf t \n',
    'int lo1 \n',
    'ip address 192.168.1.1 255.255.255.255 \n',
    'description loopback interface from paramiko \n',
    'no sh \n',
    'end \n']
    i= 0
    while i < len(commands): 
        remote_conn.send(commands[i])
        i= i+1
        time.sleep(.5)


# afficher la configuration de lo1
def question_16(remote_conn, nbytes):
    remote_conn.send("show int lo1 \n")
    time.sleep(.5) #wait for command execution
    output = remote_conn.recv(nbytes) #Get output data from the channel
    print(output.decode("utf-8"))


#envoyer show ip interface brief sur les appareil présent dans router_list ( dictionnaire)
def question_17():

    for router in router_list: 
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(router.get("ip"),
            username=router.get("username"),
            password=router.get("password"),
            look_for_keys=False, allow_agent=False,
            timeout=5)
        remote_conn = remote_conn_pre.invoke_shell()

        question_11(remote_conn,nbytes)
        time.sleep(.5) #wait for command execution

# ajouter une description aux interfaces des routers présente dnas router_list ( dictionnaire)
def question_18():
    for router in router_list:
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(router.get("ip"),
            username=router.get("username"),
            password=router.get("password"),
            look_for_keys=False, allow_agent=False,
            timeout=5)
        remote_conn = remote_conn_pre.invoke_shell()
        commands = [
        'conf t \n',
        'int {} \n'.format(router.get("int")),
        'description sub-interface for admin vlan access - set by paramiko \n',
        'no sh \n',
        'end \n']
        i= 0
        while i < len(commands): 
            remote_conn.send(commands[i])
            i= i+1
            time.sleep(.5)
    remote_conn.send("show int g 0/0.99 \n")
    time.sleep(.5) #wait for command execution
    output = remote_conn.recv(nbytes) #Get output data from the channel
    print(output.decode("utf-8"))


# sauvegarder la configuration des appareil présent dans router_list ( dictionnaire)
def save_config(devices=[]):
    for router in router_list: 
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(router.get("ip"),
            username=router.get("username"),
            password=router.get("password"),
            look_for_keys=False, allow_agent=False,
            timeout=5)
        remote_conn = remote_conn_pre.invoke_shell()
        remote_conn.send("show running-config \n")
        time.sleep(1) #wait for command execution
        output = remote_conn.recv(nbytes) #Get output data from the channel
        txt = output.decode("utf-8")
        print(output.decode("utf-8"))
        f = open("config/save_{}.conf".format(router.get("name")), "w")
        f.write(txt)
        f.close()






if __name__ == "__main__":

    nbytes = 65535
#connection a un appareil
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(device.get("ip"),
        username=device.get("username"),
        password=device.get("password"),
        look_for_keys=False, allow_agent=False,
        timeout=5)
    remote_conn = remote_conn_pre.invoke_shell()



    question_11(remote_conn,nbytes)
    question_15(remote_conn,nbytes)
    question_16(remote_conn,nbytes)
    question_17()
    question_18()
    save_config(router_list)