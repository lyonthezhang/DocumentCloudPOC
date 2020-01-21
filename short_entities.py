import json
from documentcloud import DocumentCloud
import time
import operator

client = DocumentCloud()
entities = []
titles = []
count=0
d = ['5839910-Illinois-Medical-District-Commission-2016-05-17','5839914-Illinois-Medical-District-Commission-2016-07-19','5839918-Illinois-Medical-District-Commission-2016-09-20']

for i in d:
	active_id = i
	doc = client.documents.get(active_id)
	entity = doc.entities
	title = doc.title
	entities.append(entity)
	titles.append(title)

	if count == 5000:
		break
	count += 1
	print(count)

entities_dict = {}
for i in entities:
	for j in i:
		entity_name = j.value
		try:
			entities_dict[entity_name] += 1
		except:
			entities_dict[entity_name] = 1

sorted_x = sorted(entities_dict.items(), key=operator.itemgetter(1))
print("10 LEAST REFERENCED ENTITIES:")
for i in range(10):
	print(sorted_x[i])
print("10 MOST REFERENCED ENTITIES:")
for i in range(10):
	print(sorted_x[-(i+1)])
