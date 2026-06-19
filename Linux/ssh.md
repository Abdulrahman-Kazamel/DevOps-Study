ssh keyles 
ssh-keygen -t rsa

same to ssh-copy-id /// ssh -i copy public key   

next time i try to just write root@server-ip .. to logged in without password

 

private kay that we never share and keep it in our machine // public key for the server 


## remote ssh login 
sudo grep -E "PasswordAuthentication|PubkeyAuthentication" /etc/ssh/sshd_config
systemctl restart sshd


```bash


 chmod 400 .ssh/id_rsa

aws-client ~ via 🐘 ➜  ssh -i .ssh/id_rsa ubuntu@100.31.139.4
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 6.5.0-1022-aws x86_64)

ubuntu@ip-172-31-22-137:~$ 
logout
Connection to 100.31.139.4 closed.

aws-client ~ via 🐘 ➜  sssh -v -i ~/.ssh/id_rsa ubuntu@100.31.139.4
OpenSSH_8.4p1 Debian-5+deb11u6, OpenSSL 1.1.1w  11 Sep 2023
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: Connecting to 100.31.139.4 [100.31.139.4] port 22.
debug1: Connection established.
debug1: identity file /root/.ssh/id_rsa type 0
debug1: identity file /root/.ssh/id_rsa-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_8.4p1 Debian-5+deb11u6
debug1: Remote protocol version 2.0, remote software version OpenSSH_8.9p1 Ubuntu-3ubuntu0.10
debug1: match: OpenSSH_8.9p1 Ubuntu-3ubuntu0.10 pat OpenSSH* compat 0x04000000
debug1: Authenticating to 100.31.139.4:22 as 'ubuntu'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ecdsa-sha2-nistp256
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:srmD4HrPKfnKaDUrQmy4dkZ500H/rwndeishDfv4uU0
debug1: Host '100.31.139.4' is known and matches the ECDSA host key.
debug1: Found key in /root/.ssh/known_hosts:1
debug1: ssh_packet_send2_wrapped: resetting send seqnr 3
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: ssh_packet_read_poll2: resetting read seqnr 3
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: Will attempt key: /root/.ssh/id_rsa RSA SHA256:3zrFuSE/jQIeknHCEi2T35Gcj+pkjSfN4lzDGgPzNhQ explicit
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com,webauthn-sk-ecdsa-sha2-nistp256@openssh.com>
debug1: kex_input_ext_info: publickey-hostbound@openssh.com (unrecognised)
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering public key: /root/.ssh/id_rsa RSA SHA256:3zrFuSE/jQIeknHCEi2T35Gcj+pkjSfN4lzDGgPzNhQ explicit
debug1: Server accepts key: /root/.ssh/id_rsa RSA SHA256:3zrFuSE/jQIeknHCEi2T35Gcj+pkjSfN4lzDGgPzNhQ explicit
debug1: Authentication succeeded (publickey).
Authenticated to 100.31.139.4 ([100.31.139.4]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: network
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 6.5.0-1022-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu May 21 10:45:29 UTC 2026

  System load:  0.02              Processes:             110
  Usage of /:   25.8% of 7.57GB   Users logged in:       0
  Memory usage: 24%               IPv4 address for eth0: 172.31.22.137
  Swap usage:   0%


Expanded Security Maintenance for Applications is not enabled.

243 updates can be applied immediately.
167 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release '24.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Thu May 21 10:44:35 2026 from 65.108.255.62
ubuntu@ip-172-31-22-137:~$ 

```