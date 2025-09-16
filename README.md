<!-- SEARCH: ### 'letter') -->
## NoTesk
#### No tasks with notes


# Links
<details>
  <summary>
    explore
  </summary>
  
  <!-- FIELD -->
<details>
  <summary>
    EcoRouter
  </summary>
  
  [EcoRouter-Basic]: https://pabliko.ru/@sysadmin/nastrojka_ecorouter_nachalo-280276/ "EcoRouter-Basic"
  # [EcoRouter-Basic] 
  
  ```bash
  https://pabliko.ru/@sysadmin/nastrojka_ecorouter_nachalo-280276/
```
</details>
<!-- FIELD -->
  <!-- FIELD -->
<details>
  <summary>
    VipNet xFirewall
  </summary>
  
  [VipNet xFirewall]: https://infotecs.ru/downloads/documents/vipnet-xfirewall-5/ "VipNet xFirewall"
  # [VipNet xFirewall] 
  
  ```bash
  https://infotecs.ru/downloads/documents/vipnet-xfirewall-5/
```
</details>
<!-- FIELD -->
<details>
  <summary>
    docker Grafana-Prometheus
  </summary>
  
  [Grafana-Prometheus]: https://blog.unixhost.pro/ru/2022/04/ustanovka-grafana-i-prometheus/#pll_switcher "Grafana-Prometheus"
  # [Grafana-Prometheus] 
  ```bash
  https://blog.unixhost.pro/ru/2022/04/ustanovka-grafana-i-prometheus/#pll_switcher
```
</details>
<!-- FIELD -->
<details>
  <summary>
    Flashing android
  </summary>
  <details>
<summary>
EDL
</summary>
    
  [Xiaomi_MediaTek_Pack0]: https://4pda.to/forum/index.php?showtopic=1012866&st=9680#entry114583558 "Xiaomi MediaTek Pack 0"
   # [Xiaomi_MediaTek_Pack]
  [Xiaomi_MediaTek_Pack1]: https://4pda.to/forum/index.php?showtopic=912972&view=findpost&p=104634322 "Xiaomi MediaTek Pack 1"
  # [Xiaomi_MediaTek_Pack_Advanced]
```bash

https://4pda.to/forum/index.php?showtopic=1012866&st=9680#entry114583558

```
#### Advanced
```bash
https://4pda.to/forum/index.php?showtopic=912972&view=findpost&p=104634322
```
#### TWRP
```bash
https://4pda.to/forum/index.php?showtopic=912972&view=findpost&p=80056083

```
 </details>
 </details>

<!-- FIELD -->
  
</details>

# Topics

### A)

<details>
<summary> Кибер (Acronis)  </summary>     <!-- ff -->

### +/ Alt Linux <!-- PLATFORM -->
<details>
<summary> Кибер Бэкап  </summary>     <!-- ff -->

<details>
<summary> Установка  </summary> <!-- tp -->

> ADMIN (Management Server); CLI (Storage Node) <!-- Citation -->

#### 0. Устройства должны иметь правильные dns-записи и пинговаться <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
host admin.ad.team
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
host cli.ad.team
```
<!-- CODE -->

#### 1. На ADMIN <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
useradd wsradmin
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
passwd wsradmin
```
<!-- CODE -->
---

#### SnapAPI <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get update
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
update-kernel
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
ln -s /usr/src/OS_CORE /lib/modules/OS_CORE/build
```
<!-- CODE -->

> Example: `ln -s /usr/src/linux-6.1.128-un-def-alt1 /lib/modules/6.1.79-un-def-alt1/build` <!-- Citation -->

#### Установка <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
https://download.cyberprotect.ru/releases/CyberBackup/17.2.33697/CyberBackup_17_64-bit.x86_64
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
chmod +x CyberBackup_17_64-bit.x86_64
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
./CyberBackup_17_64-bit.x86_64
```
<!-- CODE -->

### Пункты для сервера <!-- LIST -->
- `Management Server` <!-- JUST -->
- `Agent for Linux` <!-- JUST -->
- `Storage Node` <!-- JUST -->
---

#### Проверка <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
/usr/lib/Acronis/BackupAndRecovery/dsk_supp_test
```
<!-- CODE -->
---

#### После установки зайти в браузере <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
IP_ADMIN:9877
```
<!-- CODE -->

### После создать организацию и администратора <!-- LIST -->
- `wsr` в  Настройки -> Учётные записи -> Создать отдел <!-- JUST -->
- `wsradmin` в  Настройки -> Учётные записи -> Добавить учётную запись -> Из локальной машины <!-- JUST -->
---

#### 2. На CLI <!-- ACTION -->

#### Иметь второй Hard Disk (>20GB) <!-- ACTION -->

#### Создание хранилища в /backups <!-- ACTION -->

#### Найти устройство <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
lsblk
```
<!-- CODE -->

#### Форматировать <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mkfs.xfs /dev/sdX
```
<!-- CODE -->

#### Создать директорию <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mkdir -p /backups
```
<!-- CODE -->

#### Монтировать <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mount /dev/sdX /backups
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/fstab
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
/dev/sdX /backups xfs defaults 0 2
```
<!-- CODE -->

#### Проверить <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mount -a
```
<!-- CODE -->
---

#### SnapAPI <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get update
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
update-kernel
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
ln -s /usr/src/OS_CORE /lib/modules/OS_CORE/build
```
<!-- CODE -->

> Example: `ln -s /usr/src/linux-6.1.128-un-def-alt1 /lib/modules/6.1.79-un-def-alt1/build`
 <!-- Citation -->

#### Затем в `Management Server` <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
IP_ADMIN:9877
```
<!-- CODE -->

### Установка хранилища-клиента <!-- LIST -->
- Устройства -> Добавить -> Серверы -> Linux <!-- JUST -->
- Устройства -> Добавить -> Самый низ -> МАРКЕР РЕГИСТРАЦИИ (СОЗДАТЬ) <!-- JUST -->
    - СГЕНЕРИРОВАТЬ -> КОПИРОВАТЬ  <!-- SPACE -->

#### Далее в машине хранилища <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
cd /home/USERNAME/Загрузки
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
chmod +x CyberBackup_17_64-bit.x86_64
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
./CyberBackup_17_64-bit.x86_64
```
<!-- CODE -->

### Далее для хранилища <!-- LIST -->
- `Agent for Linux` <!-- JUST -->
- `Storage Node` <!-- JUST -->

### Для подключения далее <!-- LIST -->
- IP_ADMIN <!-- JUST -->
- МАРКЕР РЕГИСТРАЦИИ <!-- JUST -->
---

#### Check <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
/usr/lib/Acronis/BackupAndRecovery/dsk_supp_test
```
<!-- CODE -->
---

#### 3. Создание плана <!-- ACTION -->

#### Затем в `Management Server` <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
IP_ADMIN:9877

```
<!-- CODE -->

### Создание плана резерва <!-- LIST -->
- Планы <!-- JUST -->
- Защита <!-- JUST -->
    - Создать план <!-- SPACE -->
    - Добавить устройство -> Выбрать ADMIN <!-- SPACE -->
    - Место сохранения -> выбрать CLI <!-- SPACE -->
    - Расписание -> Указать близжайшее время <!-- SPACE -->

### Checking <!-- LIST -->
- Выбрать план <!-- JUST -->
    - Действия (Часы) <!-- SPACE -->

</details> <!-- TOPIC -->


<details>
<summary> Удаление  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
```
<!-- CODE -->

</details>            <!-- TOPIC -->

</details>             <!-- FFIELD -->

</details>             <!-- FFIELD -->

---

<details> 
<summary> ansible </summary> 

<!-- CODE -->
```bash
apt-get install ansible sudo python3 openssh sshpass
useradd sshuser
passwd sshuser
usermod -aG wheel(sudo*) sshuser
echo "sshuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
systemctl enable --now sshd
```
<!-- CODE --> 

#### SRV<!-- ACTION --> 


#### Information of machine in /etc/ansible/inventory


![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/ansible/ansible_inventory.png) <!-- SCREEN --> 

#### Specify communication options in /etc/ansible/ansible.cfg (e.g. inventory path, SSH settings, privilege escalation)
<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/ansible/ansible_cfg.png) <!-- SCREEN --> 

#### Ping all machines and run command as sudo group using Ansible<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/ansible/ansible_commands.png) <!-- SCREEN --> 

#### CLI<!-- ACTION --> 

<!-- CODE -->
```bash
apt-get install openssh sudo sshpass python3
useradd sshuser
passwd sshuser
usermod -aG wheel(sudo*) sshuser
echo "sshuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
systemctl enable --now sshd
```
<!-- CODE --> 

</details>

### B)

<details>
<summary> Backup </summary>     <!-- ff -->


<details>
<summary> systemd </summary> <!-- tp -->

<!-- CODE -->
```MarkDown Keemplate
 sudo nano /etc/systemd/backup.service
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
 [Unit] Description=Backup shared folder to /var/bac After=network.target [Service] Type=oneshot ExecStart=/bin/bash -c `tar -czf /var/bac/shared-$(date +%%Y-%%m-%%d-%%H-%%M-%%S).tar.gz /path/to/shared/folder`
```
<!-- CODE -->


- `Type=oneshot`: The unit exits after executing the command.
 <!-- JUST -->

- `ExecStart`: Creates an archive named with the current date and time
 <!-- JUST -->
#### Timer for start service at 20:00 everyday <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 sudo nano /etc/systemd/system/backup.timer
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
 [Unit] Description=Run backup.service daily at 20:00 [Timer] OnCalendar=20:00 Persistent=true [Install] WantedBy=timers.target
```
<!-- CODE -->


- `OnCalendar=20:00`: time exec <!-- JUST -->

- `Persistent=true`: If the device is off, the timer executes the task at boot time if the scheduled time was missed
 <!-- JUST -->
#### Check <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 systemctl daemon-reload systemctl enable --now backup.timer
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
 systemctl list-timers
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
 systemctl start backup.service
```
<!-- CODE -->

#### Check archive <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 ls /path/to/shared/folder
```
<!-- CODE -->


</details> <!-- TOPIC -->


</details>        <!-- FFIELD -->

### C)
### D)

<details>
<summary> Docker </summary>     <!-- ff -->

---

<details>
<summary> Install </summary> <!-- tp -->

### +/ Linux <!-- PLATFORM -->
<!-- CODE -->
```MarkDown Keemplate
 apt-get install docker-{ce,compose}
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
 systemctl enable docker.service
```
<!-- CODE -->

#### Tasks are usually not run as root
 <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 sudo usermod -aG docker username
```
<!-- CODE -->

#### Run as regular user without requiring sudo (optional)
 <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 sudo chown username:docker /var/run/docker.sock
```
<!-- CODE -->


</details> <!-- TOPIC -->

---

<details>
<summary> Local Registry (Web-app) </summary> <!-- tp -->

### +/ Linux <!-- PLATFORM -->
#### Start local storage docker-image <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 docker run -d -p 5000:5000 --restart=always --name registry registry:2
```
<!-- CODE -->


<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->


- `docker run`: Starts a new container<!-- JUST -->

- `-d`: Runs the container in detached (background) mode <!-- JUST -->

- `-p 5000:5000`: Maps host port 5000 to container port 5000 <!-- JUST -->

- `--restart=` <!-- JUST -->
  - `no`: Doesn’t restart after stopping (default) <!-- SPACE -->
  - `always`: Restarts on failure or reboot <!-- SPACE -->
  - `unless-stopped`: Doesn’t restart if manually stopped <!-- SPACE --> 

- `--name registry`: Sets the container name <!-- JUST -->

- `registry:2`: Official Docker Registry image, version 2. <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

#### Create project directory <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 mkdir web-app cd web-app
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
 nano index.html
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
    <html>
  <body>
<center><h1><b>WEB</b></h1></center>
  </body>
    </html>
```
<!-- CODE -->

