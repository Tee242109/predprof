File = open('products.csv', encoding = "UTF-8")
st = []

for i in File:
	st.append(i.split(';'))

alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧЦШЩЪЫЬЭЮЯ'
#print(st1)
total = 0
i = 0
for j in (2, alf):
    if i < len(st):
        i += 1
        baf = st[i][0]
        #print(baf[0])
        if baf[0] in alf:
            for i1 in range(1, len(st)-1):
                for j1 in range(len(st)-2, i -1, -1):
                    if st[j] < st[j+1]:
                        st[j], st[j+1] = st[j+1], st[i]

                        
for i in range(1, len(st)):         
    total = (int(str(st[i][3][:-2])) * int(str(st[i][4][:-3])))
    #print(total)
    st1 = st.append(int(total))
   
    
    

print(st1)

File.close()
