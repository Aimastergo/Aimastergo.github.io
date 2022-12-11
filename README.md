# AI+X:DeepLearning Final Project<br/>
<br><br>
## Project Video
[![Video Label](http://img.youtube.com/vi/NpJd5VtOQ-k/0.jpg)](https://www.youtube.com/watch?v=NpJd5VtOQ-k)
   - https://www.youtube.com/watch?v=NpJd5VtOQ-k
<br><br>

## Title
- 국내 표준 360ml 소주병 규격에 따른 소주병 분류 (형태, 색)
<br/><br>

## 0. Members
- **전인화** 경영학부 / 2017003290 / ai05024@hanyang.ac.kr
- **백승주** 경영학부 / 2018027283 / baeksj55@hanyang.ac.kr
<br/><br/>

## 1. Proposal
- 기존 '360mL 초록색'의 소주병 공용 기준을 깬 상품(진로와 같은 투명 소주병)들이 잇따라 출시되면서 소주병 재사용을 위한 협약이 사실상 유명무실화되면서 환경에 악영향을 줄 것이라는 우려도 대두된다.
- 기업의 공병 재사용 효율을 높이고, 환경보호에 도움이 되고자 360ml 소주병을 규격과 색에 따라 분리하는 모델을 만들고자 한다.
<br/><br/>

## 2. Datasets
### 2.1 데이터 선정 및 수집
**1) 수집 데이터 선정** 
- 360ml 소주병 병모양, 색 분류라는 주제에 부합하는 데이터 수집을 위해 수집할 360ml 소주병 종류를 분류
- 소주병 국내 점유율 데이터[0]에 기초하여 3가지 소주병으로 분류 (기존 초록색병 / 진로, 금복주 투명병 / 한라산 투명병)
<br/><br/>

**2) 데이터 수집 : 검색포털 이미지 크롤링**
- 3개의 검색포털에서 이미지 크롤링
- 추출한 이미지 3,600여 개 중, 사용 가능한 이미지 1,800여 개 수기 추출
<img src="https://user-images.githubusercontent.com/117564613/204191315-013382c4-9ec4-48f3-9793-6bedc74a4431.jpg" width="400" height="250"/>

### 2.2 데이터 라벨링
- **labelimg**를 사용하여 train, valid 데이터 라벨링
<img src="https://user-images.githubusercontent.com/117564613/204189919-70d44b69-e315-45f5-aadb-688fa7ffb06b.jpg" width="400" height="250"/>

### 2.3 Datasets
- label classess : 3
- total : 1,285 (100% / each label 430)
>- train : 900 (90% / each label 300)
>- valid : 255 (20% / each label 85)
>- test : 126 (10% / each label 42)   

<br><br>
## 3. Methology

### 3.1 YOLO(You Only Look Once)

- 기존의 객체 탐지(Object Detection) 방식들은 Region Proposal과 Classification이 순차적으로 이루어지며 객체 탐지를 수행하는 R-CNN 계열 2 Step 접근 방식 모델들이 주를 이루었다.(ex. R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN 등)
- 하지만 이러한 방식들은 처리 속도가 느리고, 최적화하기 힘들다는 단점이 있다.
- 2015년 일정 수준의 정확성을 보이면서 처리 속도가 보완된 모델인 YOLO가 공개되었다.
- YOLO는 Region Proposal과 Classification이 동시에 이루어지며 객체 탐지를 수행하는 모델로, 처리 속도가 매우 빠르고 간단하다.



<img width="560" alt="스크린샷 2022-11-29 오전 2 51 59" src="https://user-images.githubusercontent.com/117564613/204346930-8a9434c9-f5e4-468e-89cd-dc8c3e6e2a78.png"> [1]

#### 1) Unified Detection
- 입력 이미지를 S x S grid로 나눠준다.
- 각 Grid cell에 대해 B bounding boxes 와 confidence score를 예측한다.
- bounding box는 (x, y, w, h, c)로 구성되어 있다
 >- (x,y) : boundging box의 중심점 좌표
 >- w,h : 넓이와 높이
 >- c : confidence
- Confidence는 bounding box의 신뢰도를 나타내며 아래 사진과 같이 정의된다.

   <img width="180" alt="스크린샷 2022-11-29 오전 4 19 54" src="https://user-images.githubusercontent.com/117564613/204362614-6539818f-bde5-4fba-98fc-218dbb487ecf.png"> [1]
>- Pr(Object) : 해당 grid에 물체가 있을 확률.(존재하면 1, 존재하지 않으면 0)
>- IOU : 예측한 박스 /  Ground Truth 박스와의 겹치는 영역
- 각각의 Grid cell에 대해 conditional class probabilities를 계산한다.

  <img width="155" alt="스크린샷 2022-11-29 오전 5 00 33" src="https://user-images.githubusercontent.com/117564613/204369708-93137915-7e53-47a0-9bf2-1d12fe517072.png"> [1]
  