#### Create a file named Dockerfile to define container image configuration
 <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 nano Dockerfile
```
<!-- CODE -->

<!-- CODE -->
```MarkDown Keemplate
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
```
<!-- CODE -->


<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->


- `FROM nginx:alpine`: Sets the base image for the build <!-- JUST -->

- `COPY index.html /usr/share/nginx/html/index.html`: Copies index.html from the host to the container, replacing the default nginx homepage <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

#### Build docker-image <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 docker build -t web:1.0 .
```
<!-- CODE -->


<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->


- `-t web:1.0`: <!-- JUST -->

-    `web`: name image <!-- SPACE -->

-    `1.0`: version image <!-- SPACE -->

- `.`: Указывает текущую директорию как контекст сборки. <!-- JUST -->
Sets the current directory as the build context

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

#### Load the image into the local Registry <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 docker tag web:1.0 localhost:5000/web:1.0
```
<!-- CODE -->


<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->


- `docker tag`: <!-- JUST -->

-    `localhost:5000/web:1.0`: Assigns a new tag to the image with the local Docker Registry address for pushing: `docker push localhost:5000/web:1.0`
<!-- SPACE -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

#### The image is available at localhost:5000/web:1.0 <!-- ACTION -->
#### Test the Docker image <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 docker pull localhost:5000/web:1.0
```
<!-- CODE -->

#### Deploy
<!-- CODE -->
```MarkDown Keemplate
docker run -d --name web -p 80:80 --restart=always web:1.0
```
<!-- CODE -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->


- `-p 80:80`: Maps host port 80 to container port 80 <!-- JUST -->

- `--restart=always`: Enables automatic container restart on host reboot or failure <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

#### Check work on 80 port (http) <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 curl http://localhost
```
<!-- CODE -->


</details> <!-- TOPIC -->

<details>
<summary> `Hello-app` at Registry  </summary> <!-- tp -->

#### Start local storage docker-images <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```
<!-- CODE -->
---

#### Write Dockerfile <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
echo "experts" > ./name.txt
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano Dockerfile
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
FROM alpine
WORKDIR /hello
COPY name.txt ./
CMD echo "Hello! Greetings from $(cat name.txt)"
```
<!-- CODE -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->

##### 

###  <!-- LIST -->
- `FROM` <!-- JUST -->
    - base image <!-- SPACE -->
- `WORKDIR` <!-- JUST -->
    - sets the working directory inside the container <!-- SPACE -->
- `COPY` <!-- JUST -->
    - copies a file from the local host to the container’s working directory <!-- SPACE -->
- `CMD` <!-- JUST -->
    - defines the command executed after container start, then the container stops <!-- SPACE -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

---
<!-- CODE -->

```MarkDown Keemplate
docker build -t hallo-app .
```
<!-- CODE -->
---

#### Check first start <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
docker run --name Hello hallo-app
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
docker rm Hello
```
<!-- CODE -->
---

#### Build image from Dockerfile and push to local Docker Registry
 <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
docker tag hallo-app localhost:5000/hallo-app:1.0
```
<!-- CODE -->

> Load <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
docker push localhost:5000/hallo-app:1.0
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
docker images
```
<!-- CODE -->

#### Removing images <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
rmi localhost:5000/hallo-app:1.0 hallo-app
```
<!-- CODE -->
---

#### Load image from Registry <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
docker pull localhost:5000/hallo-app:1.0
```
<!-- CODE -->

#### Check start <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
docker run --name Hello localhost:5000/app:1.0
```
<!-- CODE -->

</details> <!-- TOPIC -->

---

<details>
<summary> Grafana-Prometheus-NodeExporter  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
cd /home/USER
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano monitoring.yml
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
version: '3.3'
networks:
monitoring:
driver: bridge
volumes:
prometheus_data: {}
services:
node-exporter:
image: prom/node-exporter:latest
container_name: node-exporter
restart: unless-stopped
volumes:
- /proc:/host/proc:ro
- /sys:/host/sys:ro
- /:/rootfs:ro
command:
- '--path.procfs=/host/proc'
- '--path.rootfs=/rootfs'
- '--path.sysfs=/host/sys'
- '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
ports:
- 9100:9100
networks:
- monitoring
grafana:
image: grafana/grafana-enterprise
container_name: grafana
restart: unless-stopped
ports:
- 3000:3000
prometheus:
image: prom/prometheus:latest
container_name: prometheus
restart: unless-stopped
volumes:
- ./prometheus.yml:/etc/prometheus/prometheus.yml
- prometheus_data:/prometheus
command:
- '--config.file=/etc/prometheus/prometheus.yml'
- '--storage.tsdb.path=/prometheus'
- '--web.console.libraries=/etc/prometheus/console_libraries'
- '--web.console.templates=/etc/prometheus/consoles'
- '--web.enable-lifecycle'
ports:
- 9090:9090
networks:
- monitoring
```
<!-- CODE -->

#### At /home/USER <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano prometheus.yml
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
global:
scrape_interval: 15s
scrape_configs:
- job_name: "prometheus"
scrape_interval: 5s
static_configs:
- targets: ["localhost:9090"]
- job_name: "node"
static_configs:
- targets: ["node-exporter:9100"]
```
<!-- CODE -->

#### Start <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
docker compose -f monitoring.yml up -d
```
<!-- CODE -->

#### Open Grafana at BROWSER <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
http://localhost:3000
```
<!-- CODE -->

### Sign in <!-- LIST -->
- Name: `admin` <!-- JUST -->
- Password: `admin` <!-- JUST -->

### Settings Dashboard <!-- LIST -->
- Add data source: `Prometheus` <!-- JUST -->
- Connection: `127.0.0.1:9090` <!-- JUST -->
- Save & test <!-- JUST -->
- Open menu (logo Grafana) <!-- JUST -->
- Dashboards <!-- JUST -->
- New (import) <!-- JUST -->
- id: `1860` (you may need to download .json) <!-- JUST -->
    - Check imported Dashboard <!-- SPACE -->

</details> <!-- TOPIC -->


<details>
<summary> MediaWiki  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
nano wiki.yml
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
# Access via [http://localhost:8081](http://localhost:8081) or http\://\$(docker-machine ip):8081 if using docker-machine

version: '3'
services:
mediawiki:
image: mediawiki
restart: always
networks:
- docker_network
ports:
- 8081:80
volumes:
- /var/www/html/
# After initial setup, download LocalSettings.php to the same directory as this YAML file, uncomment the specified line, and use Docker Compose to restart the mediawiki service

# - ./LocalSettings.php:/var/www/html/LocalSettings.php
database:
image: mysql:5.7
restart: always
networks:
- docker_network
environment:
MYSQL_DATABASE: wiki_db
MYSQL_ROOT_PASSWORD: root
MYSQL_USER: wikimedia
MYSQL_PASSWORD: wikimedia
volumes:
- /var/lib/mysql
networks:
docker_network:
driver: bridge
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
docker compose -f wiki.yml up -d
```
<!-- CODE -->

#### Settings at Browser <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
http://localhost:8081
```
<!-- CODE -->

### Points settings <!-- LIST -->
- Database: `MySQL` <!-- JUST -->
- Database Host: `database:3306` <!-- JUST -->
- Database name: `my_wiki` <!-- JUST -->
- Database username: `root` <!-- JUST -->
- Database password: `root` <!-- JUST -->
    - Create Administrator <!-- SPACE -->
    - Download `LocalSettings.php` <!-- SPACE -->

#### Uncomment at `wiki.yml` <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
- ./LocalSettings.php:/var/www/html/LocalSettings.php
```
<!-- CODE -->

#### Install LocalSettings.php to wiki container <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
docker cp LocalSettings.php USERNAME-mediawiki-1:/var/www/html
```
<!-- CODE -->

#### Restart and check <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
http://localhost:8081
```
<!-- CODE -->

</details>            <!-- TOPIC -->

<details>
<summary> WordPress  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
cd /home/USERNAME
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano wordpress.yml
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
version: '3.8'

services:
  wordpress:
    image: wordpress:latest
    container_name: wordpress
    networks:
      - wordpress-network
    ports:
      - "8084:80"
    environment:
      WORDPRESS_DB_HOST: mysql:3306
      WORDPRESS_DB_NAME: wp_db
      WORDPRESS_DB_USER: wp_user
      WORDPRESS_DB_PASSWORD: P@ssw0rd
    depends_on:
      - mysql

  mysql:
    image: mysql:5.7
    container_name: mysql
    networks:
      - wordpress-network
    environment:
      MYSQL_ROOT_PASSWORD: P@ssw0rd
      MYSQL_DATABASE: wp_db
      MYSQL_USER: wp_user
      MYSQL_PASSWORD: P@ssw0rd
    volumes:
      - mysql-data:/var/lib/mysql

networks:
  wordpress-network:
    driver: bridge

volumes:
  mysql-data:
	driver: local
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
docker compose -f wordpress.yml up -d
```
<!-- CODE -->
---

#### Verify in the BROWSER <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
localhost:8084
```
<!-- CODE -->

</details>            <!-- TOPIC -->

<details>
<summary> Elasticsearch - Logstash - Kibana (ELK)  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
cd /home/USERNAME
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano elk.yml
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
version: '3.8'

services:
  elasticsearch:
    image: elasticsearch:7.10.1
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
    networks:
      - elk-network

  logstash:
    image: logstash:7.10.1
    container_name: logstash
    depends_on:
      - elasticsearch
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf:ro
    networks:
      - elk-network

  kibana:
    image: kibana:7.10.1
    container_name: kibana
    depends_on:
      - elasticsearch
    ports:
      - "5601:5601"
    networks:
      - elk-network

networks:
  elk-network:
    driver: bridge

```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano logstash.conf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
input {
  beats {
    port => 5044
  }
}

filter {
  mutate {
    remove_field => ["@version", "host"]
  }
}

output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}

```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
docker compose -f elk.yml up -d
```
<!-- CODE -->
---

#### Loading may take time and require additional resources
 <!-- ACTION -->

#### Verify in the browser
 <!-- ACTION -->

> Elasticsearch <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
localhost:9200
```
<!-- CODE -->

> Kibana <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
localhost:5601
```
<!-- CODE -->

> For check work Elasticsearch <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
curl -X GET "http://localhost:9200"
```
<!-- CODE -->

</details>            <!-- TOPIC -->

</details>        <!-- FFIELD -->

### F)

<details>
<summary> FreeIPA  </summary>     <!-- ff -->

### +/ Alt linux <!-- PLATFORM -->

