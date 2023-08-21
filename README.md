<p align="center">

  <h1> 법률 조언 웹 서비스 ‘LawBot’ </h1>

  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Apache_Airflow-018CEE?style=flat&logo=Apache Airflow&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=Node.js&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Express-20c997?style=flate&logo=Express&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React-0088cc?style=flat&logo=React&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat&logo=Tailwind CSS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=flat&logo=Amazon-AWS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Python-3776AB?style=square&logo=Python&logoColor=white"/>&nbsp;[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Models%20on%20Hub-yellow)](https://huggingface.co/models?filter=keytotext)&nbsp;[![FastAPI](https://img.shields.io/badge/-FastAPI-red?logo=fastapi&labelColor=white)](https://github.com/gagan3012/keytotext#api)

</p>

<img width="1680" alt="Screenshot 2023-07-31 at 11 27 53 AM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/f9133ea0-ac5f-4937-a4f9-06a45932fdaa">

<br>

>LawBot은  유사 판례 및 법률 조항과 함께 가벼운 법률 상담 서비스를 제공합니다. LLM 모델의 기학습된 방대한 정보와 더불어 fine-tuning에 사용한 법률 지식을 사용하여 다양하고 특수한 상황에 유연하게 대응하여 답변을 생성할 수 있으며, 유사도 기반의 AI 모델을 이용하여 관련된 내용에 대한 유사 판례를 제공합니다. 

<br>

