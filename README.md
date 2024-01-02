# College Assignment 2 #

## Project Overview ##

### Part 1 ###

In your GitHub account, create a repository called "Python" and save your Python exercises. 
This repo should be to best practice as per the Python and Git/Github walkthroughs.
Create at least one feature branch and merge in the recommended way.
Include the directory structure recommended in my notes with a single readme.md explaining the repo. 


#### Part 1 methodology ### 

This assigment is broken up in to two separate parts. This README.md relates to Part One - The python exercises as outlined above.

A Github repository named Python was created.
The script supplied by Github was run on a directory locally to create a Git directory and README.md.
The recommended branch structure of test and dev branches was created in Github.
"git pull" was then run locally to bring down the newly created branches.
"git checkout dev" was then ran to checkout the dev branch.
A new feature branch was created and checkout by running "git checkout -b F231228-001"
Once the feature branch was checked out I copied my working files into the git directory locally.
"git add ." was then run followed by "git status" to show the newly added files in the feature branch.
"git commit -m " added working files to the feature branch"
The dev branch was then checked out and the changes from the feature branch merged by running "git merge F231228-001"
The Test branch was then checked out and the changes from the dev branch merged by running "git merge dev"
The main branch was then checked out and the changes from the Test branch merged by running "git merge Test"
"git push" was then run to merge changes from the main branch to GitHub.
Each of the branches were then checked out again and the following commands were run to merge changes to Github
- git push --set-upstream origin F231228-001
- git push --set-upstream origin dev
- git push --set-upstream origin Test

The branch F231228-001 would normally then be deleted following best recommended practices however to show the full history it was not in this assignment.
I created a second feature branch F231228-002 and follwed the process as outlined above to merge it.
I created a third feature branch F231228-003 and again follwed the process as outlined above to merge it.

The exercises for Python were broken down in 12 Headings and are included in a directory entitled Python in the Python repo.

1. Learning the basics
2. Documentation
3. Data Structures
4. Loops and Statements
5. Functions
6. Modules and Packages
7. Errors
8. OO Coding
9. Tests
10. Logging and Time
11. Network Utilities
12. Projects

- All working files were placed in a Python Folder.
- A sub folder was created in this Python directory for each of the above exercise headings.
- In cases where these headings were broken down into sub headings in the examples additional sub folders were created to accurately categorise each python script.
- The additional folders included in the Github repository are empty except for a blank file ".getkeep" which allows empty directories to sync to a Github repository.

