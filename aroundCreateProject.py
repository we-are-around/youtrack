#!/usr/bin/python

import sys, getopt
from youtrack.connection import Connection, httplib2
import pysvn

def main(argv):
   project_name = ''
   project_id = ''
   project_desc = ''
   project_usr = 'root'
   project_pwd = 'Sarasa12'
   svn_cli = pysvn.Client()
   try:
      opts, args = getopt.getopt(argv,"hp:i:d:",["project_name=","project_id=", "project_desc="])
   except getopt.GetoptError:
      print 'test.py -p <project_name> -i <project_id> -d <project_desc>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -p <project_name> -i <project_id> -d <project_desc>'
         sys.exit()
      elif opt in ("-p", "--project_name"):
         project_name = arg
      elif opt in ("-i", "--project_id"):
         project_id = arg
      elif opt in ("-d", "--project_desc"):
         project_desc = arg

   #yt = Connection('http://v-rot-mne-nogi.myjetbrains.com/youtrack', 'root', 'root') #, proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, 'localhost', 8888))
   yt = Connection('http://localhost:80', project_usr, project_pwd)


   #print yt.createProjectDetailed('youtrack', 'resttest', 'test', 'test', '1', 'Bug', 'Unknown', 'Open', '', '', '')
   #yt.createProjectDetailed(yt, project_name, project_id, project_desc, project_usr, 1)
   yt.createProjectDetailed(project_name, project_id, project_desc, project_usr, 1)

if __name__ == "__main__":
   main(sys.argv[1:])
