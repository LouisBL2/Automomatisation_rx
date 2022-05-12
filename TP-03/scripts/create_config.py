from time import sleep
from jinja2 import Template, Environment, FileSystemLoader
import json
import time

env = Environment(loader=FileSystemLoader("templates"))

def load_json_data_frome_file(file_path):
    with open(file_path) as json_file:
        data_sw = json.load(json_file)
        return data_sw

def render_network_config(file,data):
    template = env.get_template(file)
    return template.render(data)

def save_built_config(config,filename):
    f = open("config/{}.conf".format(filename), "w")
    f.write(config)
    f.close()

def create_config_cpe_lyon_batA():

# R1 
    data_router1 = load_json_data_frome_file("data/R1_CPE_LYON_BAT_A.json")
    print(data_router1)

    R1_vlan = render_network_config("vlan_router.j2",data_router1)
    R1_vrrp = render_network_config("vrrp_router.j2",data_router1)

    R1 = R1_vlan + R1_vrrp
    
#R2
    data_router2 = load_json_data_frome_file("data/R2_CPE_LYON_BAT_A.json")
    print(data_router2)

    R2_vlan = render_network_config("vlan_router.j2",data_router2)
    R2_vrrp = render_network_config("vrrp_router.j2",data_router2)

    R2 = R2_vlan + R2_vrrp
    
# ESW1
    data_switch = load_json_data_frome_file("data/ESW1_CPE_LYON_BAT_A.json")
    print(data_router1)

    ESW1= render_network_config("vlan_switch.j2",data_switch)

    return R1,R2, ESW1



def create_config_cpe_lyon_batB():
# R1 
    data_router1 = load_json_data_frome_file("data/R1_CPE_LYON_BAT_B.json")
    print(data_router1)

    R1_vlan = render_network_config("vlan_router.j2",data_router1)
    R1_vrrp = render_network_config("vrrp_router.j2",data_router1)

    R1 = R1_vlan + R1_vrrp
    
#R2
    data_router2 = load_json_data_frome_file("data/R2_CPE_LYON_BAT_B.json")
    print(data_router2)

    R2_vlan = render_network_config("vlan_router.j2",data_router2)
    R2_vrrp = render_network_config("vrrp_router.j2",data_router2)

    R2 = R2_vlan + R2_vrrp
    
# ESW1
    data_switch = load_json_data_frome_file("data/ESW1_CPE_LYON_BAT_B.json")
    print(data_router1)

    ESW1= render_network_config("vlan_switch.j2",data_switch)

    return R1, R2, ESW1

    
if __name__ == "__main__":

    #question 3
    create_config_cpe_lyon_batA()

    #question 4
    save_built_config(create_config_cpe_lyon_batA()[0], "R1_Bat_A")
    time.sleep(.5)
    save_built_config(create_config_cpe_lyon_batA()[1], "R2_Bat_A")
    time.sleep(.5)
    save_built_config(create_config_cpe_lyon_batA()[2], "ESW1_Bat_A")


    #question 5:
    create_config_cpe_lyon_batB()
    save_built_config(create_config_cpe_lyon_batB()[0], "R1_Bat_B")
    time.sleep(.5)
    save_built_config(create_config_cpe_lyon_batB()[1], "R2_Bat_B")
    time.sleep(.5)
    save_built_config(create_config_cpe_lyon_batB()[2], "ESW1_Bat_B")
    