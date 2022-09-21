from MainConfig import *
from jira import JIRA

jira = JIRA(server=jiraServer, basic_auth=(jiraUser, jiraPass))

myself = jira.myself() #returns dictionary of user information
myself = myself['displayName'] #selects user's name to use later on

foundIssue = False

while foundIssue == False:
    issueID = 'CU-136' #input("Enter Jira Issue ID: ")
    try:
        issue = jira.issue(issueID)
    except:
        errorMessage = 'Issue does not exist, please try again.'
        print(errorMessage)
    else:
        print(f'Issue found: {issue}')
        foundIssue = True

class JiraTicket:
    def __init__(self):
        self.issueID = issue
        self.summary = jira.issue(self.issueID).fields.summary
        self.description = jira.issue(self.issueID).fields.description
        self.comments = jira.comments(self.issueID)


print(JiraTicket().summary)
print(JiraTicket().description)
for comm in JiraTicket().comments:
    if comm.jsdPublic == True:
        public = "Replied to customer"
    if comm.jsdPublic == False:
        public = "Internal comment"
    print(f'\nDate: {comm.created}')
    print(f'Internal/Customer facing: {public}')
    print(f'Author: {comm.author.displayName}')
    print(f'Comment Body: {comm.body}')
    
