X = raw_input()
words = {X}
s_points = 0
k_points = 0

for rtrim in range(len(X)):
	for ltrim in range(len(X)):
		if rtrim == 0:
			#if X[ltrim:] != "":
				words.add(X[ltrim:])
			#print X[ltrim:]
		else:
			#if X[ltrim:-rtrim] != "":
				words.add(X[ltrim:-rtrim])
			#print X[ltrim:-rtrim]

words.remove("")

def word_points(S, sub):
	X = 0
	for i in range(len(S)):
		# Look for substring sub, within orig starting at i
		if S.find(sub, i, i + len(sub)) > -1:
			X += 1
	return X

for i in list(words):
	if len(i) > 0:
		if i[0] in {'A','E','I','O','U'}:
			k_points += word_points(X, i)
		else:
			s_points += word_points(X, i)
	else:
		continue
if k_points > s_points:
	print "Kevin", k_points
elif k_points == s_points:
	print "Draw"
elif k_points < s_points:
	print "Stuart", s_points
else:
	print "error"

	
#BFEREZKMEYKTNZZTCVZRWZSIIRLEUWGXROAHKCRZNZKUUFWEDJVPMGNGDVHNIGUNKDAUFOIYXVMVBNBMLDQAYJSXNJFVZCERKWJXYUHHLYEBBVRQTXJMGVNFKYHHPZGZOLIBDNTHTZPDJNASKAQPCTXETRZBGIPYHZHOUJPBPRCEKTOWENMEHJVEPPKQISJLTWQOLATVIFOBEXUJPMKXGUDFHBEGMFCCUXBJMXFOKRCICSPQQFFJZTIHMLURFCCVZYIPYGDTJXGXSUAHOKLVYFMSHOSMNNIIRAUPFAAOQHLQCTUGCMCQMOQUXMYBQXJVYRIIQENPTMBYVOVPFYDOJKVUWKDHDWYNVDAMUBBPNTEZZSDADELGNILAZTTMUMWGKXPSQDYVTGXWGDLAZQIJADPTFIJSLIDTLEJFJGWMOCPYLAFMVHQHRLGSIQJXQQKJAVBMFKEENTJZWBDTDVUBZHVTDFCLLETZJRMYMIQYVWWUOIVPGTNZFNTDKBVZKKFDTSQTVSRAADPWIMXEEJHBFRDDDXMOYEHCUHSBWZLHVCKZKUTVWGNTEPYPNGCDMFNKWGARVDMLZJDPIKLWYULIMBOHVOSWZICGZGBKBODQCVIAVTDZQFYLCRWIQBBGMGGERSLPGYASHNYRVVWAVJYASVATKHQNJNYFCUDXKRDNBWHLRIOFVHVFOJQGGAMKNOVDVKJVBRNAIUBZQEBPWKXZUCIRQDRTRGWKTYIJZNBRGQYKOAQCPCRKKXPAAHWLKSJUJZOOIQCSBPDCWHANQPWSIYDBZFCIEWZKYOMMHCHONSOGVMEGGOUKXLGFVOUSIYFFLZAPTLJYWIQVXZZPYVTAOQFQURGULWGFKBYIKJOCSITSBFRIJINCOBHGZRSFYTXFQRFYCIDLXFCASUQAYTHGNBPFTXLUZIXHNXFJIJQABSGNQDOAWXIDSSMLPHHQXYJGVXEJVDVJNCLLBDAYUQFDRGFAAWMAWZZVDAPLHYDU
#Stuart 406312

#NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN
	#Stuart 7501500