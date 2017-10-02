import pandas


def simple_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_id, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'male':
            predictions[passenger_id] = 0
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1

    return predictions

if __name__ == '__main__':
    print(simple_heuristic('/Users/maiq/Code/data-science-project/resources/titanic_data.csv'))
