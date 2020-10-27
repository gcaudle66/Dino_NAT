import csv
import netmiko as nm
from netmiko import ConnectHandler
import textfsm
import os
cur_path = os.getcwd()
csv_dir = "webui/uploads/"
templates_dir = "templates/"
discards_errs = []


def mine_cwd_csv():
    print("-------------------------------------------\n"
          "Scanning current directory for CSV files...\n"
          "-------------------------------------------\n")
    with os.scandir(path=csv_dir) as it:
        file_list = []
        for entry in it:
            if entry.name.endswith(".csv") and entry.is_file():
                file_list.append(entry.name)
        file_len = len(file_list)
        print(f"Located {file_len} CSV files.")
        return importCSV(file_list)


def importCSV(file_list):
    """ Choose CSV file to import  that was found in local \n""" \
        """ directory.                                         \n"""
    print("-------------------------------------------\n"
          "The files found are listed below.          \n"
          "Please select a number to select the file \n"
          "to import in.                              \n"
          "-------------------------------------------\n")
    index = 0
    choice = 0
    choices_list = {}
    for item in range(len(file_list)):
        item = file_list[index]
        print("Choice # {} : {} ".format(index, item))
        choice_entry = choices_list[index] = item
        index = index + 1
    print(choices_list)
    choice = int(input("Please select a file # from the list to import: "))
    csv_choice = csv_dir + choices_list[choice]
    return parseCSV(csv_choice)


def parseCSV(csv_choice):
    """ Here we will parse through the CSV that was imported \n""" \
        """ using a TextFSM template that looks for only certain \n""" \
        """ fields in the CSV. These fields are defined in the   \n""" \
        """ below mentioned template variable                    \n"""
    with open("templates/cisco_ap_from_csv_template-v3.textfsm") as template:
        results_template = textfsm.TextFSM(template)
        content2parse = open(csv_choice)
        content = content2parse.read()
        try:
            parsedCSV_results = results_template.ParseText(content)
        except textfsm.TextFSMError as err:
            print(err.error)
        else:
            # newLower_list(parsedCSV_results)
            return formatMacs(parsedCSV_results)


def newLower_list(content):
    """ Converts any MAC address fields to lowercase \n""" \
        """ Converts AP names fields to lowercase        \n"""
    output = []
    for entry in range(len(content)):
        entry = content.pop()
        name = str.lower(entry[0])
        mac = str.lower(entry[1])
        new_entry = [name, mac]
        output.append(new_entry)
    return formatMacs(output)


def formatMacs(content):
    """ here is where it gets fun. This function takes data from      \n""" \
        """ the imported CSV list where MAC addresses may not be in       \n""" \
        """ the correct format of xxx.xxx.xxxx and removes any existing   \n""" \
        """ delimeters, checks to make sure there are no more than 12 hex \n""" \
        """ characters, and if no error is present, rebuilds them into    \n""" \
        """ the correct xxxx.xxxx.xxxx format. If any error is raised     \n""" \
        """ during the process, that entry is ignored.                    \n"""
    print("-------------------------------------------\n"
          "Normalizing MAC Addresses found in CSV     \n"
          "All MACs will be set to lowercase and then \n"
          "checked against REGEX to make sute they are\n"
          "in format xxxx.xxxx.xxxx before proceeding \n"
          "-------------------------------------------\n")
    import re
    re_fmt = '[a-fA-F0-9][a-fA-F0-9][a-fA-F0-9][a-fA-F0-9]\.[a-fA-F0-9][a-fA-F0-9][a-fA-F0-9][a-fA-F0-9]\.[a-fA-F0-9][a-fA-F0-9][a-fA-F0-9][a-fA-F0-9]'
#    re_fmt = '^[a-fA-F0-9]{4}\.[a-fA-F0-9]{4}\.[a-fA-F0-9]{4}\b'
    final_CSVresults = []
    discards_errs = []
    bad_chars = [":", "."]
    for entry in range(len(content)):
        entry = content.pop()
        if re.match(re_fmt, entry[1]):
            final_CSVresults.append(entry)
        else:
            mac = entry[1]
            print("Incorrect format: " + mac)
            for i in bad_chars:
                mac = mac.replace(i, "")
            print(f"Removing seperators: {mac}")
            if len(mac) > 12:
                err = "Error: More than 12 characters present in MAC."
                print(
                    f"{err} \n MAC ADDRESS: {mac} \n Logging it and discarding this entry!")
                discard = {"AP MAC": mac, "Error":  err}
                discards_errs.append(discard)
            else:
                new_mac = mac[:4] + "." + mac[4:8] + "." + mac[8:12]
                print(f"Reformatted: {new_mac}")
                if re.match(re_fmt, new_mac):
                    print("Format is now correct...adding to list: " + new_mac)
                    new_entry = [entry[0], new_mac]
                    final_CSVresults.append(new_entry)
                else:
                    err = "Error: Unable to normalize MAC Address."
                    print(f"MAC ADDRESS: {new_mac} \n Possible Non-Hex Character in MAC.\n"
                          "Logging, discarding this entry and moving on!")
                    discard = {"AP MAC Address": new_mac, "Error": err}
                    discards_errs.append(discard)

    print("*********************************************************")
    print("* The following entries were found in the imported CSV  *")
    print("*********************************************************")
    for row in range(len(final_CSVresults)):
        print(final_CSVresults[row], sep="\n")
    return final_CSVresults, discards_errs


if __name__ == "__main__":
    parsedCSV_results = mine_cwd_csv()
