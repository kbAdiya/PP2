import json

print("Interface Status")
print("================================================================================")
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

with open("C:\\Users\\Lenovo\\Desktop\\python\\lab4\\sample-data.json", "r") as file:
    data = json.load(file)
    for item in data['imdata']:
        dn = item['l1PhysIf']['attributes']['dn']
        speed = item['l1PhysIf']['attributes'].get('speed', 'inherit')
        mtu = item['l1PhysIf']['attributes'].get('mtu', '')
        print("{:<50} {:<20} {:<8} {:<6}".format(dn, "", speed, mtu))



