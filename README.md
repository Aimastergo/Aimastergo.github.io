# AI+X:DeepLearning Final Project<br/>
<br><br>

## Title
- 국내 표준 소주병 규격에 따른 소주병 분류 (형태, 색)
<br/><br>

## Members
- **전인화** 경영학부 / 2017003290 / ai05024@hanyang.ac.kr
- **백승주** 경영학부 / 2018027283 / baeksj55@hanyang.ac.kr
<br/><br/>

## I. Proposal
- 진로 등 360mL·초록색이라는 소주병 공용 기준을 깬 상품들이 잇따라 출시되면서 소주병 재사용을 위한 협약이 사실상 유명무실화되면서 환경에 악영향을 줄 것이라는 우려도 대두된다.
- 기업의 공병 재사용 효율을 높이고, 환경보호에 도움이 되고자 360ml 소주병을 규격과 색에 따라 분리하는 모델을 만들고자 한다.
<br/><br/>
<br/><br/>

## II. Datasets
### 1. 데이터 선정 및 수집
**1) 수집 데이터 선정** 
- 360ml 소주병 병모양, 색 분류라는 주제에 부합하는 데이터 수집을 위해 수집할 360ml 소주병 종류를 분류
- 소주병 국내 점유율 데이터에 기초하여 3가지 소주병으로 분류 (기존 초록색병 / 진로, 금복주 투명병 / 한라산 투명병)
<br/><br/>

**2) 데이터 수집 : 검색포털 이미지 크롤링**
- 네이버, 구글, bing 3개 검색포털로 부터 이미지 크롤링 * *crawling_n.py 파일 참조*
- 추출한 이미지 3,600여 개 중, 사용 가능한 이미지 1,800여 개 수기 추출
<img src="https://user-images.githubusercontent.com/117564613/204191315-013382c4-9ec4-48f3-9793-6bedc74a4431.jpg" width="400" height="250"/>

### 2. 데이터 라벨링
- **labelimg**를 사용하여 train, valid 데이터 라벨링
<img src="https://user-images.githubusercontent.com/117564613/204189919-70d44b69-e315-45f5-aadb-688fa7ffb06b.jpg" width="400" height="250"/>

### 3.Datasets
- label classess : 3
- total : 1,800 (each label 300)
>- train : 900 (each label 300)
>- valid : 450 (each label 150)
>- test : 450 (each label 150)   

<br><br>
## III. Methology

### 1. YOLO(You Only Look Once)

- 기존의 객체 탐지(Object Detection) 방식들은 Region Proposal과 Classification이 순차적으로 이루어지며 객체 탐지를 수행하는 R-CNN 계열 2 Step 접근 방식 모델들이 주를 이루었다.(ex. R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN 등)
- 하지만 이러한 방식들은 처리 속도가 느리고, 최적화하기 힘들다는 단점이 있다.
- 2015년 일정 수준의 정확성을 보이면서 처리 속도가 보완된 모델인 YOLO가 공개되었다.
- YOLO는 Region Proposal과 Classification이 동시에 이루어지며 객체 탐지를 수행하는 모델로, 처리 속도가 매우 빠르고 간단하다.



<img width="585" alt="스크린샷 2022-11-29 오전 2 51 59" src="https://user-images.githubusercontent.com/117564613/204346930-8a9434c9-f5e4-468e-89cd-dc8c3e6e2a78.png"> [1]

- 입력 이미지를 S x S grid로 나눠준다.
- Grid cell은 B bounding boxes 와 confidence score를 예측한다.
- bounding box는 (x, y, w, h)로 구성되어 있음.
- Confidence는


<img width="572" alt="스크린샷 2022-11-29 오전 2 52 14" src="https://user-images.githubusercontent.com/117564613/204347202-e20bd6ba-3f32-452f-a84e-b7451c4662ff.png"> [1]

### 2. YOLOv5

<br><br>
## IV. Evaluation & Analysis

<br><br>
## V. Related Work
[1] You Only Look Once: Unified, Real-Time Object Detection - https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf
<br/><br/>
 *ref)*
 *국내 소주 판매순위 Top 10 https://smoothmen.tistory.com/300*
<br/><br/>
