My_Database={}
My_data=[]
Select=""

def file_Write():
  for Key,Value in My_Database.items():
    file.write(f'{Key}: {Value}\n')
  return

def duplication():
  seen=[]
  for key in My_Database:
    for val in My_Database[key]:
      if val not in seen:
          seen.append(val)
    Read_Value=seen
    My_Database[key]=Read_Value
    seen=[]
  return

def insert():
  My_data=[]
  chose=input("'TUPLE'name: ")
  My_data.append(input("Data/exit:"))
  while My_data[-1]!="exit":
    My_data.append(input("Data/exit:"))
    if not(chose in My_Database.keys()):
      My_Database.update({chose:My_data[:-1]})
    else:
      My_Database[chose]+=My_data[:-1]
      pass
  My_data=[]
  return

def view():
  for key,Value in My_Database.items():
    print(key,":",list(Value))
  return

def join():
  chose1=input("Chose1 'TUPLE: ")
  chose2=input("Chose2 'TUPLE: ")
  NewTuple=input("New TUPLE: ")
  My_Database[NewTuple]=My_Database[chose1]+My_Database[chose2]
  if NewTuple!=chose1:
    del(My_Database[chose1])
  if NewTuple!=chose2:
    del(My_Database[chose2])
  return

def delete():
  chose=input("Chose 'TUPLE: ")
  if chose in My_Database:
    del(My_Database[chose])
    for key,Value in My_Database.items():
      print(key,":",list(Value))
  else:
    print("Not find 'TUPLE'")
  return

{ # def save():
#   while(True):
#     Select=input("File Save(new/next)?:")
#     if Select=="new":
#       file=open("My_DataBase.txt",'w')
#       file_Write()
#       file.close()
#       break
#     elif Select=="next":
#       file=open("My_DataBase.txt",'a')
#       file_Write()
#       file.close()
#       break
#   return
}

def load():
  file = open("My_DataBase.txt", 'r')
  Read_Data=file.readlines()
  file.close()
  for Read_Value in Read_Data:
    Read_Value=Read_Value.strip()
    Read_Key=Read_Value[:Read_Value.find(':')]
    Read_Value=Read_Value[Read_Value.find(':')+4:-2]
    Read_Value=Read_Value.split("', '")

    if Read_Key not in My_Database.keys():
      My_Database.update({Read_Key:Read_Value})
    else:
      My_Database[Read_Key]+=Read_Value
    pass
  return



while(Select!='exit'):
  Select=input("Select[insert/join/duplication/delete/view/exit/load/save]: ")

  if Select == "insert":
    insert()
    view()

  elif Select == "view":
    print("key:",list(My_Database))
    view()

  elif Select == "join":
    join()
    view()

  elif Select == "duplication":
    duplication()

  elif Select == "delete":
    delete()

  elif Select == "exit":
    file = open("My_DataBase.txt", 'a')
    file_Write()
    file.close()
    break

  elif Select == "save":
    while(True):
      Select=input("File Save(new/next)?:")
      if Select=="new":
        file=open("My_DataBase.txt",'w')
        file_Write()        
        file.close()
        break
      elif Select=="next":
        file=open("My_DataBase.txt",'a')
        file_Write()
        file.close()
        break

  elif Select == "load":
    load()
    view()

  else:
    print("Error!")