from curses import KEY_SCANCEL
from nornir import InitNornir
from nornir.core.task import Task,Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure, napalm_cli
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command, netmiko_save_config, netmiko_commit

nr = InitNornir(config_file="inventory/config.yaml")

def question_13(nr):
    print(nr.__dict__)
    print(type(nr.__dict__))

def question_14(nr):
    print(nr.inventory.hosts)
    print(type(nr.inventory.hosts))

def question_15(nr):
    print(nr.inventory.hosts["R1-CPE-BAT-A"])
    print(type(nr.inventory.hosts["R1-CPE-BAT-A"]))

def question_16(nr):
    print(dir(nr.inventory.hosts["R1-CPE-BAT-A"]))

def question_17(nr):
    print(nr.inventory.hosts["R1-CPE-BAT-A"].keys())

def question_18(nr):
    print(nr.inventory.hosts["R1-CPE-BAT-A"].data["room"])

def question_19(nr):
    print(nr.inventory.groups)

def question_20(nr):
    print(nr.inventory.hosts.get("R1-CPE-BAT-A"))

def question_21(nr):
    print(nr.inventory.hosts.get("R1-CPE-BAT-A").groups[0].keys())

def question_22(nr):
    print(nr.inventory.hosts.get("R1-CPE-BAT-A")["vendor"])

def question_23(nr):
    print(nr.inventory.hosts.get("R1-CPE-BAT-A").hostname)
    print(nr.inventory.hosts.get("R1-CPE-BAT-B").hostname)
    print(nr.inventory.hosts.get("R1-CPE-BAT-A").hostname)
    print(nr.inventory.hosts.get("R1-CPE-BAT-B").hostname)
    print(nr.inventory.hosts.get("ESW1-CPE-BAT-A").hostname)
    print(nr.inventory.hosts.get("ESW1-CPE-BAT-B").hostname)

def question_24(nr):
    print(nr.filter(device_type="router").inventory.hosts.keys())

def question_25(nr):
    print(nr.filter(device_type="router_switch").inventory.hosts.keys())

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world"
    )

def question_26(nr):
    result = nr.run(task=hello_world)
    print(result)

def question_27(nr):
    result = nr.run(task=hello_world)
    print(type(result))    


def question_32(nr):
    result = nr.filter(device_type="router").run(task=napalm_cli,commands=["show ip interface brief"])
    print_result(result)
 
def question_33(nr):
    result = nr.filter(device_type="router_switch").run(task=napalm_get,getters=["get_arp_table"])
    print_result(result)

def question_34(nr):

    result = nr.filter(device_name="R1-CPE-BAT-A").run(task=napalm_configure,configuration="int lo 1 \n ip address 1.1.1.1 255.255.255.255")
    print_result(result)

    result = nr.filter(device_name="R2-CPE-BAT-A").run(task=napalm_configure,configuration="int lo 1 \n ip address 2.2.2.2 255.255.255.255")
    print_result(result)

def question_35(nr):

    result = nr.run(task=napalm_cli,commands=["write"])
    print_result(result)

def question_36(nr):
    result = nr.filter(device_type="router").run(task=netmiko_send_command,command_string="show ip interface brief")
    print_result(result)

def question_37(nr):

    result = nr.filter(device_name="R1-CPE-BAT-A").run(task=netmiko_send_config,config_commands=["int lo 1","ip address 1.1.1.1 255.255.255.255"])
    print_result(result)

    result = nr.filter(device_name="R2-CPE-BAT-A").run(task=netmiko_send_config,config_commands=["int lo 1","ip address 2.2.2.2 255.255.255.255"])
    print_result(result)

def question_38(nr):
    result = nr.run(task=netmiko_save_config)
    print_result(result)

def question_39(nr):

    result = nr.filter(device_name="R1-CPE-BAT-A").run(task=netmiko_send_config,config_file="config/R1_Bat_A.conf")
    print_result(result)

    result = nr.filter(device_name="R2-CPE-BAT-A").run(task=netmiko_send_config,config_file="config/R2_Bat_A.conf")
    print_result(result)

    result = nr.filter(device_name="R1-CPE-BAT-B").run(task=netmiko_send_config,config_file="config/R1_Bat_B.conf")
    print_result(result)

    result = nr.filter(device_name="R2-CPE-BAT-B").run(task=netmiko_send_config,config_file="config/R2_Bat_B.conf")
    print_result(result)

    result = nr.filter(device_name="ESW1-CPE-BAT-A").run(task=netmiko_send_config,config_file="config/ESW1_Bat_A.conf")
    print_result(result)

    result = nr.filter(device_name="ESW1-CPE-BAT-B").run(task=netmiko_send_config,config_file="config/ESW1_Bat_B.conf")
    print_result(result)
    
def question_40(nr):
    pass


def question_41(nr):
    pass

if __name__ == "__main__":
    
    
    question_13(nr)
    question_14(nr)
    question_15(nr)
    question_16(nr)
    question_17(nr)
    question_18(nr)
    question_19(nr)
    question_20(nr)
    question_21(nr)
    question_22(nr)
    question_23(nr)
    question_24(nr)
    question_25(nr)
    question_26(nr)
    question_27(nr)

    #question 28 to 29
    result = nr.run(task=hello_world)
    print_result(result)

    result2 = nr.filter(device_type="router").run(task=hello_world)
    print_result(result2)
    question_32(nr)
    question_33(nr)
    question_34(nr)
    question_35(nr)
    question_36(nr)
    question_37(nr)
    question_38(nr)
    question_39(nr)

    #question_40(nr)
    #question_41(nr)
    pass