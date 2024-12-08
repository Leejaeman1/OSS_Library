## OSS_Library

### 개요
OSS_Library는 오디오 데이터를 처리하기 위한 Python 라이브러리입니다. 이 라이브러리는 볼륨 조절, 리버브 추가, 스테레오-모노 변환, 팬닝 등의 기능을 제공합니다.

---

### 설치 방법

#### 1. Python 버전

이 프로젝트는 Python 3.12 에서 동작합니다.

#### 2. FFmpeg 설치

FFmpeg가 시스템에 설치되어 있어야 합니다:
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Windows: [FFmpeg 설치 가이드](https://ffmpeg.org/download.html)

#### 3. OSS_Library 설치

bash

 - OSS_Library에 들어가서
 - pip install dist/OSS_Library-1.0.0.tar.gz

### 주요 기능

 - 볼륨 조절 (volumeAdjustment)

 - 리버브 추가 (addReverb)

 - 스테레오 → 모노 변환 (StereoToMono)

 - 팬닝 (Panning)

### 디렉토리 구조

OSS_Library/

├── OSS_Library/         # 라이브러리 코드

│   ├── __init__.py

│   └── proc.py          # 라이브러리 함수

├── test/                # 테스트 코드

│   └── test_library.py

├── .gitignore           # 빌드 파일 (dist/) 등을 불필요한 파일이 git 저장소에서 제외되도록 함

├── setup.py             # 패키지 설정 파일

├── README.md            # 라이브러리 설명 파일

└── MANIFEST.in          # 추가 파일 포함 설정

### 테스트 방법

 - `OSS_Library/test/test_library.py`에 구현

 - python -m unittest discover -s test

--------------------------------------------------------------------
### 개발할 때

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
 
=======
그 후 GitHub에서 Pull Request 생성하고 dev에 병합

이슈 작성 규칙 
1.제목: 간단하고 명확하게 제목 작성해주세요 
2.설명: 문제 상황, 발생한 오류, 해결 방법 등을 구체적으로 작성해주세요
3.해결 완료된 이슈는 Closed로 상태 변경해주시길 바랍니다.