#### 1. Install on SRV-HQ <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install -y freeipa-server
ipa-server-install --setup-dns
```
<!-- CODE -->

###  <!-- LIST -->
- `Server host name [srv-hq.your.domain]:` <!-- JUST -->
    - Leave default or enter desired hostname <!-- SPACE -->
- `Please confirm the domain name [your.domain]:` <!-- JUST -->
    - Confirm or modify if necessary <!-- SPACE -->
- `Please provide a realm name [YOUR.DOMAIN]:` <!-- JUST -->
    - Confirm or modify realm name (usually uppercase domain) <!-- SPACE -->

### Also <!-- LIST -->
- `Directory Manager (existing master key):` <!-- JUST -->
    - Enter LDAP admin password for user/group management <!-- SPACE -->
- `IPA admin password:` <!-- JUST -->
    - Enter password for admin user (web interface and CLI) <!-- SPACE -->

### If `--setup-dns` <!-- LIST -->
- `Do you want to configure DNS forwarders? [yes]:` <!-- JUST -->
    - Choose yes to use external DNS (e.g., Google 8.8.8.8)<!-- SPACE -->
- `Enter the IP address of DNS forwarder []:` <!-- JUST -->
    - Choose yes to use external DNS (e.g., Google 8.8.8.8) <!-- SPACE -->
- `Do you want to configure the reverse DNS zone? [yes]:` <!-- JUST -->
    - Choose yes if FreeIPA should handle reverse DNS queries <!-- SPACE -->

#### 2. Create Users <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
for i in {1..30}; do
    ipa user-add user$i --first=User --last=$i --password
done
```
<!-- CODE -->

#### 3. Create Groups <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
for i in {1..3}; do
    ipa group-add group$i
done

for i in {1..10}; do
    ipa group-add-member group1 --users=user$i
done

for i in {11..20}; do
    ipa group-add-member group2 --users=user$i
done

for i in {21..30}; do
    ipa group-add-member group3 --users=user$i
done
```
<!-- CODE -->

#### 4. Connect CLI-HQ to FreeIPA <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install -y freeipa-client
ipa-client-install --server=SRV-HQ --domain=your.domain --mkhomedir
```
<!-- CODE -->

#### 5. Install CA certificate on CLI-HQ <!-- ACTION -->

#### On SRV-HQ <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
scp /etc/ipa/ca.crt root@CLI-HQ:/etc/pki/ca-trust/source/anchors/
```
<!-- CODE -->

#### On CLI-HQ <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
update-ca-trust
```
<!-- CODE -->

#### 5. Check <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
ipa user-find admin
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
curl https://srv-hq.your.domain
```
<!-- CODE -->

</details>             <!-- FFIELD -->


### G)

<details>
<summary> GRUB </summary> 
<details>
<summary> password recovery</summary> <!-- TOPIC -->
  
### +/ Linux   <!-- PLATFORM -->

#### Enter to advanced mode and click 'e' <!-- ACTION -->
  
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/grub/welcomeScreen.png) <!-- SCREEN -->

#### At the line starting with `linux /boot/vmlinuz/...`, add the required code below it, then press `F10` to continue.
<!-- ACTION -->

<!-- CODE -->
```bash
init=/bin/bash
```
<!-- CODE -->
#### Enter the following commands below
<!-- ACTION -->

<!-- CODE -->
```bash
mount -o remount,rw /
passwd root
reboot -f
```
<!-- CODE -->

</details>
</details>

### H)
### I)
### J)
### K)
### L)

<details>
<summary> LVM (Logical Volume Manager)  </summary>     <!-- ff -->

#### Components <!-- ACTION -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->

##### 

###  <!-- LIST -->
- `Physical Volume` (PV) — a physical device such as a hard disk <!-- JUST -->
- `Volume Group` (VG) — a group of physical volumes combining multiple devices <!-- JUST -->
- `Logical Volume` (LV) — a logical volume used like a regular partition or filesystem <!-- JUST -->
- `Physical Extent` (PE) — the smallest data unit used for allocation across physical volumes <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

---

<details>
<summary> Partition tables and layout for each new device </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
parted /dev/sda
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
mklabel gpt
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
mkpart primary 0% 100%
```
<!-- CODE -->
---
<!-- CODE -->

```MarkDown Keemplate
parted /dev/sdb
mklabel gpt
mkpart primary 0% 100%
```
<!-- CODE -->
---

#### Check <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
lsblk
```
<!-- CODE -->

</details> <!-- TOPIC -->


<details>
<summary> Mounting (+auto)  </summary> <!-- tp -->

#### Formating <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mkfs.ext4 /dev/sda
```
<!-- CODE -->
---

#### Create the path<!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mkdir -p /opt/data
```
<!-- CODE -->

#### Mount <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mount /dev/sda /opt/data
```
<!-- CODE -->

#### Auto <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/fstab
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
/dev/sda /opt/data ext4 defaults 0 2
```
<!-- CODE -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->

##### 

###  <!-- LIST -->
- `/dev/sda`: dev <!-- JUST -->
- `/opt/data`: point mount <!-- JUST -->
- `defaults`: generalizing <!-- JUST -->
    - (rw,suid,dev,exec,auto,nouser,async) <!-- SPACE -->
- `0`: management backup (dump-flag) <!-- JUST -->
    - `0`: do not <!-- SPACE -->
    - `1`: usually root (/) <!-- SPACE -->
    - `2`: another system check before root (/home, /opt, /var) <!-- SPACE -->
- `2`: check before restart <!-- JUST -->
    - `0`: do not <!-- SPACE -->
    - `1`: first (usually root) <!-- SPACE -->
    - `2`: another system check before root (/home, /opt, /var) <!-- SPACE -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

---
<!-- CODE -->

```MarkDown Keemplate
df -h
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
reboot
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
df -h
```
<!-- CODE -->

</details> <!-- TOPIC -->


<details>
<summary> Encryption  </summary> <!-- tp -->

#### Create key <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
dd if=/dev/urandom of=/root/ext4.key bs=1024 count=4
```
<!-- CODE -->

#### Encrypt `/dev/data_striped/lv_data` with specified key <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
cryptsetup luksFormat /dev/data_striped/lv_data /root/ext4.key
```
<!-- CODE -->

#### Open crypted part as `data_crypt` <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
cryptsetup luksOpen /dev/data_striped/lv_data data_crypt --key-file /root/ext4.key
```
<!-- CODE -->

#### Formating <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
mkfs.ext4 /dev/mapper/data_crypt
```
<!-- CODE -->

#### Autounlocking before restart <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/crypttab
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
data_crypt /dev/data_striped/lv_data /root/ext4.key luks
```
<!-- CODE -->

#### Check syntax <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
systemctl daemon-reexec
systemctl restart systemd-cryptsetup@data_crypt
```
<!-- CODE -->

#### Mounting <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/fstab
```
<!-- CODE -->

#### For lv must have one record <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
/dev/mapper/data_crypt /opt/data ext4 defaults 0 2
```
<!-- CODE -->

#### Protect key-file <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
chmod 600 /root/ext4.key
chown root:root /root/ext4.key
```
<!-- CODE -->

#### Accept <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
reboot
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
df -h
```
<!-- CODE -->

</details> <!-- TOPIC -->


<details>
<summary> striped (RAID 0)  </summary> <!-- tp -->

> Ensure you have two unpartitioned hard drives <!-- Citation -->

#### Create PV <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
pvcreate /dev/sda1 /dev/sdb1
```
<!-- CODE -->

#### Create VG <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
vgcreate vg01 /dev/sd{a,b}1
```
<!-- CODE -->

#### Create LV <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
lvcreate -l 100%FREE -n lv_data vg01
```
<!-- CODE -->
---

#### Mounting `/dev/vg01/lv_data` <!-- ACTION -->

> see topic `Mounting` <!-- Citation -->

</details> <!-- TOPIC -->


<details>
<summary> mirroring (RAID 1)  </summary> <!-- tp -->

> Ensure you have two unpartitioned hard drives <!-- Citation -->

#### Create PV <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
pvcreate /dev/sda1 /dev/sdb1
```
<!-- CODE -->

#### Create VG <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
vgcreate vg01 /dev/sd{a,b}1
```
<!-- CODE -->

#### Create LV <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
lvcreate -l 100%FREE -n lvmirror -m1 vg01
```
<!-- CODE -->

#### Mounting `/dev/vg01/lvmirror` <!-- ACTION -->

> see topic `Mounting` <!-- Citation -->
---

#### Check <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
reboot
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
df -h
```
<!-- CODE -->

</details>            <!-- TOPIC -->

</details>             <!-- FFIELD -->


### M)

<details>
<summary>Microsoft office</summary>
    
### +/ Arch Linux <!-- PLATFORM -->

<details>
<summary>Install</summary> <!-- TOPIC -->

#### YOU MUST HAVE yay <!-- ACTION -->
<!-- CODE -->

```bash
sudo pacman -S git
```

<!-- CODE -->

<!-- CODE -->

```bash
git clone https://aur.archlinux.org/packages/yay
```

<!-- CODE -->

<!-- CODE -->

```bash
cd yay
```

<!-- CODE -->

<!-- CODE -->

```bash
makepkg -si
```

<!-- CODE -->

#### Install PlayOnLinux <!-- ACTION -->
<!-- CODE -->

```bash
yay -S playonlinux
```

<!-- CODE -->

#### Then change OS to Windows XP in cfg <!-- ACTION -->
<!-- CODE -->

```bash
winecfg
```

<!-- CODE -->

#### Download <!-- ACTION -->


#### resource wine OS <!-- ACTION -->
<!-- CODE -->

```bash
https://drive.google.com/file/d/1jwb7gZ0a1YH6ko-11yrHMYaOJLB1qIft/view?usp=sharing
```

<!-- CODE -->

#### MS image <!-- ACTION -->
<!-- CODE -->

```bash
https://drive.google.com/file/d/1GiaocKaRqlPBarvofxSaj20MLbLYD1ZM/view?usp=sharing
```

<!-- CODE -->

#### Replace resource wine OS <!-- ACTION -->
#### These operations are required for successful md5sum verification in the Wizar<!-- ACTION -->
<!-- CODE -->

```bash
rm -rf /home/$USER/.PlayOnLinux/ressources/WindowsXP-KB975337-x86-ENU.exe
```

<!-- CODE -->

<!-- CODE -->

```bash
cp home/$USER/Downloads/WindowsXP-KB975337-x86-ENU.exe /home/$USER/.PlayOnLinux/ressources/
```

<!-- CODE -->

#### Install ms office 2010 <!-- ACTION -->

#### Create scenario <!-- ACTION -->
<!-- CODE -->

