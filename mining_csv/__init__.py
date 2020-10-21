import csv
import netmiko as nm
from netmiko import ConnectHandler
import textfsm
import os
cur_path = os.getcwd()
csv_dir = "../webui/uploads"

def mine_cwd_csv():
    print("-------------------------------------------\n" \
      "Scanning current directory for CSV files...\n" \
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
    print("-------------------------------------------\n" \
          "The files found are listed below.          \n" \
          "Please select a number to select the file \n" \
          "to import in.                              \n" \
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
    with open("../templates/cisco_ap_from_csv_template-v3.textfsm") as template:
        results_template = textfsm.TextFSM(template)
        content2parse = open(csv_choice)
        content = content2parse.read()
        try:
            parsedCSV_results = results_template.ParseText(content)
        except textfsm.TextFSMError as err:
            print(err.error)
        else:
            return parsedCSV_results #newLower_list(parsedCSV_results)

if __name__ == "__main__":
    parsedCSV_results = mine_cwd_csv()
