


#!/bin/bash

set -e

REPO_FILE="/etc/yum.repos.d/CentOS-Base.repo"

echo "Backing up old repo..."
cp -v $REPO_FILE ${REPO_FILE}.bak || true

echo "Writing new CentOS-Base.repo with HTTPS vault..."

cat <<EOF > $REPO_FILE
# CentOS-Base.repo (Updated to Vault + HTTPS)

[base]
name=CentOS-\$releasever - Base
baseurl=https://vault.centos.org/centos/\$releasever/os/\$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-\$releasever - Updates
baseurl=https://vault.centos.org/centos/\$releasever/updates/\$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-\$releasever - Extras
baseurl=https://vault.centos.org/centos/\$releasever/extras/\$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[centosplus]
name=CentOS-\$releasever - Plus
baseurl=https://vault.centos.org/centos/\$releasever/centosplus/\$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
EOF

echo "Disabling fastestmirror (optional but recommended)..."
sed -i '/fastestmirror/d' /etc/yum.conf || true

echo "Cleaning yum cache..."
yum clean all
rm -rf /var/cache/yum

echo "Rebuilding cache..."
yum makecache

echo "Updating system..."
yum update -y

echo "✅ DONE - Repo fixed and system updated"