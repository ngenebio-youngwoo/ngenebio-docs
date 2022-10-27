---
template: overrides/main.html
title: 리눅스에 서버 설치하기
---

# 리눅스에 서버 설치하기
리눅스에 직접 설치하려면 설치 작업이 진행되는 동안에는 리눅스 서버가 인터넷 연결이 가능해야 한다. 
NGeneAnalySys 서버 소프트웨어가 동작하는데 필요한 리눅스 소프트웨어들을 인터넷에서 다운로드해야 한다.

## 기본 OS 설정

Support only ubuntu LTS version higher than 16.04.7 

- [X] Ubuntu 16.04.7 LTS Xenial Xerus
- [X] Ubuntu 18.04.6 LTS Bionic Beaver
- [X] Ubuntu 20.04.4 LTS Bionic Beaver
- [X] Ubuntu 20.04.5 LTS Focal Fossa
- [X] Ubuntu 22.04 LTS Jammy Jellyfish
- [X] Ubuntu 22.04.1 LTS Jammy Jellyfish

!!! info "지원하지 않지만 사용 가능한 버전"
    - [ ] Ubuntu 14.04 LTS Trusty Tahr (2014년)


### 패키지 업데이트

필요한 패키지를 설치한다.

- [x] lsb-release: 리눅스 표준 베이스 버전 리포팅 유틸리티 
- [x] build-essential: 데비안 패키지 제작 필수 패키지
- [x] python2.7
- [x] zip
- [x] wget
- [x] vim
- [x] exfat-*: exFAT 파일시스템 관련 패키지
- [x] ntfs-3g: NTFS 파일시스템 관련 패키지
- [x] apt-transport-https: APT transport for downloading via the HTTP Secure protocol
- [x] ca-certificates: Common CA certificates
- [x] curl
- [x] gnupg-agent: GNU privacy guard - cryptographic agent
- [x] software-properties-common: manage the repositories that you install software
- [x] net-tools: 리눅스 네트워크 서브 시스템을 사용하기 위한 툴
- [x] ucommon-utils: lightweight C++ threading and sockets
- [x] logrotate: Log rotation utility

``` bash
apt-get update && \
apt-get install -y lsb-release build-essential python2.7 zip wget vim exfat-* ntfs-3g apt-transport-https ca-certificates curl gnupg-agent software-properties-common net-tools ucommon-utils logrotate && \
apt-get clean
```

### 사용자 계정 추가

``` bash
useradd -m -s /bin/bash -u 1500 ngenebio && \
useradd -m -s /bin/bash postgres
```
### 설치 폴더 환경 변수 설정

``` bash
echo "
export NGENEANALYSYS_APP_DIR=/ngeneanalysys_app
export NGENEANALYSYS_DATA_DIR=/ngeneanalysys_data
" >> /etc/profile && source /etc/profile

mkdir $NGENEANALYSYS_APP_DIR
mkdir $NGENEANALYSYS_DATA_DIR

```

## 도커 설치

``` bash
mkdir -p /etc/apt/keyrings && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
tee /etc/apt/sources.list.d/docker.list > /dev/null && \
apt-get update && \
apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

!!! info "버전에 맞는 :material-docker: 도커 설치"
    dpkg --print-architecture 명령으로 아키텍처 amd64를 파악하고,
    lsb_release -cs 명령으로 리눅스 배포판의 코드 네임 trusty을 버전을 알아낸다. 
    
    ```bash
    ngenebio@ngb-bi-dev:/BI2/ngeneanalysys_data$ dpkg --print-architecture
    amd64
    ngenebio@ngb-bi-dev:/BI2/ngeneanalysys_data$ lsb_release -cs
    trusty
    ```

도커의 data root directory의 경로를 변경한다. 파티션의 용량이 부족한 경우 정상적으로 docker를 운영하기 어려울 수 있다.

``` bash
vi /etc/docker/daemon.json
# 아래 부분 추가
{
  "data-root": "/ngeneanalysys_app/docker",
}
```
또는 /etc/default/docker 파일에 -g 옵션을 추가한다. 기본적으로 /etc/init.d/docker에서 사용하는 옵션을 설정할 수 있다.

``` bash
ngenebio@ngb-bi-dev:/etc/default$ cat docker
# Docker Upstart and SysVinit configuration file

