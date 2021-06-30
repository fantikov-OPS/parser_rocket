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




def content(rez):
    rel = []
    for i in rez:
        response=requests.get(f"https://apigate.tui.ru/api/office/list?subwayId=&hoursFrom=&hoursTo=&serviceIds=all&toBeOpenOnHolidays=false&cityId={i}")
        todos = json.loads(response.text)
        test = (todos['offices'])

        for key in test:
            print(key)
            rel.append( {"address": key["address"],
                         "latlon":f"{key['latitude']} {key['longitude']}",
                         "name":key['name'],
                         "phones":key['phone'],
                         "working_hours":key['hoursOfOperation']
                         })

    with open('second.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(rel, indent=4, ensure_ascii=False))


rez=[]
id_city(rez)
rez=id_city(rez)
content(rez)
