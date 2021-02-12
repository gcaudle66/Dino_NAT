import netmiko as nm


def connex(WLCclass):
    try:
        conn = nm.BaseConnection(ip=wlcClass.device_host_ip, username=wlcClass.device_user, password=wlcClass.device_pass, session_log=f"ssh_session_logfile.txt", session_log_file_mode="write", session_log_record_writes="True")
    except nm.NetMikoTimeoutException as err:
        print("*********************************************************\n")
        print("* ERROR: Connection to {} timed-out.     \n".format('wlc'))
        print("* Skipping this entry for now...                              ")
        print("*********************************************************\n")
    else:
        connIsAlive = conn.is_alive()
        return conn