```bash
#!/bin/bash
# CHANGELOG
# [Quentin PГ‚RIS] (2012-05-05 14-45)
#   Wine version set to 1.5.3, Outlook 2010 compatiblity
# [Quentin PГ‚RIS] (2012-05-05 15-05)
#   Check winbind (samba) presence on Linux, required to install
#   Adding gettext support
# [Quentin PГ‚RIS] (2012-05-12 18-36)
#   Requires 4.0.18
# [SuperPlumus] (2013-06-09 14-44)
#   gettext
# [Quentin PГ‚RIS] (2014-07-21 17-09)
#   Updating with the latest WineHQ version
# [rbelo] (2018-07-22 15-50)
#   Updating with the latest stable WineHQ version (3.0.2), ver 1.7.52 does not seem to work.
# [Mrjacobarussell] (2018-09-25 20-50)
#   Updating missing dotnet20, gdiplus, gecko, corefonts, msxml6
# [diogoborges14] (2018-12-01)
#   mspatcha
# [Dadu042] (2020-02-10 12-33)
#   Wine 3.0.2 -> 3.0.3 (more common on POL nowadays).
#   Note: I think that lines POL_Wine_OverrideDLL for riched20 and riched30 are useless.
[ "$PLAYONLINUX" = "" ] && exit 0
source "$PLAYONLINUX/lib/sources"
PREFIX="Office2010"
WINEVERSION="3.0.3"
TITLE="Microsoft Office 2010"
POL_GetSetupImages "http://files.playonlinux.com/resources/setups/Office/top.jpg" "http://files.playonlinux.com/resources/setups/Office/left.png" "$TITLE"
POL_SetupWindow_Init
POL_SetupWindow_SetID 801
POL_SetupWindow_presentation "$TITLE" "Microsoft" "http://www.microsoft.com" "Quentin PГ‚RIS" "$PREFIX"
POL_RequiredVersion 4.0.18 || POL_Debug_Fatal "$TITLE won't work with $APPLICATION_TITLE $VERSIONnPlease update"
if [ "$POL_OS" = "Linux" ]; then
        wbinfo -V || POL_Debug_Fatal "Please install winbind (or samba, on Arch Linux) before installing $TITLE"
fi
POL_Debug_Init
POL_System_SetArch "x86"
POL_SetupWindow_InstallMethod "LOCAL,DVD"
if [ "$INSTALL_METHOD" = "DVD" ]; then
        POL_SetupWindow_cdrom
        POL_SetupWindow_check_cdrom "x86/setup.exe" "setup.exe"
        SetupIs="$CDROM_SETUP"
        cd "$CDROM"
else
        POL_SetupWindow_browse "$(eval_gettext 'Please select the setup file to run')" "$TITLE"
        SetupIs="$APP_ANSWER"
fi
POL_Wine_SelectPrefix "$PREFIX"
POL_Wine_PrefixCreate "$WINEVERSION"
if [ "$POL_OS" = "Mac" ]; then
    # Samba support
    POL_Call POL_GetTool_samba3
    source "$POL_USER_ROOT/tools/samba3/init"
fi
POL_Wine_WaitBefore "$TITLE"
[ "$CDROM" ] && cd "$CDROM"
if [ ! "$(file $SetupIs | grep 'x86-64')" = "" ]; then
    POL_Debug_Fatal "$(eval_gettext "The 64bits version is not compatible! Sorry")";
fi
POL_Wine "$SetupIs"
POL_Wine_WaitExit "$TITLE"
POL_Call POL_Install_dotnet20
POL_Call POL_Install_gecko
POL_Call POL_Install_corefonts
POL_Call POL_Install_gdiplus
POL_Call POL_Install_riched20
POL_Call POL_Install_riched30
POL_Call POL_Install_msxml6
POL_Call POL_Install_mspatcha
POL_Wine_OverrideDLL "native,builtin" "riched20"
POL_Wine_OverrideDLL "native,builtin" "riched30"
POL_Wine_OverrideDLL "native,builtin" "gdiplus"
POL_Shortcut "WINWORD.EXE" "Microsoft Word 2010" "" "" "Office;WordProcessor;"
POL_Shortcut "EXCEL.EXE" "Microsoft Excel 2010" "" "" "Office;Spreadsheet;"
POL_Shortcut "POWERPNT.EXE" "Microsoft Powerpoint 2010" "" "" "Office;Presentation;"
POL_Shortcut "ONENOTE.EXE" "Microsoft OneNote 2010" "" "" "Network;InstantMessaging;"
POL_Shortcut "OUTLOOK.EXE" "Microsoft Outlook 2010" "" "" "Network;Email;"
POL_Extension_Write doc "Microsoft Word 2010"
POL_Extension_Write docx "Microsoft Word 2010"
POL_Extension_Write xls "Microsoft Excel 2010"
POL_Extension_Write xlsx "Microsoft Excel 2010"
POL_Extension_Write ppt "Microsoft Powerpoint 2010"
POL_Extension_Write pptx "Microsoft Powerpoint 2010"
if [ "$POL_OS" = "Mac" ]; then
    POL_Shortcut_InsertBeforeWine "Microsoft Word 2010" "source "$POL_USER_ROOT/tools/samba3/init""
    POL_Shortcut_InsertBeforeWine "Microsoft Excel 2010" "source "$POL_USER_ROOT/tools/samba3/init""
    POL_Shortcut_InsertBeforeWine "Microsoft Powerpoint 2010" "source "$POL_USER_ROOT/tools/samba3/init""
    POL_Shortcut_InsertBeforeWine "Microsoft OneNote 2010" "source "$POL_USER_ROOT/tools/samba3/init""
    POL_Shortcut_InsertBeforeWine "Microsoft Outlook 2010" "source "$POL_USER_ROOT/tools/samba3/init""
fi
POL_SetupWindow_message "$(eval_gettext '$TITLE has been installed successfullynnIf an installation Windows prevent your programs from running, you must remove and reinstall $TITLE')" "$TITLE"
POL_SetupWindow_Close
exit 0
```

<!-- CODE -->

```bash
nano installMS.sh 
chmod +x installMS.sh 
```

```bash
playonlinux 
```

#### Click on Utilities/Tools and select "Execute local script"
#### Then click Continue and choose the local scenario before proceeding select image MS2010 in the Wizard and wait
<!-- ACTION -->

</details>
</details>
</details>


### N)
<details>
<summary> Network settings </summary> 
	
---

<details>
<summary> Basic settings</summary> <!-- TOPIC -->
<details>

 
<summary> IP addr</summary> 

### +/ Linux Alt (etcnet) <!-- PLATFORM -->

#### Example configuration for interface ens32 <!-- ACTION -->

#### Catalog interface <!-- ACTION -->

<!-- CODE -->

```bash
mkdir -p /etc/net/ifaces/ens32
```

#### Based options <!-- ACTION -->

<!-- CODE -->

```bash
nano /etc/net/ifaces/ens32/options
```

<!-- CODE -->

```bash
TYPE=eth
BOOTPROTO=static
CONFIG_IPV4=yes
```

#### or for dynamic IP at string <!-- ACTION -->

<!-- CODE -->

```bash
BOOTPROTO=dhcp
```

#### Write IP address <!-- ACTION -->

<!-- CODE -->

```bash
nano /etc/net/ifaces/ens32/ipv4address
```

<!-- CODE -->

```bash
192.168.11.67/28 # 32 - 28 = 4 and 2**4 = 16 address where 1 - network; 16 - broadcast 
192.168.33.67 # second with /32
```

#### Write gateway <!-- ACTION -->

<!-- CODE -->

```bash
nano /etc/net/ifaces/ens32/ipv4route
```

<!-- CODE -->

```bash
default via 192.168.11.1
```

#### Accept changes <!-- ACTION -->

<!-- CODE -->

```bash
systemctl restart network
```

<!-- CODE -->


### +/ Linux Debian-based  <!-- PLATFORM -->

#### Find exist interfaces <!-- ACTION -->

<!-- CODE -->
```bash
ip a
```
<!-- CODE -->
#### In /etc/network/interfaces for static, dynamic <!-- ACTION -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/Basic/interfaces.png) <!-- SCREEN -->

#### Accept network changes<!-- ACTION -->

<!-- CODE -->
```bash
systemctl restart networking.service
```
<!-- CODE -->

</details>

<details>
<summary> DHCP  </summary> <!-- tp -->

### +/ Linux <!-- PLATFORM -->

#### 1. Install <!-- ACTION -->

> For Alt <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install dhcp-server
```
<!-- CODE -->

> For Debian <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install isc-dhcp-server
```
<!-- CODE -->
---

#### 2. Identify network interface distribution<!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
ip a -c
```
<!-- CODE -->

> For Alt <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/sysconfig/dhcpd
```
<!-- CODE -->

> For Debian <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/default/isc-dhcp-server
```
<!-- CODE -->

> Write <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
DHCPDARGS=ens34
```
<!-- CODE -->
---

#### 3. General settings <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/dhcp/dhcpd.conf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
ddns-update-style none;

subnet 192.168.11.0 netmask 255.255.255.192 {
        option routers                  192.168.11.1;
        option domain-name              "au.team";
        option domain-name-servers      77.88.8.8,192.168.11.1;

        range dynamic-bootp 192.168.11.2 192.168.11.63;
        default-lease-time 21600;
        max-lease-time 43200;
host R-HQ{
        hardware ethernet 00:0c:29:41:f2:9f;    
        fixed-address 192.168.11.1;
}
}

```
<!-- CODE -->

> For Alt <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable --now dhcpd
```
<!-- CODE -->

> For Debian <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable --now isc-dhcp-server
```
<!-- CODE -->
---

#### Check <!-- ACTION -->

> For Alt <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
systemctl status dhcpd
```
<!-- CODE -->

> For Debian <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
systemctl status isc-dhcp-server
```
<!-- CODE -->

</details>            <!-- TOPIC -->

<details>
	
<summary> vlan</summary> <!-- TOPIC --> 

### +/ Linux Alt (etcnet) <!-- PLATFORM -->

#### Check interfaces <!-- ACTION -->

<!-- CODE -->

```bash
ip a
```

<!-- CODE -->

#### VLAN for ens32 <!-- ACTION -->

<!-- CODE -->

```bash
mkdir -p /etc/net/ifaces/ens32.100
```

#### In /etc/net/ifaces/ens32.100/options <!-- ACTION -->

<!-- CODE -->

```bash
TYPE=vlan # !
CONFIG_IPV4=yes
BOOTPROTO=static
VID=100 # number vlan
HOST=ens32 # for more 'ens32 ens33'
```

#### In /etc/net/ifaces/ipv4address <!-- ACTION -->

<!-- CODE -->

```bash
192.168.11.67/24
```

#### Accepting <!-- ACTION -->

<!-- CODE -->

```bash
sytsemctl restart network
```

<!-- CODE -->

#### else emerge <!-- ACTION -->

<!-- CODE -->

```bash
dhcpd
```

<!-- CODE -->


### +/ Linux Debian <!-- PLATFORM --> 

#### Write subinterfaces /etc/network/interfaces<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/VLAN/deb_vlan.png) <!-- SCREEN --> 

<!-- CODE -->
```bash
systemctl restart networking
```
<!-- CODE --> 

</details>

---

<details> 


### +/ Linux <!-- PLATFORM --> 


<summary> SSHuser-SUDO</summary> <!-- TOPIC --> 

<!-- CODE -->
```bash
apt-get install openssh sudo
useradd sshuser
passwd sshuser
usermod -aG wheel(sudo*) sshuser
echo "sshuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
systemctl enable --now sshd
```
<!-- CODE --> 

</details>

<details>
<summary> SSH-connection automate to SERVERS  </summary> <!-- tp -->

### +/ Linux <!-- PLATFORM -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install openssh-server
```
<!-- CODE -->

#### SERVERS <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
useradd sshuser
```
<!-- CODE -->
---

#### CLIENTS <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
ssh-keygen -t rsa -b 2048 -f srv_ssh_key
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
mv srv_ssh_key* .ssh/
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano .ssh/config
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
Host srv-hq
        HostName 192.168.11.67
        User sshuser
        IdentityFile .ssh/srv_ssh_key
        Port 2025
Host srv-br
        HostName 192.168.33.67
        User sshuser
        IdentityFile .ssh/srv_ssh_key
        Port 2025
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
chmod 600 .ssh/config
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
ssh-copy-id -i .ssh/srv_ssh_key.pub sshuser@192.168.11.67
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
ssh-copy-id -i .ssh/srv_ssh_key.pub sshuser@192.168.33.67
```
<!-- CODE -->
---

#### SERVERS <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/openssh/sshd_config
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
AllowUsers sshuser
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
AuthorizedKeysFile .ssh/authorized_keys
Port 2025
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart sshd
```
<!-- CODE -->

#### Connection <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
ssh srv-hq
```
<!-- CODE -->

