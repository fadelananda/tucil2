# Nama  : Fadel Ananda Dotty
# NIM   : 13519146
# Kelas : K-03

# Asumsi test case sudah DAG (tidak ada syclical graph)
def topologicalSort(vertex, connectedTo, numberOfConnectedVertex):
    semester = 0
    while(len(vertex)!=0 and semester<8):
        solution = [] #berisi solusi dari permasalahan
        for i in range(len(numberOfConnectedVertex)): #cari yang derajat 0 masukkan ke list solusi sementara
            if(numberOfConnectedVertex[i] == 0):
                solution.append(vertex[i])

        for i in range(len(connectedTo)):
            try:
                connectedTo.remove([]) #remove list connectedTo yang isinya kosong
            except ValueError: #error handling jika tidak ada elemen
                1

        for element in connectedTo: #menghapus dari list connectedTo yang sama dengan list solusi sementara
            for i in range(len(solution)):
                try:
                    element.remove(solution[i])
                except ValueError: #error handling jika tidak ada elemen
                    1

        for i in range(len(solution)): #menghapus dari list connectedTo
            try:
                vertex.remove(solution[i])
            except ValueError: #error handling jika tidak ada elemen
                1

        for i in range(len(numberOfConnectedVertex)): #mengurangi indeks dengan elemen sama dengan 0
            try:
                numberOfConnectedVertex.remove(0)
            except ValueError: #error handling if gaada elemen
                1

        for i in range(len(numberOfConnectedVertex)): #assign list numberOfConnectedVertex dengan panjang list connectedTo yang baru
            numberOfConnectedVertex[i] = len(connectedTo[i])

        print("Semester", semester+1 ,"mahasiswa dapat mengambil matkul: ", solution) #solusi
        semester += 1

def createGraph(filename):
    listMatkul = open("../test/"+filename, "r").readlines() #membuka file dan memasukkannya ke array listMatkul

    vertex = [] #berisi semua simpul unik yang ada pada soal
    connectedTo = [] #berisi simpul yang bertetangga dengan simpul di list vertex
    numberOfConnectedVertex = [] #berisi derajat masuk simpul2 yang ada

    for i in range(len(listMatkul)): #mencari semua vertex dari text file dan dimasukkan ke dalam vertex
        stored = []
        listMatkul[i] = listMatkul[i].strip().replace('.', '').replace(' ', '').rsplit(",")
        for j in range(len(listMatkul[i])):
            if(j!=0):
                stored.append(listMatkul[i][j])
            else:
                vertex.append(listMatkul[i][j])
        numberOfConnectedVertex.append(len(stored))
        connectedTo.append(stored)
    print("--------------------------------------------------------------------------------------------\n")
    print("Simpul-simpul yang ada pada graf: ", vertex)
    for i in range(len(vertex)):
        print("Simpul lain yang masuk ke dalam simpul ", vertex[i], " :", connectedTo[i])
    print("")
    print("--------------------------------------------------------------------------------------------\n")
    print("Jumlah derajat masuk masing2 simpul:", numberOfConnectedVertex)
    print()
    print("--------------------------------------------------------------------------------------------")

    print("Matkul yang dapat diambil :")
    return vertex, connectedTo, numberOfConnectedVertex

#Main Program
filename = input("Masukkan nama file: ")
try:
    vertex, connectedTo, numberOfConnectedVertex = createGraph(filename)
    semester=0 #semester

    #Topological Sort
    topologicalSort(vertex, connectedTo, numberOfConnectedVertex)

except:
    print("File tidak ditemukan")