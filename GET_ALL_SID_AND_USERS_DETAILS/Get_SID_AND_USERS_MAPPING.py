from winreg import *

reg_path = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList"
k = OpenKey(HKEY_LOCAL_MACHINE,reg_path)
n = QueryInfoKey(k)[1]
print(n)

for i in range(n):
    sub_key = EnumKey(k,i)
    new_reg_path = reg_path+'\\'+sub_key
    k1 = OpenKey(HKEY_LOCAL_MACHINE,new_reg_path)
    n1 = QueryInfoKey(k1)[1]
    for i1 in range(n1):
        v = EnumValue(k1,i1)
        print(v)
        if v[0] == 'ProfileImagePath':
            x = v[1].split('\\')
            #print(sub_key,' :: ',x[-1])
