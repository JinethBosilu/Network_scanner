import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print("IP\t\t\tMAC Address\n.........................................")
    # for element in answered:
    #     print(element[1].psrc + "\t\t" + element[1].hwsrc)

    client_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n.........................................")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

def get_user_input():
    ip = input("Enter the IP range to scan: ")
    if ip == "":
        print("Please enter a valid IP range.")
        exit()
    return ip

user_ip = get_user_input()
results = scan(user_ip)
print_result(results)
