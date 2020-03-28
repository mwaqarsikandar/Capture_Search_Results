
try:
    import csv
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search for query = "Geeksforgeeks"
query = "Geeksforgeeks"
with open('top.csv', 'w', newline='') as file:
    fieldnames = ['Results']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    with open('o.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                str1 = ''.join(row)
                query = str1
                print("TOP 3 SEARCH RESULTS For:" + query)
                writer.writerow({'Results': "For: " + query})
                for j in search(query, tld="co.in", num=10, stop=3, pause=2):
                    writer.writerow({'Results': j})
                    print(j)
