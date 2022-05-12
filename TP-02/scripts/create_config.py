
from yaml import load
from jinja2 import Template, Environment, FileSystemLoader
import json

env = Environment(loader=FileSystemLoader("templates"))

#charger fichier json contenant les données des routers/ switchs
def load_json_data_frome_file(file_path):
    with open(file_path) as json_file:
        data_sw = json.load(json_file)
        return data_sw

#générer une configuration à partir d'un json ou yaml et d'un teamplate j2.
def render_network_config(file,data):
    template = env.get_template(file)
    return template.render(data)
    
#enregistrer la configuration dans un fichier .conf
def save_built_config(config,filename):
    f = open("config/{}.conf".format(filename), "w")
    f.write(config)
    f.close()

def create_vlan_config_cpe_marseille():
    pass

def create_vlan_config_cpe_paris():
    pass


if __name__ == "__main__":




    data_sw2= load_json_data_frome_file("data/ESW2.json")
    data_router2 = load_json_data_frome_file("data/R2.json")

    data_sw4 = load_json_data_frome_file("data/ESW4.json")
    data_router3 = load_json_data_frome_file("data/R3.json")

    data_router1 = load_json_data_frome_file("data/R1.json")

    ESW2 = render_network_config("template_switch.j2",data_sw2)
    R2 = render_network_config("template_router.j2",data_router2)

    ESW4 = render_network_config("template_switch.j2",data_sw4)
    R3 = render_network_config("template_router.j2",data_router3)

    R1 = render_network_config("template_router.j2",data_router1)

    save_built_config(ESW2,"ESW2")
    save_built_config(R2,"R2")
    save_built_config(ESW4,"ESW4")
    save_built_config(R3,"R3")
    save_built_config(R1,"R1")


