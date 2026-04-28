.:
file.txt
home
notes_backup.txt
project
project_backup
task2.txt

./home:
file1.txt

./project:
Docs
Src
notes.txt
readme.md

./project/Docs:

./project/Src:

./project_backup:
Docs
Src
Tests
notes.txt
readme.md

./project_backup/Docs:
notes.txt

./project_backup/Src:

./project_backup/Tests:
    1  ls
    2  ls -a
    3  hostname
    4  sudo hostnamectl set-hostname server
    5  su -
    6  history
    7  sudo hostnamectl set-hostname server
    8  sudo -i
    9  ls
   10  cd
   11  ls
   12  apt update
   13  sudo apt update
   14  sudo apt upgrade
   15  sudo apt update
   16  su -i
   17  su - i
   18  sudo -i
   19  su abdulrahman
   20  su - abdulrahman
   21  su -i
   22  sudo -i
   23  cat /var/log/ubuntu-advantage.log
   24  cat /var/log/ubuntu-advantage-apt-hook.log
   25  ls /bin
   26  ll
   27  vim file.txt
   28  mkdir project
   29  touch notes.txt
   30  mkdir Src Docs Tests project/
   31  mkdir Src Docs Tests project
   32  ll
   33  mv Src/ Docs/ Tests/ project/
   34  ll
   35  ls project/
   36  touch project/readme.md
   37  ls project/
   38  help(ls)
   39  ls.help
   40  help ls
   41  man ls
   42  ls -f
   43  ls
   44  ls -a
   45  #List all files in the current directory.
   46  history
   47  ls project/
   48  cp notes.txt notes_backup.txt
   49  ls
   50  cp notes project/
   51  cp notes.txt project/
   52  ls
   53  ls project/
   54  cp notes.txt project/Docs/
   55  ls project/Docs/
   56  cp project/ project_backup/
   57  ls
   58  cp -R project/ project_backup/
   59  ls
   60  ls project_backup/
   61  mv notes.txt project/Docs/
   62  mv project/Docs/notes.txt project/Docs/todo.txt
   63  ls project/Docs/
   64  rm  project/Docs/todo.txt
   65  ls project/Docs/
   66  rm project/Tests/
   67  rm -r project/Tests/
   68  ls -R
   69  ls -R >> task2.txt
   70  history >> task2.txt