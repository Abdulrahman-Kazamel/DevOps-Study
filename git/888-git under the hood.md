
how git works ,

- when we commit , it's creates sha1 object for each file and directory
- then store this in blob storage 
- then creates another object called tee to store this blobs
- the the commit 

```bash
git cat-file --batch-all-objects --batch-check

##output example
2aceb162196eb00e6542aa5358c43f09900a1a0b blob 155
3349a166df2f292c4c22e4fcf009eec298328e04 blob 250
35802dbbb5e2bcd938b8b482d9e53432533cc29d tree 83
391af6ee20abe0cafe6717f272566cbf259b6245 blob 131
4532d4d8db8d3045db702b938b63dd824449f1a5 tree 39
464ba9e6c4b09ba107eb39f520e035fd317e6183 blob 180
52a2ad6813a0d80c1b6ed39f015bfc02ebbe66e8 tree 78
5aad892a97af003b02df229481244c05c94cd9ea blob 13
82554c1d051eb6662bea7e8c0044abc6e083e0f5 blob 349
931aa6db032bcbf0de1415ad338ef38155264a2f blob 1264
9fbbac061d36039438a3a423dcdf0d7857670d76 commit 221
a74984fe2d57a1c59d6404a58bad4258cb3f746b tree 206
d5bec0f0dff7f0bffaaca79e4611c10bcb5ca219 blob 22


```


*important --->*

when modifying some data on some files ,then commit, git only creates blob (snapshot) for the changed files as another version of this file,
and sure new tree pointing to the new version 

