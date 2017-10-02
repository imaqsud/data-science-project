import pandas as pd

if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print(football['year'])
    print('')
    print(football.year)  # shorthand for football['year']
    print('')
    print(football[['year', 'wins', 'losses']])

if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print(football.iloc[[0]])
    print("")
    print(football.loc[[0]])
    print("")
    print(football[3:5])
    print("")
    print(football[football.wins > 10])
    print("")
    print(football[(football.wins > 10) & (football.team == "Packers")])
