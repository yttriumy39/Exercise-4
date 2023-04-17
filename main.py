import glob, pathlib, json, csv, os
from flatten_json import flatten


def main():
    # your code here

    #crawl directory with rglob and find json files
    folder = pathlib.Path(os.getcwd()+"/data")
    filelist = list(folder.rglob("*.json"))
    data = []
    for i in filelist:
        with open(i) as f:
            data.append(flatten(json.load(f)))
    
    #get list of json file names and convert the names to csv names
    fileliststr = [str(x) for x in filelist]
    fileliststr = [x.replace(".json",".csv") for x in fileliststr]

    #convert json files to csv's
    x = 0
    for i in data:
        with open(fileliststr[x], 'w', newline ='') as file:
            writer = csv.writer(file)
            for key, value in i.items():
                writer.writerow([key, value])
        x=x+1

    pass


if __name__ == '__main__':
    main()