#
# THIS FILE DOES NOT APPLY TO SYSTEMD
#
#   Please see the documentation for "systemd drop-ins":
#   https://docs.docker.com/engine/admin/systemd/
#

# Customize location of Docker binary (especially for development testing).
#DOCKERD="/usr/local/bin/dockerd"

# Use DOCKER_OPTS to modify the daemon startup options.
#DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4"
DOCKER_OPTS="-g /BI2/ngeneanalysys_app/docker"

# If you need Docker to use an HTTP proxy, it can also be specified here.
#export http_proxy="http://127.0.0.1:3128/"

# This is also a handy place to tweak where Docker's temporary files go.
#export DOCKER_TMPDIR="/mnt/bigdrive/docker-tmp"
```

리눅스 재시작할 때 자동으로 docker를 시작하도록 설정

``` bash
service docker restart
update-rc.d docker defaults
```

!!! info "update-rc.d 명령어"
    시스템의 부팅과 종료에 관여하는 스크립트 관리기로 /etc/init.d/에 구동하기 위한 스크립트를 작성하고
    실행 권한을 준 후 update-rc.d를 실행하면 된다.

    모든 서비스 목록 확인
    
    ``` bash hl_lines="11"
    ngenebio@ngb-bi-dev:/etc/init.d$ service --status-all
    [ + ]  acpid
    [ + ]  apache2
    [ - ]  apparmor
    [ ? ]  apport
    [ + ]  atd
    [ ? ]  console-setup
    [ + ]  cron
    [ - ]  dbus
    [ ? ]  dns-clean
    [ + ]  docker
    [ + ]  friendly-recovery
    [ ? ]  gridengine-exec
    [ ? ]  gridengine-master
    [ - ]  grub-common
    [ ? ]  irqbalance
    [ ? ]  killprocs
    [ ? ]  kmod
    [ ? ]  msm_profile
    [ ? ]  mysql
    [ ? ]  networking
    [ ? ]  ondemand
    [ - ]  postfix
    [ ? ]  pppd-dns
    [ - ]  procps
    [ - ]  pulseaudio
    [ ? ]  rc.local
    [ + ]  resolvconf
    [ + ]  rpcbind
    [ - ]  rsync
    [ + ]  rsyslog
    [ ? ]  screen-cleanup
    [ ? ]  sendsigs
    [ ? ]  socat-cromwell
    [ + ]  ssh
    [ - ]  sudo
    [ - ]  sysstat
    [ + ]  udev
    [ ? ]  umountfs
    [ ? ]  umountnfs.sh
    [ ? ]  umountroot
    [ - ]  unattended-upgrades
    [ - ]  urandom
    [ + ]  vivaldiframeworkd
    [ - ]  x11-common
    ```


도커 소켓 및 도커 그룹에 ngenebio 계정 추가

``` bash
chmod 666 /var/run/docker.sock
usermod -aG docker ngenebio
```

!!! info "docker.sock 권한 오류"
    docker를 시작하는데 permission denied 에러가 발생하는 경우 docker.sock 파일의 권한을 666으로 변경한 경우 일시적인 조치로 docker 서비스를 재시작하면 권한이 660으로 돌아오게 된다.
    docker 그룹을 만들어서 사용자를 추가하여 사용한다.

도커 스웜 초기화

``` bash
docker swarm init --advertise-addr {Ethernet 인터페이스 또는 서버 아이피 예: eth0, ens0, em1 등등 } 
```

!!! info "도커 상태 확인" 
    도커 데몬을 확인한다.

    ``` bash
    ngenebio@ngb-bi-dev:/BI2/ngeneanalysys_app/docker$ service docker status
    docker start/running, process 2008
    ```

    ``` bash  hl_lines="57"
    ngenebio@ngb-bi-dev:/BI2/ngeneanalysys_app/docker$ docker info
    Containers: 11
    Running: 7
    Paused: 0
    Stopped: 4
    Images: 58
    Server Version: 18.06.3-ce
    Storage Driver: overlay2
    Backing Filesystem: extfs
    Supports d_type: true
    Native Overlay Diff: true
    Logging Driver: json-file
    Cgroup Driver: cgroupfs
    Plugins:
    Volume: local
    Network: bridge host macvlan null overlay
    Log: awslogs fluentd gcplogs gelf journald json-file logentries splunk syslog
    Swarm: active
    NodeID: z0nvpbshkta467jxoal65d90j
    Is Manager: true
    ClusterID: tvwgxrn6n0f4yqzidju9y92jh
    Managers: 1
    Nodes: 1
    Orchestration:
    Task History Retention Limit: 5
    Raft:
    Snapshot Interval: 10000
    Number of Old Snapshots to Retain: 0
    Heartbeat Tick: 1
    Election Tick: 10
    Dispatcher:
    Heartbeat Period: 5 seconds
    CA Configuration:
    Expiry Duration: 3 months
    Force Rotate: 0
    Autolock Managers: false
    Root Rotation In Progress: false
    Node Address: 192.168.1.160
    Manager Addresses:
    192.168.1.160:2377
    Runtimes: runc
    Default Runtime: runc
    Init Binary: docker-init
    containerd version: 468a545b9edcd5932818eb9de8e72413e616e86e
    runc version: a592beb5bc4c4092b1b1bac971afed27687340c5
    init version: fec3683
    Security Options:
    apparmor
    Kernel Version: 4.4.0-128-generic
    Operating System: Ubuntu 14.04.6 LTS
    OSType: linux
    Architecture: x86_64
    CPUs: 64
    Total Memory: 503.8GiB
    Name: ngb-bi-dev
    ID: LESO:AQXK:NWEY:7O2L:3CUD:3JZ5:LN44:LYIK:CPJQ:72B5:2KZ7:MHYQ
    Docker Root Dir: /BI2/ngeneanalysys_app/docker
    Debug Mode (client): false
    Debug Mode (server): false
    Registry: https://index.docker.io/v1/
    Labels:
    Experimental: false
    Insecure Registries:
    127.0.0.0/8
    Live Restore Enabled: false

    WARNING: No swap limit support
    ```

## 데이터베이스 설치

:simple-postgresql: PostgreSQL을 설치

```bash
install_postgresql=$($THIS_DIR/postgresql-9.6.18/configure --prefix $NGENEANALYSYS_APP_DIR/postgresql-9.6.18 --without-readline --without-zlib && make -j 2 && make install 2>&1)
echo "$install_postgresql"
change_owner=$(chown -R postgres:postgres $NGENEANALYSYS_APP_DIR/postgresql-9.6.18 && mkdir -p $NGENEANALYSYS_DATA_DIR/postgresql_data && chown -R postgres:postgres $NGENEANALYSYS_DATA_DIR/postgresql_data)

