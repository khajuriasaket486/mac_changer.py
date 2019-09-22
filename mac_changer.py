from subprocess import call
from optparse import OptionParser

def get_options():
    parser=OptionParser()
    parser.add_option('-i','--interface', dest='interface', help="Enter interface name to change its mac-address")
    parser.add_option('-m','--mac',dest='new_mac', help="Enter new mac-address")

    (options,arguements)=parser.parse_args()
    if not options.interface:
        parser.error("[-]no valid interface-name")
    elif not options.new_mac:
        parser.error("[-]No valid mac-address")
    return options

def change_mac(interface, new_mac):
    print("[+]Changing mac_address for ", interface , "to new mac_address: ", new_mac)
    call(["ifconfig", interface, "down"])
    call(["ifconfig", interface, "hw ether", new_mac])
    call(["ifconfig", interface, "up"])

options = get_options()
get_options()
change_mac(options.interface, options.new_mac)