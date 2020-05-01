import ipaddress

f2 = open("resultSuccess.txt","a")
f3 = open("resultFixed.txt","a")
f4 = open("resultFail.txt","a")
with open("data.txt","r") as f:
    for row in f.readlines():
        row = row.replace("\n","")
        row = row.replace(" ","")
        row = row.strip()
        try:
            ipaddress.ip_address(row)
            f2.write(row+"\n")
        except:
            if len(row) == 11 and "." not in row:
                row = row[0:2]+"."+row[2:5]+"."+row[5:8]+"."+row[8:11]
                if ipaddress.ip_address(row):
                    print (row)
                    f3.write(row + "\n")
            else:
                f4.write(row + "\n")
