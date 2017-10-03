import pandas
import pandasql

def select_first_50(fileName):
    aadhaar_data = pandas.read_csv(fileName)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = 'SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50'

    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

if __name__ == '__main__':
    fileName = '/Users/maiq/Code/data-science-project/resources/aadhaar_data.csv'
    print(select_first_50(fileName))