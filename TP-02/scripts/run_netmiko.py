#importer les modules necessaire pour napalm, netmiko ou paramiko. Ou bien des finction d'autres fichiers

from netmiko import ConnectHandler
import json, time


R1 = {
    'device_type': 'cisco_ios',
    'host': '172.16.100.126',
    'username': 'cisco',
    'password': 'cisco'
}

# envoyer la commande show ip int brief
def question_25(net_connect):

    command = "show ip int brief"

    output = net_connect.send_command(command)

    print()
    print(output)
    print()

# envoyer la commande show ip int brief
def question_26(net_connect):
    command = "show ip int brief"

    output = net_connect.send_command(command, use_textfsm=True)

    print()
    print(output)
    print()


# envoyer la commande show ip route
def question_27(net_connect):
    command = "show ip route"

    output = net_connect.send_command(command, use_textfsm=True)

    print()
    print(output)
    print()


# afficher l'état des interfaces du router R1
def question_28(net_connect):
    command = "show int description \n"

    output = net_connect.send_command(command, use_textfsm=True)
    print(output)
    for a in output:
        print("Port : {} | Status : {}".format(a.get("port"),a.get("status")))



# executer des commandes en modes config puis sauvegarder.
def question_29(net_connect):

    commands = [
        'conf t \n',
        'int lo1',
        'description sub-interface for admin vlan access - set by paramiko \n',
        'ip address 192.168.1.1 255.255.255.255 \n \n',
        'end \n'
        ]
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

    print()
    print(output)
    print()

#supprimer l'interface lo1
def question_30(net_connect):
    commands = [
        'no int lo1 \n'
        ]
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

    print()
    print(output)
    print()

# déployer une configuration a partir d'un fichier .conf
def question_31(net_connect):

    file_conf = ("config/loopback_R01.conf")

    output = net_connect.send_config_from_file(file_conf)
    output += net_connect.save_config()

    print()
    print(output)
    print()

#supprimer des interfaces de loopback
def question_32(net_connect):
    commands = [
        'no int lo1 \n',
        'no int lo2 \n',
        'no int lo3 \n',       
        'no int lo4 \n'  
        ]
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

    print()
    print(output)
    print()

#affiche le contenu du fichier hosts.json
def get_inventory():
    
    with open("inventory/hosts.json") as json_file:
        data_sw = json.load(json_file)
        print(data_sw)
    

# affichier la configuration de chaue router du fichier hosts.json
def question_35():

    with open("inventory/hosts.json") as json_file:
        data_sw = json.load(json_file)


    for host in data_sw: 
        if "R" in host.get("hostname"):
            tmp = host.pop("hostname",None)
            net_connect = ConnectHandler(**host)
        commands = [
            'end',
            'show int g0/0.99' 
        ]
        output = net_connect.send_config_set(commands)
        time.sleep(1)


        print()
        print(output)
        print()



#deployer une configuration sur tout les routers et switchs du fichier hosts.json
def question_36():


    with open("inventory/hosts.json") as json_file:
            data_sw = json.load(json_file)


    for host in data_sw: 
        if "R" or "ESW" in host.get("hostname"):
            file_conf = ("config/{}.conf").format(host.get("hostname"))
            tmp = host.pop("hostname",None)
            #connection a un appareil
            net_connect = ConnectHandler(**host)
            

        

        output = net_connect.send_config_from_file(file_conf)
        time.sleep(2)
        output += net_connect.save_config()

        print()
        print(output)
        print()
    

if __name__ == "__main__":  

    net_connect = ConnectHandler(**R1)

    question_25(net_connect)
    question_26(net_connect)
    question_27(net_connect)
    question_28(net_connect)
    question_29(net_connect)
    question_30(net_connect)
    question_31(net_connect)
    get_inventory()
    question_35()
    question_36()