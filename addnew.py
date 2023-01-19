import os
path = 'C:\\Users\\sparky\\onedrive\\desktop\\box\\scripts'

a = input('New Item is called?\\n').rstrip()
b = input('Description\\n').rstrip()

info = path + 'myhelp.ps1'

info1 = open(info, 'a')
info1.write('echo ' + a + ': ' + b)
info1.close()
#add to profile
pro = open('C:\\Users\\sparky\\OneDrive\\Documents\\PowerShell\\Microsoft.PowerShell_profile.ps1', 'a')
pro.write('set-alias ' + a + ' -Value ' + 'C:\\Users\\Sparky\\OneDrive\\Desktop\\box\\scripts\\' + a + '.ps1')
#create item
os.system('notepad ' + path + '\\' + a + '.ps1')
