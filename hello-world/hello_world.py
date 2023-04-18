

def print_name(myname : str = ""):
    print(myname)

def print_tram_name(team_name : str = ""):
    print(team_name)

##############
#### Main ####
##############
if __name__ == '__main__':
    print('Hello world')
    print('Print my name')
    myname = 'Chethan'
    print_name(f'My name is : {myname}')

    myteamname = 'Team A'
    print_name(f'My team name is : {myteamname}')
