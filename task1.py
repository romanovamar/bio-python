
unique=lambda e: sorted(set(e))
transposeDict=lambda d: {d[key]:key for key in d}
mex=lambda e,i=1: i if i not in e else mex(e,i=i+1)             
frequencyDict=lambda s: {i:d.count(i) for i in d}   


		
