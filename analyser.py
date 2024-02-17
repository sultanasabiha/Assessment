import os

#getting the working path
wpath=input(("\nEnter path of log file -- "))
os.chdir(wpath)

#getting the file name and opening it to extract information
lpath=input(("\nEnter log file name -- "))
log=open(lpath)

errors=dict()
timestamps=dict()
users=dict()

for line in log:
    if "ERROR" in line:
        errorkey=line[line.index("ERROR"):len(line)-1]
        timestampkey=line[:line.index("ERROR")]

        if errorkey not in errors:
            errors[errorkey]=1
        else:
            errors[errorkey]+=1
        
        if errorkey not in timestamps:
            timestamps[errorkey]=[]
            timestamps[errorkey].append(timestampkey)
        else:
            timestamps[errorkey].append(timestampkey)
    
    if "User" in line:
        userkey=line[line.index("User"):line.rindex("'")+1]
        useract=line[line.rindex("'")+1:len(line)-1]
        if userkey not in users:
            users[userkey]=[]
            users[userkey].append(useract)
        else:
            users[userkey].append(useract)

max=0
min=float('inf')
most=""
least=""
for key in users:
    if max<len(users[key]):
        max=len(users[key])
        most=key
    if min>len(users[key]):
        min=len(users[key])
        least=key

sum=open("logSummary.txt","w")

sum.write("\n---  UNIQUE ERROR MESSAGES AND THEIR OCCURRENCES  ---\n\n")
for key in errors:
    s=key+" -- "+str(errors[key])+"\n"
    sum.write(s)

sum.write("\n\n---  TIMESTAMPS OF THE ANOMALIES  ---\n\n")
for key in timestamps:
    s=key+" -- "+str(timestamps[key])+"\n"
    sum.write(s)

sum.write("\n\n---  USER ACTIVITY SUMMARY  ---\n\n")
for key in users:
    s="\n"+key+" -- "+str(users[key])+"\n"
    sum.write(s)
s="\nMOST ACTIVE "+most+" with "+str(max)+" activities" +"\n"  
sum.write(s)
s="\nLEAST ACTIVE "+least+" with "+str(min)+" activities" +"\n" 
sum.write(s)

sum.close()
log.close()

print("\nLog file analysed and analysis stored in logSummary.txt")