#!/usr/bin/env python
def char_freq(str1):
	frequency_in_english = {'a':0.080,'h':0.060,'n':0.070, 't':0.090,'b':0.015,'i':0.065,'o':0.080,'u':0.030,'c':0.030,'j':0.005,'p':0.020,'v':0.010,'d':0.040,'k':0.005,'q':0.002,'w':0.015,'e':0.130,'l':0.035,'r':0.065,'x':0.005,'f':0.020,'m':0.030,'s':0.060,'y':0.020,'g':0.015,'z':0.002}
 	dict={}
 	for i in str1:
 		if i in dict.keys():
 			dict[i]+=1
 		else:
 			dict[i]=1
 	print dict
 	freq_in_text={k : v * frequency_in_english[k] for k, v in dict.items() if k in frequency_in_english}
 	return freq_in_text
print(char_freq('qebmxpptloafpnnwwnnw'))
'''	
iterate through dict, if the key in dict matches key in frequency, then muptiply their values together and return
input the frequencies into formula below and run!
'''	
sum = 0.0
for i in range(1,27):
	sum = (.05*.08*((0.0-i)%26))+ \
	(0.05*.15*((1.0-i)%26))+ \
	(0.05*.04*((3.0-i)%26))+ \
	(0.05*.02*((5.0-i)%26))+ \
	(0.05*.035*((11.0-i)%26))+ \
	(0.05*.03*((12.0-i)%26))+ \
	(0.2*.07*((13.0-i)%26))+ \
	(0.05*.08*((14.0-i)%26))+ \
	(0.15*.02*((15.0-i)%26))+ \
	(0.05*.002*((16.0-i)%26))+ \
	(0.05*.09*((19.0-i)%26))+ \
	(0.15*.015*((22.0-i)%26))+ \
	(0.05*.005*((23.0-i)%26))
	print i,": ",sum
sum = 0