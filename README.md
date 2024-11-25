## OSS_Library

### 1. branch 규칙

 - main : 최종 릴리스 브랜치. 나중에 제출할 때 사용
 - dev : default 브랜치로 모든 개인 작업은 dev로 병합
 - indiv/<작업명> : 개별 작업 브랜치

### 2. 작업할 때 브랜치 흐름

모든 개인 작업은 개별 작업 브랜치에서 하고 병합은 dev로만 

 - git checkout dev - 브랜치 변경
 - git pull origin dev - dev 브랜치 내용 가져오기
 - git checkout -b indiv/<작업명> - 개별 브랜치 생성

개별 브랜치에서 작업을 끝내면

 - git add . 
 - git commit -m "작업 내용" - commit할 때 작업 내용 꼭 쓰기
 - git push origin indiv/<작업명>

그 후 GitHub에서 Pull Request 생성하고 dev에 병합
