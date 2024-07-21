#!/bin/bash

########## This Script will Read and Clone all Repos from RepoList.txt  ##########
echo "Welcome!!!"
echo

# Define the input file
INFILE=RepoList.txt

# Initialising Git
git init

# Read the input file line by line
while read -r LINE
do
    printf '%s\n' "$LINE"
    repo_name=$(basename "${LINE}" | sed 's/.git$//') # Extracting Repo Name
    echo "Cloning the Repo $repo_name"
    echo "#######################################"
    git clone $LINE # running git clone command
    echo "#######################################"
    echo "Done Cloning"
    echo "#######################################"
    echo "Creating Feature Branch"
    cd $repo_name # changing directory to make new feature branch
    echo "#######################################"
    git checkout -b FeatureBranch
    cd .. # switching one level up to clone next repository
    echo "#######################################"
    echo "Created Feature Branch Successfully!"
    echo "#######################################"
done < "$INFILE"