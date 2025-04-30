# MLOP_DVC1

Welcome to my MLOP learning.  

This project tells us about the data version control. 

These are the steps:

creat git repo and clone it in local
creat mycode.py and addcode to fit. (it willsave a csv file to a new "data" folder)
do a git add-commit-push before initializing dvc
pip install dvc
Now we do "dvc init"(creats .dvcignore, .dvc)
Now do "mkdir s3"(createsa new s3 directory)
now we do "dvc remote add -d myremote s3"
Next "dvc add data/"
 To stop tracking from Git:
            git rm -r --cached 'data'
            git commit -m "stop tracking data" 
again "dvc add data/"
dvc commit and push
Do a git add-commit-push to mark this stage as first version of data 
Now make changes to mycode.py to append a new row in data , check changes via dvc status
Again --"dvc commit" and then "dvc push"

git log --oneline
git checkout<hash>  -git chechout main
dvc pull
