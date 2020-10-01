TEST DATA


-------------------ap_rename20.matches for testing ---------------
ap_rename20.matches = [['78bc.1adb.c70e', {'Old_Name': 'AP78BC.1ADB.C70E', 'New_Name': 'DarthVaderConfRoom', 'wlc': '198.18.134.100'}], ['aaaa.1adb.dddd', {'Old_Name': 'APAAAA.1ADB.DDDD', 'New_Name': 'EmperorConfRoom', 'wlc': '192.168.1.100'}]]

--------------------CSV Inventory for testing ------------------------------
final_CSVresults = [['dllstxatapn01v281a', '6c8b.d3fe.7afc'], ['my.ap.101', '5c5a.c7f0.7c24'], ['DarthVaderConfRoom', '78bc.1adb.c70e']]

--------------------wifi_inv for testing------------------------------------
wifi_inv = [[{'hostname': 'C9800-WLC', 'platformId': 'C9800-CL-K9', 'mgmntIP': '198.18.134.100', 'location': None, 'instanceUuid': '32c2efca-57d6-47e7-bcc2-c89f1ccbfa0a'}], [{'hostname': 'AP78BC.1ADB.C70E', 'platformId': 'AIR-AP3802I-B-K9', 'mgmntIP': '198.18.128.61', 'associatedWlcIp': '198.18.134.100', 'instanceUuid': 'f82c846d-c394-40a9-ac5e-8c5023354c8e', 'ethMacAddress': '78:bc:1a:db:c7:0e', 'location': None}, {'hostname': 'AP5C5A.C7F0.785E', 'platformId': 'AIR-AP3802I-B-K9', 'mgmntIP': '198.18.128.65', 'associatedWlcIp': '198.18.134.100', 'instanceUuid': 'ab623191-5b37-4f80-bda6-2c769e620484', 'ethMacAddress': '5c:5a:c7:f0:78:5e', 'location': None}]]

------------------DNAC INVENTORY FOR TESTING----------
>>> dnac_inventory = 
[{'memorySize': 'NA', 'family': 'Unified AP', 'hostname': 'AP5C5A.C7F0.785E', 'macAddress': '68:3b:78:57:e2:60', 'apManagerInterfaceIp': '', 'associatedWlcIp': '198.18.134.100', 'bootDateTime': None, 'collectionStatus': 'Managed', 'upTime': '03:20:24.210', 'softwareType': None, 'softwareVersion': '16.12.3.13', 'snmpLocation': 'default location', 'tagCount': '0', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'serialNumber': 'FCW2325N3E9', 'roleSource': 'AUTO', 'lastUpdateTime': 1588898868771, 'errorCode': 'null', 'errorDescription': None, 'interfaceCount': '0', 'lastUpdated': '2020-05-08 00:47:48', 'lineCardCount': '0', 'lineCardId': '', 'locationName': None, 'managementIpAddress': '198.18.128.65', 'platformId': 'AIR-AP3802I-B-K9', 'reachabilityFailureReason': 'NA', 'reachabilityStatus': 'Reachable', 'series': 'Cisco 3800I Series Unified Access Points', 'snmpContact': '', 'location': None, 'type': 'Cisco 3800I Unified Access Point', 'role': 'ACCESS', 'collectionInterval': 'NA', 'inventoryStatusDetail': 'NA', 'instanceUuid': 'ab623191-5b37-4f80-bda6-2c769e620484', 'instanceTenantId': '5d8d2b5927a4ee004328f51d', 'id': 'ab623191-5b37-4f80-bda6-2c769e620484'}, {'memorySize': 'NA', 'family': 'Unified AP', 'hostname': 'AP78BC.1ADB.C70E', 'macAddress': '68:3b:78:50:ad:c0', 'apManagerInterfaceIp': '', 'associatedWlcIp': '198.18.134.100', 'bootDateTime': None, 'collectionStatus': 'Managed', 'upTime': '03:20:39.210', 'softwareType': None, 'softwareVersion': '16.12.3.13', 'snmpLocation': 'Global/United States/North Carol', 'tagCount': '0', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'serialNumber': 'FCW2325N3G5', 'roleSource': 'AUTO', 'lastUpdateTime': 1588898868771, 'errorCode': 'null', 'errorDescription': None, 'interfaceCount': '0', 'lastUpdated': '2020-05-08 00:47:48', 'lineCardCount': '0', 'lineCardId': '', 'locationName': None, 'managementIpAddress': '198.18.128.61', 'platformId': 'AIR-AP3802I-B-K9', 'reachabilityFailureReason': 'NA', 'reachabilityStatus': 'Reachable', 'series': 'Cisco 3800I Series Unified Access Points', 'snmpContact': '', 'location': None, 'type': 'Cisco 3800I Unified Access Point', 'role': 'ACCESS', 'collectionInterval': 'NA', 'inventoryStatusDetail': 'NA', 'instanceUuid': 'f82c846d-c394-40a9-ac5e-8c5023354c8e', 'instanceTenantId': '5d8d2b5927a4ee004328f51d', 'id': 'f82c846d-c394-40a9-ac5e-8c5023354c8e'}, {'memorySize': 'NA', 'family': 'Wireless Controller', 'hostname': 'C9800-WLC', 'macAddress': '00:1e:bd:4e:90:00', 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2020-05-07 21:25:48', 'collectionStatus': 'Managed', 'upTime': '3:22:23.87', 'softwareType': 'Cisco Controller', 'softwareVersion': '16.12.3', 'snmpLocation': '', 'tagCount': '0', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'serialNumber': '9YLDKDUP0SZ', 'roleSource': 'AUTO', 'lastUpdateTime': 1588898868771, 'errorCode': None, 'errorDescription': None, 'interfaceCount': '0', 'lastUpdated': '2020-05-08 00:47:48', 'lineCardCount': '0', 'lineCardId': '', 'locationName': None, 'managementIpAddress': '198.18.134.100', 'platformId': 'C9800-CL-K9', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9800 Wireless Controllers for Cloud', 'snmpContact': '', 'location': None, 'type': 'Cisco Catalyst 9800-CL Wireless Controller for Cloud', 'role': 'ACCESS', 'collectionInterval': 'Global Default', 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'instanceUuid': '32c2efca-57d6-47e7-bcc2-c89f1ccbfa0a', 'instanceTenantId': '5d8d2b5927a4ee004328f51d', 'id': '32c2efca-57d6-47e7-bcc2-c89f1ccbfa0a'}]

