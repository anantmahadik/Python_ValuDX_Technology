file_read =open("valuedx.txt","r")
data1 = file_read.read()
file_read.close()

file_write = open("valuexd_write.text","w")
file_write.write(data1)
file_write.close()


