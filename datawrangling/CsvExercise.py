import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    dataFrame = pandas.read_csv(path_to_csv)
    dataFrame['nameFull'] = dataFrame['nameFirst'] + " " + dataFrame['nameLast']
    dataFrame.to_csv(path_to_new_csv)


if __name__ == "__main__":
    path_to_csv = "/Users/maiq/Code/data-science-project/resources/Master.csv"
    path_to_new_csv = "/Users/maiq/Code/data-science-project/resources/NewMaster.csv"
    add_full_name(path_to_csv, path_to_new_csv)
