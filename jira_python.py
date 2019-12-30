from jira import JIRA

jira = JIRA(basic_auth=('admin', 123456), options={'server': 'http://IP/jira'})
project = jira.projects()
for i in project:
    print(i)
print(project)