------------------------DNAC INVENTORY AP ENTRY ONLY---------------------------
{'memorySize': 'NA', 'family': 'Unified AP', 'hostname': 'AP78BC.1ADB.C70E', 'macAddress': '68:3b:78:50:ad:c0', 'apManagerInterfaceIp': '', 'associatedWlcIp': '198.18.134.100', 'bootDateTime': None, 'collectionStatus': 'Managed', 'upTime': '03:20:39.210', 'softwareType': None, 'softwareVersion': '16.12.3.13', 'snmpLocation': 'Global/United States/North Carol', 'tagCount': '0', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'serialNumber': 'FCW2325N3G5', 'roleSource': 'AUTO', 'lastUpdateTime': 1588898868771, 'errorCode': 'null', 'errorDescription': None, 'interfaceCount': '0', 'lastUpdated': '2020-05-08 00:47:48', 'lineCardCount': '0', 'lineCardId': '', 'locationName': None, 'managementIpAddress': '198.18.128.61', 'platformId': 'AIR-AP3802I-B-K9', 'reachabilityFailureReason': 'NA', 'reachabilityStatus': 'Reachable', 'series': 'Cisco 3800I Series Unified Access Points', 'snmpContact': '', 'location': None, 'type': 'Cisco 3800I Unified Access Point', 'role': 'ACCESS', 'collectionInterval': 'NA', 'inventoryStatusDetail': 'NA', 'instanceUuid': 'f82c846d-c394-40a9-ac5e-8c5023354c8e', 'instanceTenantId': '5d8d2b5927a4ee004328f51d', 'id': 'f82c846d-c394-40a9-ac5e-8c5023354c8e'}