initdb=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/initdb -D "$NGENEANALYSYS_DATA_DIR"/postgresql_data')
echo "$initdb"
start_db=$(su postgres -c '"$NGENEANALYSYS_APP_DIR/"postgresql-9.6.18/bin/pg_ctl -D "$NGENEANALYSYS_DATA_DIR"/postgresql_data -l "$NGENEANALYSYS_DATA_DIR"/postgresql_data/pg.log start')
echo "$start_db"
ngas_db=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/createdb ngeneanalysys')
echo "$ngas_db"
restart_db=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/pg_ctl -D "$NGENEANALYSYS_DATA_DIR"/postgresql_data -l "$NGENEANALYSYS_DATA_DIR"/postgresql_data/pg.log restart')
echo "$restart_db"
db_ngenebio_user=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/psql -c "CREATE USER ngenebio;"')
db_uta_user=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/createuser -U postgres uta_admin')
db_uta_passwd=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/psql -c "alter user uta_admin with password 'uta_admin';"')
db_uta=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/createdb -U postgres -O uta_admin uta gzip -cdq "$NGENEANALYSYS_APP_DIR"/etc/uta_20180821.pgd.gz | "$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/psql -U uta_admin -1 -v ON_ERROR_STOP=1 -d uta -Eae')
echo "$db_user"
db_grant=$(su postgres -c '"$NGENEANALYSYS_APP_DIR"/postgresql-9.6.18/bin/psql -c "GRANT postgres TO ngenebio;"')
echo "$db_grant"
postgre_conf_file=${NGENEANALYSYS_DATA_DIR}/postgresql_data/postgresql.conf
postgresql_hba_file=${NGENEANALYSYS_DATA_DIR}/postgresql_data/pg_hba.conf
cat << EOF >> $postgre_conf_file
listen_addresses = '*'
EOF
cat << EOF >> $postgresql_hba_file
host all all	 0.0.0.0/0 md5
host all all	 ::/0 md5
EOF
```

## 설치 파일 복사

준비된 파일을 서버에 복사한다.

``` bash
fdisk -l
mkdir /mnt/tmp
mount /dev/sdb1 /mnt/tmp
```

``` bash
cd /mnt/tmp
cp -r * $NGENEANALYSYS_APP_DIR
```

복사된 파이프라인 압축을 해제한다. 압축해제 후에는 사용할 도커 이미지의 압축파일이 `docker-image` 폴더에 생성되며,
각 파이프라인 압축파일 또한 생성된다.

``` bash
cd $NGENEANALYSYS_APP_DIR
tar xzf $NGENEANALYSYS_APP_DIR/pipeline_workflow_1.5.2.0.tar.gz
```

파이프라인 별 압축 해제

=== "DNA 파이프라인"

    `workflow-ngb` 폴더에 파이프라인 압축 해제됨
    ``` bash
    tar xzf $NGENEANALYSYS_APP_DIR/workflow-ngb.1.5.2.0.tar
    ```

=== "RNA 파이프라인"

    `workflow-rna` 폴더에 파이프라인 압축 해제됨
    ``` bash
    tar xzf $NGENEANALYSYS_APP_DIR/workflow-rna.1.5.2.0.tar
    ```

=== "ONCO 파이프라인"

    `workflow-onco` 폴더에 파이프라인 압축 해제됨
    ``` bash
    tar xzf $NGENEANALYSYS_APP_DIR/workflow-onco.1.5.2.0.tar
    ```

!!! info "workflow 폴더"
    공통으로 사용되는 파이프라인이 존재하는 `workflow` 폴더는 기본으로 압축해제되어 생성된다. 

This will create the following structure:

```
.
├─ ngeneanalysys_app/
│  └─ CLIENT_UPDATE_FILES/   # 클라이언트 업데이트를 위한 폴더
│  └─ docker/                # 도커 data root 폴더
│  └─ docker-image/          # 도커 이미지 압축 파일 임시 폴더
│  └─ ngeneanalysys-server/  # 서버 구성 및 데몬 실행 파일   
│  │  └─ geneList.txt
│  │  └─ java/
│  │  └─ ngeneanalysys.conf  # 서버 설정
│  │  └─ ngeneanalysys.log   # 서버 로그
│  │  └─ ngeneanalysys-server-http-assembly-1.6.5.3.jar
│  │  └─ shutdown.sh         # 데몬 정지 스크립트
│  │  └─ startup.sh          # 데몬 시작 스크립트
│  └─ ngeneanalysys-variantvalidator/ ## VV 설치 폴더
│  └─ PDF_COMPONENT/         # pdf 라이브러리
│  └─ WEB_APP_FILES/         # 웹서비스 파일
│  └─ workflow/               # 공통 파이프라인
│  └─ workflow-ngb/           # DNA 파이프라인
│  └─ workflow-onco/          # ONCO 파이프라인
│  └─ workflow-rna/           # RNA 파이프라인
└─ ngeneanalysys_data/       # 분석 결과 폴더
│  └─ ANALYSIS_FILES/        # 최종 분석 결과
│  └─ CLIENT_UPDATE_FILES/
│  └─ FASTQ/                 # 업로드 데이터
│  └─ postgresql_data/       # db 저장 폴더
│  └─ REPORT_TEMPLATE_COMPONENTS/
│  └─ REPORT_TEMPLATE_IMAGES/
│  └─ workflow_out/           # 분석 중간 결과
```

## 파이프라인 설치

=== "DNA 파이프라인"

    ```bash
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngeneanalysys-1.5.tar
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngenebio_pcgr_1.2.tar
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngenebio_vv_api_1.0.tar
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngenebio_vv_db_1.0.tar
    ```

=== "RNA 파이프라인"

    ```bash
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/rnapanel_1.0.tar
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngenebio_web_screenshot_1.0.tar
    ```

=== "ONCO 파이프라인"

    ```bash
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/oncoaccupanel_1.1.tar
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngenebio_pcgr_1.2.tar
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngenebio_vv_api_1.0.tar
    docker load < $NGENEANALYSYS_APP_DIR/docker-image/ngenebio_vv_db_1.0.tar
    ```

## Variant Validator 설정

variant validator[^1] 

  [^1]: [Variant Validator][1]는 transcript와 genomic variants 사이의 정확한 매핑과 HGVS 시퀀스 변이를 검증하는 서비스이다.

  [1]: https://variantvalidator.org/

### UTA용 MySQL 서버 

도커 설정 파일 `docker.ini`의 IP 주소를 현재 서버의 IP 주소로 변경한다.

``` bash
cd $NGENEANALYSYS_APP_DIR/ngeneanalysys-variantvalidator
sed -i "s/127.0.0.1/{ 서버 IP 주소 }/" configuration/docker.ini
sed -i "s/127.0.0.1/10.0.0.10/" configuration/docker.ini
```

MySQL 데이터베이스를 `3306 포트`에서 도커 데몬으로 항상 실행되도록 설정한 후 실행한다.

``` bash
docker run --name ngenebio_vv_db -d -p 3306:3306 --restart=always ngenebio_vv_db:1.0
```


!!! info "restart=always 옵션"
    재시작 옵션을 `always`로 설정하면 해당 컨테이너는 항상 재시작한다. 수동으로 종료한 경우, Docker가 재시작되면 같이 재시작된다.
    이는 컨테이너를 항상 재시작할 때는 문제 없지만, 직접 옵션을 주어 옵션에 따라 원하는 동작이 명확하고, 
    always 설정인 경우 누군가는 서비스 파일을 인지하지 못할 수도 있기 때문이다.

###  VV API 서버

=== "BRCA, HERED, HEME, SOLID 파이프라인"

    ``` bash
    docker run --name ngenebio_vv_api -d -p 8000:8000 --restart=always -v $NGENEANALYSYS_APP_DIR/workflow-ngb/dependencies/HGVS/seq_repo:/usr/local/share/seqrepo -v /etc/localtime:/etc/localtime -v $NGENEANALYSYS_APP_DIR/ngeneanalysys-variantvalidator/configuration:/root/config ngenebio_vv_api:1.0
    ```

=== "ONCO의 DNA 파이프라인"

    ``` bash
    docker run --name ngenebio_vv_api -d -p 8000:8000 --restart=always -v $NGENEANALYSYS_APP_DIR/workflow-onco/dependencies/HGVS/seq_repo:/usr/local/share/seqrepo -v /etc/localtime:/etc/localtime -v $NGENEANALYSYS_APP_DIR/ngeneanalysys-variantvalidator/configuration:/root/config ngenebio_vv_api:1.0
    ```

!!! tip "VV API 테스트"

    로컬호스트의 8000번 포트에 접속하여 `NM_000088.3:c.589G>T`에 대한 정보를 쿼리해본다.

    ``` bash
    ngenebio@ngb-bi-dev:/BI2/ngeneanalysys_app/ngeneanalysys-variantvalidator$ curl -X GET  http://0.0.0.0:8000/variantvalidator/hg19/NM_000088.3%3Ac.589G%3ET/all
    {"flag": "gene_variant", "NM_000088.3:c.589G>T": {"selected_assembly": "hg19", "submitted_variant": "NM_000088.3:c.589G>T", "gene_symbol": "COL1A1", "gene_ids": {"hgnc_id": "HGNC:2197", "entrez_gene_id": "1277", "ensembl_gene_id": "ENSG00000108821", "ucsc_id": "uc002iqm.4", "omim_id": ["120150"], "ccds_ids": ["CCDS11561"]}, "transcript_description": "Homo sapiens collagen type I alpha 1 chain (COL1A1), mRNA", "hgvs_transcript_variant": "NM_000088.3:c.589G>T", "genome_context_intronic_sequence": "", "refseqgene_context_intronic_sequence": "", "hgvs_refseqgene_variant": "NG_007400.1:g.8638G>T", "hgvs_predicted_protein_consequence": {"tlr": "NP_000079.2(LRG_1p1):p.(Gly197Cys)", "slr": "NP_000079.2:p.(G197C)"}, "validation_warnings": [], "hgvs_lrg_transcript_variant": "LRG_1t1:c.589G>T", "hgvs_lrg_variant": "LRG_1:g.8638G>T", "alt_genomic_loci": [], "primary_assembly_loci": {"grch37": {"hgvs_genomic_description": "NC_000017.10:g.48275363C>A", "vcf": {"chr": "17", "pos": "48275363", "ref": "C", "alt": "A"}}, "hg19": {"hgvs_genomic_description": "NC_000017.10:g.48275363C>A", "vcf": {"chr": "chr17", "pos": "48275363", "ref": "C", "alt": "A"}}, "grch38": {"hgvs_genomic_description": "NC_000017.11:g.50198002C>A", "vcf": {"chr": "17", "pos": "50198002", "ref": "C", "alt": "A"}}, "hg38": {"hgvs_genomic_description": "NC_000017.11:g.50198002C>A", "vcf": {"chr": "chr17", "pos": "50198002", "ref": "C", "alt": "A"}}}, "reference_sequence_records": {"transcript": "https://www.ncbi.nlm.nih.gov/nuccore/NM_000088.3", "protein": "https://www.ncbi.nlm.nih.gov/nuccore/NP_000079.2", "refseqgene": "https://www.ncbi.nlm.nih.gov/nuccore/NG_007400.1", "lrg": "http://ftp.ebi.ac.uk/pub/databases/lrgex/LRG_1.xml"}}, "metadata": {"variantvalidator_version": "1.0.4.dev74+g88f5f1b", "variantvalidator_hgvs_version": "1.2.5.vv1", "uta_schema": "uta_20180821", "seqrepo_db": "2018-08-21"}}
    ```

!!! tip "SeqRepo 테스트"

    vv-api 컨테이너에 접속하여 파이썬을 통해 원하는 transcript의 sequence를 확인한다.
    ``` bash
    ngenebio@ngb-bi-dev:/BI2/ngeneanalysys_app/ngeneanalysys-variantvalidator$ docker exec -it e298ab1c456a /bin/bash
    root@e298ab1c456a:/app# python
    Python 3.6.10 (default, Jun  9 2020, 18:36:16)
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from biocommons.seqrepo import SeqRepo
    >>> sr=SeqRepo("/usr/local/share/seqrepo/latest")
    >>> sr["NC_000001.11"][780000:780020]
    'TGGTGGCACGCGCTTGTAGT'
    ```

## 폴더 권한 설정

``` bash
chown -R ngenebio:ngenebio $NGENEANALYSYS_APP_DIR
chown -R ngenebio:ngenebio $NGENEANALYSYS_DATA_DIR
chown -R postgres:postgres $NGENEANALYSYS_APP_DIR/postgresql-9.6.18/
chown -R postgres:postgres $NGENEANALYSYS_DATA_DIR/postgresql_data
chmod -R 700 $NGENEANALYSYS_APP_DIR
chmod -R 700 $NGENEANALYSYS_DATA_DIR/postgresql_data
chmod 777 $NGENEANALYSYS_APP_DIR
chmod 777 $NGENEANALYSYS_DATA_DIR
```

## 서버 환경 설정

서버 설정 파일 수정

``` bash
cd $NGENEANALYSYS_APP_DIR
cd ngeneanalysys-server
nano ngeneanalysys.conf
```

### 설치 용도 선택

``` bash
mode = "development | production"
```

### 통신 방식 선택

``` bash
httpFlag = "https | http"
```

### 서버 환경 선택

``` bash
serverType = "standAlone | cluster | google"
```

### API 접속 주소

akka.http.server.remote-address-header = on 설정

``` bash
akka {
  http {
    server {
      remote-address-header = on
    }
  }
}
```

### 인증 토큰 설정

``` bash
allowTokenShare = false
```

### 암호 기간 설정

``` bash
passwordUsagePeriod = 7776000000
```

### 구글 클라우드 설정

``` bash
googleConfig {
    zone = "asia-northeast3-a"
    region = "asia-northeast3"
    pipelineInstanceImage = "image-ngas-devel-pipeline-v1"
    network = "network-name"
    subnet = "subnet-name"
    storagePath = "gs://"
}
```

### 내부 상태 조회

``` bash
healthCheckToken = “fdjsakfljdsaklfjdsaklfa”
```

### 설치 폴더 설정

``` bash
ngeneanalysysAppDir = "/ngeneanalysys_app"
ngeneanalysysDataDir = "/ngeneanalysys_data"
```

## 서버 자동 시작

### rc.local 등록

``` bash
chmod 755 /etc/rc.local
echo "
chmod 666 /var/run/docker.sock
su -c 'export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:\$NGENEANALYSYS_APP_DIR/postgresql-9.6.18/lib; \$NGENEANALYSYS_APP_DIR/postgresql-9.6.18/bin/pg_ctl -D \$NGENEANALYSYS_DATA_DIR/postgresql_data -l \$NGENEANALYSYS_DATA_DIR/postgresql_data/pg.log restart' - postgres
su -c '\$NGENEANALYSYS_APP_DIR/ngeneanalysys-server/shutdown.sh' - ngenebio
su -c '(sleep 10 && \$NGENEANALYSYS_APP_DIR/ngeneanalysys-server/startup.sh) &' - ngenebio
" >> /etc/rc.local
nano /etc/rc.local
```

!!! warning "exit 0"
    rc.local 파일의 맨마지막 라인은 `exit 0` 으로 설정한다.

!!! info "rc.local 파일"
    rc.local은 부팅시 자동 실행 명령어 스크립트로 서버 부팅시마다 매번 자동 실행된다.
    .profile이 로그인시 /etc 의 설정 파일보다 먼저 계정에 적용되어 path나 shell 환경변수가 설정되는것에 반해
    rc.local은 부팅시 실행될 데몬 같은 것들이 들어간다.


### 로그 백업

``` bash
/ngeneanalysys_app/ngeneanalysys-server/ngeneanalysys.log {
daily
create 0600 ngenebio ngenebio
dateext
compress
copytruncate
notifempty
size 100M
maxage 30
rotate 30
nomail
}
```

``` bash
/etc/cron.daily/logrotate
```