---
template: overrides/main.html
---

# Variant annotation data

## Data sources

We currently obtain variant annotation data from several data resources and
keep them up-to-date, so that you don't have to do it:

Total hg19 variants loaded: x,xxx,xxx,xxx

| Source                     | version                 | # of variants             | key name       |
| :--------------------------| :-----------------------| :-------------------------| :--------------|
| dbNSFP                     | 4.2a                 | 82,754,233             | dbnsfp [^1]       |


  [^1]:
    key name을 대소문자를 섞어서 진행해야 하는지? 모두 소문자로 진행하는것으로 방향을 잡고 진행
    This is the key for the specific annotation data in a variant object.

!!! warning "Note"

    Each data source may have its own usage restrictions (e.g. CADD data are free for non-commercial use only). 
    Please refer to the data source pages above for their specific restrictions.

## Variant object

Variant annotation data are both stored and returned as a variant object, 
which is essentially a collection of fields (attributes) and their values:

``` json

{
  "hg19Chr": "chr17",
  "hg19Pos": 41244936,
  "hg38Chr": null,
  "hg38Pos": null,
  "ref": "G",
  "alt": "A",
  "cytoBand": "17q21.31",
  "hg19Key": "chr17:g.41244936G>A",
  "hg38Key": null,
  "dbSNP": [
    {
      "rsId": 799917
    }
  ],
  "kova": [
    {
      "altCount": 612,
      "totalCount": 2108,
      "homozygous": 89,
      "frequency": 0.2903
    }
  ],
  ...
```

The example above omits many of the available fields. 
For a full example, check out [this example] variant, or try the [interactive API page].

  [this example]: http://192.168.1.14:8084/hg19/all-database/chr1%3Ag.11856378G%3EA
  [interactive API page]: http://192.168.1.14:9000/

## Available fields

| Field      | Type   | Searched by default [^2]    | hg19    | hg38   | Description                          |
| ---------  | -------| -----------------------| ------- | -------| -------------------------------------|
| `hg19Chr`  | text |                        |         |        |                                      |
| `hg19Pos`  | integer |                        |         |        |                                      |
| `hg38Chr`  | text |                        |         |        |                                      |
| `hg38Pos`  | integer |                        |         |        |                                      |
| `ref`  | text |                        |         |        |                                      |
| `alt`  | text |                        |         |        |                                      |
| `cytoBand`  | text |                        |         |        |                                      |
| `hg19Key`  | text |                        |         |        |                                      |
| `hg38Key`  | text |                        |         |        |                                      |
| `dbSNP`  | object |                        |         |        |                                      |
| `kova`  | object |                        |         |        |                                      |
| `dbNSFP`  | object |                        |         |        |                                      |
| `dbscSNV`  | object |                        |         |        |                                      |
| `clinVar`  | object |                        |         |        |                                      |
| `gnomadExomes`  | object |                        |         |        |                                      |
| `gnomadGenomes`  | object |                        |         |        |                                      |
| `cancerHotspots`  | object |                        |         |        |                                      |
| `koexid`  | object |                        |         |        |                                      |
| `krgdb`  | object |                        |         |        |                                      |
| `vep`  | object |                        |         |        |                                      |

  [^2]:
    search의 q=xxx인 경우 기본 검색되는 필드 (cadd.gene.genename, clingen.caid, clinvar.gene.symbole, clinvar.hgvs.coding  )

### dbSNP

| Field      | Type   | Searched by default [^2]    | hg19    | hg38   | Description                          |
| ---------  | -------| -----------------------| ------- | -------| -------------------------------------|
| `dbSNP.rsId`  | text |                        |         |        |                                      |

### kova

| Field      | Type   | Searched by default [^2]    | hg19    | hg38   | Description                          |
| ---------  | -------| -----------------------| ------- | -------| -------------------------------------|
| `kova.altCount`  | integer |                        |         |        |                                      |
| `kova.totalCount`  | integer |                        |         |        |                                      |
| `kova.homozygous`  | integer |                        |         |        |                                      |
| `kova.frequency`  | float |                        |         |        |                                      |

### dbNSFP

| Field      | Type   | Searched by default [^2]    | hg19    | hg38   | Description                          |
| ---------  | -------| -----------------------| ------- | -------| -------------------------------------|
| `dbNSFP.aminoAcid`  | object |                        |         |        |                                      |
| `dbNSFP.aminoAcid.alt`  | text |                        |         |        |                                      |
| `dbNSFP.aminoAcid.ref`  | text |                        |         |        |                                      |
| `dbNSFP.frequency`  | object |                        |         |        |                                      |
| `dbNSFP.frequency.alspac`  | float |                        |         |        |                                      |
| `dbNSFP.frequency.twinsuk`  | float |                        |         |        |                                      |
| `dbNSFP.frequency.uk10k`  | float |                        |         |        |                                      |
| `dbNSFP.conservationScores`  | object |                        |         |        |                                      |
| `dbNSFP.conservationScores.gerp`  | object |                        |         |        |                                      |
| `dbNSFP.conservationScores.gerp.prediction`  | text |                        |         |        |                                      |
| `dbNSFP.conservationScores.gerp.nr`  | float |                        |         |        |                                      |
| `dbNSFP.conservationScores.gerp.rs`  | float |                        |         |        |                                      |
| `dbNSFP.conservationScores.gerp.rsRankscore`  | float |                        |         |        |                                      |
| `dbNSFP.conservationScores.gerp.category`  | text |                        |         |        |                                      |

* conservationScores
* metaScores
* individualPredictions
* transcriptList 
    - metaScores
    - individualPredictions

transcript에 따라 다른 것들은 transcriptList에 넣어 두었는데,
1단계에 넣고 transcript를 지정해서 넣어야 하지 않을까? 한다.

* metaScores
    - metaLR
    - metaSVM
    - metaRNN
        - 0
            - transcript: ENST000000376592
            - category: Benign
            - prediction: Tolerated
            - score: 0.0016527474
            - rankscore: 0.0002
    - revel