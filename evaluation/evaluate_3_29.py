#!/usr/bin/env python
import numpy as np
import os
from utils.acc_cal_v2 import topKaccuracy, evaluate, output_result
from utils.acc_cal_for_interaction import topKaccuracy_temp, evaluate_temp, output_result_temp
from PIL import Image
#import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc

#def evaluate_tmp(predict_matrix,ccmpred_matrix,contact_matrix):
#input_acc=[]
output_acc=[]
#DeepCov_acc=[]
#psicov_acc=[]
#ccmpred_acc=[]
j=0
output_dir='/home/huanghe/huangh/GAN-collection/image-inpainting/Inpainting/workspace_3_28/output_dir'
for filename in os.listdir('/home/huanghe/huangh/GAN-collection/image-inpainting/Inpainting/workspace_3_28/output_dir'):
	temp=filename.split('.')
	name=temp[0]
	length_dir=os.path.join('/home/huanghe/huangh/GAN-collection/image-inpainting/Inpainting/workspace_3_28/length_dir',name+'.txt')
#	fasta_file=os.path.join('/home/huanghe/huangh/inter_protein_contact_prediction_data_prepare/dc_train/feature_contact_matrix/ccmpred/',name+'.ccmpred')
#	temp_matrix=np.loadtxt(fasta_file)
#	ccmpred_matrix=temp_matrix
	length=np.loadtxt(length_dir)
	L1=length[0]
	L2=length[1]
	l1=int(L1)
	l2=int(L2)
	L=l1+l2
#	L=temp_matrix.shape[1]
#	ccmpred_matrix_name=fasta_file
#	DeepCov_matrix_name=os.path.join('./feature_2_21/feature_contact_matrix/DeepCov',name+'.matrix')
#	psicov_matrix_name=os.path.join('./feature_2_21/feature_contact_matrix/psicov',name+'.matrix')
#	true_image_name=os.path.join('/home/huanghe/huangh/GAN-collection/image-inpainting/Inpainting/workspace_3_19/true_dir',name+'.txt')
	output_image_name=os.path.join('/home/huanghe/huangh/GAN-collection/image-inpainting/Inpainting/workspace_3_28/output_dir',name+'.jpg')
#	predict_matrix_file=os.path.join(output_dir,name+'-outputs.png')
#	ccmpred_matrix=os.path.join('./TEST.1.7/images/',name+'-inputs.png')
#	contact_matrix_file=os.path.join('./hh_2_21_1/images/',name+'-targets.png')
#	true_matrix_file_gray=Image.open(true_image_name).convert('L')
#	true_matrix_file_temp=misc.imresize(true_matrix_file_gray,[L,L],interp='nearest')
#	true_matrix=np.array(true_matrix_file_temp)
	output_matrix_file_gray=Image.open(output_image_name).convert('L') 
        output_matrix_file_temp=misc.imresize(output_matrix_file_gray,[L,L],interp='nearest')
        output_matrix=np.array(output_matrix_file_temp)
#	true_sub_matrix=true_matrix[:l1,l1:L]
	output_sub_matrix=output_matrix[:l1,l1:L]
	true_matrix_name=os.path.join('/home/huanghe/huangh/GAN-collection/image-inpainting/Inpainting/workspace_3_28/pre_input_dir',name+'.txt')
	true_matrix=np.loadtxt(true_matrix_name)
	true_sub_matrix=true_matrix[:l1,l1:L]
#	matrix_A_B_name=os.path.join('/home/huanghe/huangh/bioinfo_hh/Complex_Tool/contact_1_14/',pdb_name+'_'+chain_A+'_'+chain_B+'.contact_matrix')
#	contact_matrix_file_temp=misc.imresize(contact_matrix_file,[L,L],interp='nearest')
#	contact_matrix_file_temp
#	im1=Image.open(predict_matrix_file_temp)
#	im1=predict_matrix_file_temp
#	im2=Image.open(contact_matrix_file_temp)
#	predict_matrix=np.array(predict_matrix_file_temp)
#	predict_name=os.path.join('/home/huanghe/huangh/bioinfo_hh/deepcontact/result_3_10/',name+'.txt')
	#predict_matrix=np.loadtxt(predict_name)
#	predict_matrix=np.loadtxt(predict_name)
#	contact_matrix=np.array(im2)
#	contact_matrix=np.loadtxt(contact_matrix_name)
	
#	DeepCov_matrix=np.loadtxt(DeepCov_matrix_name)
#	psicov_matrix=np.loadtxt(psicov_matrix_name)
#	DeepCov_acc.append(evaluate(DeepCov_matrix, contact_matrix))
#	psicov_acc.append(evaluate(psicov_matrix, contact_matrix))
#	ccmpred_acc.append(evaluate(ccmpred_matrix, contact_matrix))
#	input_acc.append(evaluate(_matrix, contact_matrix))
	output_acc.append(evaluate_temp(output_sub_matrix,true_sub_matrix))
	print "\n"
	print "*"*50
	print "\nAcc result:%s" %name
	print "*"*50
#	print "\nccmpred result accuracy:" 
#        output_result(ccmpred_acc[j])
#	print "\npsicov result accuracy:"
 #       output_result(psicov_acc[j])
#	print "\nDeepCov result accuracy:"
 #       output_result(DeepCov_acc[j])
        print "\nOutput result accuracy:" 
        output_result_temp(output_acc[j])
#	print "\nDeepCov result:"
#        output_result(DeepCov_acc[j])
        j+=1

#print "Input result:"
#output_result(np.mean(np.array(input_acc), axis=0))
print "\n"*5
print "*"*50
#print "\nccmpred total result:"
#print "*"*50
#output_result(np.mean(np.array(ccmpred_acc), axis=0))
#print "\n"*5
#print "*"*50
#print "\nDeepCov total result:"
#output_result(np.mean(np.array(DeepCov_acc), axis=0))
#print "\n"*5
#print "*"*50
#print "\npsicov total result:"
#output_result(np.mean(np.array(psicov_acc), axis=0))
#print "\n"*5
#print "*"*50
print "\noutput total result:"
output_result_temp(np.mean(np.array(output_acc), axis=0))
