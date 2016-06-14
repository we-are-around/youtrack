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
   svn_working_path = '/tmp'
   youtrack_url = 'http://localhost:80'
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

   #yt = Connection('http://v-rot-mne-nogi.myjetbrains.com/youtrack', 'root', 'root') 
   #, proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, 'localhost', 8888))
   yt = Connection(youtrack_url, project_usr, project_pwd)

   #def createProjectDetailed(self, projectId, name, description, projectLeadLogin, startingNumber=1)
   print yt.createProjectDetailed(project_id, project_name, project_desc, project_usr, 1)

   #Create SVN Project with pysvn   
   #svn_cli.add(svn_working_path/project_name)
   #committing the change actually adds the file to the repository
   #svn_cli.checkin(svn_working_path, 'Adding a Directory')

if __name__ == "__main__":
   main(sys.argv[1:])
