import requests, os, json
from github import Github

#Read blocklist from Mastodon-Account
url='%s/api/v1/blocks' % os.environ['M_API_BASE_URL']
auth={'Authorization':'Bearer %s' % os.environ['M_ACCESS_TOKEN']}
blocks = json.loads(requests.get(url, headers=auth).text)
blocklist = ""
for block in blocks:
  if blocklist:
    blocklist = blocklist + '\n' + block['acct']
  else:
    blocklist = block['acct']

print(blocklist)

# Push Blocklist To Gitub-Repo
git = Github(os.environ['G_TOKEN'])
repo = git.get_repo("freesbie/mastodon_blocklister")
contents = repo.get_contents("blocklist.csv")
repo.update_file(contents.path, "test", f"{blocklist}", contents.sha, branch="main")
