voted = dict()

def check_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = "already voted"
        print('let them vote!')