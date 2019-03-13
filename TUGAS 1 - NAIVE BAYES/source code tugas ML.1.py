import csv
import collections
import numpy as N

def BacaFile(): #membaca data train
    with open('TrainsetTugas1ML.csv') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        dataTrain = [] #array penampung data Train
        for row in reader:
            dataTrain.append(row[1:])
        return dataTrain

def BacaTest(): #membaca data Test
    with open('TestsetTugas1ML.csv') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        dataTest = [] #array penampung data Train
        for row in reader:
            dataTest.append(row[1:7]) #membaca data dari 1-7
        return dataTest
    
def BandingData(data):  #fungsional membandingkan data train 
    L50 = []    #L50 data yang lebih dari 50 Ribu
    K50 = []    #K50 data yang kurang dari 50 Ribu
    for x in data:
        if(x[7] == '>50K'):
            L50.append(x)
        else:
            K50.append(x)
    return L50, K50

def Peluang(n):
    Peluang = N.transpose(n)  #PELUANG  #syntax
    ArrayPeluang = []  #Untuk menyimpan hasil data peluang
    for i in Peluang[:7]:
        dataPeluang = collections.Counter(i) 
        for j in dataPeluang:
            dataPeluang[j] = dataPeluang[j] / len(n) 
        ArrayPeluang.append(dataPeluang)
    return ArrayPeluang

SAVE=[]
HasilTrain = BacaFile()
HasilTest = BacaTest()
L50, K50 = BandingData(HasilTrain)
PeluangL = len(L50)/len(HasilTrain) #membagi peluang yang lebih dari 50 dengan seluruh jumlah data train
PeluangK = len(K50)/len(HasilTrain) #membagi peluang yang kurang dari 50 dengan seluruh jumlah data train

PeluangLebih50 = Peluang(L50)
PeluangKurang50 = Peluang(K50)
Hasil = [] #array untuk menyimpan hasil dari operasi

for i in HasilTest:
    Lebih50 = PeluangL
    Kurang50 = PeluangK
    for j in range(0, 6):
        Lebih50 = Lebih50 * PeluangLebih50[j][i[j]]
        Kurang50 = Kurang50 * PeluangKurang50[j][i[j]]
    if(Lebih50 > Kurang50):
        print('>50K')
        Hasil.append('>50K')
    else:
        print('<=50K')
        Hasil.append('<=50K')
SAVE.append(Hasil)

with open('TebakanTugas1ML.csv', mode='w') as file:  #untuk mengsave data kedalam file excel
            writer = csv.writer(file, delimiter='.', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            i = 1                           #memberi nomor pada data
            for hasil in SAVE:
                writer.writerow([i, hasil])
                i +=1
