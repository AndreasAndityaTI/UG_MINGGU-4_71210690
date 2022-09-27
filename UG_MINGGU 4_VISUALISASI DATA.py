#IMPORT LIBRARY
import matplotlib.pyplot as plt

#MENANGANI FILE
nama_file = input("Masukkan nama file data : ")
handle=open(nama_file,'r')
list_data=handle.readlines()

#MENGOLAH DATA
data1=[]
data2=[]
for data in list_data:
    data_kolom=data.split(",")
    data1.append(data_kolom[0])
    data2.append(float(data_kolom[1].strip()))
print(data1)
print(data2)

#target: TANGGAL DAN BANYAKNYA KEJADIAN

#MEMBUAT CHART
plt.plot(data1,data2)
plt.show()