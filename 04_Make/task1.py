import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here

print(ipAddresses)

count4 = 0
count6 = 0
count0 = 0

reg4 = re.

for ip in ipAddresses:
    if ip == reg4:
        count4 +=1
    elif ip == reg6:
        count6 +=1
    else:
        count= += 1