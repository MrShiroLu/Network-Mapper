import pyfiglet

def opening():
    print("="*80)    
    wellcome = pyfiglet.figlet_format("Wellcome To")
    netowkrMapper = pyfiglet.figlet_format("NetowrkMapper", font="slant")
    
    print(wellcome)
    print(netowkrMapper)

    print("It will take a few minutes.")
    print("Please wait for the results.")
    print("Use -p option to specify the port you want to scan. (80-8888 or 80,443,8080)")
    print("Use -a optipn to specify the arguments (eg: -a -T4 -Pn )")
    print("Ex: [host/ip] -p [ports] -a [arguments]\n")