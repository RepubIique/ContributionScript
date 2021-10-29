import git
from git_contributions_importer import *

repos_path = ["../MyPassGlobal/mypass-global-suite/","../mypass-domains"]
repos=[]

for repo_path in repos_path:
    repos.append(git.Repo(repo_path))

mock_repo_path = "./MockRepo"
mock_repo = git.Repo.init(mock_repo_path)
importer = Importer(repos, mock_repo)
importer.set_author(['Kendrickbong1996@gmail.com', 'kbong@mypassglobal.com'])
importer.import_repository()
