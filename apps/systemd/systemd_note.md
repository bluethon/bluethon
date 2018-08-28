Systemd Note
============

Create
------

### 1. create service file

    vim /etc/systemd/system/jenkins.service

### 2. add

``` ini
[Unit]
Description=Jenkins Daemon

[Service]
ExecStart=/usr/bin/java -jar /home/jenkins_user/jenkins.war
User=jenkins_user

[Install]
WantedBy=multi-user.target
```

### 3. reload

    sudo systemctl daemon-reload

### 4. manage service

``` bash
sudo systemctl start jenkins.service
sudo systemctl stop jenkins.service
sudo systemctl restart jenkins.service
sudo systemctl enable jenkins.service
sudo systemctl disable jenkins.service
```