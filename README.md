# mongocsv
Python script to import a csv file into a MongoDB with CLI
Your CSV MUST HAVE at the first line your fieldsnames !

# How to use
The script can be called with python as :
```bash
python .\csvimport.py -f /path/to/csvfile.csv -c mongo_collection -d mongo_database -a localhost -p 27017 [-delim ','] [-encod 'utf-8'] [-t str, str, str] 
```

## flags
### Required
| -flag  | --fullflag  | DESCRIPTION                                                               |
|--------|-------------|---------------------------------------------------------------------------|
| -f     | --file      | the path to the csv file                                                  |
| -c     | --collection| the mongo collection you want to insert datas                             |
| -d     | --database  | the mongo database                                                        |
| -a     | --address   | the address of the mongo server                                           |
| -p     | --port      | the port of the mongo server                                              |


### Optionals
| -flag  | --fullflag  | DESCRIPTION                                                               | Default value                    |
|--------|-------------|---------------------------------------------------------------------------|----------------------------------|
| -delim | --delimiter | the delimiter string which delimits the differents csv components         | ','                              |
| -rk    | --restkey   | the name of the key which will contains values overflowing the fieldsname | 'restkey'                        |
| -rv    | --restvalue | the default value when a value is not found or given for a fieldname      | None                             |
| -encod | --encoding  | the encoding of your csv file                                             | 'utf-8'                          |
| -t     | --type      | a list of string of types of the fields for fieldsname                    | will turn unfound type to string |
