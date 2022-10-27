---
template: overrides/main.html
title: 시스템 요구 사항
---

# 소개
이 문서는 NGeneAnalySys 1.5.x.x 소프트웨어 시스템 중 특히 서버 소프트웨어의 시스템 요구사항, 설치 및 문제해결 방법을 설명한다. 
NGeneAnalySys 서버 소프트웨어는 :material-ubuntu: 리눅스에 직접 설치 또는 :fontawesome-brands-windows: Windows 10 Hyper-V 가상 머신 이미지 설치 두 가지 방식을 제공한다. 
제공되는 가상 머신 이미지는 Ubuntu 16.04 Linux에 NGeneAnalySys 서버 소프트웨어가 설치되어 있다. 
소프트웨어를 설치하는 기관의 IT 보안 및 프라이버시 정책에 따라서 이 문서에서 다루지 않는 추가적인 설정 과정[^1]이 필요할 수 있다.

[^1]:
    리눅스에 직접 설치하는 방식은 일반 사용자가 직접 설치하기 힘들기 때문에 권장하지 않으며 제조사 또는 대리점에 설치 지원을 요청해야 한다. 
    리눅스 직접 설치 가능 여부는 판매 국가 별로 다르므로 제조사 또는 대리점에 문의해야 한다.

## 하드웨어 요구사항
NGeneAnalySys 서버 소프트웨어가 동작하기 위해서는 최소한 40GB 의 RAM 및 논리적 4 Core CPU가 필요하다.
윈도우즈 10 Hyper-V 가상 머신 이미지 설치 방식의 경우 최소 20GB의 RAM이 필요하다.

!!! info "대기 모드 해제"
    NGeneAnalySys 서버가 설치되는 서버는 대기(stanby) 상태로 변경되지 않도록 반드시 설정해 주어야 한다. 
    NGeneAnalySys 운영 중 서버가 대기 상태로 변경되면 분석이 중단될 수 있다. 또한 분석이 진행 중일 때 서버를 재시작하면 분석이 중단될 수 있다. 
    윈도우 10의 경우 자동 업데이트 기능으로 인해서 서버가 자동 재시작 될 수 있으므로 자동 업데이트 기능은 반드시 꺼 두고 사용자가 직접 주기적으로 운영체제의 보안 업데이트를 해주어야 한다.

NGeneAnalySys 서버를 리눅스에 직접 설치할 경우에는 최소 300GB의 디스크 여유 공간이 필요하며 모든 파이프라인을 설치할 경우 최대 700 GB의 기본 설치공간이 필요할 수 있다. 
분석 결과의 저장을 위해서 1TB 이상의 디스크 사용을 권장한다. 윈도우 10에서 Hyper-V 가상화 기능을 사용하려면 [하드웨어 요구 사항]을 만족해야 한다.

  [하드웨어 요구 사항]: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/hyper-v-requirements

윈도우 10의 Hyper-V 가상화를 이용하여 NGeneAnalySys를 설치할 경우 리눅스에 직접 설치하는 방식 보다 더 많은 디스크 공간이 필요하며 최소 1TB 이상의 디스크 여유 공간이 필요하다.
NGeneAnalySys는 서버와 클라이언트가 분리된 소프트웨어 형태이며 상호 간에 네트워크를 통해서 통신하기 때문에 서버에 네트워크 연결 가능한 하드웨어가 필요하다. 
네트워크는 최소 100Mbps 이상의 속도가 필요하며 1Gbps의 속도를 권장한다. 
NGeneAnalySys 소프트웨어 설치 파일은 외장 디스크에 저장된 상태로 제공되기 때문에 외장 디스크의 데이터를 서버로 전송하기 위해서는 :fontawesome-brands-usb: USB 2.0 A 타입 또는:fontawesome-brands-usb: USB 3.0 A 타입 포트가 필요하다.

## 소프트웨어 요구사항
NGeneAnalySys 서버는 리눅스 운영체제 기반으로 동작하도록 개발되었다. NGeneAnalySys v1.5.0.0는 Ubuntu 16.04 또는 CentOS 7 운영체제에서 정상적으로 설치 가능하다.

!!! info "사용자 계정"
    NGeneAnalySys는 분석 파이프라인을 :simple-docker: 도커 컨테이너를 이용하여 실행하고, 분석 파이프라인의 작업 스케쥴링은 Docker Swarm를 이용한다. 
    NGeneAnalySys는 분석 결과를 저장하기 위해 PostgreSQL 데이터베이스 소프트웨어를 설치 및 NGeneAnalySys 소프트웨어의 동작을 위해 postgres, ngenebio 두 개의 리눅스 사용자 계정을 생성해야 한다. 
    이미 운영 중인 리눅스 운영체제에 직접 NGeneAnalySys 서버를 설치할 경우 위 사항에 대해서 확인이 필요하다.

NGeneAnalySys 서버는 윈도우 10의 Hyper-V 가상화 시스템에서도 동작한다. [Hyper-V 가상화]는 윈도우 10 Pro 또는 윈도우 10 Enterprise에서만 동작하며 윈도우 10 Home 버전에서는 지원하지 않는다. 

  * 윈도우 10의 경우 1809 버전 이상의 윈도우 업데이트가 필요하다. 윈도우 10의 초기 릴리스 버전의 경우 Hyper-V 호환성 문제로 NGeneAnalySys 서버가 정상적으로 설치되지 않는다.
  * 윈도우 10에 Hyper-V를 제외한 기타 가상화 소프트웨어를 사용할 경우 Hyper-V가 정상적으로 동작하지 않는다. Hyper-V를 사용하려면 VMWare 또는 VirtualBox와 같은 다른 가상화 소프트웨어를 삭제해야 한다.

  [Hyper-V 가상화]: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/
