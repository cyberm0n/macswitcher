import random
import os
interface = input("[?] Computer Interface (Exm=wlan0) >>>")
new_mac = input("[?] New Mac Adress (Exm=FF:FF:FF:FF:FF:FF) >>>")
os.system("ip link set dev "+interface+" down")
os.system("sudo ip link set dev "+interface+" address "+new_mac)
os.system("ip link set dev "+interface+" down")
