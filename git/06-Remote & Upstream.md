

```bash
git remote add origin git@github.com:Abdulrahman-Kazamel/DevOps-Study.git
```


git remote add (name) url
git remote add origin https:git 




Managing Git remotes involves connecting your local repository to versions of your project hosted elsewhere (like [GitHub](https://github.com/), GitLab, or another server) to collaborate with others. [](https://git-scm.com/book/ms/v2/Git-Basics-Working-with-Remotes#:~:text=To%20be%20able%20to%20collaborate,tracked%20or%20not%2C%20and%20more.)

![Git](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADtUlEQVRYhbVXPWwcRRT+3uzu7eXOdhyLNFDQROdtQEJEgtR3+RG+WxdOhIREhCkoqGgQSIgQISGFNrIACZQiQaIgBbc2ko0CdUgXaMYWUKYCDt/Z8d7uzQ7F3fpm/27vVslUs2/efO9737yZ2SEUbP6qtXY4CK4RgKrOPtHb/IciOFQw+DqAWzGQq3qb33mqBPq2ZRDhHQAb8YlFSbBZnAGchsQGAMjYwOj79mDVevOpETAd/kgCb4TRngSJqQi4tvVRr7m8PSLxnQSuPCkSuTXg2uOCc0Vwf/HHvXMA0Let17u+2AgknjllagmgaWtiIoEje3kdwC1S3I5E8KCisbrp8AMA8FateQDvA/i4CIlMAo9by+tE4VajuOOXZYe/qxo6K7WHVZ29GAfNI5FaA49bw8zl8QJLSGW1hZRL8Tka8F8aVl5NJAgctpbfgnLISKXKwm5vEKy4trWgzjM19kWRwowoezjKPDEAgBQDgdAbBH/N66xGgGE63AWAvm2tEXAXEd9EP7Icx+MHrbDgMtilkMBQwSU/kLdLjNZMh7t927pMwPfh5LzCZGrwmG9CStXwrydk2eGy7PB/DEav9QaCA4Dp8LsSuCID+e2RCO7nLQf1mlYLgEMUdc1TouMJPLv9BwHAo0tn5FJJhyuCX09orGk6/O/Q11u1bgD4IEOJFdb1xdcAIGX2kZDIImYgUAAAZY29AuCCOlZq8w87fZFamF1ffMUYUW8MTBEHGZuQRUJCMsVPnzYRIuqyqo6rUeCoEpNIpPl1fXHDta3Tob1vWzcXSxrStuiczt4mAOg2axcJbDvKbnJNdDyB53bGNXCqpI3GCPueQEVnW14gn5/T2QsRjPHuOG+0+T0GAAtbezsSwcVIRjlKhAEBYNHQlDGJkyUNBqNmVQl+jDEEqhttfg9QTsKFrb2f8kio7WAQ/K70/0TKiRnvj74bpTb/JfyOHMV5JMLC3PdFp6qzs6F9Tmcvd3zRz7o7FBIN0+E/q/iJu2AaJRYM7Zvq5q4Xflc2d/cXDe3O0DeSrdqvx4OnElBIXMoi4Yrg1ficw8HYlqJEo+yMZVfbxB+SbrN2gcB2IhPGu+MzAJ/TMInrAN7LuDvqJ5zd1OC5BEYkMrfovidABJxUdkEEkNCoOLsJ2WciMCIxSYkE0KjfqGxODj41gWlIxIDq1c1s2dU29bsgrzCVu6MxbXCgwNswR4n63AzBgdmfZpOUOD9rcKDg6xgAus3aS4OAPiXA1xldn9/ivxXB+R9WO7IF6Q7yGAAAAABJRU5ErkJggg==)Git +1

**Essential Remote Commands**

|Task|Command|Description|
|---|---|---|
|**List remotes**|`git remote -v`|Shows the names and URLs for fetch and push operations.|
|**Add a remote**|`git remote add <name> <url>`|Connects a new remote repository to your project.|
|**Change URL**|`git remote set-url <name> <new_url>`|Updates the URL for an existing remote (e.g., switching from HTTPS to SSH).|
|**Rename**|`git remote rename <old> <new>`|Changes the shortname used to reference the remote.|
|**Remove**|`git remote remove <name>`|Deletes the connection to a remote from your local setup.|
|**Show details**|`git remote show <name>`|Provides detailed tracking info, branch statuses, and push/pull URLs.|

---

**Common Workflows**

- **Sharing Your Work**: After committing local changes, use `git push <remote> <branch>` (e.g., `git push origin main`) to upload them to the remote server.
- **Collaborating with Upstream**: In open-source projects, it's common to add the original repository as an "upstream" remote:
    1. `git remote add upstream <original_repo_url>`.
    2. `git fetch upstream` to get the latest changes from the original project.
    3. `git merge upstream/main` to sync your local branch with the original.
- **Switching Protocols**: If you need to change your remote from HTTPS to SSH for better security, use the GitHub Guide for Switching URLs or the Bitbucket URL Update Guide. [](https://git-scm.com/book/ms/v2/Git-Basics-Working-with-Remotes#:~:text=To%20be%20able%20to%20collaborate,tracked%20or%20not%2C%20and%20more.)
    
    ![Git](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADtUlEQVRYhbVXPWwcRRT+3uzu7eXOdhyLNFDQROdtQEJEgtR3+RG+WxdOhIREhCkoqGgQSIgQISGFNrIACZQiQaIgBbc2ko0CdUgXaMYWUKYCDt/Z8d7uzQ7F3fpm/27vVslUs2/efO9737yZ2SEUbP6qtXY4CK4RgKrOPtHb/IciOFQw+DqAWzGQq3qb33mqBPq2ZRDhHQAb8YlFSbBZnAGchsQGAMjYwOj79mDVevOpETAd/kgCb4TRngSJqQi4tvVRr7m8PSLxnQSuPCkSuTXg2uOCc0Vwf/HHvXMA0Let17u+2AgknjllagmgaWtiIoEje3kdwC1S3I5E8KCisbrp8AMA8FateQDvA/i4CIlMAo9by+tE4VajuOOXZYe/qxo6K7WHVZ29GAfNI5FaA49bw8zl8QJLSGW1hZRL8Tka8F8aVl5NJAgctpbfgnLISKXKwm5vEKy4trWgzjM19kWRwowoezjKPDEAgBQDgdAbBH/N66xGgGE63AWAvm2tEXAXEd9EP7Icx+MHrbDgMtilkMBQwSU/kLdLjNZMh7t927pMwPfh5LzCZGrwmG9CStXwrydk2eGy7PB/DEav9QaCA4Dp8LsSuCID+e2RCO7nLQf1mlYLgEMUdc1TouMJPLv9BwHAo0tn5FJJhyuCX09orGk6/O/Q11u1bgD4IEOJFdb1xdcAIGX2kZDIImYgUAAAZY29AuCCOlZq8w87fZFamF1ffMUYUW8MTBEHGZuQRUJCMsVPnzYRIuqyqo6rUeCoEpNIpPl1fXHDta3Tob1vWzcXSxrStuiczt4mAOg2axcJbDvKbnJNdDyB53bGNXCqpI3GCPueQEVnW14gn5/T2QsRjPHuOG+0+T0GAAtbezsSwcVIRjlKhAEBYNHQlDGJkyUNBqNmVQl+jDEEqhttfg9QTsKFrb2f8kio7WAQ/K70/0TKiRnvj74bpTb/JfyOHMV5JMLC3PdFp6qzs6F9Tmcvd3zRz7o7FBIN0+E/q/iJu2AaJRYM7Zvq5q4Xflc2d/cXDe3O0DeSrdqvx4OnElBIXMoi4Yrg1ficw8HYlqJEo+yMZVfbxB+SbrN2gcB2IhPGu+MzAJ/TMInrAN7LuDvqJ5zd1OC5BEYkMrfovidABJxUdkEEkNCoOLsJ2WciMCIxSYkE0KjfqGxODj41gWlIxIDq1c1s2dU29bsgrzCVu6MxbXCgwNswR4n63AzBgdmfZpOUOD9rcKDg6xgAus3aS4OAPiXA1xldn9/ivxXB+R9WO7IF6Q7yGAAAAABJRU5ErkJggg==)Git +5

For further detailed documentation, refer to the official [Git-Remote Documentation](https://git-scm.com/docs/git-remote) or the [GitHub Basics for Remotes](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories). 


