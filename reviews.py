data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1 
		if count % 1000 == 0:
		    print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
#print(data)

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均是', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言的長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到Good')
print(good[0])


good =[d for d in data if 'good' in d]

bad = ['bad' in d for d in data]
print(bad)

bad = []
for = d in data:
	bad.append('bad' in d)
