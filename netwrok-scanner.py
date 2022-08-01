from scapy.all import ARP, Ether, srp

print ('''
                     █████                       
                    ░░███                        
  ██████  █████ ████ ░███████   ██████  ████████ 
 ███░░███░░███ ░███  ░███░░███ ███░░███░░███░░███
░███ ░░░  ░███ ░███  ░███ ░███░███████  ░███ ░░░ 
░███  ███ ░███ ░███  ░███ ░███░███░░░   ░███     
░░██████  ░░███████  ████████ ░░██████  █████    
 ░░░░░░    ░░░░░███ ░░░░░░░░   ░░░░░░  ░░░░░     
           ███ ░███                              
          ░░██████                               
           ░░░░░░                                
          ████  ████   ███            █████      
         ░░███ ░░███  ░░░            ░░███       
  ██████  ░███  ░███  ████   ██████  ███████     
 ███░░███ ░███  ░███ ░░███  ███░░███░░░███░      
░███████  ░███  ░███  ░███ ░███ ░███  ░███       
░███░░░   ░███  ░███  ░███ ░███ ░███  ░███ ███   
░░██████  █████ █████ █████░░██████   ░░█████    
 ░░░░░░  ░░░░░ ░░░░░ ░░░░░  ░░░░░░     ░░░░░                                                                                    
''')
print ("Don't forget to visit our website to learn more")
print ("https://cyberelliot.com")

# IP Address for the destination
print("example target ip >>> (192.168.0.1/24)")
target_ip = input(str("please enter target_ip : " ))

# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18 +"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))