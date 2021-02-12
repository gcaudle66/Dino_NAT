import netmiko as nm
import time

connIsAlive = False
gathered_ap_inventory = []


def connex(wlcClass):
    global conn
    try:
        conn = nm.BaseConnection(ip=wlcClass.device_host_ip, username=wlcClass.device_user, password=wlcClass.device_pass, session_log=f"ssh_session_logfile.txt", session_log_file_mode="write", session_log_record_writes="True")
    except nm.NetMikoTimeoutException:
        print("*********************************************************\n")
        print("* ERROR: Connection to {} timed-out.     \n".format('wlc'))
        print("* Skipping this entry for now...                              ")
        print("*********************************************************\n")
    else:
        connIsAlive = conn.is_alive()
        return conn


def getApInventory(conn):
    """ Here we will run commands against the WLC to gather \n""" \
        """ necessary data for comparison against CSV           \n"""
    cli_output = conn.send_command_timing("show ap config general",
                                          use_textfsm=True, textfsm_template="./templates/cisco_ios_show_ap_template-v3.textfsm")
    for ap in cli_output:
        for key,value in ap.items():
            print(f'{key} : {value}')
        print('------')
    gathered_ap_inventory.append(cli_output)
    return cli_output


def get_ap_tags(conn):
    cli_output = conn.send_command_timing("show ap tag summary",
                                          use_textfsm=True, textfsm_template="./templates/cisco_ios_show_ap_tag_summary_template-v1.textfsm")
    for tag in cli_output:
        for key, value in tag.items():
            print(f'{key} : {value}')
    print('-----')
    return cli_output


def set_ap_tags(conn):
    print('**Warning: "Associating/Disassociating tags will cause associated AP to reconnect; Roughly 30 seconds AP will be offline**')
    pass


def compare_imported_2_gathered(imported, gathered):
    pass



