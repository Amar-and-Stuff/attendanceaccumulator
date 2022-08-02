from datetime import date
import json
import calendar
data_file = open("data.json","r")
data = json.load(data_file)
data_file.close()
dt = date.today()
if data["todaysdate"] == dt.strftime("%d%m%Y"):
    print("Today is done")
else:
    sub_list = data['time_table'][calendar.day_name[dt.weekday()]]
    print("todays subjects are ",sub_list)
    print("0 - absent, 1 - no class, 2 - present")
    for i in sub_list:
        attendance_for_sub = input(i+" : ")
        data["attendance"][i]["attendancesequence"] += attendance_for_sub
        if attendance_for_sub != 1:
            data["attendance"][i]["totoalclasses"] += 1
            if attendance_for_sub == 2:
                data['attendance'][i]['classespresent'] += 1
    for i in data["subjects"]:
        if i in sub_list:
            continue
        data["attendance"][i]["attendanceseqence"] += "1"
    print("program attendance taken")
    data['todaysdate'] = dt.strftime("%d%m%Y")
    with open("data.json","w") as outfile:
        outfile.write(json.dumps(data,indent=4))

print("End of program")
