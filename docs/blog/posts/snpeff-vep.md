---
date: 2022-10-05
authors: [ngenebio]
description: >
  해석 서비스에서 보다 정확한 변이의 변화에 대한 예측하기 위해서, 대표적인 프로그램인 SnpEff와 VEP의 분석 결과 비교 진행
categories:
  - Blog
links:
  - Getting started: variant-annotation-data
---

# snpEff vs. VEP

__해석 서비스에서 보다 정확한 변이의 변화에 대한 예측하기 위해서, 대표적인 프로그램인 SnpEff와 VEP의 분석 결과 비교 진행__

주어진 변이에 대한 annotation [^1]을 수행하기 위해서 잘 알려진 툴로는 snpEff, VEP 등을 사용한다. 여기서는 이 두개의 툴을 비교하기 위해서 다음과 같은 버전으로 BRCA1/2 변이에 113,787개를 이용하여 검증하였다.

<!-- more -->

  1. SnpEff v5.1
  2. VEP v107
  3. Reference.RefSeq v107

비교 결과 주로 3가지 변이 타입에서 서로 다른 결과를 보였다.

  1. Delin 변이
  2. Splice site 변이
  3. Exon loss 변이

  [^1]:
    일반적인 annotation이라고 하면, hgvs 표기법과 transcript에 따른 consequence를 의미한다.


## Delins 변이

SO에 따르면 "A sequence alteration which included an insertion and a deletion, affecting 2 or more bases"로 아래와 같은 경우 두 개의 툴은 consequence에서 서로 차이를 보였다.

snpEff는 해당 delins에 대해서 frameshift_variant, stop_gained, synonymous_variant의 3개를 제공하는 반면, vep는 frameshift_variant만을 제공한다. 이는 3개의 모든 경우가 모두 해당한다. 

  1. chromosome—position—ref seq—variant seq: [chr13-32972745-C-GAATTATATCT]
  2. hgvs.g: chr13:g.32972745C>GAATTATATCT (x)
  3. hgvs.g: chr13:g.32972745delinsGAATTATATCT (o)

이러한 전반적인 문제는 [goldenhelix 블로그]를 확인하기 바란다.


  [chr13-32972745-C-GAATTATATCT]: https://varsome.com/variant/hg19/chr13-32972745-C-GAATTATATCT?annotation-mode=germline

## Splice site 변이

Exon과 Intron 영역에 모두 포함한 Del, Delins 형태의 splice site 변이에 대해서 vep는 hvgs.p를 예측하지 않고 consensequence 또한 amino acid가 변하지 않는 coding_sequence_variant로 예측한다.

## Exon loss 변이

SnpEff과 달리 VEP에서는 “exon_loss_variant”를 판정하지 않기때문에, 아래의 변이에 대해서 다른 consequence로 판정함

## 기능 비교

vep와 SnpEff의 기능들을 비교한 결과, 대부분의 기능들은 공통적으로 제공함
  1. Lossoffunctionprediction: SnpEff에서는기본적으로제공하지만,VEP는plugins모듈로추가가능함(LOFEE)
  2. Nonsense mediate decayassessment(NMD): 해당 결과는 CLNANN에서 반드시 필요한 기능이나,대체 프로그램이 존재함(AutoPVS1)


## HGVS 표기법 비교

HGVS Nomenclature에 의거하여 계산한 VEP와 다르게, SnpEff는 기준에 부합되지 않는 HGVS.c와 HGVS.p 정보를 제공하는 경우가 확인됨

  [goldenhelix 블로그]: https://blog.goldenhelix.com/the-sate-of-variant-annotation-a-comparison-of-annovar-snpeff-and-vep/
