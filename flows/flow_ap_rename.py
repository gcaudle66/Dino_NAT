import netmiko as nm
import time

connIsAlive = False


def connex(*args, **kwargs):
    try:
        conn = nm.BaseConnection(ip=kwargs.get(device_host_ip), username=kwargs.get(device_user), password=kwargs.get(
            device_pass), session_log=f"ssh_session_logfile.txt", session_log_file_mode="write", session_log_record_writes="True")
    except nm.NetMikoTimeoutException:
        print("*********************************************************\n")
        print("* ERROR: Connection to {} timed-out.     \n".format('wlc'))
        print("* Skipping this entry for now...                              ")
        print("*********************************************************\n")
    else:
        connIsAlive = conn.is_alive()
        return conn


def getApInventory():
    """ Here we will run commands against the WLC to gather \n""" \
        """ necessary data for comparison against CSV           \n"""
    cli_output = conn.send_command_timing("show ap config general | include ^Cisco AP Name|^MAC Address",
                                          use_textfsm=True, textfsm_template="./templates/cisco_ios_show_ap_template-v3.textfsm")
    return cli_output


def get_ap_tags():
    cli_output = conn.send_command_timing("show ap tag summary",
                                          use_textfsm=True, textfsm_template="./templates/cisco_ios_show_ap_tag_summary_template-v1.textfsm")
    return cli_output


def set_ap_tags():
    print('**Warning: "Associating/Disassociating tags will cause associated AP to reconnect; Roughly 30 seconds AP will be offline**')
