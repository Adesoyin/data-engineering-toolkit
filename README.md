# data-engineering-toolkit
*Purpose of the project*
This project aim to understand and practice the fundamental of repository creation, branch strategy, development of script on feature branch to run ETL processes, request pull and merge request on remote repository. 
This will further heighten my understanding and logic flow of the whole processes of git and github. 

**Documentation**
*Repository Creation*
The first step carried out was the craetion of a repository named "data-engineering-toolkit" ensuring the README.md file is turned on.
![alt text](image.png)

The https link was copied out and then used to clone the repository on my local machine. A .gitignore file was created in the main folder which was used to hide all virtual environment and .pyc files to avoid public viewing of secrets. 

*Branching Strategy*
The git flow branching stategy was adopted by creating different branches for each task/new feature.
In my README.md, documentation was written to make the first commit to the remote repo. 
New branches (Develop and feature/branch-name) were created and on my github, I ensured branch protection rules were created on main branch to require pull request before merging.
![alt text](image-1.png)
The first wriiten documentation was added and pushed to Develop branch, it craeted a pull request on the remote repo, and changes was checked befored being merged to the main branch
![alt text](image-2.png)
![alt text](image-3.png)

**git Code written**
To create virtual environment
    python -m venv venv
To activate the environment
    source venv/Scripts/activate
To see status of the repo
    git status
To create a new branch called "Develop" -which serves as a branch for all integration.
    git branch Develop
    git checkout Develop   -m "moved to the new branch craeted"
Also created a Feature branch for new features/script addition.