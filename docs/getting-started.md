---
template: overrides/main.html
title: Getting started
---

# 작성 테스트 
  * 2022-11-24 16:11
  * 2022-11-25 10:33
  * 2022-11-25 10:42
  * 2022-11-25 14:20
  * SOPHiA DDM™ for Solid Tumors

# 정밀의료
:material-dna: 유전체 기반의 정밀의학이 적시에 제공되기 위해서 분자 진단 검사실은 
증가하는 유전자 검사를 최신 과학적 근거, 약물 승인 및 치료 지침을
효율적이고 철저한 방식으로 신속하게 분석하고 해석해야 하는 과제를 안고 있다.
차세대 시퀀싱 (NGS) 데이터의 해석 및 보고를 위한 전문가 큐레이션된 지식,
소프트웨어 및 [서비스를 제공]하여 진료에 있어서 신뢰할 수 있는 의사 결정이 필요합니다.

[서비스를 제공]: https://digitalinsights.qiagen.com/products-overview/

## 정밀의료와 소프트웨어
NGS 데이터 처리 및 변이해석 소프트웨어에 대한 규제 동향을 :flag_kr: 국내, :flag_us: 미국, :flag_eu: 유럽으로 나누어 볼 수 있다.

- [x] 미국: FDA는 최근 CDS 소프트웨어 지침[^1]을 통해 NGS 데이터 처리와 변이 해석 소프트웨어 모두를 감독 대상으로 명시
- [x] 유럽: IVD medical device assays의 데이터를 input으로 받는 MDSW는 CE-IVDR 대상

  [^1]: 
   [Clinical Decision Support Software - Guideance for Industry and FDA Staff][1]
     [1]: https://www.fda.gov/media/109618/download

??? question "IVD 소프트웨어 및 시스템은 IVDR에 따라 어떻게 분류되는가?"
    기기 (device)를 구동하거나 기기 사용에 영향을 미치는 소프트웨어/시스템은
    기기와 같은 등급에 속해야 한다.
    소프트웨어/시스템이 다른 장치와 독립적인 경우,
    그 적용에 따라 자체적으로 분류되어야 한다.
    
## Sophia Genetics

소피아제네틱스의 genomics 관련 플랫폼은 SOPHiA DDM for Genomics를 기반으로
oncology 관련 솔루션을 제공하고 있다.

  * SOPHiA DDM™ for Solid Tumors
  * SOPHiA DDM™ for Blood Cancers
  * SOPHiA DDM™ for Hereditary Cancers

### Sophia Genetics CE-IVD
소피아제네틱스의 [CE-IVD 기사] (2022년)에 따르면, 올해 2개를 추가하여 총 5개의 CE-IVD를 DDM Platform에 대해서 획득하였다.

  * SOPHiA DDM™ Dx Homologous Recombination Deficiency (HRD) Solution
  * SOPHiA DDM™ Dx RNAtarget Oncology Solution (ROS)
  * SOPHiA DDM™ Dx Solid Tumor Solution (STS)
  * SOPHiA DDM™ Dx Myeloid Solution (MYS)
  * SOPHiA DDM™ Dx Hereditary Cancer Solution (HCS)

[![CE-IVD Oncology][110]][110]

  [110]: assets/screenshots/sophia.png

  [CE-IVD 기사]: https://www.genomeweb.com/regulatory-news-fda-approvals/sophia-genetics-gets-ce-ivd-mark-ddm-platforms-analytics?_ga=2.227213021.1115069856.1666315814-1673504714.1665445574&adobe_mc=MCMID%3D22851554295355469673754877065205084752%7CMCORGID%3D138FFF2554E6E7220A4C98C6%2540AdobeOrg%7CTS%3D1666315827&CSAuthResp=1%3A%3A2455941%3A1911%3A24%3Asuccess%3AF2DE22E6E75C7FA66C9A2FDB82D6080F#.Y1H2O-xBxhE

소피아제네틱스의 DDM 플랫폼 중 상단의 5개 솔루션과 함께 DDM 웹 플랫폼이 사용되는 경우에 대해서 CE-IVD 제품으로 체외진단용으로 사용이 가능하다.
소피아제네틱스는 패널을 번들 솔루션이라고 부르고 있으며, 이는 DDM 플랫폼을 메인으로 보고 패널을 그에 따르는 번들로 인식하고 있음을 시사하며
소피아제네틱스는 이를 :material-bird: SOPHiA DDM (Data Driven Medicine) 플랫폼 이라고 부르고 있다. 

### CE-IVD Q&A

??? question "What is the in vitro diagnostic regulation (IVDR)?"

    IVDR is the new in vitro diagnostic Regulation (EU) 2017/745 [^4] of the European Parliament and 
    of the Council of April 5, 2017 on medical devices, 
    which went into effect on May 26, 2022, amending Directive 2001/83/EC, 
    Regulation (EC) No 178/2002 and Regulation (EC) 
    No 1223/2009 and repealing Council Directive 90/385/EEC and 
    Medical Device Directive 93/42/EE [^5].

  [^3]:
    EU의 법령안은 공동체 입법의 종류에 맞도록 적절히 구분되어야 하며, 특히 구속력의 여부에 따라 규정(regulation), 지침(directive), 결정(decision), 권고(recommendation) 등으로 구분되어야 한다.
  [^4]:
    규정 2017/745: 의료기기(MDR, Medical Device Regulation)
  [^5]:
    지침 93/42/EEC: 의료기기(MDD, Medical Device Directive)