</details>            <!-- TOPIC -->

---

<details>
<summary> Repository</summary> 

### +/ Linux   <!-- PLATFORM -->

#### In /etc/apt/sources.list commenting first string and write<!-- ACTION -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/Basic/reps.png) <!-- SCREEN -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/Basic/reps_alt.png) <!-- SCREEN -->

</details>
<details>
<summary> Delegation DNS</summary> 

### +/ Linux   <!-- PLATFORM -->

#### In /etc/resolv.conf<!-- ACTION -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/Basic/resolv.png) <!-- SCREEN -->

</details>


<!-- UPDATING PLATFORM -->

<!-- UPDATING PLATFORM -->
</details>


---

<details>
<summary> Tunneling </summary> 
<details>
<summary> GRE</summary> <!-- TOPIC -->

### +/ Alt linux (etcnet) <!-- PLATFORM -->

#### Turn on ip_forward<!-- ACTION -->

<!-- CODE -->

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

<!-- CODE -->

<!-- CODE -->

```bash
nano /etc/sysctl.conf
```

<!-- CODE -->

<!-- CODE -->

```bash
net.ipv4.ip_forward=1
```

<!-- CODE -->

<!-- CODE -->

```bash
sysctl -p
```

<!-- CODE -->

<!-- CODE -->

```bash
mkdir -p /etc/net/ifaces/tun
```

<!-- CODE -->

<!-- CODE -->

```bash
nano /etc/net/ifaces/tun/options
```

<!-- CODE -->

<!-- CODE -->

```bash
TYPE=iptun
TUNTYPE=gre
TUNLOCAL=172.16.4.1 # interface ens33
TUNREMOTE=172.16.5.1 # input remote network
HOST=ens33 # output interface
TUNOPTIONS='ttl 64'
TUNTTL=64
TUNMTU=1476
```

<!-- CODE -->

<!-- CODE -->

```bash
nano /etc/net/ifaces/tun/ipv4address
```

<!-- CODE -->

<!-- CODE -->

```bash
10.10.10.2/30
```

<!-- CODE -->

<!-- CODE -->

```bash
systemctl restart network
```

<!-- CODE -->

#### Mirror on another router <!-- ACTION -->

### +/ Linux Debian <!-- PLATFORM -->

#### In /etc/modules write 'ip_gre'
#### or just turn on

<!-- CODE -->

```bash
modprobe ip_gre
```

<!-- CODE -->

#### Turn on ip_forward<!-- ACTION -->

<!-- CODE -->
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
<!-- CODE -->
#### Uncomment string in /etc/sysctl.conf <!-- ACTION -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/Tunneling/sysctlForward.png) <!-- SCREEN -->

#### Accept changes <!-- ACTION -->

<!-- CODE -->
```bash
sysctl -p
```
<!-- CODE -->

#### In /etc/network/interfaces write new tunnel and mirror on another device<!-- ACTION -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/Tunneling/int_tunn.png) <!-- SCREEN -->

#### Accept network changes<!-- ACTION -->

<!-- CODE -->
```bash
systemctl restart networking.service
```
<!-- CODE -->

<details>
  <summary>manual</summary>
  
<!-- GENERAL COMMENT -->
  
** **
<!-- GENERAL COMMENT -->
</details>
<details>
<summary>unaccept</summary>
<!-- UPDATING PLATFORM -->

<!-- UPDATING PLATFORM -->
</details>

</details>

<details>
<summary>IPsec</summary> <!-- TOPIC -->

### +/ Linux <!-- PLATFORM -->

#### A functional tunnel is required to encrypt the connection
<!-- ACTION -->

<!-- CODE -->

```bash
apt-get install strongswan
```

<!-- CODE -->

#### May be /etc/ipsec.conf /etc/ipsec.secrets <!-- ACTION -->

#### On router with 10.10.10.1 <!-- ACTION -->

<!-- CODE -->

```bash
nano /etc/strongswan/ipsec.conf
```

<!-- CODE -->

<!-- CODE -->

```bash
config setup

conn nameConnect
        authby=psk # use secret key
        keyexchange=ikev2 # protocol Internet Key Exchange      

        leftid=10.10.10.1 # public id address (@tunnel.example.com)

        left=10.10.10.1 # local ip
        leftsubnet=10.10.10.0/30 # local net for working connection

        rightid=10.10.10.2 # remote public id address (@tunnel.example.com)

        right=10.10.10.2 # remote local ip
        rightsubnet=10.10.10.0/30 # remote local net for working connection

        auto=start # install connect before restart
```

<!-- CODE -->

<!-- CODE -->

```bash
nano /etc/strongswan/ipsec.secrets
```

<!-- CODE -->

<!-- CODE -->

```bash
10.10.10.1 10.10.10.2 : PSK "P@ssw0rd"
```

<!-- CODE -->

#### Mirror actions on another router <!-- ACTION -->

<!-- CODE -->

```bash
systemctl enable --now strongswan-starter ipsec
```

<!-- CODE -->

#### Check <!-- ACTION -->

<!-- CODE -->

```bash
ipsec status
```

<!-- CODE -->

<!-- CODE -->

```bash
ping 10.10.10.2
```

<!-- CODE -->

</details>

</details>

<!-- FIELD (FIRST LETTER ALFABET) -->
<details>
<summary> NAT </summary> 
<details>
<summary> nftables</summary> <!-- TOPIC -->
  
### +/ Linux   <!-- PLATFORM -->
#### Turn on ip_forward<!-- ACTION -->

<!-- CODE -->
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
<!-- CODE -->
#### Uncomment string in /etc/sysctl.conf <!-- ACTION -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/NAT/sysctlForward.png) <!-- SCREEN -->

#### Accept changes <!-- ACTION -->

<!-- CODE -->
```bash
sysctl -p
```
<!-- CODE -->

---

### +/ Alt <!-- PLATFORM -->

#### Rules for accept before restart <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/nftables/nftables.nft
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
table ip nat {
	chain postrouting{
	type nat hook postrouting priority 100; policy accept;
	oif "ens32" masquerade
	}
}
```
<!-- CODE -->

#### Accept <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable nftables
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart nftables
```
<!-- CODE -->

---

### +/ Debian <!-- PLATFORM -->

#### Save changes<!-- ACTION -->

<!-- CODE -->
```bash
nft list ruleset > /etc/nftables.conf
```
<!-- CODE -->

#### Find provider interface<!-- ACTION -->

<!-- CODE -->
```bash
ip a
```
<!-- CODE -->

#### In /etc/nftables.conf<!-- ACTION -->
![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/Network_settings/NAT/nftConf.png) <!-- SCREEN -->

#### Enable service changes <!-- ACTION -->

<!-- CODE -->
```bash
nft -f /etc/nftables.conf
systemctl enable nftables.service
systemctl restart nftables.service
```
<!-- CODE -->

<details>
  <summary>manual</summary>
  
<!-- GENERAL COMMENT -->
  
** **
<!-- GENERAL COMMENT -->
</details>
<details>
<summary>unaccept</summary>
<!-- UPDATING PLATFORM -->

<!-- UPDATING PLATFORM -->
</details>

</details>
</details>

---

<details> 
<summary> ospf </summary> 

### +/ Linux Alt (quagga - old) <!-- PLATFORM -->

<!-- CODE -->

```bash
apt-get install quagga
```

<!-- CODE -->

<!-- CODE -->

```bash
chown -R quagga:quagga /etc/quagga
```

<!-- CODE -->

#### Important enable and start services separately <!-- ACTION -->

```bash
systemctl enable zebra ospfd
systemctl start zebra ospfd
```

#### Check output interface <!-- ACTION -->

<!-- CODE -->

```bash
ip a
```

<!-- CODE -->

#### In vtysh, configure the local network and tunnel <!-- ACTION -->

#### Set all interfaces except the local output interface as passive to prevent route injection <!-- ACTION -->

<!-- CODE -->

```bash
vtysh
conf t
ip forwarding
int tun
ip ospf message-digest-key 1 md5 P@ssw0rd
ip ospf network point-to-point
router ospf
ospf router-id 1.1.1.1
network 10.10.10.0/30 area 0
network 192.168.11.0/26 area 0
network 192.168.11.65/28 area 0
network 192.168.11.81/29 area 0
passive-interface default
no passive-interface tun
no passive-interface ens35 # subnets
area 0 authentication message-digest
do wr mem
do sh run
```

<!-- CODE -->

#### And mirror on another router <!-- ACTION -->

#### For check connect <!-- ACTION -->

<!-- CODE -->

```bash
ip route sh
```

<!-- CODE -->

<!-- CODE -->

```bash
vtysh
sh ip ospf neighbour
```

<!-- CODE -->

### +/ For quagga and frr also <!-- PLATFORM -->

#### Type interface <!-- ACTION -->
- `point-to-point`: saves trafic and use for 2 node (multicast 224.0.0.5) <!-- JUST -->
- `broadcast`: use for >2 node and supply Backup Designated Router(DR/BDR) (multicast 224.0.0.5; 224.0.0.6) <!-- JUST -->

### +/ Linux Debian (frr) <!-- PLATFORM -->

<!-- CODE -->
```bash
apt-get install frr
```
<!-- CODE --> 

#### turn on ospf /etc/frr/daemons<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/OSPF/frr_daemons.png) <!-- SCREEN --> 

<!-- CODE -->
```bash
systemctl enable --now frr
vtysh
conf t
ip forwarding
int tun
ip ospf message-digest-key 1 md5 P@ssw0rd
ip ospf network point-to-point
router ospf
ospf router-id 1.1.1.1
network 10.10.10.0/30 area 0
network 192.168.11.0/26 area 0
network 192.168.11.65/28 area 0
network 192.168.11.81/29 area 0
passive-interface default
no passive-interface tun
no passive-interface ens33 # subnets
area 0 authentication message-digest
do wr mem
```
<!-- CODE --> 

#### do show ip ospf route && ip route sh<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/OSPF/ospf_route.png) <!-- SCREEN --> 

</details>

<details> 
<summary> DNS </summary> 
<details>
<summary> bind</summary> <!-- TOPIC --> 

#### SRV-HQ<!-- ACTION --> 
  
<!-- CODE -->

```bash

apt-get update && apt-get install -y bind bind-utils
nano /etc/bind/options.conf
listen-on { any; };
allow-query { any; };
allow-transfer { srv-slave; };

```

<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_options0.png) <!-- SCREEN --> 

#### at logging category lame-servers {null;};<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_options1.png) <!-- SCREEN --> 

<!-- CODE -->

```bash
nano /etc/net/ifaces/ens33/resolv.conf
```

<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_resolv.png) <!-- SCREEN --> 

<!-- CODE -->

```bash
systemctl restart network
systemctl enable --now bind
nano /etc/bind/local.conf
```

<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_local.png) <!-- SCREEN --> 

#### Copy default-record<!-- ACTION --> 

<!-- CODE -->

```bash
cp /etc/bind/zone/{localhost,au.db}
cp /etc/bind/zone/127.in-addr.arpa /etc/bind/zone/11.168.192.in-addr.arpa.db
cp /etc/bind/zone/127.in-addr.arpa /etc/bind/zone/33.168.192.in-addr.arpa.db
```

<!-- CODE --> 

#### Let's assign right<!-- ACTION --> 

<!-- CODE -->

```bash
chown named:named /etc/bind/zone/au.db
chown named:named /etc/bind/zone/11.168.192.in-addr.arpa.db
chown named:named /etc/bind/zone/33.168.192.in-addr.arpa.db
```

