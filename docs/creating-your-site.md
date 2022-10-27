---
template: overrides/main.html
---

# Creating your site

After you've [installed][1] Material for MkDocs, you can bootstrap your project 
documentation using the `mkdocs` executable. Go to the directory where you want
your project to be located and enter:

```
mkdocs new .
```

Alternatively, if you're running Material for MkDocs from within Docker, use:

=== "Unix"

    ```
    docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material new .
    ```

=== "Windows"

    ```
    docker run --rm -it -v "%cd%":/docs squidfunk/mkdocs-material new .
    ```

This will create the following structure:

```
.
├─ docs/
│  └─ index.md
└─ mkdocs.yml
```

  [1]: getting-started.md

## 기술적 관점에서의 개요

seqr is a web-based tool for rare disease genomics. 
This repository contains code that underlies the [Broad seqr instance] and other seqr deployments. 
To check for any active incidents occuring on the Broad seqr instance, check [here]

Consists of the following components:

  * `postgres` - SQL database used by seqr to store project metadata and user-generated content such as variant notes, etc.
  * `elasticsearch` - NoSQL database used to store variant callsets.
  * `redis` - in-memory cache used to speed up request handling.
  * `seqr` - the main client-server application built using react.js, python and django.
  * `pipeline-runner` - optional container for running hail pipelines to annotate and load new datasets into elasticsearch. If seqr is hosted on google cloud (GKE or GCE), Dataproc spark clusters can be used instead.
  * `kibana` - optional dashboard and visual interface for elasticsearch.

You can use our API to access NGeneBio API endpoints,
which can get information on various database query results.
This page describes the reference for variant query web service. 
It’s also recommended to try it live on our [interactive API page].

  [Broad seqr instance]: http://seqr.broadinstitute.org/
  [here]: https://github.com/broadinstitute/seqr/blob/master/INCIDENTS.md
  [interactive API page]: http://192.168.1.14:9000/


## Service endpoint

  ``` GET httpe://example.com/hg19/all-database ```

## Authentication

Kitten expects for the API key to be included in all API requests to the server
in a header that look like the following: `Authorization: meowmeowmeow`

!!! info "You must replace meowmeowmeow with your personal API key."

  [developer portal]: http://example.com/developers

To authorize, use this code:

=== "shell"

    ``` sh
    # With shell, you can just pass the correct header with each request
    curl "api_endpoint_here" \
    -H "Authorization: meowmeowmeow"
    ```

=== "python"

    ``` python
    import kittn

    api = kittn.authorize('meowmeowmeow') 
    ```

Make sure to replace meowmeowmeow with your API key.

## Query parameters

| Parameter  | Required  | Type  | Description                                                                    |
| :--------------- | :--------------| :------- | :----------------------------------------------------------------------------- |
| hgvsg            | true           | String   | HGVS.g nomemclature   ex) chr17:g.41244936G>A                                  |

The above command returns JSON structred like this:

## Query syntax

## Returned object