??? question "시중에 나와 있는 CE-IVD 제품을 계속 사용할 수 있나요?"
    네. IVDD에 등록된 CE-IVD 제품은 유럽 위원회가 제품 분류를 위해 발표한 일정에 따라 시장에 남아 있을 수 있습니다. 
    IVDR에 따르면 SOPHiA GENESTIONS™ 제품은 Class C 장치로 분류되며 2026년 5월 26일까지 시판될 수 있습니다.

??? question "유전자 검사를 위한 새로운 IVDR은 무엇이 바뀌었는가?"
    IVD 제품의 분류와 위험 계층화가 바뀌었고, 이제는 유전자 검사와 동반 진단도 포함한다.
    IVDR에는 이제 소프트웨어 및 사내 개발 검사(in-house developed assays, IHAs)가 포함됩니다. 
    둘 다 보다 강력한 통제의 대상이 되며 통보된 기관의 승인을 받아야 한다.
    제조업체가 안전 및 성능 주장을 입증하기 위해서는 보다 심층적인 임상 데이터가 필요하다.
    현재 IVD 지침의 약 10%에 비해, IVD 제품의 80%에 대해서는 통보된 기관의 승인이 필요하다.

??? question "SOPHiA DDM™ 플랫폼에는 CE-IVD가 있습니까?"
    CE-IVD 번들 솔루션 (our 5 CE-IVD bundle solutions) 중 하나와 함께 사용할 경우, SOPHiA DDM™ 웹 플랫폼은 
    유럽, 터키 및 이스라엘에서 체외 진단 용도로 CE-IVD 제품으로 제공됩니다.


## QIAGEN

### QCI Analyze

QCI Analyze는 QIAGEN GeneReader와 연동하여 NGS 데이터를 분석하기 위해
`CLC Genomics Server`와 `QIAGEN CLC 바이오 알고리즘`의 기능을 사용하는 
브라우저 기반 인터페이스입니다. 또한 QCI Analyze는 보고된 변이를
QCI Interpret에 원활하게 직접 업로드 할 수 있다.

QCI Analyze workflows

  * `AIT Basic FFPE` workflow: QIAact Actionable Insights Tumor Panel (AIT)
  * `AIT Basic plasma` workflow: QIAact Actionable Insights Tumor Panel (AIT)
  * `AIT UMI FFPE` workflow: QIAact AIT DNA UMI Panel
  * `BRCA 1/2 Basic FFPE` workflow: QIAact BRCA 1/2 Panel
  * `BRCA UMI FFPE and BRCA UMI germline` workflow: QIAact BRCA Advance DNA UMI Panel
  * `Myeloid DNA UMI` workflow: QIAact Myeloid DNA UMI Panel
  * `Lung DNA UMI FFEP and Lung DNA UMI plasma` workflow: QIAact Lung DNA Panel
  * `Lung Plasma Track` workflow: QIAact Lung Plasma Track Panel 

### QCI Secondary Analysis

QCI Secondary Analysis는 DNAnexus가 제공하는 NGS 2차 분석을 위한 클라우드 기반 서비스입니다.
모든 NGS 장비 및 패널 조합과 함께 사용할 수 있으며 QIAGEN의 임상 NGS 해석 플랫폼인
QCI Interpret에 원할하게 연결하여 통합되어 FASTQ에서 보고서까지 자동화된 워크플로우를 제공합니다.

[![QCI Secondary Analsysis][111]][111]

  [111]: assets/screenshots/QSAworkflow.png

데이터가 QCI Secondary Analysis에 업로드 되면
사용자는 특정 패널, 정책 및 표준절차 (SOP)에 맞게 최적화된 사전 구성된 분석 파이프라인을 선택합니다.
사용자는 QCI Secondary Analysis 내에서 QIAGEN의 CLC Genomics Workbench와 같은
생물정보학 도구를 실행하고 배포할 수 있는 옵션도 있습니다.

QCI Secondary Analysis는 여러 시퀀싱 런의 분석을 동시에 자동화하여 몇 분 내에 변이를 생성한 후
사용자는 클라우드 플랫폼에서 직접 게놈 브라우저에서 read pileups과 같은 분석 결과를 시각화 할 수 있습니다.
또는 사용자가 VCF 파일을 QCI Interpret로 직접 전송하거나 결과를 다운로드 하여 원하는 플랫폼을 전송할 수 있습니다.

  * QIAGEN QIASeq Panel Pipeline: Using QIAGEN CLC Genomics Tool Suite
  * Illumina TSO500 Panel Pipeline: Using Illumina Analysis Tool Suite
  * Aglient Panel Pipeline: Using QIAGEN CLC Genomics Tool Suite

### QCI Interpret

  * QCI Interpret preconfigured for TSO500

## VarSome

VarSome Clinical은 EC 98/97/ECC의 요구사항에 따라 체외진단 의료 장치로 임상적으로 인증되었습니다.
체외진단지침 (IVDD) 98/97/EC는 체외의 안전, 품질 및 성능을 구체적으로 다루고 있습니다. 
체외진단규정 (IVDR)은 새로운 규제로 [VarSome Clinical이 준비중]에 있다. 

  [VarSome Clinical이 준비중]: https://youtu.be/gMYuBDZpSPU