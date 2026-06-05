import json
from datetime import datetime
class System:
  '''DATA PENTING SYSTEM'''
  def __init__(self):
    self.data = self.loads()
  def loads(self):
    with open('Data.json','r') as file:
      return json.load(file)
  def save(self):
    with open('Data.json','w') as file:
      json.dump(self.data,file)
  def questionTeks(self,x):
    return input(x)
  def questionAngka(self,x):
    while True:
      try:
        return int(input(x))
      except ValueError:
        print('[System]: Only angka ya')
  def saveTran(self,x,y):
    return self.data[x]['history'].append(y)
  
  '''DATA STRUKTUR ATM'''
  def headAtm(self):
    print(self.rapi)
    print(f"{'ATM BCC MOBILE':^28}")
    print(self.rapi)
    print(f'''1. Login
2. Daftar
3. Keluar''')
    pilih = self.questionAngka('Pilih: ')
    return pilih
  def login(self):
    userNot=0
    while True:
      if (userNot<=2):
        print(self.rapi)
        user=self.questionTeks('Masukkan username anda: ')
        if (user in self.data):
          if (self.data[user]['status']=='blokir'):
            print('AKUN ANDA TERBLOKIR')
            print('[SYSTEM]: Restart')
            return
          pwNot=0
          while True:
            pw=self.questionTeks('Masukkan password anda: ')
            if (pwNot<2):
              if (pw==self.data[user]['password']):
                print('\n')
                pilih=self.bodyAtm(user)
                
                return
              else:
                pwNot+=1
                sisa = 3-pwNot
                print(self.rapi)
                print("Password Wrong")
                print(f'Sisa kesempatan anda = {sisa}')
                continue
            print(self.rapi)
            print('[SYSTEM]: AKUN ANDA TERBLOKIR')
            print('[System]: Restart'.upper())
            pwNot=0
            self.data[user]['status']='blokir'
            self.save()
            return
        else:
          print('AKUN TIDAK DITEMUKAN')
          userNot+=1
          continue
      else:
        print(self.rapi)
        print('Silahkan Buat akun baru')
        print('[System]: Restart'.upper())
        userNot=0
        return
  def daftar(self):
    for i in range(5):
      print(self.rapi)
      user=self.questionTeks('Buat username baru anda: ')
      if(len(user)<3):
        print("minimal 3 kalimat")
        continue
      if(not user.replace(" ", "").isalnum()):
        print("Hanya boleh alfabet,spasi,and number")
        continue
        
      if user in self.data:
        print('Username telah dipakai, gunakan username lain')
      else:
        pw=self.questionTeks('Buat password baru anda: ')
        if(len(pw)<3):
          print("minimal 3 kalimat")
          continue
        print('[SYSTEM]: Akun anda sudah tercatat')
        self.data[user]={
          'password': pw,
          'money': 0,
          'history': [],
          'status': 'aman'
        }
        self.save()
        print(self.rapi)
        return
    print('[SYSTEM]: Restart ulang')
        
  '''Menu Atm'''
  def bodyAtm(self,user):
    while True:
      self.sekarang = datetime.now()
      self.time = self.sekarang.strftime("%A, %d %B %Y - %H:%M")
      print(self.rapi)
      print(f"{'ATM BCC MOBILE':^28}")
      print(self.rapi)
      print(f'''Selamat datang {user}
  1. Tarik Saldo
  2. Setor Saldo
  3. Transfer
  4. Cek saldo
  5. Cek History
  6. Clear history
  7. Keluar''')
      pilih = self.questionAngka('Pilih: ')
      if pilih == 7:
        print('Exit')
        return
      self.cabangAtm(pilih,user)
  def cabangAtm(self,pilih,user):
    if (pilih==1):
      self.tarikSaldo(user)
      print('\n')
      print('\n')
    elif (pilih==2):
      self.setorSaldo(user)
      print('\n')
      print('\n')
    elif (pilih==3):
      self.transferSaldo(user)
      print('\n')
      print('\n')
    elif (pilih==4):
      self.cekSaldo(user)
      print('\n')
      print('\n')
    elif (pilih==5):
      self.cekHistory(user)
      print('\n')
      print('\n')
    elif (pilih==6):
      self.clearHistory(user)
      print('\n')
      print('\n')
    else:
      print('MENU TIDAK TERSEDIA')
  def tarikSaldo(self,user):
    self.data=self.loads()
    self.detail=self.data[user]
    print('\n')
    print(self.rapi)
    print(f"{'TARIK SALDO':^28}")
    print(self.rapi)
    money=self.questionAngka('MASUKKAN JUMLAHNYA: Rp.')
    if (self.detail['money']<money):
      print('SALDO ANDA TIDAK MENCUKUPI')
      return
    elif (money<=0):
      print('TARIK TIDAK BOLEH 0')
      return
    else:
      print(f'OKEY UANG SEJUMLAH Rp.{money:,} SUKSES DITARIK ✓')
    sisa= self.detail['money'] - money
    self.detail['money']=sisa
    self.saveTran(user,f'''{self.time}\n|TARIK SALDO|{money:,}
{self.rapi}''')
    self.save()
  def setorSaldo(self,user):
    self.data=self.loads()
    self.detail=self.data[user]
    print('\n')
    print(self.rapi)
    print(f"{'SETOR SALDO':^28}")
    print(self.rapi)
    money=self.questionAngka('MASUKKAN JUMLAHNYA: Rp.')
    if money <= 0:
      print('[SYSTEM]: Tidak boleh kurang dari 0')
      return
    print(f'OKEY UANG SEJUMLAH Rp.{money:,}\nBERHASIL DISETOR KE REKENING ANDA {user.upper()} ✓')
    sisa= self.detail['money'] + money
    self.detail['money']=sisa
    self.saveTran(user,f'''{self.time}\n|SETOR SALDO|{money:,}
{self.rapi}''')
    self.save()
  def transferSaldo(self,user):
    self.data=self.loads()
    detail=self.data[user]
    print('\n')
    print(self.rapi)
    print(f"{'TRANSFER ANGGOTA':^28}")
    print(self.rapi)
    userTemen=self.questionTeks('Masukkan Username yang ingin anda transfer: ')
    if(userTemen==user):
      print('Tidak boleh menggunakan username anda')
      return
    else:
      if(userTemen in self.data):
        namaTemen=userTemen
        tanya=self.questionTeks(f'Apakah benar nama yang anda dituju adalah: {namaTemen}\nKetik [y/n]').lower()
        if(tanya=='n'):
          print('Okey,Silahkan Restart ulang')
          return
        while True:
          money=self.questionAngka('Masukkan jumlah saldo yang ingin ditransfer: Rp.')
          if(money>detail['money']):
            print('SALDO ANDA TIDAK MENCUKUPI')
            continue
          elif(money<=0):
            print('JUMLAH TRANSFER TIDAK BOLEH KURANG DARI 0')
            continue
          print(f'[System]: Sukses Transfer Rp.{money:,} ke {namaTemen}')
          sisaKita=detail['money']-money
          detail['money']=sisaKita
          transfer=self.data[userTemen]['money']+money
          self.data[userTemen]['money']=transfer
          self.saveTran(userTemen,f'''{self.time}\n|MENERIMA TRANSFER SALDO: {user}|{money:,}
{self.rapi}''')
          self.saveTran(user,f'''{self.time}\n|TRANSFER SALDO: {userTemen}|{money:,}
{self.rapi}''')
          self.save()
          return
      else:
        print('Username tidak ditemukan !!!')
  def cekSaldo(self,user):
    self.data=self.loads()
    self.detail=self.data[user]
    print('\n')
    print(self.rapi)
    print(f"{'CEK SALDO':^28}")
    print(self.rapi)
    print(f'''SALDO ANDA SAAT INI = {self.detail['money']:,}''')
  def cekHistory(self,user):
    print('\n')
    print(self.rapi)
    print(f"{'RIWAYAT':^28}")
    print(self.rapi)
    for i in self.data[user]['history']:
      print(i)
  def clearHistory(self,user):
    print('\n')
    print(self.rapi)
    print(f"{'Clear History':^28}")
    print(self.rapi)
    print('Yakin anda ingin clear semua history')
    pilih=self.questionTeks('Ketik [y/n]: ').lower()
    if(pilih=='y'):
      print('OKEY SUKSES CLEAR HISTORY ✓')
      self.data[user]['history']=[]
      self.save()
      return
    print('BATAL SUKSES ✓')
    return
    
  '''TAMPILAN DEKORATIF'''
  rapi = (f'{5*"======":^20}')
  
    
    
  