<!-- CODE --> 

#### Forward zone /etc/bind/zone/au.db<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_dbau.png) <!-- SCREEN --> 

#### Reverse zones<!-- ACTION --> 

<!-- CODE -->

```bash
nano /etc/bind/zone/11.168.192.in-addr.arpa.db
```
  
<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_db11.png) <!-- SCREEN --> 

<!-- CODE -->

```bash
nano /etc/bind/zone/33.168.192.in-addr.arpa.db
```
<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_db33.png) <!-- SCREEN --> 

#### Checking zone<!-- ACTION --> 

<!-- CODE -->

```bash
named-checkconf -z

```

<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_namedcheckconf.png) <!-- SCREEN --> 

#### SRV-DT<!-- ACTION --> 

<!-- CODE -->

```bash
apt-get update && apt-get install -y bind bind-utils
nano /etc/bind/options.conf
listen-on { any; };
allow-query { any; };
allow-transfer { none; };
nano /etc/bind/local.conf

```

<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_local1.png) <!-- SCREEN --> 

<!-- CODE -->

```bash
nano /etc/net/ifaces/ens33/resolv.conf
```

<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_resolv1.png) <!-- SCREEN --> 

<!-- CODE -->

```bash
systemctl restart network
systemctl enable --now bind
```

<!-- CODE --> 

#### Turn on slave mode<!-- ACTION --> 

<!-- CODE -->

```bash
control bind-slave enabled
```

<!-- CODE --> 

#### Checking slave-zone<!-- ACTION --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/dns/bind_slaveZones.png) <!-- SCREEN --> 

</details>

</details>


<details> 
<summary> NTP </summary> 

<!-- CODE -->
```bash
apt-get install chrony
```
<!-- CODE --> 

#### SRV<!-- ACTION --> 

<!-- CODE -->
```bash
nano /etc/chrony.conf
```
<!-- CODE --> 

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/chrony/chrony_srv.png) <!-- SCREEN --> 

<!-- CODE -->
```bash
systemctl restart chronyd
```
<!-- CODE --> 

#### CLI<!-- ACTION --> 

<!-- CODE -->
```bash
apt-get install chrony
echo "server 192.168.11.67/28 iburst" >> /etc/chrony.conf
systemctl restart chronyd
```
<!-- CODE --> 

#### Checking Universal time<!-- ACTION --> 

<!-- CODE -->
```bash
timedatectl
```
<!-- CODE --> 

</details>
</details>

</details>

---

<details>
<summary>  Nginx  </summary>     <!-- ff -->

### +/ Linux <!-- PLATFORM -->

<details>
<summary> General settings  </summary> <!-- tp -->

<!-- CODE -->

```MarkDown Keemplate
  apt-get install nginx
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
  systemctl enable --now nginx
```
<!-- CODE -->

#### 1. CREATE CONFIG <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
  nano /etc/nginx/sites-available.d/MySite.conf
```
<!-- CODE -->
---

#### 2.1 Example PROXY_PASS (domains www.au.team; zabbix.au.team) <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
  server {
    listen 8081;
    server_name www.au.team;

    location / {
        proxy_pass http://192.168.11.67:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 8081;
    server_name zabbix.au.team;

    location / {
        proxy_pass http://127.0.0.1:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
<!-- CODE -->
- `listen 8081` – specifies the server listens for incoming requests on port `8081` <!-- JUST -->
- `location /` – handles all incoming requests to root (/) <!-- JUST -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->

##### 
- `proxy_pass http://192.168.11.67:80` – forwards requests from www.au.team to server 192.168.11.67:80<!-- JUST -->
- `proxy_pass http://127.0.0.1:80` – forwards requests from zabbix.au.team to localhost port 80 where Zabbix runs <!-- JUST -->
  - `proxy_set_header Host $host` – forwards original Host header for correct request handling <!-- SPACE -->
  - `proxy_set_header X-Real-IP $remote_addr` – forwards client's real IP address <!-- SPACE -->
  - `proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for` – appends client IP to X-Forwarded-For chain <!-- SPACE -->
  - `proxy_set_header X-Forwarded-Proto $scheme` – forwards protocol (http or https)<!-- SPACE -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->


