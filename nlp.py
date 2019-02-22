from nltk.tokenize import BlanklineTokenizer
import text
import nltk

from nltk.corpus import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

import csv
import re
def find_agrees(mails = text.preload(), labels =text.get_label()):
	i = 0
	agreements = []
	while i < len(labels):
		if labels[i] == 0:
			agreements.append(mails[i])

	return agreements



def gnums(parag, word):
	nums = []
	parag_cont = nltk.sent_tokenize(parag)
	for e in parag_cont:
		if word in parag_cont:
			nums = re.finadll('\d+', parag_cont)
			avg = nums.sum()/len(nums)

		for  num in nums:
			if num > 0.5*avg:
				return num
				break






def namedchunks(para):
	chunked  = ne_chunk(pos_tag(word_tokenize(text)))
	continuous_chunk = []
	current_chunk  = []
	for i in chunked:
		if type(i) == Tree:
			current_chunk.append(" ".join([token for token, pos in i.leaves()]))
		elif current_chunk:
			named_entity = " ".join(current_chunk)
			if named_entity not in continuous_chunk:
				continuous_chunk.append(named_entity)
				current_chunk = []

		else:
			continue

	return continuous_chunk





def main(data = find_agrees()):
	csvData = [['Name of Employer', 'Name of Employee', 'Base Salary',  'Stocks', 'Insurance', 'Bonus', 'Vacations']]
	for e in data:
		tempData = []
		names = namedchunks(e)
		tempData.append(names[0])   #name of employer
		tempData,append(names[1])   #name of the employee
		salary = 'NA'
		stocks = 'NA'
		insurance = 'NA'
		bonus = 'NA'
		vacations = 'NA'

		salary = gnums(e, 'SALARY')
		stocks = gnums(e, 'STOCKS')
		insurance = gnums(e, 'INSURANCE')
		bonus  = gnums(e, 'BONUS')
		vacations = gnums(e, 'VACATION')

		tempData.append(salary)
		tempData.append(stocks)
		tempData.append(insurance)
		tempData.append(bonus)
		tempData.append(vacations)


		csvData.append(tempData)


	with open('person.csv', 'w')as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(csvData)

	csvFile.close()

	return True











