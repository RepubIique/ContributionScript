import git
from git_contributions_importer import *

repos_path = ["../local-development-docker/ss-identity-service/",
            "../local-development-docker/ss-notification-connection-lambda/", 
            "../local-development-docker/staff-app/",
            "../local-development-docker/ss-notification-service/",
            "../local-development-docker/ss-sts-access-lib/",
            "../local-development-docker/sts-token-lib/",
            "../local-development-docker/ss-sts-consume-lambda/"]
repos=[]

for repo_path in repos_path:
    repos.append(git.Repo(repo_path))

mock_repo_path = "./MockRepo"
mock_repo = git.Repo.init(mock_repo_path)
importer = Importer(repos, mock_repo)
importer.set_author(['Kendrickbong1996@gmail.com', 'kendrick.bong@educationhorizons.com'])
importer.import_repository()
