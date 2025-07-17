from pyfiglet import figlet_format

def opening():
    print("="*80)    
    wellcome = figlet_format("Welcome To")
    netowkrMapper = figlet_format("NetowrkMapper", font="slant")
    
    print(wellcome)
    print(netowkrMapper)

    print("It will take a few minutes.")
    print("Use -p option to specify the ports. (80-8888 or 80,443,8080)")
    print("Use -a option to specify the arguments. (eg:-T4 -Pn)")
    print("Ex: [host/ip] -p [ports] -a [arguments]\n")