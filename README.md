# 법률 조언 웹 서비스 ‘LawBot’

<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=PyTorch&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Apache_Airflow-018CEE?style=flat-square&logo=Apache Airflow&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=Node.js&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Express-20c997?style=flat-square&logo=Express&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React-0088cc?style=flat-square&logo=React&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat-square&logo=Tailwind CSS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=flat-square&logo=Amazon-AWS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=TailwindCSSr&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/pandas-%23150458?style=flat-square&logo=pandas&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>&nbsp;[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Models%20on%20Hub-yellow)](https://huggingface.co/models?filter=keytotext)&nbsp;[![API Call](https://img.shields.io/badge/-FastAPI-red?logo=fastapi&labelColor=white)](https://github.com/gagan3012/keytotext#api)

<img width="1680" alt="Screenshot 2023-07-31 at 11 27 53 AM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/f9133ea0-ac5f-4937-a4f9-06a45932fdaa">

 
>Lawbot은  유사판례, 법률 조항과 함께 가벼운 법률 상담 서비스를 제공합니다. LLM 모델의 기학습된 방대한 정보와 더불어 fine-tuning에 사용한 법률 지식을 사용하여 다양하고 특수한 상황에 유연하게 대응하여 답변을 생성할 수 있으며, 유사도 기반의 AI 모델을 이용하여 관련된 내용에 대한 유사 판례를 제공합니다. 

🖥 **[LawBot 웹서비스 체험하기](http://yoonseul.link)**

**※ 본 웹 서비스는 8월 말까지 계속 배포예정이며, 추가적인 서비스 고도화 및 성능 개선 작업이 이루어질 예정입니다..**

## Projects BackGround

### 기획 의도 및 기대효과 

<img width="1407" alt="Screenshot 2023-07-31 at 11 36 29 AM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/04b09ea4-af5a-41b2-be34-8eff23abfd15">

* **`배경`** : 국제적으로 리걸 테크 산업은 매우 빠르게 발전하고 있으며, 국내에서도 관련 서비스 수요가 꾸준히 증가하고 있습니다. 일반인들의 그러나 법률 용어나 문장은 해석하기 어려워 일반인들에게 이해도는 낮은 편이며, 관련 정보를 얻기 위해서는 많은 비용이 필요합니다. 

* **`목표`**: 따라서 윤슬팀은 이러한 상황을 해결하기위해 법률 상황에 대해 이해하기 쉬운 가이드라인을 제시하고,관련된 유사판례 및 법률 조항을 제공함으로써 법의 장벽을 낮출 수 있는 가벼운 법률 상담 서비스를 제공하고자 합니다.

<br/>

### 기존 Legal Tech 서비스와의 차별점

- 기존의 Legal Tech 서비스는 **기존의 변호사를 매칭시켜주거나 여전히 어려운 법률조항 및 판례에 대한 직접적인 검색**만을 제공하는 서비스와 다르게 AI 모델을 이용하여  법률적인 분쟁 상황에 대한 유사판례를 찾아주고,가벼운 가이드라인을 직접 생성해서 빠른 시간내에 User에게 제공한다는 점에서 차이점이 있습니다. 

<br/>

## ⚙️ Use Case

![예시-케이스](https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/03d80449-819c-4c63-9c1c-6e0492230ba8)

>1. 웹 서버 접속
>2. 메시지 프롬프트 창에 자신이 처한 법률적인 상황 입력 
>3. AI 모델이 상황 맥락을 이해하여 법적인 가이드라인을 메시지 형태로 제공
>4. 우측 사이드바에서 사용자가 입력한 상황과 비슷한 최대 3가지의 유사 판례 제공
>5. 링크를 통해 법률 정보를 직접 확인 가능 

## 🧑🏻‍💻 Team Introduction & Members 

> Team name : 윤슬 [ NLP 08조 ] 
## 팀 소개
**조화와 지속 가능한 성장을 추구하는 `팀 윤슬`입니다!**

**팀 개개인 모두 주어진 위치에 상관없이 모든 일에 `오너십`을 가지고 `적극적으로 참여`하는 것을 최우선으로 생각하였습니다. 좋은 동료가 되기 위해 치열하게 고민하고, 학습하고, 성장하고 있습니다.**

## 👨🏼‍💻 Members
강민재|김주원|김태민|신혁준|윤상원|
:-:|:-:|:-:|:-:|:-:
<img src='https://avatars.githubusercontent.com/u/39152134?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/81630351?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/96530685?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/96534680?v=4' height=130 width=130></img>|<img src='https://avatars.githubusercontent.com/u/38793142?v=4' height=130 width=130></img>|
<a href="https://github.com/mjk0618" target="_blank"><img src="https://img.shields.io/badge/Github-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/Kim-Ju-won" target="_blank"><img src="https://img.shields.io/badge/Github-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/taemin6697" target="_blank"><img src="https://img.shields.io/badge/Github-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/jun048098" target="_blank"><img src="https://img.shields.io/badge/Github-black.svg?&style=round&logo=github"/></a>|<a href="https://github.com/SangwonYoon" target="_blank"><img src="https://img.shields.io/badge/Github-black.svg?&style=round&logo=github"/></a>
<a href="mailto:kminjae618@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:uomnf97@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:taemin6697@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:jun048098@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|<a href="mailto:iandr0805@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-EA4335?style&logo=Gmail&logoColor=white"/></a>|

### 👨🏼‍💻 역할 분담
<img width="1498" alt="Screenshot 2023-07-31 at 11 54 33 AM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/556d4b1c-49be-4386-8b75-b5cebf1ad400">

### 🗓️ Project TimeLine
- 최소한의 기능을 우선적으로 구현하고, 이후 팀원들의 피드백을 통해 개선해나가는 애자일 방식으로 개발했습니다. 

<img width="1589" alt="Screenshot 2023-07-31 at 11 54 44 AM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/d1ba5cf2-45a6-4c23-8816-83bc318f6df0">


## ⌘ 서비스 Archiecture
<img width="1653" alt="Screenshot 2023-07-31 at 12 03 17 PM" src="https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08/assets/81630351/5102884e-3c6f-44b8-b606-0af61dcd497e">

>네이버 커넥트 재단으로부터 제공받은 V100 서버 4대를 모두 활용하기 위해 첫 설계 때부터 **서비스 확장이 쉬운 마이크로 서비스 아키텍처**를 고려했습니다. 또한 서비스 간의 상호 의존도를 낮춰 서버에 장애가 발생할 경우 전체 서비스가 중단되는 것을 방지하고자 하여 위와 같이 웹 서버, 모델 서버를 독립적으로 분리하고 API를 통해 서로 통신하는 구조로 설계했습니다. 이를 통해 한 대의 V100 서버에 장애가 발생하더라도 나머지 서비스는 전혀 영향을 받지 않고 서비스를 제공할 수 있습니다.

- 아래는 구현한 내용이고 관련된 내용을 확인하실 수 있는 링크입니다. 각 링크에서 왜 해당 기능을 구현을 했으며, 어떤 것들을 중점적으로 고려했는지 살펴보실 수 있습니다. 

  - 🛠️ [CI 파이프라인 구축](https://uomnf97.notion.site/CI-f687f03b192f49fa80d451f8850a03f6?pvs=4)
  - ✍🏻 [로드 밸런싱 적용](https://uomnf97.notion.site/96f697aab756407aadbe51582a0a68d4?pvs=4)
  - ✍🏻 [Airflow를 이용한 모델 학습 파이프라인](https://uomnf97.notion.site/64a55c1e1f4a4ff985343a97b224a101?pvs=4)
  - 🛠️ [Auto Scaling을 통한 Failover](https://uomnf97.notion.site/Auto-Scaling-Failover-fa0ab424dcda44739ababe1eb719a106?pvs=4)

## 모델
- 

## 데이터


💻 Getting Started

---

> 아래 Readme를 통해 직접 프로젝트를 실행할 수 있으며, 구현된 코드를 살펴볼 수 있습니다.  

### 📊 Model
- [Model](model) / [README.md](model/README.md)

### 💽 Data
- [Data Pipeline](data_pipeline) / [README.md](data_pipeline/README.md)

### 🎨 Frontend
- [Frontend](frontend) / [README.md](frontend/README.md)

### 💻 Backend
- [Backend](backend) / [README.md](backend/README.md)

---

## Further Information

### 개발 스택 


### 협업 Tools

- 노션 :
  - K

- GitHub




