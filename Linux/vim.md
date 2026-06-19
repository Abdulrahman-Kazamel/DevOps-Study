

```
```
```
set expandtab
set tabstop=2
set shiftwidth=2


```
copy 1 line ---> yy ---> yanked
copy multiple lines 4 ---> 4yy 

gg ---> first of the file
G -> end of the file 
p -0--> paste before
P --> pase before 


dd -->delete and copy 
u --> undo 
```
expandtab: use spaces for tab
tabstop: amount of spaces used for tab
shiftwidth: amount of spaces used during indentation



```

### search and replace


```
# vim search or replace
$s/word/replacedWord/g for global
$s/word//g for global ---> replace for nothing 

## serach
sed 's/word/replacedWord/g' filepath


## search and replace

sed -i 's/word/replacedWord/g' filepath


# showing third column in a file 
cut -d, -f3 text.csv 
cut -d: -f3 text.csv 



#comand and 2 in redirection means standerd error output 
comand 2 >> test
command & >> test ----------> redirect standard output + errors 

```



### generate  random words

```bash
shuf -n 100 /usr/share/dict/words > random_words.txt

```


## word count
```
wc -l filepath
wc -l < filepath


# ls | wc -l
4
# ls /etc | wc -l 
249





```


## locate and updatedb but not real time as find 
```
install mlocate 
```


### list files open by particular user

```bash
lsof -u kazamel

```

## get who is logged into the system

last


userdel -r ---> to delete the user home dir 




## sudoers file

NOPASSWD ----> for stop asking for root user
% ---> means a group



# how to find the system arch

```
arch
uname -m
```



# curl



```
curl link -o (output)  outputName
```


	systemctl reload service name ---> to reload the configration without restrarting the service.


systemctl is-active or is-enabled serviceName

ps -ef ======> shows process ID and their parents 
ps -ef | grep processName | grep -v "grep"


ps -ef | grep processName | grep -v "grep" | awk  '{print  $2 }' | xargs kill -9 



adduser is better in ubuntu based systems 

export EDITOR=vim



clean uninstall --------------> apt purge 




