from subprocess import call
from optparse import OptionParser
from subprocess import check_output
import re

def get_options():
    # Parse arguments and options against it on terminal.
    parser = OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help="Enter interface name to change its mac-address")
    parser.add_option('-m', '--mac', dest='new_mac', help="Enter new mac-address")

    (options, arguments) = parser.parse_args()
    # print(options)
    # print(arguments)
    if not options.interface:
        parser.error("[-]no valid interface-name")
    elif not options.new_mac:
        parser.error("[-]No valid mac-address")
    return options

def change_mac(interface, new_mac):
    # Changes the mac-address.
    print("[+]Changing mac_address for ", interface, "to new mac_address: ", new_mac)
    call(["ifconfig", interface, "down"])
    call(["ifconfig", interface, "hw", "ether", new_mac])
    call(["ifconfig", interface, "up"])

def check_mac(interface, current_mac="00:00:00:00:00:00"):
    # compares new_mac returned by options variable of get_options() function and the one taken from regular expression string.

    interface_info = str(check_output(["ifconfig", interface]))
    changed_mac_addr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_info)
    if changed_mac_addr.group(0) == current_mac:
        print("[+]mac changed successfully to:" + changed_mac_addr.group(0))
    else:
        print("[-] cant change mac")

options = get_options()
change_mac(options.interface, options.new_mac)
check_mac(options.interface, options.new_mac)

