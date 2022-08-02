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
    attendence = {
        sub : [no.of presents, noof working days, attendance sequence]
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

data["attendance"] = {}
for sub in data["subjects"]:
    data["attendance"][sub] = {}
    data["attendance"][sub]["classespresent"] = 0
    data["attendance"][sub]["totoalclasses"] = 0
    data["attendance"][sub]["attendancesequence"] = ""



with open("data.json",'w') as datafile:
    datafile.write(json.dumps(data,indent=4))