- 최종 출력은 아래의 식과 같이 S x S x (B * 5 + C)개의 예측 tensor가 나온다.
- 논문에서는 S=7, B=2, C=20이므로, 7 x 7 x (2 x 5 + 20)개의 예측 tensor가 나온다.
<img width="572" alt="스크린샷 2022-11-29 오전 2 52 14" src="https://user-images.githubusercontent.com/117564613/204347202-e20bd6ba-3f32-452f-a84e-b7451c4662ff.png"> [1]

- 인코딩 된 결과를 시각화해보면 다음과 같다.

  ![1*YG6heD55fEmZeUKRSlsqlA](https://user-images.githubusercontent.com/117564613/204378112-174995a5-dbea-4aff-8cf2-a1471965fc8e.png) [2]


#### 2) Network Design
<img width="800" alt="스크린샷 2022-11-29 오전 2 52 32" src="https://user-images.githubusercontent.com/117564613/204372953-c6181b60-3ba4-4844-9049-d74a48c829bf.png"> [1]

- YOLOv1의 네트워크 구조에는 총 24개의 convolutional layers(이미지로부터 특징 추출)와, 2개의 fully connected layers(클래스 확률 & bounding box의 좌표 예측)가 있다.
- ImageNet 1000-class competition dataset을 사용하여 convolutional layers 첫 20개를 pre-train 시켰다.
- 1x1과 3x3 convolutional layer를 사용하여 feature space를 축소시켰다.
- 해상도를 위해 224x224 크기의 input 이미지를 2배하여 448x448로 변경하였다.

### 3.2 YOLOv5
- 지금까지 YOLO의 초기 버전인 YOLOv1을 간단히 살펴보았고, 이제는 우리가 적용할 기법인 YOLOv5에 대해 알아보고자 한다.
- YOLOv5는 YOLO의 5번째 버전으로, Pytorch 프레임워크 기반으로 구현되었다. YOLOv4와 구조는 유사하나, 추론 시간이 더욱 적게 소요되어 실시간 검출에 더 적합하다.

#### 1) Network Design
<img width="671" alt="스크린샷 2022-11-29 오전 7 22 48" src="https://user-images.githubusercontent.com/117564613/204393468-20550c40-1944-4f39-a41e-502e70ca65a0.png"> [3]

- YOLOv5의 Network Design은 Backbone, neck, Head 이렇게 세 가지 주요 파트로 이루어져 있다.
- Backbone
  - Backbone network는 multiple convolution과 pooling을 통해 입력 이미지에서 다양한 크기의 feature map을 추출하는 convolutional neural network이다.
  - CSP(Cross-Stage-Partial Network)는 계산 속도를 줄이고 추론 프로세스의 속도를 높이는 기법이다.
  - SPP(Spatial Pyramid Pooling)는 fixed-size input image 필요없이, 서로 다른 커널 크기로 max pooling을 수행하고 이들을 서로 연결하여 기능을 융합하는 pooling module이다. [3]
  - YOLOv5의 backbone은 YOLOv5n6, YOLOv5s6, YOLOv5m6, YOLOv5l6, YOLOv5x6 이렇게 총 5종류로 구성되어 있다.
- Neck
  - FPN(Feature Pyramid Network)과 PAN(Path Aggregation Network) structure가 사용된다.
  - FPN structure는 top feature maps에서 lower feature map으로 강력한 semantic features을 전달한다.
  - 동시에 PAN structure는 lower feature map에서 higher feature map으로 강력한 지역화 feature를 전달한다.
  - 두 structure는 공동으로 Neck network의 feature fusion capability를 강화한다. [3]
- Head
  - 생성된 feature maps에서 객체를 검출한다. [3]
  
#### 2) Loss Function

- YOLOv5의 Loss function은 3가지가 있다. 3가지의 Loss function들을 각각 가중치를 곱하고 더해 Loss값을 구한다.

     <img width="360" alt="스크린샷 2022-11-29 오전 10 18 34" src="https://user-images.githubusercontent.com/117564613/204414780-ee2343ef-6378-4d87-9ee6-8eef2c2051ed.png"> [4]

  - Classes Loss : Class를 잘 찾기 위한 Loss
  - Objectness Loss : 해당 grid 안에 목표물이 있을 지에 대한 Loss
  - Location Loss : (x,y,w,h)를 찾기 위한 Regression Loss
  
- Classes Loss와 Objectness Loss는 Binary Cross Entropy + Sigmoid layer인 'torch.nn.BCEWithLogitsLoss()'를 사용한다. 이것은 모든 class의 합을 1로 만들어 가장 값이 높은 하나의 class가 결과로 나오는 것이 아니라 일정 임계점 이상이 되면 두 개 이상의 class도 결과가 될 수 있는 Loss function이다. [5]
- Location Loss는  IoU 기반인 CIoU Loss를 사용한다. CIoU는 area of overap과 central point distance, 그리고 종횡비(aspect ratio)를 고려한 Loss function이다. [6]

  <img width="627" alt="스크린샷 2022-11-29 오전 10 53 58" src="https://user-images.githubusercontent.com/117564613/204419108-0fba6f61-38b4-4b61-9fe1-91a9412b50dd.png"> [6]

 
 
#### 3) 모델 선택

- 소주병 분류 모델은 실시간으로 소주병을 빠르게 탐지해야 한다. 위에서 확인하였듯이 YOLOv5는 다양한 종류의 모델이 있다. 
- 밑의 표는 객체 탐지 모델인 YOLOv5와 EfficientDet의 성능을 비교 분석한 그래프인데, 거의 모든 YOLOv5 모델이 EfficeientDet의 성능과 비슷하거나 압도하는 것을 볼 수 있다.
- 컨베이어 벨트 위에서 소주병들이 실시간으로 분리되어야 하는 현장 상황을 고려했을 때, FPS(Frame Per Second)가 가장 높은 모델인 YOLOv5s를 사용하기로 결정했다.

<img width="700" alt="스크린샷 2022-11-29 오전 6 21 48" src="https://user-images.githubusercontent.com/117564613/204383621-8118178f-cfb3-45d4-9dde-c7c8605e161a.png"> [7]

<br><br>
## 4. Evaluation & Analysis
### 4.1. 학습 결과 (train result)
- **training 소요 시간** : 8.930 hours
- **28 Epochs 훈련 결과**
<img src="https://user-images.githubusercontent.com/117564613/206830895-f2c1bb33-d4eb-4227-b373-eccc23b64110.png">
<img src="https://user-images.githubusercontent.com/117564613/206834961-e2dffb49-8e26-4f9d-a31c-684581946a34.png">
<br><br>

- **validation 실제값과 예측값 비교**
<img src="https://user-images.githubusercontent.com/117564613/206831406-7337cc5a-a441-4ade-8c4a-b59881884469.png">

### 4.2. 소주병 분류기 실행 결과
#### 1) 사진
- 컨베이어 벨트 위에서 소주병들이 분류된다고 가정한 편집 사진으로 실행
<img width="990" src="https://user-images.githubusercontent.com/117564613/206834170-4f32f881-512b-4969-bc4e-2c9d292c5391.png">
<img width="990" src="https://user-images.githubusercontent.com/117564613/206832918-3f84ca20-793a-4b29-9275-64d426154314.png">

#### 2) 실시간 영상
- 웹캠을 통해 실시간 소주병 분류
<br><br>
[![Video Label](http://img.youtube.com/vi/iJJL30N7cS4/0.jpg)](https://youtu.be/iJJL30N7cS4)

    https://youtu.be/iJJL30N7cS4 (링크나 이미지 클릭을 통해 영상 시청 가능)
<br><br>

- 초록병(g0)의 경우, 상하좌우 다양한 각도에서 비교적 높은 정확도를 보였다
- 투명병(w0,w1)의 경우, 어두운 곳이나 다른 색의 배경에 두면 정확도가 떨어졌다. 병의 색이 투명해서 주변 환경의 영향을 많이 받았다.

<br><br>
## 5. Evaluation & Analysis
### 5.1 기대효과
- 최근 3년 사이 소주병 표준화 규격을 깬 사례들이 증가하면서, 기업들은 재활용 소주병에 예상하지 못한 비용을 지불하게 되었다.
이번 360ml 소주병 분류 모델로 병 분류를 자동화하면서 인적 자원에 지출되는 비용을 예전수준으로 줄일 수 있을 것으로 기대한다.

### 5.2 보완
- 소주 상품의 용기가 병으로 제한되지 않으면서 비슷한 생김새의 종이팩, 페트병 소주 상품이 섞여 들어오는 경우가 많다.
모델이 실제 현장에서 사용되기 위해서는 컨베이어 벨트 무게 센서 등 다양한 도구의 결합을 통해 분류 정확도를 보완할 필요가 있다.
- 분류 범위를 소주병에서 맥주, 칵테일 등 주류 병으로 확대하여 모델을 구현한다면 정확도를 높임과 동시에 모델 활용도를 높일 수 있을 것이다.

<br><br>
## 6. Related Work
[0] 국내 소주 판매순위 Top 10 - https://smoothmen.tistory.com/300

[1] You Only Look Once: Unified, Real-Time Object Detection - https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf

[2] Review: YOLOv1 — You Only Look Once (Object Detection) - https://towardsdatascience.com/yolov1-you-only-look-once-object-detection-e1f3ffec8a89

[3] Improving YOLOv5 with Attention Mechanism for Detecting Boulders from Planetary Images - https://www.mdpi.com/2072-4292/13/18/3776/htm

[4] YOLOv5 Documentation- https://docs.ultralytics.com/tutorials/architecture-summary/

[5] [Object Detection] YOLO v5, v6 Loss - https://leedakyeong.tistory.com/m/entry/Object-Detection-YOLO-v5-v6-Loss

[6][Object Detection] YOLO v1 ~ v6 비교(2) - https://leedakyeong.tistory.com/entry/Object-Detection-YOLO-v1v6-%EB%B9%84%EA%B5%902

[7] ultralytics/yolov5 - https://github.com/ultralytics/yolov5

<br/><br/>
## 7. Contribution
#### 전 인화
- YOLOv5 Modeling, Data Crawling, Data Analysis, YouTube recording
#### 백 승주
- YOLOv5 Review, Dataset Preprocessing, YouTube recording
