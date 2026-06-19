

```
git branch # list branches  
git checkout master # switch to master  
git checkout -b myNewBranch # create + switch



git branch -d myNewBranch # delete becuase not needed and they are the same state

```


- `-b` = create + switch in one step
- Always know where you are before committing


`git branch` command is used to list, create, or delete branches. Below are the most common options categorized by their function. 

**Listing Branches**

- **`-a` (or `--all`)**: Lists all local and [remote-tracking branches](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches).
- **`-r` (or `--remotes`)**: Lists only the [remote-tracking branches](https://git-scm.com/docs/git-branch).
- **`-v` (or `--verbose`)**: Shows the [last commit SHA-1 and subject line](https://git-scm.com/book/en/v2/Git-Branching-Branch-Management) for each branch.
- **`-vv`**: Shows more detailed information, including upstream tracking relationship and whether local branches are ahead/behind their remotes.
- **`--merged [<commit>]`**: Lists only branches already merged into the current branch (or a specified commit).
- **`--no-merged [<commit>]`**: Lists branches that contain work not yet merged.
- **`--contains <commit>`**: Lists only branches that contain a specific commit. 
**Managing Branches**

- **`-d` (or `--delete`)**: Deletes a branch. This [only works if the branch has been merged](https://www.w3schools.com/git/git_branch.asp) into its upstream branch.
- **`-D`**: Force-deletes a branch regardless of its merge status.
- **`-m` (or `--move`)**: Renames a branch.
- **`-M`**: Force-renames a branch, [even if the new name already exists](https://linux.die.net/man/1/git-branch).
- **`-c` (or `--copy`)**: Copies a branch along with its configuration and reflog.
- **`-C`**: Force-copies a branch, overwriting an existing branch name. 
**Tracking Information**

- **`-u <upstream>` (or `--set-upstream-to`)**: Sets up tracking information so that `git pull` knows which remote branch to use.
- **`--unset-upstream`**: Removes the [upstream tracking information](https://git-scm.com/docs/git-branch/2.0.5) for the specified branch.

**Alternative Commands for Switching**

While `git branch` creates branches, it does not switch to them.

- **`git switch -c <name>`**: A modern command that [creates and switches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) to a new branch in one step.
- **`git checkout -b <name>`**: The traditional command to create and switch to a new branch. 



```bash
### creating a branch based on a specfic branch
git branch new-branch-name source-branch

## pushing from another branch
git push --set-upstream origin features ##features is my branch name
#or through
git push -u origin features ## creates the relationship

```