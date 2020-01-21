import json
from documentcloud import DocumentCloud
import time
import operator
import numpy as np

with open('../studio-documenters/data/DocumentCloud/filtered_documents.json') as f:
    d = json.load(f)

client = DocumentCloud()
entities = []
titles = []
urls = []
currtime = time.time()
count = 0
for i in d:
	active_id = i['id']
	doc = client.documents.get(active_id)
	entity = doc.entities
	title = doc.title
	url = doc.canonical_url
	entities.append(entity)
	titles.append(title)
	urls.append(url)

	if count == 20:
		break
	count += 1
	print(count)
	print(time.time()-currtime)

entities_dict = {}
for i in range(len(entities)):
	entity_list = entities[i]
	doc_info = (titles[i],urls[i])
	for j in entity_list:
		entity_name = j.value
		try:
			entities_dict[entity_name][0] += 1
			entities_dict[entity_name].append(doc_info)
		except:
			entities_dict[entity_name] = [1, doc_info]
			print(entity_name)


with open('short_data.json', 'w') as fp:
    json.dump(entities_dict, fp)
# sorted_x = sorted(entities_dict.items(), key=operator.itemgetter(1))
# sorted_x.reverse()

# final = np.reshape(sorted_x,[len(sorted_x),2])
# print(final[1:10,:])
# np.savetxt('test_file.txt',final)
