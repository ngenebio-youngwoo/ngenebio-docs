---
template: overrides/main.html
title: NGS와 진단
---

# NGS와 진단
Our platform can process data from any type of biological sample, including fresh frozen tissue, formalin-fixed paraffin-embedded samples as well as liquid circulating tumor DNA samples. It can also process data from any nucleic acid source across DNA and RNA. We can identify with confidence any type of genomic alteration, including single nucleotid variants (SNVs), insertions-deletions (indels), copy-number variations (CNVs) and gene fusions, as well as more complex mutational signatures such as microsatellite instability (MSI), tumor mutational burden (TMB), homologous recombination deficiency or minimal residual disease. Our smart algorithms allow us to reach high accuracy on the detection and identification of challenging genomic alterations, such as mutations in CEBPA or FLT3-ITD, MET exon14 skipping mutations, or rare gene fusions.

## 유전체학 분야
- [x] Process sample
    * Liquid Circulating tumor DNA (ctDNA)
    * Fresh frozen tissue (FFT)
    * Formalin-Fixed Paraffin-Embedded (FFPE)
- [x] Process nucleic sources
    * DNA
    * RNA
- [x] Identify genomic alterations
    * SNVs
    * Indels
    * CNVs
    * Fusion
    * MRD
- [x] Identify genomic signatures
    * MSI
    * HRD
    * TMB
- [x] Challenging alterations
    * CEBPA
    * FLT3-ITD
    * MET exon14 skipping
    * Rare fusions (e.g, NTRK1/2/3, RET)

## MSI
자동차가 고장이 나면 자동차 정비소의 정비사는 자동차의 어느부분이 문제가 생겼는지를 확인하고
문제에 따라 해당 부품을 교체하거 수리하여 고장을 해결하게 된다.

우리몸의 각 세포들도 어떻게 자라고 어떤한 일을 하고 분열하고 죽는지에 대한 지시를 하는 정비사와 같은 역할을 하는 MMR (염색체 불일치 복구) 유전자[^1]가 존재한다.
정비사가 제역할을 하지 못하는 경우 더 솜씨 좋은 정비사로 교체하는 등의 적절한 해결 (종양에서는 적절한 치료법을 선택)을 위해서는
정비사가 제대로 역할을 하는지를 확인해야 한다. 우리몸에서도 MMR이 제역할을 하는지를 확인하는 방법이 바로 MSI-H (현미부수체 불안정성)[^2]라는 바이오마커이다. 

세포의 DNA는 Microsatellite라고 불리는 짧고 반복적인 DNA 서열이 존재한다. 서열의 반복 횟수가 신체의 모든 세포에서 동일한 경우는 안정적이라고 간주하고 이를 MSS라고 한다.
하지만 일부 암 환자의 경우 MMR 과정에 결합이 생기는 dMMR (정비사가 제대로 일을 하지 못하면서)에 의해 건강한 세포에 비해 너무 많거나 일정하지 않은 반복 횟수를 보이는 MSI-H를 보이게 된다.

[^1]:
    염색체 불일치 복구 유전자(mismatch repair genes: MMR): LH1, MSH2, MSH6, PMS2
[^2]:
    현미부수체 불안정성 (Microsatellite instability-high: MSI-H)
    

### MSI-H 검사와 치료
MSI-H와 같은 종양 바이오마커의 세부사항을 아는 것은 종양의 특성에 특화된 개인화된 치료의 결정에 도움을 줄 수 있다.

- [x] MSI-H와 dMMR은 예측 바이오마커로 전체적으로 MSI-H 종양환자는 MSS 종양 환자보다 예후가 좋다.
- [x] 면역치료에 대한 긍정적인 반응을 예측하지만 불소우라실 기반 화학요법 (fluorouracil-based chemotherapy)에는 잘 반응하지 않는 예측 바이오마커이다.
- [x] MSI-H인 경우 면역체크포인트 억제제 (옵디보, 키트루다[^3], 여보이 등)를 사용하는 승인된 치료법을 사용할 수 있다.

!!! info "면역치료와 면역항암제"
    암세포뿐 아니라 정상세포도 같이 공격하여 부작용이 심한 기존 항암제와 다르게
    인공면역 단백질을 체내에 주입하여 면역체계를 자극함으로써 면역세포가 선택적으로 암세포만을 공격하도록 하는 치료 약제로
    표적 항암제의 문제점이었던 내성을 개선하여 장기간 효과가 지속되는 장점이 있다.

    다양한 면역항암제가 FDA의 승인을 받았으며 그중 MSI-H에 대해 승인 받은 옵디보(성분명: nivolumab), 키트루다 (성분명: pembrolizumab),
    여보이 (성분명: lpilimumab)이 존재하며 특히, 키트루다는 전암종에 대해서 MSI-H인 경우 승인을 받았다.

