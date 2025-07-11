word1="abcdf"
word2="xyz"
w1=list(word1)
w2=list(word2)
w11 = w1[::-1]
w22 = w2[::-1]
wl1=len(w1)
wl2=len(w2)
wf=[]
for i in range(min(wl1,wl2)):
    
    wf.append( w1[i]+w2[i])

if wl1>wl2:
    for i in range(wl1-wl2):
        wf.append(w1[wl2+i])
elif wl1<wl2:
    for i in range(wl2-wl1):
        wf.append(w2[wl1+i])
wff=''.join(wf)
print(wff)