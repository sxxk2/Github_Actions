# 원티드 프리온보딩 LabQ 기업과제 Team H

<br>

## 👩‍💻 Team
- [고희석](https://github.com/GoHeeSeok00)
- [김훈희](https://github.com/nmdkims)
- [김민지](https://github.com/my970524)
- [이정석](https://github.com/sxxk2)
- [김상백](https://github.com/tkdqor)

- **[Team-H-노션](https://www.notion.so/pre-onboarding-3rd-team-H-03162526802541328690696ec4588fdd)**

<br>

<img src="https://img.shields.io/badge/프로젝트 진행 기간 2022.06.28 ~ 2022.07.01-D3D3D3?style=for-the-badge">

<br>

## 🛠 기술 스택

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">

<br>

## :ballot_box_with_check: 서비스 개요
- 조직의 다양하고 복잡한 업무에 최신 AI 기술을 적용하여 의사결정 최적화와 프로세스 자동화를 실현하는 서비스를 제공


<br>

## 📌 과제 분석
- **과제 : Open API 방식의 공공데이터를 수집, 가공하여 전달하는 REST API와 이를 요청하는 클라이언트 개발**

- **데이터**
  - [서울시 하수관로 수위 현황](https://data.seoul.go.kr/dataList/OA-2527/S/1/datasetView.do)
  - [서울시 강우량 정보](http://data.seoul.go.kr/dataList/OA-1168/S/1/datasetView.do)

- **개발요건**
  - **REST API 기능**
    - 서울시 하수관로 수위 현황과 강우량 정보 데이터를 수집
    - 출력값 중 GUBN_NAM과 GU_NAME 기준으로 데이터를 결합
    - 데이터는 JSON으로 전달

  - **클라이언트 기능**
    - GUBN(구분코드)를 명시해서 REST API를 호출할 수 있음
    - 서버에서 전송받은 결과를 출력

- **분석결과**


<br>


## DB Modeling
![Untitled](https://user-images.githubusercontent.com/95380638/176635745-467ca0d2-c75f-44b5-9607-28202a1dd657.png)
- **SewerPipe 모델** : 서울시 하수관로 수위 현황 데이터 저장
- **Rainfall 모델** : 서울시 강우량 정보 데이터 저장
- **GuName 모델** : GUBN(구분코드)와 해당하는 서울시 자치구 이름 저장, SewerPipe 및 Rainfall 모델과 각각 1:N 관계 설정


<br>

## API 개발 내역
| Method | Request                                               | URL                                                                              |
|--------|-------------------------------------------------------|----------------------------------------------------------------------------------|
| GET    | 서울시 하수관로 수위 현황과 강우량 정보 데이터를 수집 | http://127.0.0.1:8000/api/data/v1/rainfall-and-drainpipe-info/\<gubn\>/\<datetime\>/ |

- **URL 설정 의도** : URL에 추가적인 확장 및 수정을 진행하는데 용이하다는 점에서 쿼리 파라미터로 Request URL 설정 진행
