import urllib
import kmp
import iptablexe as ipt
#import findusername

usrname='root'
sqlfh=open('/%s/Desktop/project_waf/sqldatabase/sqlsheet.txt'%(usrname),'r')
sqlread=sqlfh.read()
print(sqlread)
sqlreadlist=sqlread.split('\n')
print(sqlreadlist)

def extract_data(arg_data,s_ip,d_ip):
      data = 'GET /?id=1%20order%20by%201 HTTP/1.1'
      data = arg_data
      flag=None
      if 'GET' in data:
          pos = data.find('GET')
          lpos = data.find('HTTP/1.1')
          required_data = data[pos + 3:lpos].rsplit()
          print(required_data)
          print(urllib.unquote(required_data[0]).decode('utf8'))
          print(s_ip + "  " + d_ip)
          print('\n\n')
          required_data_decoded = urllib.unquote(required_data[0]).decode('utf8')

          for sqldata in sqlreadlist:
              if sqldata is '':
                  continue
              flag = kmp.KMPSearch(sqldata, required_data_decoded)

              if flag is True:
                  print(flag)
                  ipt.iptable_adminblock(s_ip)
                  break
              else:
                  continue


#extract_data('GET /?id=1 HTTP/1.1','800.800.800.800','888.888.888.888')