=== "Example"

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
    }
    ```

## Variant query service

This page describes the reference for MyVariant.info variant query web service. It’s also recommended to try it live on our interactive API page.

## API 조회 결과 Variant object

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

| Field      | Type   | 
| ---------  | -------|
| `hg19Chr`  | text 
| `hg19Pos`  | integer |
| `hg38Chr`  | text |
| `hg38Pos`  | integer |
| `ref`  | text |
| `alt`  | text |
| `cytoBand`  | text |
| `hg19Key`  | text |
| `hg38Key`  | text |
| `dbSNP`  | object |
| `kova`  | object |
| `dbNSFP`  | object |
| `dbscSNV`  | object |
| `clinVar`  | object |
| `gnomadExomes`  | object |
| `gnomadGenomes`  | object |
| `cancerHotspots`  | object |
| `koexid`  | object |
| `krgdb`  | object |
| `vep`  | object |

  [^2]:
    search의 q=xxx인 경우 기본 검색되는 필드 (cadd.gene.genename, clingen.caid, clinvar.gene.symbole, clinvar.hgvs.coding  )

## API 조회 결과 Variant object

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


## 시작하기

최근 comprehensive genomic profiling을 사용한 대규모 코호트 연구들에 따르면 90%가 유용한 alteration 을 가지고 있다고 보고되고 있다[^1]. 
엔젠바이오는 연구자들을 돕기 위해 323개의 암관련 유전자 (225 coding exon, 98 hotspot cover)를 분석하는 ONCOaccuPanel을 제공한다. 
small nucleotide variants(SNVs), insertions/deletions(indels), copy-number variations(CNVs), splice variants, fusions과 함께 
최근 다수의 genomic loci 분석을 기반으로 하는 tumor mutational burden(TMB) and microsatellite instability(MSI) 분석을 제공한다.

  [^1]:
    Peter Priestley, Jonathan Baber, Martijn P Lolkema, et al. "Pan-cancer whole-genome analyses of metastatic solid tumours". In: Nature (Oct. 2019), pp. 1–24 (cit. on p. 1).

## 사고 발생
### 지해 배터리실
지난 15일 오후 3시 33분 발생한 SK C&C 데이터센터 화재. 지하 3층 배터리실에서 시작된 불은 오후 11시46분 완전진압됐고, 서버실 전원은 다음날 00시를 넘겨 차례로 들어오기 시작했다. 과학기술정보통신부에 따르면 사고 발생 나흘째인 18일 오전 9시 기준 전원 공급은 95%가량 이뤄졌다.

:octicons-file-code-24: Source ·
:octicons-unlock-24: Feature flag ·
:octicons-beaker-24: Experimental ·
:octicons-heart-fill-24:{ .mdx-heart } Insiders only

When _search suggestions_ are enabled, the search will display the likeliest
completion for the last word, saving the user many key strokes by :material-share-variant: accepting the
suggestion with the ++arrow-right++ key.

### 복구 진행중
카카오의 서비스들은 아직도 완전히 복구되지 못했지만, 네이버는 달랐다. 화재 발생 4시간여 만에 일부 장애가 발생했던 서비스들이 정상화된 것이다. 3만 2,000여 대의 서버를 맡겼던 카카오보다 적은 수이지만, 네이버 역시 2~3만 대의 서버를 SK 판교센터에 두고 전체 트래픽의 10%를 처리하고 있었다. 그런데 어떻게 화재가 진압되기도 전에, 전원 공급이 재개되기도 전에, 서비스를 정상화할 수 있었을까.

## 자체 센터 ‘각’ 설립 주도
### 자가 데이터 센터

Operating systems:
:fontawesome-brands-apple:
:fontawesome-brands-windows:
:fontawesome-brands-linux:

!!! error "분석 가능한 암종 (tumor type)"

    ``` sh
    mkdocs serve
    # => INFO    -  Building documentation...
    # => ERROR   -  Config value: 'theme'. Error: Unrecognised theme 'material'.
    # => ...
    # => ConfigurationError: Aborted with 1 Configuration Errors!
    ```
    
서비스를 하는 조직은 규모가 커지고 확장되면서 다양한 제품을 만들어가게 됩니다. 
시간이 지나면서 서비스에 대한 기획서도 작성하게 되고 개발과 관련된 다양한 문서들도 생깁니다. 
기획서를 위한 디자인 툴과 개발을 위한 hand-off 소프트웨어도 트렌드에 따라 다양하게 사용하는데
google drive ppt, whimsical, zeplin, miro, figma 등 많은 도구들과 또한 개발 관련 문서 역시 confluence와 notion 등이 있습니다.

어떤 프로젝트가 진행된 후 히스토리는 당시 참여했던 개발자나 기획자의 기억에 의존하는 경우가 종종 생깁니다. 
이후 개발 히스토리를 파악하려 할 때 문서라도 있으면 다행이지만 그렇지 않은 경우도 있습니다. 
중앙집권식으로 관리되지 않고 프로젝트 참여자에 의해 각각 만들어진 문서들은 해당 참여자가 퇴사하면 문맥을 파악하기 어려워집니다.

### 분석 가능 Cancer Type
박원기 대표는 2009년 당시 NHN의 인프라서비스본부장으로 입사해 네이버의 IT인프라 서비스 전반을 책임지기 시작했다. 네이버가 2013년, 국내 IT 기업 가운데 처음으로 자체 데이터센터인 ‘각’을 만들 때, 이를 주도했다. 춘천 구봉산 자락에 만든 ‘각’은 네이버 서비스의 대부분을 담당하고 있다. 네이버는 ‘각’에 이어 두 번째 데이터센터인 ‘각 세종’을 2023년 2월 완공을 목표로 세종시 집현동 산 163번지 도시첨단산업단지에 만들고 있다. ‘각’이 네이버 서비스를 위한 서버 자원관리차원이었다면, ‘각 세종’은 글로벌 클라우드 사업 확장의 전초기지가 될 전망이다. ‘각 세종’은 최소 10만대 이상의 서버를 구축할 수 있어 △빅데이터 △인공지능(AI)△로봇 등 첨단 산업의 컴퓨팅 환경을 대규모로 확장할 것으로 보인다.

Material for MkDocs provides the following template blocks:

| Block name        | Wrapped contents                                |
|:------------------|:------------------------------------------------|
| `analytics`       | Wraps the Google Analytics integration          |
| `announce`        | Wraps the announcement bar                      |
| `config`          | Wraps the JavaScript application config         |
| `content`         | Wraps the main content                          |
| `disqus`          | Wraps the Disqus integration                    |
| `extracopyright`  | Empty block to add custom copyright information |
| `extrahead`       | Empty block to add custom meta tags             |


  * :fontawesome-brands-behance: – `fontawesome/brands/behance`
  * :fontawesome-brands-docker: – `fontawesome/brands/docker`
  * :fontawesome-brands-github: – `fontawesome/brands/github`
  * :fontawesome-brands-instagram: – `fontawesome/brands/instagram`

## ‘각’에 3,000억 이상 들어…이해진 GIO가 공감해줘
### 네이버 각
10년 전에 자체 데이터센터를 만들자고 했을 때 반대는 없었을까. 애플, 구글, 메타, 아마존, MS 같은 글로벌 빅테크들은 데이터센터, 재난복구 등에 100조 원 넘게 투자한다지만, 덩치가 작은 국내 IT기업으로선 쉽지 않은 결정이다. 네이버가 ‘각’을 지었을 때 땅값을 빼고 3000~4000억 원 정도 들었다고 한다.

1. Go to your Google Analytics __admin settings__
2. Select the property for the respective tracking code
3. Go to the __view settings__ tab.
4. Scroll down and enable __site search settings__
5. Set the __query parameter__ to `q`.

``` java
import java.util.Scanner;

