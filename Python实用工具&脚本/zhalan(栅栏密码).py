#KIQLWTFCQGNSOO

#!/usr/bin/env python
# -*- coding: utf-8 -*-
e = raw_input('str\n')
elen = len(e)
field=[]
for i in range(2,elen):
            if(elen%i==0):
                field.append(i)

for f in field:
    b = elen / f
    result = {x:'' for x in range(b)}
    for i in range(elen):
        a = i % b;
        result.update({a:result[a] + e[i]})
    d = ''
    for i in range(b):
        d = d + result[i]
    print ': \t'+str(f)+'\t'+',result: '+d