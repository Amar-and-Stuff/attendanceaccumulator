from datetime import date
import json
'''
    name = name of student
    sem = 5
    start date = sem starting date
    end date = 
    today date = current date
    subjects = []
    time table = {
        day : [subjects]
    }
    periodwiseattendance = {
        date : []
        period : ""
    }

'''

data = {}

data["name"] = input("Enter name : ")
data["sem"] = input("Enter sem : ")
data["start_date"] = date.today().strftime("%d%m%Y")
data['todaysdate'] = data['start_date']
data["subjects"] = list(input("Enter all subjects + labs that consider attendance :").split())
data["time_table"] = {}
for day in ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]:
    data["time_table"][day] = list(input("Enter "+day+" sequence : ").split())

data["periodwiseattendance"] = {}
n = int(input("Enter nubmber clases each day : "))
data["periodwiseattendance"]["date"] = []
for i in range(1,n+1):
    data["periodwiseattendance"]["P"+str(i)] = ""


with open("data.json",'w') as datafile:
    datafile.write(json.dumps(data,indent=4))

