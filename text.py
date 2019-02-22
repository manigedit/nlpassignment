import os
import cPickle
import numpy


from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif



cwd =  os.getcwd()


path = cwd + '/document-analytics/employment contracts'


files = []

for filename in os.listdir(path):
	files.append(filename)



def preload(filelist = files):
	features = []

	for file in filelist:
		words_file = path + '/' + file

		temp = ""


		with open(words_file) as infile:
			for line in infile:
				temp += line

		features += [temp]




	return features






def get_label(filelist = files):
	labels = []

	#employment agreement = 0 and ammendment =1

	for file in files:
		if 'AMEND' in file:
			labels.append(1)

		else:
			labels.append(0)

	return labels