#### 2.2 Example PROXY with SSL-certification (domain moodle.company.prof) <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
  server {
    listen 443 ssl;
    server_name moodle.company.prof;

    ssl_certificate /etc/letsencrypt/company.prof/gost.example.com.cer;
    ssl_certificate_key /etc/letsencrypt/company.prof/gost.example.com.key;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://10.0.10.2/moodle:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
<!-- CODE -->
- `listen 443 ssl` – server listens on port 443 with SSL/TLS support <!-- JUST -->
  - `ssl_certificate /etc/letsencrypt/company.prof/gost.example.com.cer` – path to SSL certificate <!-- SPACE -->
  - `ssl_certificate_key /etc/letsencrypt/company.prof/gost.example.com.key` – path to SSL private key <!-- SPACE -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->

##### 
- `ssl_protocols TLSv1 TLSv1.1 TLSv1.2` – specifies allowed TLS versions <!-- JUST -->
- `ssl_prefer_server_ciphers on` – enforces server cipher preference over client preferences <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

---

#### 3. CREATE symbol link in 'sites-enabled.d' <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
  sudo ln -s /etc/nginx/sites-available.d/MySite.conf /etc/nginx/sites-enabled.d/
```
<!-- CODE -->
---

#### 4. CHECK config <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
  nginx -t
```
<!-- CODE -->
---

#### 5. ACCEPT changes <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
  systemctl restart nginx
```
<!-- CODE -->

</details> <!-- TOPIC -->

<details>
<summary> Balance  </summary> <!-- tp -->

#### Add BLOCK in every site config <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
upstream backend_site1 {
    METHOD;
    server 192.168.1.101;
    server 192.168.1.102;
}

server { # begining configuration
sd Method types
- round-robin (weights)
-- `server 192.168.1.101 weight=3;`
- `least_conn` (minimal active connection server)
- `ip_hash` (client by server)
- advanced
-- keepalive connection (`keepalive 32;`)
-- timeout on the connection (`server 192.168.1.101 max_fails=3 fail_timeout=30s;`)
```
<!-- CODE -->

</details>            <!-- TOPIC -->

</details>             <!-- FFIELD -->

### O)

<details>
<summary> OpenSSL  </summary>     <!-- ff -->

---

<details>
<summary> ГОСТ (GOST)  </summary> <!-- tp -->

#### SRV <!-- ACTION -->

#### 0. <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install openssl-gost-engine
```
<!-- CODE -->

#### Connect GOST to openssl <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/openssl/openssl.cnf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
openssl_conf = openssl_def

[openssl_def]
engines = engine_section

[engine_section]
gost = gost_section

[gost_section]
engine_id = gost
dynamic_path = /usr/lib64/openssl/engines-1.1/gost.so #	путь до	самого шифрования
default_algorithms = ALL
```
<!-- CODE -->
---

#### 1. <!-- ACTION -->

> Create root certificate <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
openssl genpkey -algorithm gost2012_256 -pkeyopt paramset:A -out ca.key
```
<!-- CODE -->

#### С учётом ip сервера в `Common name` (корневой сервер) <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
openssl req -x509 -new -key ca.key -days 365 -out ca.crt -engine gost -md_gost12_256 
```
<!-- CODE -->

#### 2. <!-- ACTION -->

> Create domain(subroot) certificate <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
openssl genpkey -algorithm gost2012_256 -pkeyopt paramset:A -out router.key
```
<!-- CODE -->

#### В `Common name` ip или `домен(ы)`. Например, `*.au.team` <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
openssl req -new -key router.key -out router.csr -engine gost -md_gost12_256
```
<!-- CODE -->

#### 3. <!-- ACTION -->

> Sign DOMAIN certificate by ROOT certificate <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
openssl x509 -req -in router.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out router.crt -days 365 -engine gost -md_gost12_256
```
<!-- CODE -->
---

#### Check accessible names <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
openssl x509 -in router.crt -text -noout

```
<!-- CODE -->

</details> <!-- TOPIC -->

---

<details>
<summary> Sharing and accept  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
rsync -avz ./ca.crt ./router.crt ./router.key USERNAME@IP_RTR:/etc/nginx/ssl/WEB.com/
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
cd /etc/nginx/ssl/WEB.com/
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
cp ./* /etc/pki/ca-trust/source/anchors/
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
update-ca-trust
```
<!-- CODE -->

</details>            <!-- TOPIC -->

<details>
<summary> Setting Nginx (revers-proxy)  </summary> <!-- tp -->

#### RTR <!-- ACTION -->

#### Add to nginx site config (see `Nginx`) <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
host zabbix.au.team
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
 server {
    listen 443 ssl;
    server_name zabbix.au.team;

    ssl_certificate /etc/nginx/ssl/WEB.com/router.crt;
    ssl_certificate_key /etc/nginx/ssl/WEB.com/router.key;
    ssl_client_certificate /etc/nginx/ssl/WEB.com/ca.crt;
    ssl_protocols TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://192.168.11.67/zabbix/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart nginx
```
<!-- CODE -->
---

#### Check connection <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
curl -v https://zabbix.au.team
```
<!-- CODE -->

</details>            <!-- TOPIC -->

</details>             <!-- FFIELD -->

---

<details>
<summary> Open WebUI (ollama chat) [Single-mode] </summary> <!-- tp -->

#### You must have Docker installed and ollama <!-- ACTION -->
#### Continue if Docker is already running and ollama <!-- ACTION -->
<!-- CODE -->
```MarkDown Keemplate
 docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 -e API_URL=http://127.0.0.1:3000 -e WEBUI_AUTH=False --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```
<!-- CODE -->

#### To verify, open [http://localhost:8080](http://localhost:8080) in a browser<!-- ACTION -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->


- `ollama` connected due to `-e OLLAMA_BASE_URL=http://127.0.0.1:11434` <!-- JUST -->

- `Single-mode` due to `-e WEBUI_AUTH=False` <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->


</details> <!-- FIELD -->

### P)
### Q)
### R)
### S)

<details>
  <summary>samba</summary>

### +/ Linux  <!-- PLATFORM -->
<details>
<summary>Primary Active Directory Domain Controller </summary> <!-- TOPIC -->

#### BIND9_DLZ on basic BIND<!-- ACTION -->

<!-- CODE -->
```bash
apt-get install -y task-samba-dc
```
<!-- CODE -->

<!-- CODE -->
```bash
control bind-chroot disabled
```
<!-- CODE -->

<!-- CODE -->
```bash
grep -q 'bind-dns' /etc/bind/named.conf || echo 'include "/var/lib/samba/bind-dns/named.conf";' >> /etc/bind/named.conf
```
<!-- CODE -->

#### In /etc/bind/options.conf<!-- ACTION -->

<!-- CODE -->
```bash
tkey-gssapi-keytab "/var/lib/samba/bind-dns/dns.keytab";
minimal-responses yes;
```
<!-- CODE -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_options0.png) <!-- SCREEN -->

#### At logging<!-- ACTION -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_options1.png) <!-- SCREEN -->

<!-- CODE -->
```bash
systemctl stop bind
```
<!-- CODE -->

#### In /etc/sysconfig/network<!-- ACTION -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_sycconfig.png) <!-- SCREEN -->

#### Zone conflicts occur when identical domains are defined in both BIND and SAMBA BIND9_DLZ configurations<!-- ACTION -->

<!-- CODE -->
```bash
hostnamectl set-hostname srv-hq.ad.team;exec bash
domainname ad.team
```
<!-- CODE -->

#### Remove outdated samba old<!-- ACTION -->

<!-- CODE -->
```bash
rm -f /etc/samba/smb.conf
rm -rf /var/lib/samba
rm -rf /var/cache/samba
mkdir -p /var/lib/samba/sysvol
```
<!-- CODE -->

#### specify server ip as dns server at '/etc/resolv.conf' <!-- ACTION -->

<!-- CODE -->
```bash
nameserver 127.0.0.1 # or your dns server
```
<!-- CODE -->

#### Provision samba domain ad.team<!-- ACTION -->

<!-- CODE -->
```bash
samba-tool domain provision --realm=ad.team --domain=ad --adminpass='P@ssw0rd' --dns-backend=BIND9_DLZ --server-role=dc --use-rfc2307
```
<!-- CODE -->

<!-- CODE -->
```bash
systemctl enable --now samba
systemctl enable --now bind
```
<!-- CODE -->

#### Copy new krb5.conf<!-- ACTION -->

<!-- CODE -->
```bash
cp /var/lib/samba/private/krb5.conf /etc/krb5.conf
```
<!-- CODE -->

#### Check records<!-- ACTION -->

<!-- CODE -->
```bash
samba-tool domain info 127.0.0.1
```
<!-- CODE -->

<!-- CODE -->
```bash
host -t SRV _kerberos._udp.ad.team
```
<!-- CODE -->

<!-- CODE -->
```bash
host -t SRV _kerberos._udp.
```
<!-- CODE -->

<!-- CODE -->
```bash
host -t SRV _ldap._tcp.ad.team
```
<!-- CODE -->

<!-- CODE -->
```bash
host -t SRV _ldap._tcp.
```
<!-- CODE -->

<!-- CODE -->
```bash
host -t A hq-srv.ad.team
```
<!-- CODE -->

<!-- CODE -->
```bash
host -t A hq-srv.
```
<!-- CODE -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_checkDC.png) <!-- SCREEN -->

#### Checking kerberos<!-- ACTION -->

<!-- CODE -->
```bash
kinit administrator@AD.TEAM
```
<!-- CODE -->

<!-- CODE -->
```bash
klist
```
<!-- CODE -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_klist.png) <!-- SCREEN -->

#### Join domain as client <!-- ACTION -->

<!-- CODE -->
```bash
apt-get update && apt-get install -y task-auth-ad-sssd
```
<!-- CODE -->

<!-- CODE -->

```bash
systemctl enable --now smb winbind sssd
```

#### Ensure server IP is set in /etc/krb5.conf <!-- ACTION -->

<!-- CODE -->

```bash
nano /etc/krb5.conf
```

<!-- CODE -->

```bash
[libdefaults]
default_realm = AD.TEAM
dns_lookup_kdc = true
dns_lookup_realm = false
ticket_lifetime = 24h
renew_lifetime = 7d
forwardable = true
rdns = false
# default_realm = EXAMPLE.COM
default_ccache_name = KEYRING:persistent:%{uid}

[realms]
AD.TEAM={
        kdc = 192.168.11.67
        default_domain = ad.team
        admin_server = 192.168.11.67
}

# EXAMPLE.COM = {
#  default_domain = example.com
# }

[domain_realm]
.ad.team = AD.TEAM
ad.team = AD.TEAM
```

#### Check kerberos <!-- ACTION -->

<!-- CODE -->

```bash
kinit administrator
```

<!-- CODE -->

<!-- CODE -->

```bash
klist
```

<!-- CODE -->


#### Connection to primary server <!-- ACTION -->

#### in /etc/resolv.conf<!-- ACTION -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_resolvClient.png) <!-- SCREEN -->

#### Check nameserver<!-- ACTION -->

<!-- CODE -->
```bash
host srv-hq
```
<!-- CODE -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_checkNS.png) <!-- SCREEN -->

#### Enter to a domain Alt*<!-- ACTION -->

<!-- CODE -->
```bash
su -
acc
```
<!-- CODE -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_acc0.png) <!-- SCREEN -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_acc1.png) <!-- SCREEN -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_acc2.png) <!-- SCREEN -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_acc3.png) <!-- SCREEN -->

<!-- CODE -->
```bash
reboot
```
<!-- CODE -->

#### Log in as domain user and verify <!-- ACTION -->

<!-- CODE -->
```bash
id
```
<!-- CODE -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_checkID.png) <!-- SCREEN -->


</details>

---

<details>
<summary> Samba tool scripts</summary> <!-- TOPIC --> 
<details>
<summary> MIGRATION TO DYNAMIC ZONE</summary> <!-- TOPIC --> 

<!-- CODE -->
```bash
touch intDep.sh
```
<!-- CODE -->

<!-- CODE -->
```bash
chmod +x intDep.sh
```
<!-- CODE -->

#### At intDep.sh<!-- ACTION -->

<!-- CODE -->
```bash
#!/bin/bash
SERVER="192.168.11.67"
ZONE="ad.team" # bind9_DLZ
USER="administrator"
PASSWORD="P@ssw0rd"

while read -r line; do
    name=$(echo "$line" | awk '{print $1}')
    ttl=$(echo "$line" | awk '{print $2}')
    type=$(echo "$line" | awk '{print $3}')
    data=$(echo "$line" | awk '{print $4}')
    
    case "$type" in
        A|AAAA|CNAME|MX|SRV|TXT|PTR|NS)
            echo "Adding record: Name=$name Type=$type Data=$data"
            echo "$PASSWORD" | samba-tool dns add "$SERVER" "$ZONE" "$name" "$type" "$data" -U "$USER"
            ;;
        *)
            echo "Skipping unsupported record type: $type"
            ;;
    esac
done < /etc/bind/zone/au.db
echo "End importing"
```
<!-- CODE -->
</details>
<details>
<summary> CREATING USERS AND GROUPS, OU</summary> <!-- TOPIC --> 

<!-- CODE -->
```bash
touch usrGrp.sh
```
<!-- CODE -->

<!-- CODE -->
```bash
chmod +x usrGrp.sh
```
<!-- CODE -->

#### At usrGrp.sh<!-- ACTION -->

<!-- CODE -->
```bash
#!/bin/bash

PASSWORD="P@ssw0rd"

echo "Creating groups..."
samba-tool group add group1 --description="Group 1"
samba-tool group add group2 --description="Group 2"
samba-tool group add group3 --description="Group 3"

echo "Creating organizational units..."
samba-tool ou create "OU=CLI"
samba-tool ou create "OU=ADMIN"

echo "Creating users and adding them to groups..."

for i in {1..30}; do
    USER="user$i"
    
    if [ $i -le 10 ]; then
        GROUP="group1"
        OU="OU=CLI"
    elif [ $i -le 20 ]; then
        GROUP="group2"
        OU="OU=CLI"
    else
        GROUP="group3"
        OU="OU=ADMIN"
    fi

    samba-tool user create "$USER" "$PASSWORD" --userou="$OU" --description="User $i"
    echo "Created $USER in $OU"

    samba-tool group addmembers "$GROUP" "$USER"
    echo "Added $USER to $GROUP"
done

echo "All users and groups created successfully!"
samba-tool user list
```
<!-- CODE -->
</details>
<details>
<summary> DELETE USER, GROUP, OU</summary> <!-- TOPIC --> 

<!-- CODE -->
```bash
touch dUG.sh
```
<!-- CODE -->
<!-- CODE -->
```bash
chmod +x dUG.sh
```
<!-- CODE -->
#### At dUG.sh<!-- ACTION -->
<!-- CODE -->
```bash
#!/bin/bash

PASSWORD="P@ssw0rd"

echo "Deleting users..."

for i in {1..30}; do
    USER="user$i"

    samba-tool user delete "$USER"
    echo "Delete $USER"
done

echo "Deleting groups..."
samba-tool group list
samba-tool group delete group1
samba-tool group delete group2
samba-tool group delete group3

echo "Deleting organizational units..."
samba-tool ou list
samba-tool ou delete "OU=CLI"
samba-tool ou delete "OU=ADMIN"

echo "All users and groups, OU delete successfully!"
```
<!-- CODE -->
</details>
</details>

---

<details>
<summary> Reserve ad domain controller</summary> <!-- TOPIC --> 

#### SRV-DT<!-- ACTION -->

<!-- CODE -->
```bash
apt-get install -y task-samba-dc
```
<!-- CODE -->

#### In /etc/resolv.conf<!-- ACTION -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_resolvDT.png) <!-- SCREEN -->

#### In /etc/krb5.conf<!-- ACTION -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_krbDT.png) <!-- SCREEN -->

#### Secondary AD must have a dynamic record in BIND9\_DLZ (refer to samba-tool scripts <!-- ACTION -->

<!-- CODE -->
```bash
samba-tool dns add srv-hq ad.team srv-dt A 192.168.33.67 -Uadministrator
```
<!-- CODE -->

#### Checking<!-- ACTION -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_checkDT.png) <!-- SCREEN -->

#### Log in as domain controller<!-- ACTION -->

<!-- CODE -->
```bash
samba-tool domain join ad.team DC -Uadministrator --realm=ad.team --workgroup=ad
systemctl enable --now samba
```
<!-- CODE -->
</details>
<details>
<summary> Shared folder</summary> <!-- TOPIC --> 

#### SRV<!-- ACTION -->

<!-- CODE -->
```bash
mkdir /opt/data
chmod 777 /opt/data
```
<!-- CODE -->

#### In /etc/samba/smb.conf<!-- ACTION -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_smbShareFolder.png) <!-- SCREEN -->

#### CLI<!-- ACTION -->

#### Open Explorer and write path<!-- ACTION -->

<!-- CODE -->
```bash
smb://srv/
```
<!-- CODE -->

![image](https://github.com/Gerasti/NoTesk/blob/main/documents/screen/samba/samba_cliCheckFolder.png) <!-- SCREEN -->



</details>
</details>
</details>

---

<details>
<summary> SQL  </summary>     <!-- ff -->
<details>
<summary> PostgreSQL  </summary>     <!-- ff -->

### +/ Linux <!-- PLATFORM -->

<details>
<summary> Install  </summary> <!-- tp -->

#### Install <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install -y postgresql16 postgresql16-server postgresql16-contrib
```
<!-- CODE -->

#### Deploy <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
/etc/init.d/postgresql initdb
systemctl enable --now postgresql
```
<!-- CODE -->

#### Enable listen ALL address <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /var/lib/pgsql/data/postgresql.conf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
listen_addresses = '*'
```
<!-- CODE -->

#### Accept <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart postgresql
```
<!-- CODE -->
---

#### Check (no necessary) <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
ss -tlpn | grep postgres
```
<!-- CODE -->
---

#### Enter as root <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
psql -U postgres
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
ALTER USER postgres WITH PASSWORD 'P@ssw0rd';
```
<!-- CODE -->

#### Create databases <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
CREATE DATABASE one;
CREATE DATABASE two;
```
<!-- CODE -->

#### Create users <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
CREATE USER oneuser WITH PASSWORD 'P@ssw0rd';
CREATE USER twouser WITH PASSWORD 'P@ssw0rd';
```
<!-- CODE -->

#### Assign owner <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
GRANT ALL PRIVILEGES ON DATABASE one to oneuser;
GRANT ALL PRIVILEGES ON DATABASE two to twouser;
```
<!-- CODE -->

#### Exit from shell <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
\q
```
<!-- CODE -->

#### Fill database <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
pgqbench -U postgres -i one
pgqbench -U postgres -i two
```
<!-- CODE -->
---

#### Check (no necessary) <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
\c one
\dt+
\c one
\c two
```
<!-- CODE -->
---

#### Setting remote authentication <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /var/lib/pgsql/data/pg_hba.conf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
# Under!!!
host    all             all             0.0.0.0/0               md5
# IPv6 local connections:
host    all             all             ::1/128                 trust
# Allow replication connections from localhost, by a user with the
# replication privilege.
# 
# Under!!! (for replication)
host    replication     all             0.0.0.0/0               md5
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart postgresql
```
<!-- CODE -->

</details> <!-- TOPIC -->


<details>
<summary> Replication  </summary> <!-- tp -->

> SRV-HQ(basic); SRV-BR(second) <!-- Citation -->
---

#### SRV-BR <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install -y postgresql16 postgresql16-server postgresql16-contrib
```
<!-- CODE -->
---

#### SRV-HQ <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /var/lib/pgsql/data/postgresql.conf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
wal_level = replica
max_wal_senders = 2
max_replication_slots = 2
hot_standby = on
hot_standby_feedback = on
```
<!-- CODE -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->

##### 
- `wal_level` specifies the amount of data written to WAL (write-ahead log used for replication) [minimal/replica/logical] <!-- JUST -->
- `max_wal_senders` — defines the number of allowed standby servers<!-- JUST -->
- `max_replication_slots` — sets the maximum number of replication slots <!-- JUST -->
- `hot_standby` — enables read-only queries on PostgreSQL during recovery<!-- JUST -->
- `hot_standby_feedback` — controls whether the standby server reports query activity back to the masters <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

<!-- CODE -->

```MarkDown Keemplate
systemctl restart postgresql
```
<!-- CODE -->
---

#### SRV-BR <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
systemctl stop postgresql
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
rm -rf /var/lib/pgsql/data/*
```
<!-- CODE -->

#### Replication <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
pg_basebackup -h 192.168.11.67 -U postgres -D /var/lib/pgsql/data --wal-method=stream --write-recovery-conf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
chown -R postgres:postgres /var/lib/pgsql/data/
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl start postgresql
```
<!-- CODE -->
---

#### Check (no necessary) <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
\c one
\dt+
\c one
\c two
```
<!-- CODE -->
---

</details> <!-- TOPIC -->


<details>
<summary> HAproxy  </summary> <!-- tp -->

#### SW-BR (proxy [switch]) <!-- ACTION -->

#### Install <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install haproxy
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable --now haproxy
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/haproxy/haproxy.cfg
```
<!-- CODE -->

#### Required parameters only others are not essential <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
global
    # log to /dev/log
    log /dev/log daemon

    # log to local syslogd from chroot over UDP
    #log         127.0.0.1:514 local2
    #log         tcp@127.0.0.1:514 local2 notice

    # send log to systemd-journald
    #log stdout format short daemon

    chroot	/var/lib/haproxy
   #pidfile     /run/haproxy.pid
    maxconn     4000
    user        _haproxy
    group	_haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats
    defaults
    mode                    http
    log                     global
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    
    listen stats
    bind 0.0.0.0:8989
    mode http
    stats enable
    stats uri /haproxy_stats
    stats realm HAProxy\ Statistics
    stats auth admin:toor
    stats admin if TRUE

frontend postgre
    bind 0.0.0.0:5432
    default_backend POSTGRE

backend POSTGRE
    balance roundrobin # mode
    server srv-hq 192.168.11.65:5432 check
    server srv-br 192.168.33.67:5432 check
```
<!-- CODE -->

<details>
<summary> manual </summary> <!-- gc -->

<!-- GENERAL COMMENT -->

##### Balance methods
- `roundrobin`: Requests distributed cyclically across servers (all servers have equal capacity) <!-- JUST -->
- `leastconn`: Requests sent to server with the fewest active connections (for long-lived connections) <!-- JUST -->
- `source`: Same client IP always routed to the same server <!-- JUST -->
- `uri`: Requests with identical URI sent to the same server (static content, API)] <!-- JUST -->
- `url_param`: Load balancing based on specific URL parameter value (e.g., ?session_id=123) <!-- JUST -->
- `hdr`: Requests with identical HTTP header values sent to the same server (e.g., User-Agent or Cookie) <!-- JUST -->
- `rdp-cookie`: Load balancing by RDP Cookie when HAProxy manages RDP servers<!-- JUST -->
- `random`: Requests sent to a random server (priority adjustable via random[start_weight])<!-- JUST -->
- `first`: Requests always sent to the first available server in backend list (failover) <!-- JUST -->

<!-- GENERAL COMMENT -->

</details> <!-- COMMENT -->

---

#### Check <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
systemctl status haproxy
```
<!-- CODE -->

</details>            <!-- TOPIC -->

</details>             <!-- FFIELD -->

</details>             <!-- FFIELD -->

---

<details>
<summary> squid  </summary>     <!-- ff -->

### with work domain samba <!-- LIST -->
- squid <!-- JUST -->
- squid-helpers
 <!-- JUST -->
<!-- CODE -->

```MarkDown Keemplate
auth_param basic program /usr/lib/squid/basic_smb_lm_auth AD/srv-hq.ad.team
auth_param basic children 5
auth_param basic realm Proxy Authentication Required
auth_param basic credentialsttl 2 hours

external_acl_type check_group %LOGIN /usr/lib/squid/ext_wbinfo_group_acl -d
acl authenticated proxy_auth REQUIRED
acl group1 external check_group group1
acl group2 external check_group group2
acl group3 external check_group group3
acl enterprise_services dst 192.168.0.0/16
acl monitoring_system dst 192.168.1.100
acl cli_hq src 192.168.2.10
acl forbidden_domains dstdomain vk.com mail.yandex.ru worldskills.org

http_access allow authenticated group1 enterprise_services
http_access allow authenticated group2 monitoring_system
http_access deny group3
http_access allow cli_hq !forbidden_domains
http_access deny all

http_port 3128

```
<!-- CODE -->

#### For replace password <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
samba-tool user setpassword USER
```
<!-- CODE -->

#### Check <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
squid -k
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
curl -v -x http://192.168.1.101:3128 --proxy-user "user1:P@ssw0rd" http://192.168.0.10
```
<!-- CODE -->

</details>             <!-- FFIELD -->


### T)
### U)
### V)
### W)
### X)
### Y)
### Z)

<details>
<summary> Zabbix  </summary>     <!-- ff -->

### +/ Linux <!-- PLATFORM -->

<details>
<summary> Install (PostgreSQL)  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install postgresql16-server zabbix-server-pgsql fping
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
/etc/init.d/postgresql initdb
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable --now postgresql
```
<!-- CODE -->

#### Create user and database for Zabbix <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
su - postgres -s /bin/sh -c 'createuser --no-superuser --no-createdb --no-createrole --encrypted --pwprompt zabbix'
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
su - postgres -s /bin/sh -c 'createdb -O zabbix zabbix'
```
<!-- CODE -->

#### Add entry to the database for web access<!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
su - postgres -s /bin/sh -c 'psql -U zabbix -f /usr/share/doc/zabbix-common-database-pgsql-7.0.8/schema.sql zabbix'
```
<!-- CODE -->

> version zabbix-common-database-pgsql-7.0.8 may be differ <!-- Citation -->

#### Also <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
su - postgres -s /bin/sh -c 'psql -U zabbix -f /usr/share/doc/zabbix-common-database-pgsql-7.0.8/images.sql zabbix'
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
su - postgres -s /bin/sh -c 'psql -U zabbix -f /usr/share/doc/zabbix-common-database-pgsql-7.0.8/data.sql zabbix'
```
<!-- CODE -->

#### Install Apache2 <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install apache2 apache2-mod_php8.2
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable --now httpd2
```
<!-- CODE -->

#### Install PHP <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install php8.2 php8.2-mbstring php8.2-sockets php8.2-gd php8.2-xmlreader php8.2-pgsql php8.2-ldap php8.2-openssl
```
<!-- CODE -->

#### Change options php <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/php/8.2/apache2-mod_php/php.ini
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
memory_limit = 256M
post_max_size = 32M
max_execution_time = 600
max_input_time = 600
date.timezone = Europe/Moscow
always_populate_raw_post_data = -1
```
<!-- CODE -->

#### Restart apache2 <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart httpd2
```
<!-- CODE -->

#### Options Zabbix-server <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/zabbix/zabbix_server.conf
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=zabbixpwd
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable --now zabbix_pgsql
```
<!-- CODE -->

> see next topic <!-- Citation -->

</details> <!-- TOPIC -->


<details>
<summary> Install web-interface  </summary> <!-- tp -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install zabbix-phpfrontend-apache2 zabbix-phpfrontend-php8.2
```
<!-- CODE -->

#### Enable Apache2 addons
 <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
ln -s /etc/httpd2/conf/addon.d/A.zabbix.conf /etc/httpd2/conf/extra-enabled/
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart httpd2
```
<!-- CODE -->

#### Change owner for web-installer <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
chown apache2:apache2 /var/www/webapps/zabbix/ui/conf
```
<!-- CODE -->

#### Access the server at IP 192.168.33.67 via browser
 <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
http://192.168.33.67/zabbix
```
- Follow the instructions steps for <!-- JUST -->
  - type database: `PostgreSQL` <!-- SPACE -->
  - host `localhost` <!-- SPACE -->
  - port database `0` <!-- SPACE -->
  - name database `zabbix` <!-- SPACE -->
  - scheme database `public` <!-- SPACE -->
  - user `zabbix` <!-- SPACE -->
  - password `zabbixpwd` <!-- SPACE -->
- Use to `Sign in` <!-- JUST -->
  - username: `Admin` <!-- SPACE -->
  - password: `zabbix` <!-- SPACE -->

<!-- CODE -->

</details>            <!-- TOPIC -->

<details>
<summary> zabbix-AGENT  </summary> <!-- tp -->

> On Zabbix-agent <!-- Citation -->
<!-- CODE -->

```MarkDown Keemplate
apt-get install zabbix-agent
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
nano /etc/zabbix/zabbix_agentd.conf
```
<!-- CODE -->

#### Add next <!-- ACTION -->
<!-- CODE -->

```MarkDown Keemplate
Server=IP_ZABBIX_SERVER # IP or Host Zabbix server
ServerActive=IP_ZABBIX_SERVER
Hostname=HOST_CLIENT     # like at web-interface
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl restart zabbix-agentd
```
<!-- CODE -->
<!-- CODE -->

```MarkDown Keemplate
systemctl enable zabbix-aagentd
```
<!-- CODE -->
---

> On Zabbix server <!-- Citation -->
- Open web-interface <!-- JUST -->
- Monitoring -> Hosts <!-- JUST -->
- Create host <!-- JUST -->
- Fill next <!-- JUST -->
    - Host name (like at zabbix-agentd.conf) <!-- SPACE -->
    - Templates (in the search bar `Templates` and looks for `Linux by Zabbix agent`) <!-- SPACE -->
    - Host groups (Discovered hosts) <!-- SPACE -->
- Add interface (Agent) <!-- JUST -->
    - fill `IP address Zabbix agent` and Port `10050` <!-- SPACE -->
---

> You can then add it in Dashboards <!-- Citation -->

</details>            <!-- TOPIC -->

</details>             <!-- FFIELD -->
