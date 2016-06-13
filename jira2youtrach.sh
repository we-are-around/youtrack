#!/bin/bash

# Edit the following variables
jira_url="<Put your Public Jira URL here>"
youtrack_url="<Put your Public YouTrack URL here>"
jira_usr=<put your Jira user here>
jira_pwd=<put your Jira password here>
youtrack_usr=<put your YouTrack user here>
youtrack_pwd=<put your YouTrack password here>
jira_projects="<Full path of the Jira projects list - one project per line>"

# Import every project on the list from Jira to YouTrack
for project in $(cat $jira_projects)
do
python /youtrack/youtrack-rest-python-library/python/jira2youtrack.py $jira_url $jira_usr $jira_pwd $youtrack_url $youtrack_usr $youtrack_pwd $project
done
