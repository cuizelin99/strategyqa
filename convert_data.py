import json
import sys

json_file = open(sys.argv[1])
creak_lines = json_file.readlines()
out_file = sys.argv[2]

#data = json.load(json_file)

with open(out_file, "w") as outfile:
	outfile.write('[\n')
	for i in range(len(creak_lines) - 2):
		example = creak_lines[i]
		outfile.write('\t{\n')
		data = json.loads(example)
		uid = data['ex_id']
		entity = data['entity']
		sentence = data['sentence']
		label = data['label']
		desc = ""
		if '(' in entity and ')' in entity:
			desc = entity.split('(')[1].split(')')[0]
			entity = entity.split(' (')[0]
		id_line = "\t\t\"qid\": \"{}\",\n".format(uid)
		term_line = "\t\t\"term\": \"{}\",\n".format(entity)
		description_line = "\t\t\"description\": \"{}\",\n".format(desc)
		question_line = "\t\t\"question\": \"{}\",\n".format(sentence)
		answer_line = "\t\t\"answer\": {},\n".format(label)
		fact_line = "\t\t\"facts\": [],\n"
		decomp_line = "\t\t\"decomposition\": [],\n"
		evidence_line = "\t\t\"evidence\": []\n"
		outfile.write(id_line)
		outfile.write(term_line)
		outfile.write(description_line)
		outfile.write(question_line)
		outfile.write(answer_line)
		outfile.write(fact_line)
		outfile.write(decomp_line)
		outfile.write(evidence_line)
		outfile.write('\t},\n')
	example = creak_lines[-2]
	outfile.write('\t{\n')
	data = json.loads(example)
	uid = data['ex_id']
	entity = data['entity']
	sentence = data['sentence']
	label = data['label']
	desc = ""
	if '(' in entity and ')' in entity:
		desc = entity.split('(')[1].split(')')[0]
		entity = entity.split(' (')[0]
	id_line = "\t\t\"qid\": \"{}\",\n".format(uid)
	term_line = "\t\t\"term\": \"{}\",\n".format(entity)
	description_line = "\t\t\"description\": \"{}\",\n".format(desc)
	question_line = "\t\t\"question\": \"{}\",\n".format(sentence)
	answer_line = "\t\t\"answer\": {},\n".format(label)
	fact_line = "\t\t\"facts\": [],\n"
	decomp_line = "\t\t\"decomposition\": [],\n"
	evidence_line = "\t\t\"evidence\": []\n"
	outfile.write(id_line)
	outfile.write(term_line)
	outfile.write(description_line)
	outfile.write(question_line)
	outfile.write(answer_line)
	outfile.write(fact_line)
	outfile.write(decomp_line)
	outfile.write(evidence_line)
	outfile.write('\t}\n')
	outfile.write(']\n')