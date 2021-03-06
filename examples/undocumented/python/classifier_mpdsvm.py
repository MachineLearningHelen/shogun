#!/usr/bin/env python
traindat = '../data/fm_train_real.dat'
testdat = '../data/fm_test_real.dat'
label_traindat = '../data/label_train_twoclass.dat'

parameter_list = [[traindat,testdat,label_traindat,1,1e-5],[traindat,testdat,label_traindat,0.9,1e-5]]

def classifier_mpdsvm (train_fname=traindat,test_fname=testdat,label_fname=label_traindat,C=1,epsilon=1e-5):

	from modshogun import RealFeatures, BinaryLabels
	from modshogun import GaussianKernel
	from modshogun import MPDSVM, CSVFile

	feats_train=RealFeatures(CSVFile(train_fname))
	feats_test=RealFeatures(CSVFile(test_fname))
	labels=BinaryLabels(CSVFile(label_fname))
	width=2.1
	kernel=GaussianKernel(feats_train, feats_train, width)

	svm=MPDSVM(C, kernel, labels)
	svm.set_epsilon(epsilon)
	svm.train()

	predictions = svm.apply(feats_test)
	return predictions, svm, predictions.get_labels()

if __name__=='__main__':
	print('MPDSVM')
	classifier_mpdsvm(*parameter_list[0])
