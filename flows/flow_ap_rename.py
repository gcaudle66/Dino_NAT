import netmiko as nm
import time

net_connect = nm.BaseConnection


def connex(*args, **kwargs):
    try:
        net_connect = nm.BaseConnection(ip=kwargs.get(device_host_ip), username=kwargs.get(device_user)
, password=kwargs.get(device_pass), session_log=f"ssh_session_logfile.txt", session_log_file_mode="write", session_log_record_writes="True")
    except nm.NetMikoTimeoutException:
        print("*********************************************************\n")
        print("* ERROR: Connection to {} timed-out.     \n".format('wlc'))
        print("* Skipping this entry for now...                              ")
        print("*********************************************************\n")
    else:
        connIsAlive = net_connect.is_alive()
        return net_connect


def getApInventory():
    """ Here we will run commands against the WLC to gather \n""" \
        """ necessary data for comparison against CSV           \n"""
    while connIsAlive is False:
        print("SSH Connection to WLC has closed. Reconnecting....")
        conn = connect()
    try:
        cli_output = conn.send_command_timing("show ap config general | include ^Cisco AP Name|^MAC Address", use_textfsm=True, textfsm_template="./templates/cisco_ios_show_ap_template-v2_5.textfsm")
    except nm.NetMikoTimeoutException as err:
        print("Timeout Error occured. Timeout waiting for device for an operation to continue.")
        return err.with_traceback
# except:
# print("Unexpected error:", sys.exc_info()[0])
# raise
    else:
        return cli_output
