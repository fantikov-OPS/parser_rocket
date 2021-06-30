import json
import requests



def id_city(rez):
    response = requests.get("https://apigate.tui.ru/api/office/cities/")
    todos = json.loads(response.text)
    test = (todos['cities'])
    rez = []
    for r in range(len(test)):
        rez.append(
            test[r]['cityId'])

    return rez

rez=[]
id_city(rez)
rez=id_city(rez)
# print(rez)

def content(rez):

    for i in rez:
        response=requests.get(f"https://apigate.tui.ru/api/office/list?subwayId=&hoursFrom=&hoursTo=&serviceIds=all&toBeOpenOnHolidays=false&cityId={i}")
        todos = json.loads(response.text)
        test = (todos['offices'])
        print(test)
        rel = []
        for r in range(len(todos['offices'])):
            rel.append(
                {
                    "address": test[r]['address'],
                    "latlon": f"{test[r]['latitude']}, {test[r]['longitude']}",
                    "name": test[r]['name'],
                    "phones": test[r]['phone'],
                    # "working_hours": f"пн-пт{test[r]['startStr']}-{test[r]['endStr']}, сб-вс {test[r]['startStr']} {test[r]['endStr']}"
                }
            )

            print (rel)


content(rez)