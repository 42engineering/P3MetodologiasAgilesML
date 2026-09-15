from scripts.data_acquisition.data_acquisition_tsla import dataTeslaCsv

def main():
    
    df = dataTeslaCsv()
    print(df.head())

if __name__ == "__main__":
    main()
    