
#MENGIMPORT LIBRARY
import requests 
import json

#MENGAMBIL DATA DARI JSON
url="https://data.covid19.go.id/public/api/update.json"

req=requests.get(url)
if req.status_code!=200:
    print("Terjadi kesalahan saat request data")
    exit()
json_=json.loads(req.content)
json_data=json_['update']['harian']

#MEMASUKKAN JUMLAH DATA, MAKSIMAL BERDASARKAN JUMLAH DATA YANG ADA DI TAMPUNGAN
limit=int(input(f"Masukkan jumlah data yang mau dilihat (max {len(json_data)}) : "))

if limit>len(json_data):
    limit=len(json_data)
  


key_data=[]
kasus_data=[]
sembuh_data=[]
meninggal_data=[]
dirawat_data=[]
print()
data_yang_mau_dilihat=input("Masukkan data yang mau dilihat (kasus,sembuh,meninggal,dirawat) : ")
data_yang_mau_dilihat.lower()

for data in json_data[0:limit]:
    kasus_data.append(data['jumlah_positif']["value"])
    sembuh_data.append(data['jumlah_sembuh']['value'])
    meninggal_data.append(data['jumlah_meninggal']['value'])
    dirawat_data.append(data['jumlah_dirawat']['value'])
    key_data.append(data['key_as_string'])
data1=[]
data2=[]

#APABILA INGIN MELIHAT JUMLAH KASUS
if data_yang_mau_dilihat=="kasus":
    print()
    print("Daerah serta jumlah kasusnya yaitu : ")
    for i in range(limit):
        data1.append(key_data[i])
        data2.append(kasus_data[i])
        print(f"{i+1}# {data1[i][:10]} : {data2[i]}")

#APABILA INGIN MELIHAT JUMLAH YANG SEMBUH
elif data_yang_mau_dilihat=="sembuh":
    print()
    print("Daerah serta jumlah yang sembuh yaitu : ")
    
    for i in range(limit):
        
        data1.append(key_data[i])
        data2.append(sembuh_data[i])
        print(f"{i+1}# {data1[i][:10]} : {data2[i]}")

#APABILA INGIN MELIHAT DATA YANG MENINGGAL
elif data_yang_mau_dilihat=="meninggal":
    print()
    print("Daerah serta jumlah yang meninggal yaitu : ")
    for i in range(limit):
        data1.append(key_data[i])
        data2.append(meninggal_data[i])
        print(f"{i+1}# {data1[i][:10]} : {data2[i]}")
  

#APABILA INGIN MELIHAT DATA YANG DIRAWAT
elif data_yang_mau_dilihat=="dirawat":
    print()
    print("Daerah serta jumlah yang dirawat yaitu : ")
    for i in range(limit):
        data1.append(key_data[i])
        data2.append(dirawat_data[i])
        print(f"{i+1}# {data1[i][:10]} : {data2[i]}")

#MEMASUKKAN DATA KE CSV
nama_file=input("Masukkan nama file (.csv):")
nama_file_csv=nama_file+".csv"
print(f"Nama filenya {nama_file_csv}")
handle = open(nama_file_csv,'w')
for i in range(len(data2)):
    baris = str(data1[i])+','+str(data2[i])+"\n"
    handle.write(baris)
handle.close()
print("Data berhasil disimpan")
