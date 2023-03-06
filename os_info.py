import platform 
import os 
import socket
import cpuinfo
import webbrowser
my_cpuinfo = cpuinfo.get_cpu_info()
try:
    webbrowser.open('https:cyberyemen.blogspot.com')
    os.system('cls')
    print("""\033[31m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░██████╗░░█████╗░░░██╗███╗░░██╗███████╗░█████╗░░
░██╔══██╗██╔══██╗░░██║████╗░██║██╔════╝██╔══██╗░
░██████╔╝██║░░╚═╝░░██║██╔██╗██║█████╗░░██║░░██║░
░██╔═══╝░██║░░██╗░░██║██║╚████║██╔══╝░░██║░░██║░
░██║░░░░░╚█████╔╝░░██║██║░╚███║██║░░░░░╚█████╔╝░
░╚═╝░░░░░░╚════╝░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n""")
    print("\033[32m|-------[\033[31mBy : @YM_RX  \033[32m-\033[31m @DeadKurd\033[32m]-------| ")
    print('\033[31m===============================================')
    print(f"\033[31m| Python Version  :\033[32m ",my_cpuinfo['python_version'])
    print(f"\033[31m| Arch  : \033[32m",my_cpuinfo['arch'])
    print(f"\033[31m| IP System :\033[32m {socket.gethostbyname(socket.gethostname())}")
    print('===============================================')
    print(f"\033[31m| Architecture :\033[32m {platform.architecture()[1]} : {platform.architecture()[0]} ")
    print(f"\033[31m| Machine Type :\033[32m {platform.machine()}")
    print(f"\033[31m| Network Name :\033[32m {platform.node()}")
    print(f"\033[31m| Platform :\033[32m {platform.platform()}")
    print(f"\033[31m| Processor :\033[32m {platform.processor()}")
    print(f"\033[31m| System Release :\033[32m {platform.release()}")
    print(f"\033[31m| System OS :\033[32m {platform.system()}")
    print(f"\033[31m| System Version :\033[32m {platform.version()}")
    print(f"\033[31m| Mac Version :\033[32m {platform.mac_ver()}")
    print(f"\033[31m| Python Version :\033[32m {my_cpuinfo['python_version']}")
    print(f"\033[31m| Windwos Version :\033[32m {platform.win32_ver()[0]} : {platform.win32_ver()[1]} - {platform.win32_ver()[2]} - {platform.win32_ver()[3]}")
    print('\033[31m===============================================')

except Exception as e:
    print(e)