--------------------------------------------------------------------------------------
---------------------Matches list for testing-multi WLCs and APs-------
ap_rename20.matches = [
 ['5c5a.c7f0.1111', {'Old_Name': 'AP1', 'New_Name': 'sithlord.meetingrm.ap1', 'wlc': '198.18.134.111'}],
 ['5c5a.c7f0.2222', {'Old_Name': 'AP2', 'New_Name': 'sithlord.meetingrm.ap2', 'wlc': '198.18.134.222'}],
 ['5c5a.c7f0.3333', {'Old_Name': 'AP3', 'New_Name': 'sithlord.meetingrm.ap3', 'wlc': '198.18.134.333'}],
 ['5c5a.c7f0.4444', {'Old_Name': 'AP4', 'New_Name': 'sithlord.meetingrm.ap4', 'wlc': '198.18.134.444'}],
 ['5c5a.c7f0.5555', {'Old_Name': 'AP5', 'New_Name': 'sithlord.meetingrm.ap5', 'wlc': '198.18.134.555'}],
 ['5c5a.c7f0.6666', {'Old_Name': 'AP6', 'New_Name': 'sithlord.meetingrm.ap6', 'wlc': '198.18.134.666'}],
 ['5c5a.c7f0.7777', {'Old_Name': 'AP7', 'New_Name': 'sithlord.meetingrm.ap7', 'wlc': '198.18.134.777'}],
 ['5c5a.c7f0.8888', {'Old_Name': 'AP8', 'New_Name': 'sithlord.meetingrm.ap8', 'wlc': '198.18.134.999'}],
 ['5c5a.c7f0.9999', {'Old_Name': 'AP9', 'New_Name': 'sithlord.meetingrm.ap9', 'wlc': '198.18.134.999'}],
 ['aaaa.c7f0.1111', {'Old_Name': 'AP11', 'New_Name': 'sithlord.meetingrm.ap11', 'wlc': '198.18.134.1'}],
 ['bbbb.c7f0.2222', {'Old_Name': 'AP22', 'New_Name': 'sithlord.meetingrm.ap12', 'wlc': '198.18.134.2'}],
 ['cccc.c7f0.3333', {'Old_Name': 'AP33', 'New_Name': 'sithlord.meetingrm.ap13', 'wlc': '198.18.134.3'}],
 ['dddd.c7f0.4444', {'Old_Name': 'AP44', 'New_Name': 'sithlord.meetingrm.ap14', 'wlc': '198.18.134.444'}],
 ['eeee.c7f0.5555', {'Old_Name': 'AP55', 'New_Name': 'sithlord.meetingrm.ap15', 'wlc': '198.18.134.555'}],
 ['ffff.c7f0.6666', {'Old_Name': 'AP66', 'New_Name': 'sithlord.meetingrm.ap16', 'wlc': '198.18.134.666'}],
 ['gggg.c7f0.7777', {'Old_Name': 'AP77', 'New_Name': 'sithlord.meetingrm.ap17', 'wlc': '198.18.134.777'}],
 ['hhhh.c7f0.8888', {'Old_Name': 'AP88', 'New_Name': 'sithlord.meetingrm.ap18', 'wlc': '198.18.134.888'}],
 ['iiii.c7f0.9999', {'Old_Name': 'AP99', 'New_Name': 'sithlord.meetingrm.ap19', 'wlc': '198.18.134.999'}],
 ['5c5a.c7f0.7716', {'Old_Name': 'AP2', 'New_Name': 'sithlord.meetingrm.ap1', 'wlc': '198.18.134.100'}]]

------------AP Inverntoy for testing--------------------
ap_inv = {'AP78BC.1ADB.C70E': {'hostname': 'AP78BC.1ADB.C70E', 'platformId': 'AIR-AP3802I-B-K9', 'mgmntIP': '198.18.128.61', 'associatedWlcIp': '198.18.134.100', 'instanceUuid': 'f82c846d-c394-40a9-ac5e-8c5023354c8e', 'location': None}, 'AP5C5A.C7F0.785E': {'hostname': 'AP5C5A.C7F0.785E', 'platformId': 'AIR-AP3802I-B-K9', 'mgmntIP': '198.18.128.65', 'associatedWlcIp': '198.18.134.100', 'instanceUuid': 'ab623191-5b37-4f80-bda6-2c769e620484', 'location': None}}

------------WLC wlc_inv ----------------------------------
wlc_inv = [[{'hostname': 'C9800-WLC', 'platformId': 'C9800-CL-K9', 'mgmntIP': '198.18.134.100', 'location': None, 'instanceUuid': '32c2efca-57d6-47e7-bcc2-c89f1ccbfa0a'}], [{'hostname': 'AP78BC.1ADB.C70E', 'platformId': 'AIR-AP3802I-B-K9', 'mgmntIP': '198.18.128.61', 'associatedWlcIp': '198.18.134.100', 'instanceUuid': 'f82c846d-c394-40a9-ac5e-8c5023354c8e', 'ethMacAddress': '78:bc:1a:db:c7:0e', 'location': None}, {'hostname': 'AP5C5A.C7F0.785E', 'platformId': 'AIR-AP3802I-B-K9', 'mgmntIP': '198.18.128.65', 'associatedWlcIp': '198.18.134.100', 'instanceUuid': 'ab623191-5b37-4f80-bda6-2c769e620484', 'ethMacAddress': '5c:5a:c7:f0:78:5e', 'location': None}]]