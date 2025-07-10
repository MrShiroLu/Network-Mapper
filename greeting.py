import pyfiglet

def opening():


    print("-"*80)    
    wellcome = pyfiglet.figlet_format("Wellcome To")
    netowkrMapper = pyfiglet.figlet_format("NetowrkMapper", font="slant")

    print(wellcome)
    print(netowkrMapper)    
    print("It will take a few minutes.")
    print("Please wait for the results.\n")