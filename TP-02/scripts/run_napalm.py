#importer les modules necessaire pour napalm, netmiko ou paramiko. Ou bien des finction d'autres fichiers

from base64 import encode
import time, json
from napalm import get_network_driver
from .create_config import load_json_data_frome_file, render_network_config, save_built_config
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

def get_inventory():
    pass


def get_json_data_from_file(file):
    pass

# envoyer la commande show ip interface bried
def question_41(device):

    commands = ["show ip interface brief"]
    output = device.cli(commands)
    print(output)


def question_42(device):
    commands = ["show ip interface brief"]
    output = device.cli(commands)
    print(type(output))

    output = device.get_arp_table(vrf='')
    print(output)
    print(type(output))


# deployer une configuration depuis un fichier .conf
def question_45(device):

    device.load_merge_candidate(filename="config/R01.conf")
    print(device.compare_config())
    device.commit_config()



#generer different fichiers de configuration
def question_46():
    


    data_ospf_R1 = load_json_data_frome_file("data/ospf_R01.json")
    data_ospf_R2 = load_json_data_frome_file("data/ospf_R02.json")
    data_ospf_R3 = load_json_data_frome_file("data/ospf_R03.json")


    ospf_R1 = render_network_config("ospf.j2",data_ospf_R1)
    ospf_R2 = render_network_config("ospf.j2",data_ospf_R2)
    ospf_R3 = render_network_config("ospf.j2",data_ospf_R3)



    save_built_config(ospf_R1,"data_ospf_r01")
    save_built_config(ospf_R2,"data_ospf_r02")
    save_built_config(ospf_R3,"data_ospf_r03")

# déployer la configuration ospf sur les routers 
def question_47():

    with open("inventory/router_backbone.json") as json_file:
        data_ospf = json.load(json_file)


    for router in data_ospf:
        if "R"  in router.get("name"):
            driver = get_network_driver('ios')
            filename_conf = "config/data_ospf_{}.conf".format(router.get("name"))
            tmp = router.pop("name",None)
            device = driver(**router)
            device.open()
            device.load_merge_candidate(filename=filename_conf)
            print(device.compare_config())
            device.commit_config()
            device.close()
            time.sleep(1)



def question_49():

    with open("inventory/router_backbone.json") as json_file:
        data_ospf = json.load(json_file)


    for router in data_ospf:
        driver = get_network_driver('ios')
        file_save = "config/backup/{}.bak".format(router.get("name"))
        tmp = router.pop("name",None)
        device = driver(**router)
        device.open()
        f = open(file_save, "a")
        save = device.get_config()['running']
        f.write(save)
        time.sleep(1)
        device.close()
        time.sleep(1)

if __name__ == "__main__":

    r01 = {
    'hostname':"172.16.100.126",
    'username': "cisco",
    'password': "cisco"
    }
    driver = get_network_driver('ios')
    device = driver(**r01)
    device.open()

    question_41(device)
    question_42(device)
    question_45(device)
    question_46()
    question_47()
    question_49()