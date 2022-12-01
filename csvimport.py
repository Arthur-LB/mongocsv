import argparse
import csv
import pymongo

"""
This script imports a CSV file into a MongoDB collection.
"""
if "__main__" == __name__:
    # Build the parser
    my_parser = argparse.ArgumentParser(description='Python script to import csv file to mongoDB Get the csv file from the command line Get the collection name from the command line Get the database name from the command line Get the host name from the command line Get the port number from the command line exemple: node csvimport.js -f file.csv -c collection -d database -h localhost -p 27017')
    # Add the arguments
    my_parser.add_argument('-f', '--file', metavar='file', type=str, help='file', required=True)
    my_parser.add_argument('-c', '--collection', metavar='collection', type=str, help='collection', required=True)
    my_parser.add_argument('-d', '--database', metavar='database', type=str, help='database', required=True)
    my_parser.add_argument('-a', '--address', metavar='address', type=str, help='address', required=True)
    my_parser.add_argument('-p', '--port', metavar='port', type=str, help='port', required=True)
    my_parser.add_argument('-delim', '--delimiter', metavar='delimiter', type=str, help='delimiter', required=False, default=',')
    my_parser.add_argument('-rk', '--restkey', metavar='restkey', type=str, help='restkey', required=False, default='restkey')
    my_parser.add_argument('-rv', '--restvalue', metavar='restvalue', type=str, help='restvalue', required=False, default=None)
    my_parser.add_argument('-encod', '--encoding', metavar='encoding', type=str, help='encoding', required=False, default='utf-8')
    my_parser.add_argument('-t', '--type', metavar='types', nargs="+" ,type=str, help='type', required=False, default=None)
    # Execute the parse_args() method
    args = my_parser.parse_args()

    toInsert = []
    
    print(args)
    with open(args.file, encoding=args.encoding) as f:
        reader = csv.DictReader(f, delimiter=args.delimiter)
        for row in reader:
            typedRow = {}
            if args.type:
                for field in reader.fieldnames:
                    i = reader.fieldnames.index(field)
                    if not row[field] or not args.type[i]:
                        typedRow[field] = row[field]
                        continue
                    if args.type[i] == 'int':
                        typedRow[field] = int(row[field])
                    elif args.type[i] == 'float':
                        typedRow[field] = float(row[field])
                    elif args.type[i] == 'bool':
                        typedRow[field] = bool(row[field])
                    elif args.type[i] == 'str':
                        typedRow[field] = str(row[field])
            else :
                typedRow = row
            toInsert.append(typedRow)
    
        
    client = pymongo.MongoClient(host=args.address, port=int(args.port))
    db = client[args.database]
    collection = db[args.collection]
    print("Inserting data...")
    x = collection.insert_many(toInsert)
    print("Done.")
    print("Inserted", len(x.inserted_ids), "documents.")
    print("The _ids of the inserted documents are", x.inserted_ids)
    client.close()
    
