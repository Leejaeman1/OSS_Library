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

 - pip install oss-library

### 주요 기능

 - 볼륨 조절 (volumeAdjustment)

 - 리버브 추가 (addReverb)

-----------------------------------

 - AudioSegments는 오디오의 단편을 나타내는 불변객체, 오디오를 밀리초 단위로 조작가능

 - overlay는 오디오 세그멘트에 오디오 세그먼트를 오버레이하는데 사용됨

   처음 인자로는 오버레이할 오디오 세그멘트를 받고
   
   (선택)두번째 인자로 어디 위치에서 오버레이 시키냐를 정수로 받음.

   (선택)세번째 인자로는 오디오 세그먼트에 길이에 맞도록 반복을 시킬 것인지 bool 값을 받고 ->사용 안함
   
   (선택)네번째 인자로는 오디오 세그멘트의 길이까지 반복할 반복횟수를 정수로 받고  ->사용 안함
   
   (선택)다섯번째 인자로는 오버레이하는 동안 겹쳐진 오디오 세그먼트의 볼륨을 지정한 데시벨만큼 변화 시킵니다. ->사용 안함

--------------------------------------

    - 스테레오 → 모노 변환 (StereoToMono)

    - 팬닝 (Panning)

--------------------------------------

 - input_audio.set_channels()
   
   지정된 채널 수(1은 모노, 2는 스테레오)로 이 AudioSegment를 만듭니다.

 - input_audio.split_to_mono()
   
   스테레오 AudioSegment를 각 채널(왼쪽/오른쪽)에 대해 두 개로 분할합니다. 왼쪽 채널이 인덱스 0이고 오른쪽 채널이 인덱스 1인 새 AudioSegment 객체가 있는 목록을 반환합니다 .

 - AudioSegment.from_mono_audiosegments()
   
   여러 모노 AudioSegment(2개 이상)로 멀티채널 AudioSegment를 생성합니다. 전달된 각 모노 AudioSegment의 길이는 프레임 수까지 정확히 같아야 합니다.

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