public class HelloWorld {

    public static void main(String[] args) {

        // Creates a reader instance which takes
        // input from standard input - keyboard
        Scanner reader = new Scanner(System.in);
        System.out.print("Enter a number: ");

        // nextInt() reads the next integer from the keyboard
        int number = reader.nextInt();

        // println() prints the following line to the output screen
        System.out.println("You entered: " + number);
    }
}
```

### 배터리 없음
그런데 ‘각’에는 이번 화재사고에서 발화가 시작된 화재에 취약한 배터리가 없다. 박 대표는 “각에는 배터리 없이 전기를 공급하는 다이나믹 UPS(무정전전원공급장치)를 썼다”면서 “전원에 장애가 있을 때 발전기가 자동으로 킥오프되는 방식으로 구축했다. 돈은 많이 든다”고 했다.

### 비용
비용 문제로 데이터센터 건립에 내부 반대는 없었을까. 그는 “뭐 그랬다”면서 “우리 GIO(이해진 글로벌투자책임자)가 굉장히 많이 공감해줬다”고 전했다.

### 이해진
이해진 GIO는 자국 데이터를 보호하겠다는 의지가 남다른 것으로 전해진다. 은둔의 경영자로 꼽히지만, 지난 6월 20일 두번 째 데이터센터 ‘각 세종’ 상량식에 참석해 직원들을 격려했다. 이 GIO는 2019년 한국사회학회·한국경영학회 공동 심포지엄에 참석해 “4차 산업혁명 시대에 데이터를 뺏기는 건 매출을 뺏기는 것과 같다”고 힘줘 말하기도 했다.

## 위험을 외부에 맡긴 카카오와 달라

자체 센터 ‘각’을 메인센터로 해서 6개 데이터센터에 데이터를 분산한 덕분에, 네이버는 데이터센터 화재라는 큰 위기를 넘길 수 있었다. 반면, 카카오는 남의 데이터센터를 메인센터로 빌려 쓰는 바람에 기본적인 위험을 SK에 의존한 셈이 됐다.

박원기 대표는 데이터 보호와 재난대비를 위해 제일 중요한 것은 따로 있다고 했다. 그는 “서비스 로직과 비즈니스 로직을 분산해 제공할 수 있도록 하는 서비스 아키텍처(설계)가 중요하다”면서 “이런 상황이 발생했을 때 여러 센터에서 서비스를 제공할 수 있어야 한다는 의미”라고 했다.

이 같은 재난대비 운영 기술과 경험을 쌓기 위해 네이버는 BCP(Business Continuity Plan, 업무연속성계획)를 만들어 모의훈련을 한다고 했다. 박 대표는 “가뭄이든, 화재든, 전쟁이든, 팬데믹으로 사람이 운영하기 어려운 상황이든 시나리오별로 BCP를 만들어 1년에 두 번씩 실제 모의 훈련을 한다”고 전했다.

Material for MkDocs is a theme for [우리나라 대한민국][1], a static site generator geared
towards (technical) project documentation. If you're familiar with Python, you
can install Material for MkDocs with [`pip를 사용하기`][2], the Python package manager.
If not, we recommended using [`docker 도커`][3].

In case you're running into problems, consult the [troubleshooting][4] section.

  [1]: https://www.mkdocs.org
  [2]: #with-pip
  [3]: #with-docker
  [4]: troubleshooting.md

## 설치하기

### pip를 이용한 설치

Material for MkDocs can be installed with `pip`:

```
pip install mkdocs-material
```

This will automatically install compatible versions of all dependencies:
[MkDocs][1], [Markdown][5], [Pygments][6] and [Python Markdown Extensions][7].
Material for MkDocs always strives to support the latest versions, so there's
no need to install those packages separately.

  [5]: https://python-markdown.github.io/
  [6]: https://pygments.org/
  [7]: https://facelessuser.github.io/pymdown-extensions/

### with docker

The official [Docker image][8] is a great way to get up and running in a few
minutes, as it comes with all dependencies pre-installed. Pull the image for the 
`latest` version with:

```
docker pull squidfunk/mkdocs-material
```

The `mkdocs` executable is provided as an entry point and `serve` is the 
default command. If you're not familiar with Docker don't worry, we have you
covered in the following sections.

The following plugins are bundled with the Docker image:

- [mkdocs-minify-plugin][9]
- [mkdocs-redirects][10]

  [8]: https://hub.docker.com/r/squidfunk/mkdocs-material/
  [9]: https://github.com/byrnereese/mkdocs-minify-plugin
  [10]: https://github.com/datarobot/mkdocs-redirects

??? question "도커 이미지에 plugins 추가 방법?"

    Material for MkDocs bundles useful and common plugins while trying not to
    blow up the size of the official image. If the plugin you want to use is
    not included, create a new `Dockerfile` and extend the official Docker image
    with your custom installation routine:

    ``` Dockerfile
    FROM squidfunk/mkdocs-material
    RUN pip install ...
    ```

    Next, you can build the image with the following command:

    ```
    docker build -t squidfunk/mkdocs-material .
    ```

    The new image can be used exactly like the official image.

### with git

Material for MkDocs can be directly used from [GitHub][11] by cloning the
repository into a subfolder of your project root which might be useful if you
want to use the very latest version:

```
git clone https://github.com/squidfunk/mkdocs-material.git
```

The theme will reside in the folder `mkdocs-material/material`. When cloning
from `git`, you must install all required dependencies yourself:

```
pip install -r mkdocs-material/requirements.txt
```

  [11]: https://github.com/squidfunk/mkdocs-material


## Configuration

### Minimal configuration

Simply add the following lines to `mkdocs.yml` to enable the theme. Note that
since there are several [installation methods][2], configuration might be
slightly different:

=== "pip, docker"

    ``` yaml
    theme:
      name: material
    ```

=== "git"

    ``` yaml
    theme:
      name: null
      custom_dir: mkdocs-material/material

      # 404 page
      static_templates:
        - 404.html

      # Necessary for search to work properly
      include_search_page: false
      search_index_only: true

      # Default values, taken from mkdocs_theme.yml
      language: en
      font:
        text: Roboto
        code: Roboto Mono
      favicon: assets/favicon.png
      icon:
        logo: logo
    ```

_If you cloned Material for MkDocs from GitHub, you must list all of the themes'
defaults, because_ [`mkdocs_theme.yml`][3] _is not loaded automatically as
[described in the official documentation][4]._

  [2]: getting-started.md#installation
  [3]: https://github.com/squidfunk/mkdocs-material/blob/master/src/mkdocs_theme.yml
  [4]: https://www.mkdocs.org/user-guide/custom-themes/#creating-a-custom-theme

### Advanced configuration

Material for MkDocs comes with many configuration options. The _setup_ section
explains in great detail how to configure and customize colors, fonts, icons
and much more:

<div class="mdx-columns" markdown="1">

- [Changing the colors][5]
- [Changing the fonts][6]
- [Changing the language][7]
- [Changing the logo and icons][8]
- [Setting up navigation][9]
- [Setting up site search][10]
- [Setting up site analytics][11]
- [Setting up versioning][12]
- [Setting up the header][13]
- [Setting up the footer][14]
- [Adding a git repository][15]
- [Adding a comment system][16]

</div>

  [5]: setup/changing-the-colors.md
  [6]: setup/changing-the-fonts.md
  [7]: setup/changing-the-language.md
  [8]: setup/changing-the-logo-and-icons.md
  [9]: setup/setting-up-navigation.md
  [10]: setup/setting-up-site-search.md
  [11]: setup/setting-up-site-analytics.md
  [12]: setup/setting-up-versioning.md
  [13]: setup/setting-up-the-header.md
  [14]: setup/setting-up-the-footer.md
  [15]: setup/adding-a-git-repository.md
  [16]: setup/adding-a-comment-system.md

## Previewing as you write

MkDocs includes a live preview server, so you can preview your changes as you
write your documentation. The server will automatically rebuild the site upon
saving. Start it with:

```
mkdocs serve
```

If you're running Material for MkDocs from within Docker, use:

=== "Unix"

    ```
    docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
    ```

=== "Windows"

    ```
    docker run --rm -it -p 8000:8000 -v "%cd%":/docs squidfunk/mkdocs-material
    ```

End-to-end workflow of of CE-IVD Oncology Applications by SOPHiA GENETICS™
(Tools and reports will vary depending on product.)

[![CE-IVD Oncology][1]][1]

  [1]: assets/screenshots/sophia.png

## Building your site

When you're finished editing, you can build a static site from your Markdown
files with:

```
mkdocs build
```

The contents of this directory make up your project documentation. There's no
need for operating a database or server, as it is completely self-contained.
The site can be hosted on [GitHub Pages][19], [GitLab Pages][20], a CDN of your
choice or your private web space.

  [19]: publishing-your-site.md#github-pages
  [20]: publishing-your-site.md#gitlab-pages
