import pandas
import pandasql


def aggregate_query(fileName):
    aadhaar_data = pandas.read_csv(fileName)
    aadhaar_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = 'SELECT gender, district, sum(aadhaar_generated) FROM aadhaar_data WHERE age > 50 GROUP BY gender, district'

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

if __name__ == '__main__':
    fileName = '/Users/maiq/Code/data-science-project/resources/aadhaar_data.csv'
    print(aggregate_query(fileName))