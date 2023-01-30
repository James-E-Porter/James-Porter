def clean_csv(csv_file):
    # import csv
    import csv
    
    # open the csv file
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    # create a list to store the cleaned data
    cleaned_data = []

    # loop through each row in the data
    for row in data:
        # create a list to store the cleaned row
        cleaned_row = []
        # loop through each element in the row
        for element in row:
            # remove any leading or trailing whitespace
            element = element.strip()
            # remove any extra spaces
            element = element.replace('  ', ' ')
            # remove any commas
            element = element.replace(',', '')
            # add the cleaned element to the cleaned row
            cleaned_row.append(element)
        # add the cleaned row to the cleaned data
        cleaned_data.append(cleaned_row)

    # return the cleaned data
    return cleaned_data
