Sepatu = []

# Menu Tampil
def tampil():
    print('-'*40)
    print(" Tampil Barang".center(40, '='))
    print('-'*40)
    index=0
    if len(Sepatu)<=0:
        print('Barang masih kosong')
    else:
        for barang in Sepatu :
            print(str(index)+ "."  +barang)
            index= index+1
            
# Menu tambah 
def tambah():
    print('-'*40)
    print(" Tambah Barang".center(40, '='))
    print('-'*40)          

    Nama_Sepatu = (input('Masukkan nama sepatu :'))+ " ,Ukr " +str(input('Masukkan Ukuran Sepatu : ') )+ " ,Stok " +str(input('Masukkan Jumlah Stok : ') )
    
    Sepatu.append(Nama_Sepatu)
    print('Barang Berhasil ditambahkan')

# Menu Edit
def edit():
    print('-'*40)
    print(" Edit Barang".center(40, '='))
    print('-'*40)
    tambah()
    index=int(input('masukkan index :'))
    
    
    
def menu():
    print('-'*40)
    print(" Pilihan Menu".center(40, '='))
    print('-'*40)
    print('1. Tampil Barang')
    print('2. Tambah Barang')
    print('3. Edit Barang')
    print('4. Hapus Barang')
    
    kode=input('Masukkan Kode :')
    if kode == '1':
        tampil()
    elif kode == '2':
        tambah()
    elif kode == '3':
        edit()
    elif kode == '4':
        hapus()
    else :
        print('Kode salah')
    
while(True):
    menu()