[^3]:
    식품의약품안전처는 21년 6월  수술 불가능하거나 전이성인 고빈도-현미부수체 불안정성(microsatellite instability high, MSI-H) 또는 불일치 복구 결함(mismatch repair deficient, dMMR) 대장암 1차 치료에 키트루다 단독요법을 허가 승인했다.
    키트루다는 지난해 8월 MSI-H/dMMR 바이오마커가 있는 7개 고형암(자궁내막암, 위암, 소장암, 난소암, 췌장암, 담도암, 직결장암) 2차 치료에 이어, MSI-H/dMMR 직결장암 환자에서 1차 치료에 사용 가능한 유일한 면역항암제가 됐다. 
    출처 : 청년의사(http://www.docdocdoc.co.kr)

### 전통적인 검사 방법
전통적인 MSI 검사방법은 동일한 환자의 종양/정상조직의 genomic DNA를 PCR로 증폭하여 전기영동을 통해 microsatellite에서 종양과 정상조직간 길이 변화로 MSI를 판정하게 된다.
이 방법은 gold-standard로서 정상조직을 사용하기에 검사 기관사이의 일치도와 정확도가 높은 반면, tumor percentage가 낮은 검체는 반복서열의 길이가 normal가 비슷하게 보여 instability를 확인하기 어렵고 polymerase slippage에 의해 생성되는 false positive artifact로 true positive instability와 구분하기 어렵다. 특히 mononucleotide에서 자주 발생하며 반복서열의 길이가 길어질수록 빈도가 높아지게 된다.

* High microsatellite instability (MSI-H): 2개 이상에서 불안정성
* Low microsatellite instability (MSI-L): 1개에서 불안정성
* Microsatellite stability (MSS): 불안정성이 없는 경우

!!! info "MSI PCR 검사 표지자"
    5개의 표지자를 사용하여 PCR 검사를 수행함

    * mononucleotide 영역: BAT25, BAT26
    * dinucleotide 영역: D2S123, D5S346, D17S250

### NGS를 이용한 검사 방법
NGS를 이용하게 되면 multiple target을 동시게 검사할 수 있어 cost effective하며 적은 양의 sample로도 검사가 가능하다. 
MSI status는 T/N 매칭 샘플을 활용하는 것이 더 간단하고 바람직하나, 그렇지 못한 상황에서 NGS는 그 대안이 될 수 있다.
하지만 tumor 조직만으로 sequencing error나 polymorphism과 구별이 어렵고 gold standard가 없기에 기존의 PCR 검사로 다시 검증하는 과정이 필요하다. 
하지만, NGS 보험수가 적용에 따라 NGS를 이용하여 MSI를 확인하고 필요에 따라 PCR 검사를 수행한다면 불필요한 cost를 줄일 수 있게 된다.

### 소피아제네틱스
The SOPHIA DDM™ Algorithm for MSI Detection was effectively developed to perform MSI classification in multiple cancers and trained on a specific selection of more than 100 microsatellite regions identified as highly performant in different cancer types.[^10]

[^10]:
    https://www.sophiagenetics.com/science-hub/pan-cancer-testing-of-microsatellite-instability-to-optimize-cancer-management-strategies/

### 엔젠바이오
SNV/INDE >30, INDEL index >20%, hotspot(ACVR2A mutation)를 이용[^4]

[^4]:
    Mutation Burden and I Index for Detection of Microsatellite Instability in Colorectal Cancer by Targeted Next-Generation Sequencing [https://www.sciencedirect.com/science/article/pii/S1525157818300783][6]

  [6]: https://www.sciencedirect.com/science/article/pii/S1525157818300783

### 일루미나 TSO500
일루미나 TSO500은 130 repeat loci를 기반으로 내부 알고리즘을 사용
(130 MSI marker sites to calculate a quantitative score)

### MSK-IMPACT
FDA에 somatic mutation과 MSI에 대한 정보만 제공하는것으로 승인
MSK-IMPACT within tumor samples against the matched normal DNA using the program MSIsensor (Nui B et al. 2014).

### FMI
To determine a patient’s MSI status, F1CDx employs a fraction-based (FB) MSI algorithm to categorize a
tumor specimen as MSI-High (MSI-H) or microsatellite stable (MSS).

## 참고 문헌

* 소피아 DDM을 이용한 논문 [Tumor BRCA testing in ovarian cancer and EQA scheme: our experience of a critical evaluation][1]
* 분석 플랫폼 프로젝트 관리 참고 [NEAT: a framework for building fully automated NGS pipelines and analyses][2]
* 분석 파이프라인 [How to create a data pipeline for Next Generation Sequencing][3]
* 인실리코 NGS 파이프라인 검증 [Recommendations for the Use of in Silico Approaches for Next-Generation Sequencing Bioinformatic Pipeline Validation][4]
* FDA의 CDS 소프트웨어 지침 [Clinical Decision Support Software Guidance for Industry and Food and Drug Administration Staff] [5]

  [1]: https://link.springer.com/article/10.1007/s11033-021-06812-0
  [2]: https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-0902-3
  [3]: https://www.opensourcerers.org/2020/12/14/industry-use-case-next-generation-sequencing-for-a-distributed-data-pipeline/
  [4]: https://www.jmdjournal.org/article/S1525-1578(22)00287-2/fulltext
  [5]: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software