import pandas as pd
def generateCSV(list_of_jobs):
    print("Generating CSV")
    df = pd.DataFrame.from_dict(list_of_jobs) 
    df.to_csv (r'biojobs.csv', index = False, header=True)