🖥 **[LawBot 웹서비스 체험하기](http://yoonseul.link)**

**※ 본 웹 서비스는 포스트 세션 종료일인 2023년 8월 18일까지만 이용하실 수 있으니 참고바랍니다. 종료일까지 서비스 고도화 및 성능 개선 작업이 이루어질 예정입니다.**

<br>

## ⌘ Project BackGround

### 기획 의도 및 기대효과 

<img width="1407" alt="Screenshot 2023-07-31 at 11 36 29 AM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/04b09ea4-af5a-41b2-be34-8eff23abfd15">

<br>

* **`배경`** : 국제적으로 리걸 테크 산업은 매우 빠르게 발전하고 있으며, 국내에서도 관련 서비스 수요가 꾸준히 증가하고 있습니다. 그러나 법률 용어나 법률 문장은 해석하기 어려워 일반인들에게 이해도는 낮은 편이며, 관련 정보를 얻기 위해서는 많은 비용이 필요합니다. 

* **`목표`**: 윤슬 팀은 이러한 상황을 해결하기 위해 법률 상황에 대해 이해하기 쉬운 가이드라인을 제시하고, 관련된 유사 판례 및 법률 조항을 제공함으로써 법의 장벽을 낮출 수 있는 가벼운 법률 상담 서비스를 제공하고자 합니다.

<br>

### LawBot 서비스의 차별점

- 기존의 주류 Legal Tech 서비스는 **변호사를 매칭시켜주거나 여전히 어려운 법률조항 및 판례에 대한 직접적인 검색**만을 제공합니다. LawBot은 이와 다르게 AI 모델을 이용하여 법적 분쟁 상황에 대한 유사판례를 찾아주고, 빠른 시간 내에 가벼운 가이드라인을 직접 생성해서 유저에게 제공한다는 점에서 차별점을 가지고 있습니다. 

<br>

## ⚙️ Use Case

![예시-케이스](https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/03d80449-819c-4c63-9c1c-6e0492230ba8)



>1. 웹 서버 접속
>2. 메시지 프롬프트 창에 자신이 처한 법적 분쟁 상황 및 연관된 질문 입력 
>3. AI 모델이 상황 맥락을 이해하여 가이드라인을 메시지 형태로 제공
>4. 우측 사이드바에서 사용자가 입력한 상황과 비슷한 최대 3가지의 유사 판례 제공
>5. 링크를 통해 법 조항 등 관련된 법령 정보를 직접 확인 가능 

<br>


## 🧑🏻‍💻 Team Introduction & Members 

### 💬 팀 소개
>**조화와 지속 가능한 성장을 추구하는 팀 `윤슬`입니다!**<br><br>**팀 개개인 모두 주어진 위치에 상관없이 모든 일에 `오너십`을 가지고 `적극적으로 참여`하는 것을 최우선으로 생각하였습니다. 좋은 동료가 되기 위해 치열하게 고민하고, 학습하고, 성장하고 있습니다.**

<br>

### 👨🏼‍💻 Members
강민재|김주원|김태민|신혁준|윤상원|
:-:|:-:|:-:|:-:|:-:
<img src='https://avatars.githubusercontent.com/u/39152134?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/81630351?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/96530685?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/96534680?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/38793142?v=4' height=130 width=130></img>|
<a href="https://github.com/mjk0618" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/Kim-Ju-won" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/taemin6697" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/jun048098" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/SangwonYoon" target="_blank"><img src="https://img.shields.io/badge/GitHub-black.svg?&style=round&logo=github"/></a>
<a href="mailto:kminjae618@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:uomnf97@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:taemin6697@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:jun048098@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:iandr0805@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|

<br>

### 👨🏼‍💻 역할 분담
<img width="1504" alt="Screenshot 2023-08-20 at 11 21 39 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/dd0e497a-e2a4-432b-b501-5769453c08ef">

<br>

## 🗓️ Project TimeLine
- 초기에 핵심 기능을 우선적으로 개발하였고, 그 후 팀원들의 의견을 수렴하여 지속적으로 발전시키는 애자일적인 접근 방식을 적용하여 서비스 고도화 작업을 진행했습니다.

<img width="1589" alt="Screenshot 2023-07-31 at 11 54 44 AM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/d1ba5cf2-45a6-4c23-8816-83bc318f6df0">

<br>

## ⌘ Service Archiecture
<img width="1653" alt="Screenshot 2023-07-31 at 12 03 17 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/5102884e-3c6f-44b8-b606-0af61dcd497e">

<br>

>네이버 커넥트 재단으로부터 제공받은 V100 서버 4대를 모두 활용하기 위해 첫 설계 때부터 **서비스 확장이 쉬운 마이크로 서비스 아키텍처**를 고려했습니다. 또한 서비스 간의 상호 의존도를 낮춰 서버에 장애가 발생할 경우 전체 서비스가 중단되는 것을 방지하고자 하여 위와 같이 웹 서버, 모델 서버를 독립적으로 분리하고 API를 통해 서로 통신하는 구조로 설계했습니다. 이를 통해 한 대의 V100 서버에 장애가 발생하더라도 나머지 서비스는 전혀 영향을 받지 않고 서비스를 제공할 수 있습니다.

<br>

- 아래는 구현한 내용이고 관련된 내용을 확인하실 수 있는 링크입니다. 각 링크에서 왜 해당 기능을 구현을 했으며, 어떤 것들을 중점적으로 고려해서 개발했는지 살펴보실 수 있습니다. 

  - 🛠️ [CI 파이프라인 구축](https://uomnf97.notion.site/CI-f687f03b192f49fa80d451f8850a03f6?pvs=4)
  - ✍🏻 [로드 밸런싱 적용](https://uomnf97.notion.site/96f697aab756407aadbe51582a0a68d4?pvs=4)
  - ✍🏻 [Airflow를 이용한 모델 학습 파이프라인](https://uomnf97.notion.site/64a55c1e1f4a4ff985343a97b224a101?pvs=4)
  - 🛠️ [Auto Scaling을 통한 Failover](https://uomnf97.notion.site/Auto-Scaling-Failover-fa0ab424dcda44739ababe1eb719a106?pvs=4)

<br>

## 💿 Data
<img width="1208" alt="Screenshot 2023-07-31 at 12 30 46 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/e9b220b5-ba51-489f-aa5e-c6c98cfd3eff">

- 데이터는 위와 같이 단계별로 나누어 목표를 설정하고 데이터를 탐색, 수집, EDA 및 전처리, 생성모델을 통한 증강을 하여 학습데이터 셋을 구축하였습니다. 

<br>

<img width="1552" alt="Screenshot 2023-07-31 at 12 31 04 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/05c47fc3-e2ff-4997-9396-effcbf966a7b">

- 데이터 파이프라인을 도식화한 순환 DMOps 구조도는 위와 같습니다. 

<br>


### 1️⃣ 법률 QA 데이터

| 데이터셋 이름 | 데이터 개수 | 출처 |
| :---: | :---: | :---: |
| easylaw_kr | 2,195 | https://huggingface.co/datasets/juicyjung/easylaw_kr |
| LegalQA | 1,830 | https://github.com/haven-jeon/LegalQA |
|대한법률구조공단의 법률상담사례 데이터|9994|https://www.klac.or.kr/legalinfo/counsel.do|
|대한법률구조공단의 국내 사이버상담 데이터|2463|https://www.klac.or.kr/legalstruct/cyberConsultation.do|
|Open AI GPT증강|8666| - |

<br>

### 2️⃣ 판례 데이터

| 데이터셋 이름 | 데이터 개수 | 출처 |
| :---: | :---: | :---: |
| 법률/규정 (판결서, 약관 등) 텍스트 분석 데이터 |77382| https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=580 |

<br>

- 데이터 전처리, EDA, 증강에 대한 자세한 내용은 아래에서 확인하실 수 있습니다.
  
  - 💿[데이터 수집](https://uomnf97.notion.site/a5f4628cdc7b4ce3928ce626c727ff32?pvs=4)
  - 📈[EDA 및 전처리](https://uomnf97.notion.site/EDA-b53d75aaa7574ea586cbd6cdbd5c755a?pvs=4)
  - 🛠️[생성모델을 통한 데이터 증강](https://uomnf97.notion.site/5e8e9ecc27694d7497fbad68f72136c0?pvs=4)

<br>

## 📊 Model

### Overview
<img width="1537" alt="Screenshot 2023-07-31 at 12 17 55 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/b115fc5b-093d-4955-848f-957a34f94e3f">

<br>

> 먼저 유저가 입력하면 모델에서는 Question Filtering 모델을 통해 법률적인 질문인지 아닌지 구분하게 됩니다. 법률적인 질문이라면 Similar Precedent Mode과 Law LLM Model 통해 유사판례와 법률적인 조언을 생성합니다.

<br>

### 1️⃣ Question Filtering Model 
<img width="1516" alt="Screenshot 2023-07-31 at 12 47 58 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/582ed391-bdea-4c08-b942-6cf8eab163b8">

<br>

### 2️⃣ Similar Precedent Model 
<img width="1516" alt="Screenshot 2023-07-31 at 12 48 08 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/dd67685f-5682-4bc7-9104-170de86fb37a">
 
<br>

### 3️⃣LLM 모델 

<img width="1566" alt="Screenshot 2023-07-31 at 12 48 28 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/c7e22058-7901-40f8-b0c8-e7d72564d521">


- 구축한 모델 리스트(활용한 데이터 + Backbone 모델)<br><img width="1573" alt="Screenshot 2023-08-21 at 5 35 27 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/873b6103-8ed9-4696-8072-3a2bcd13c6f1">

#### 평가지표 
- LLM 모델은 명확한 평가지표가 없어 직접 평가지표를 만들어 평가했습니다. 평가지표를 만들 때 고려했던 부분은 도메인 특성상 법률적인 정확도가 중요하므로 법률적인 정확도와 언어의 자연스러움 두가지 모두 평가할 수 있도록 metric을 제작하여 평가했습니다. 

<br>

**[ Dialogue Evaluation Metric ]**

- Kullm 모델의 Dialogue Evaluation Metric 평가요소를 도메인에 맞게 변형하여 활용하였고, 해당 지표를 직접 변호사에게 의뢰하여 답변을 평가했습니다. 추가로 모든 모델들은 모델 A, B, C ... 등 모델 이름을 가리는 블라인드 평가를 진행했으며, 명확한 평가지표를 만들기 위해 ChatGPT, BARD 모델과 함께 평가를 진행하였습니다. 최종적으로 저희가 구축한 **kfkas/legal-llama-2-ko-7b-Chat** 모델이 가장 좋은 성능을 보였습니다. 

<img width="1584" alt="Screenshot 2023-07-31 at 12 56 06 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/9cc5938c-2559-42ac-a478-78554a5befc6">

<br>

**[ Perplexity ]**
- 얼마나 생성모델이 법률적인 용어를 생성해내는지 평가하기 위해 Perplexity 평가지표를 활용하였습니다. 낮을 수록 좋은 값을 나타내는 metric인데, 크롤링 데이터와 탐색한 데이터로 학습한 모델들이 대체로 높은 성능을 나타내는 경향을 보였습니다. 
<br><img width="613" alt="Screenshot 2023-07-31 at 12 58 26 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/94fce5cd-dfea-4a09-b251-cdcaba5d9800">



## 💻 Getting Started

> 아래 Readme를 통해 직접 프로젝트를 실행할 수 있으며, 구현된 코드를 살펴볼 수 있습니다.  

### 📊 Model
- [Model](model) / [README.md](model/README.md)

### 💽 Data
- [Data Pipeline](data_pipeline) / [README.md](data_pipeline/README.md)

### 🎨 Frontend
- [Frontend](frontend) / [README.md](frontend/README.md)

### 💻 Backend
- [Backend](backend) / [README.md](backend/README.md)

<br>

## 📚 Further Information

### 1️⃣ 개발 스택 및 개발 환경
<img width="1516" alt="Screenshot 2023-07-31 at 12 44 34 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/f62c2c58-a755-47e0-96e9-9859feafc738">

<br>

### 2️⃣ 협업 Tools

- 노션 :
  - Kanban Board를 이용하여 체계적으로 To do List 관리
  - 노션 협업기구를 활용해 회의 및 기록 체계화å<img width="1579" alt="Screenshot 2023-07-31 at 12 38 10 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/ecc791e2-6001-44c1-bdc1-3fb3d4c61f39">

- GitHub : 
  - GitHub Flow를 이용하여 브랜치 전략 수립
  - PR Template, Issue Template을 이용하여 체계젹으로 관리.
  - Ground Rule을 정해 모두 일관된 Commit convention을 유지<img width="1422" alt="Screenshot 2023-07-31 at 12 38 50 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/2fdfce62-6c07-4e36-8312-1588e5204653">

<br>

### 3️⃣ Links : 

- [개발 관련 Notion 링크](https://uomnf97.notion.site/NLP-08-LawBot-b2dfef92f666458583d6b459af53aa66?pvs=4)
- [Youtube 발표 영상](https://www.youtube.com/watch?v=fgboxtWM4B4)
- [발표 영상 자료](https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/files/12394029/NLP_08_.LawBot.pdf)

