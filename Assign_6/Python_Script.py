import git

with open('RepoList.txt', 'r') as f:  # Open file for read
    for line in f:           # Read line-by-line
        line = line.strip()  # Strip the leading/trailing whitespaces and newline
        
        # Process the line
        last_part = line.split('/')[-1] # Extracting the last part
        repo_name = last_part.replace('.git', '') #.git->''

        # Cloning the Repo
        git.Repo.clone_from(line, repo_name)

        # Initialising git in the newly cloned repo
        directory = repo_name 
        repo = git.Repo.init(directory) # Specifying to Initialise in the folder named "Repo Name"

        # Create a new branch
        branchName = "branchOf"+repo_name 
        repo.git.branch(branchName)
# File closed automatically upon exit of with-statement
