# AI+X:DeepLearning Final Project<br/>
<br/><br/>

## Title
- 국내 표준 소주병 규격에 따른 소주병 분류 (형태, 색)
<br/><br/>

## Members
- **전인화** 경영학부 / 2017003290 / ai05024@naver.com
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
- 네이버, 구글, bing 3개 검색포털로 부터 이미지 크롤링 * crawling_n.py 파일 참조
- 추출한 이미지 3,600여 개 중, 사용 가능한 이미지 1,800여 개 수기 추출
<img src="https://user-images.githubusercontent.com/117564613/204189919-70d44b69-e315-45f5-aadb-688fa7ffb06b.jpg" width="560" height="350"/>
<br/><br/>

### 2. 데이터 라벨링
- **labelimg**를 사용하여 train, valid 데이터 라벨링
<img src="https://user-images.githubusercontent.com/117564613/204189919-70d44b69-e315-45f5-aadb-688fa7ffb06b.jpg" width="560" height="350"/>
<br/><br/>

### 3.Datasets
- label classess : 3
- total : 1,800 (each label 300)
>- train : 900 (each label 300)
>- valid : 450 (each label 150)
>- test : 450 (each label 150)
<br/><br/>
<br/><br/>

## III. Proposal


<br/><br/>
 *ref)*
 *국내 소주 판매순위 Top 10 https://smoothmen.tistory.com/300*
<br/><br/>
