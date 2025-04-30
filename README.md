# MLOP_DVC1

Welcome to my MLOP learning.  

This project tells us about the data version control. 

These are the steps:

1. creat git repo and clone it in local.
2. creat mycode.py and addcode to fit. (it willsave a csv file to a new "data" folder).
3. do a git add-commit-push before initializing dvc.
4. pip install dvc
5. Now we do "dvc init"(creats .dvcignore, .dvc).
6. Now do "mkdir s3"(createsa new s3 directory).
7. Now we do "dvc remote add -d myremote s3".
8. Next "dvc add data/".
9. To stop tracking from Git:
            git rm -r --cached 'data'
            git commit -m "stop tracking data"
10.again "dvc add data/"
11.dvc commit and push
12.Do a git add-commit-push to mark this stage as first version of data 
13.Now make changes to mycode.py to append a new row in data , check changes via dvc status
14.Again --"dvc commit" and then "dvc push"

git log --oneline
git checkout<hash>  -git chechout main
dvc pull
