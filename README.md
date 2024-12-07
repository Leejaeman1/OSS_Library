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

1. 이슈 작성 규칙
제목: 간단하고 명확하게 제목 작성해주세요
설명: 문제 상황, 발생한 오류, 해결 방법 등을 구체적으로 작성해주세요

2. 이슈 해결
완료된 이슈는 Closed로 상태 변경해주세요
