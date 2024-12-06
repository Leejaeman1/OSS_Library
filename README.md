## OSS_Library

### 디렉토리는 재량껏 수정

#### 1. branch 규칙

 - main : 최종 릴리스 브랜치. 나중에 제출할 때 사용
 - dev : default 브랜치로 모든 개인 작업은 dev로 병합
 - indiv : 개별 작업 브랜치

#### 2. 작업할 때 흐름

 - git clone 레포지토리 URL
 - cd 레포지토리

모든 개인 작업은 개별 작업 브랜치에서 하고 병합은 dev로만

 - git checkout dev   # 브랜치 변경
 - git pull origin dev   # dev 브랜치 내용 가져오기
 - git checkout -b indiv   # 개별 브랜치 생성

개별 브랜치에서 작업을 끝내면

 - git add . 
 - git commit -m "작업 내용"   # commit할 때 작업 내용 꼭 쓰기
 - git push origin indiv

그 후 GitHub에서 Pull Request 생성하고 dev에 병합

--------------------------------------------------------------------

### 목적

 - 오디오 데이터를 처리하기 위한 라이브러리로 볼륨 조정, 팬닝, 리버브 효과 등을 지원.

### 주요 기능
 
- volumeAdjustment : 오디오의 볼륨을 조정.
- StereoToMono : 스테레오 오디오를 모노로 변환.
- addReverb : 리버브 효과 추가.
- Panning : 좌우 팬닝 효과 적용.

### 디렉토리 구조

- proc.py : 오디오 처리 관련 함수들.
- tests/ : 테스트 코드 디렉토리.