def parse_int_brief():
    """
    Function will parse the output of "show ip int brief" and count the number of interfaces up and down.
    Params:
        cmd_output: the output of the "show ip int brief" command (at the moment it takes none; using a local file for testing).
    Returns:
        Python dictionary 
        ex:
            {"up" : 4, "down" : 2}
    """
    
    interface_data = open("int_brief.txt", "r")  # text file for testing (with interface brief data)

    total_int_up_down = {"up" : 0, "down" : 0} # initializes dict with counters

    header = interface_data.readline() # basically skipping the file handler to the next line

    for line in interface_data:
        interface = line.split()
        # print(interface)
        if interface[-2] == "up" and interface[-1] == "up":
            # print("{} is up".format(interface[0]))
            total_int_up_down["up"] += 1
        
        elif interface[-2] == "down" and interface[-1] == "down":
            # print("{} is down".format(interface[0]))
            total_int_up_down["down"] += 1
    
    interface_data.close()
    
    return total_int_up_down
    

# module testing    
if __name__ == "__main__"

    total = parse_int_brief()
    print(total)
