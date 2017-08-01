#author:ch3rry

a = 'a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws'  

b = a.encode('rot13')     #str_rot13()

c = b[::-1]					#第二个strrev()

d = c.decode('base64')		#base64_encode()
g = ''
for i in d:					#substr()
	e = ord(i)-1			#ord()+1
	f = chr(e)				#chr()
	g = g+f
h = g[::-1]					#第一个strrev()  
print h