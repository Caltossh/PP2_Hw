import json
print("Interface Status")
print("=======================================================================================")
print("DN                                                 Description           Speed   MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

a=open("/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/HW_4/json/json.py")

b = json.load(a)

for i in b["imdata"]:
    print(i['l1PhysIf']['attributes']["dn"], "\t", "\t", i['l1PhysIf']['attributes']['speed'], '\t', i['l1PhysIf']['attributes']['mtu'])




        
        