- name: Create empty file
  hosts: app
  become: yes

  tasks:
    - name: Ensure /tmp/file.txt exists
      ansible.builtin.file:
        path: /tmp/file.txt
        state: file   # needs touch at beging to create it 
        mode: '0644' 
        owner: root 
        group: root
