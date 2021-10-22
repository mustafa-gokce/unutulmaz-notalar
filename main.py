import helper

result = helper.Database.from_database("SELECT DISTINCT makam FROM eserler ORDER BY makam ASC")
print(len(result))
for result in result:
    print(result[0])
