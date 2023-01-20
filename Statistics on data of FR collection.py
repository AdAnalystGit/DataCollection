import json

with open('allExtractForExp.json') as json_data:
    data_dict = json.load(json_data)


with open('ExperimentsData6personas.json') as all_data:
    all_data_dict = json.load(all_data)


for element in data_dict['ads']:

    NotPersonalisedVideos = element['NotPersonalisedVideos']
    for ele in NotPersonalisedVideos:
        for element2 in all_data_dict['ads']:
            NotPersonalisedVideos2 = element2['NotPersonalisedVideos']
            for ele2 in NotPersonalisedVideos2:
                if ele['contextual'] == ele2['contextual'] and ele['title'] == ele2['title']:
                     ele['type'] =  ele2['type']
                     break
advertisersAll = []
uniqueadverts = {}

profile = 3
for element in data_dict['ads']:

    advertisersOther = []
    advertisersKids = []
    gap = 0
    NotPersonalisedVideos = element['NotPersonalisedVideos']

    for ele in NotPersonalisedVideos:
        if ele['contextual'] == True and 'other' in ele['type'] and ele['advertiser'] not in advertisersOther :
            advertisersOther.append(ele['advertiser'])
        if ele['contextual'] == True and 'YK' in ele['type'] and ele['advertiser'] not in advertisersKids:
            advertisersKids.append(ele['advertiser'])
    for ele in advertisersKids :
        if ele in advertisersOther:
            gap += 1
    print('Profile ',profile,' has ',gap ,' same advertisers between kids content (',len(advertisersKids),' advertisers) and adulte content (',len(advertisersOther)," advertisers )")
    profile +=1


for element in data_dict['ads']:
    advertisers = []
    NotPersonalisedVideos = element['NotPersonalisedVideos']

    for ele in NotPersonalisedVideos:
        if ele['contextual'] == True and 'other' in ele['type'] and ele['advertiser'] not in advertisers :
            advertisers.append(ele['advertiser'])
        if ele['contextual'] == True and 'YK' in ele['type']:

            if ele['advertiser'] not in uniqueadverts:
                uniqueadverts[ele['advertiser']] = 1
            else :  uniqueadverts[ele['advertiser']] += 1
    advertisersAll.append(advertisers)

#print("unique advertiser",json.dumps(uniqueadverts))

#overlap between 1 and 2
overlap12 = 0
for element in advertisersAll[0]:
    if element not in advertisersAll[1]:
        overlap12+=1

for element in advertisersAll[1]:
    if element not in advertisersAll[0]:
        overlap12+=1
print ("overlap 3 and 5 ",overlap12,(len(advertisersAll[1])+ len(advertisersAll[0]) ))

overlap13 = 0
for element in advertisersAll[0]:
    if element not in advertisersAll[2]:
        overlap13+=1

for element in advertisersAll[2]:
    if element not in advertisersAll[0]:
        overlap13+=1
print ("overlap 3 and 4 ",overlap13,(len(advertisersAll[2])+ len(advertisersAll[0]) ))

overlap23 = 0
for element in advertisersAll[1]:
    if element not in advertisersAll[2]:
        overlap23+=1

for element in advertisersAll[2]:
    if element not in advertisersAll[1]:
        overlap13+=1
print ("overlap 4 and 5 ",overlap23,(len(advertisersAll[2])+ len(advertisersAll[1]) ))



overlap123 = 0
for element in advertisersAll[1]:
    if element not in advertisersAll[2] and element not in advertisersAll[0]:
        overlap123+=1

    else : print(element)

for element in advertisersAll[2]:
    if element not in advertisersAll[1] and element not in advertisersAll[0]:
        overlap123+=1
    else : print(element)

for element in advertisersAll[0]:
    if element not in advertisersAll[1] and element not in advertisersAll[2]:
        overlap123+=1
    else : print(element)



print ("overlap 3 and 4 and 5 ",overlap123,(len(advertisersAll[2])+ len(advertisersAll[1]) + len(advertisersAll[0]) ))


json_data_write = json.dumps(data_dict)
with open("resultat2311.json", "w") as outfile:
    outfile.write(json_data_write)