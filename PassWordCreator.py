import base64
import hashlib
def GetPassWord(web, ID, code):
        Pw = hashlib.md5()
        Pw.update(web.encode("utf8"))
        Pw.update(ID.encode("utf8"))
        Pw.update(code.encode("utf8"))
        Pw.update('陈'.encode("utf8"))
        Pw.update('420116'.encode("utf8"))
        str = Pw.hexdigest()
        flag = [False for x in range (0, len(str))]
        ans = ""
        for i in range (len(str)):
                if flag[i]:
                        ans += str[i].upper()
                else:
                        ans+= str[i]
                if str[i].isdigit():
                        j = i +int(str[i])
                        if  j < len(str):
                                flag[j] = True
        print ('\n\n'+ans[6:21]+'\n\n')
while(True):
        web = input('输入要取密码的网站: ')
        ID = input('输入要取密码的账号: ')
        code = input('输入密钥: ')
        GetPassWord(web,ID,code)
        opt = input('继续？（Y/N）')
        if opt.upper() == 'N':
                break;
