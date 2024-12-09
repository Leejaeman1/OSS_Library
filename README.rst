OSS_Library
===========

OSS_Library는 오디오 데이터를 처리하기 위한 Python 라이브러리입니다. 이 라이브러리는 볼륨 조절, 리버브 추가, 스테레오-모노 변환, 팬닝 등의 기능을 제공합니다.

---

설치 방법
---------

**Python 버전**

   이 프로젝트는 Python 3.12에서 동작합니다.

**FFmpeg 설치**

   FFmpeg가 시스템에 설치되어 있어야 합니다:
   - Ubuntu/Debian:

        sudo apt install ffmpeg

   - Windows:
     `FFmpeg 설치 가이드 <https://ffmpeg.org/download.html>`_

**OSS_Library 설치**

   - OSS_Library 디렉토리로 이동 후, 아래 명령 실행:

        pip install 


---
OSS_Library 주요 함수 
---------------------
volumeAdjustment
-----------------
**기능**  

오디오 볼륨을 조정합니다.

**사용된 모듈 및 함수** 
 
- ``pydub.AudioSegment``: 오디오 데이터를 조작.
- ``math.log10``: 볼륨 데시벨 계산.

**인자**  

- ``input_audio (AudioSegment)``: 조정할 오디오 객체.
- ``volume_persent (int | float)``: 볼륨 조절 비율 (0~200%).

**예외 처리**  

- ``TypeError``: ``input_audio``가 ``AudioSegment``가 아니거나, ``volume_persent``가 숫자가 아닌 경우.
- ``ValueError``: 볼륨이 0 미만, 200 초과인 경우.

**수식**  

- 데시벨 계산: ``volume_dB = 20 * log10(volume_persent / 100)``

**사용 예시**  

   adjusted_audio = volumeAdjustment(audio, volume_persent=150)

---

StereoToMono
-----------------
**기능**  

스테레오 오디오를 모노로 변환합니다.

**사용된 모듈 및 함수**  

- ``pydub.AudioSegment.set_channels``: 채널 변환.

**인자**  

- ``input_audio (AudioSegment)``: 변환할 오디오 객체.

**예외 처리**  

- ``TypeError``: ``input_audio``가 ``AudioSegment``가 아닌 경우.
- ``ValueError``: 입력 오디오가 스테레오가 아닌 경우.

**사용 예시**  

   mono_audio = StereoToMono(audio)

---

addReverb
-----------------
**기능**  

울림(리버브) 효과를 추가합니다.

**사용된 모듈 및 함수**  

- ``pydub.AudioSegment.overlay``: 오디오 겹치기.
- 내부 함수 ``volumeAdjustment``: 반복적으로 볼륨 감소.

**인자**  

- ``input_audio (AudioSegment)``: 리버브 효과를 추가할 오디오 객체.
- ``gapsecond (float)``: 리버브 간격 (초 단위, 기본값 0.3).
- ``reverb_count (int)``: 리버브 반복 횟수 (0~10, 기본값 5).
- ``decreace_volume_persent (int | float)``: 반복 리버브 시 감소되는 볼륨 비율 (0~70, 기본값 30).

**예외 처리**  

- ``TypeError``: 인자의 타입이 올바르지 않은 경우.
- ``ValueError``: 범위 외의 값이 입력된 경우.

**사용 예시**  

   reverbed_audio = addReverb(audio, gapsecond=0.5, reverb_count=3, decreace_volume_persent=20)

---

Panning
-----------------
**기능**  

팬닝 효과를 추가해 소리를 좌우로 분리합니다.

**사용된 모듈 및 함수**  

- ``pydub.AudioSegment.split_to_mono``: 오디오를 좌우 채널로 분리.
- ``pydub.AudioSegment.from_mono_audiosegments``: 좌우 채널 병합.
- ``math.log10``: 팬닝 볼륨 조정 계산.

**인자**  

- ``input_audio (AudioSegment)``: 팬닝 효과를 추가할 오디오 객체.
- ``pan_percent (int | float)``: 팬닝 값 (-100~100).  
  - ``-100``: 완전히 왼쪽.
  - ``100``: 완전히 오른쪽.

**예외 처리**  

- ``TypeError``: ``input_audio``가 ``AudioSegment``가 아니거나 ``pan_percent``가 숫자가 아닌 경우.
- ``ValueError``: ``pan_percent``가 -100~100 범위 밖인 경우.

**수식**  

- 팬닝 계산:  

      pan_value = pan_percent / 100

- 볼륨 조정 예시:  

  ``right = right + 20 * log10(1 - abs(pan_value))``

**사용 예시**  

   panned_audio = Panning(audio, pan_percent=50)

AudioSegment
-------------
**기능**  
오디오의 단편(Segment)을 나타내는 **불변 객체**로, 오디오를 **밀리초 단위**로 조작할 수 있습니다.  
Pydub 라이브러리에서 제공하며, 다양한 오디오 데이터의 조작과 처리를 지원합니다.

**주요 메서드**  
- ``from_file``: 파일에서 오디오 세그먼트를 생성.
- ``set_channels``: 채널 수를 변경.
- ``overlay``: 오디오 세그먼트를 다른 세그먼트 위에 겹쳐 놓음.
- ``split_to_mono``: 스테레오 오디오를 좌우 채널로 분리.
- ``export``: 오디오 세그먼트를 파일로 저장.

**사용 예시**  

   # 오디오 파일 로드
   audio = AudioSegment.from_file("example.wav")

   # 채널 변경
   mono_audio = audio.set_channels(1)

   # 오디오 저장
   mono_audio.export("output.wav", format="wav")

---

overlay
-------
**기능**  

오디오 세그먼트 위에 다른 세그먼트를 오버레이하는 데 사용됩니다.  
기본적으로 겹쳐진 오디오 세그먼트가 원래 세그먼트와 병합됩니다.

**인자**  

1. **첫 번째 인자**: 오버레이할 오디오 세그먼트 (필수).  
   - ``AudioSegment`` 객체로 제공.

2. **두 번째 인자**: 오버레이할 위치 (선택).  
   - 정수 값 (밀리초 단위)으로 제공.  
   - 기본값: ``0``.

3. **세 번째 인자**: 오버레이할 오디오 세그먼트를 반복할지 여부 (선택).  
   - ``bool`` 값으로 제공.  
   - 기본값: ``False`` (사용하지 않음).

4. **네 번째 인자**: 반복 횟수 지정 (선택).  
   - 정수 값으로 제공.  
   - 기본값: ``0`` (사용하지 않음).

5. **다섯 번째 인자**: 오버레이 동안 겹쳐진 오디오 세그먼트의 볼륨 변경 (선택).  
   - ``int`` 값으로 제공 (데시벨 단위).  
   - 기본값: ``0`` (사용하지 않음).

**사용 예시**  

   # 두 오디오 세그먼트를 오버레이
   overlayed_audio = audio.overlay(other_audio, position=1000)

   # 오버레이 결과 저장
   overlayed_audio.export("output_overlay.wav", format="wav")

---

디렉토리 구조
--------------

OSS_Library/
├── OSS_Library/              # 라이브러리 소스 코드

│   ├── __init__.py           # 패키지 초기화 파일

│   ├── proc.py               # 주요 라이브러리 함수 (볼륨 조절, 리버브 등)

├── test/                # 테스트 코드

│   └── test_library.py
├── .gitignore           # 빌드 파일 (dist/) 등을 불필요한 파일이 git 저장소에서 제외되도록 함

├── LICENSE                   # MIT 라이선스 파일

├── README.rst                # 프로젝트 설명 (PyPI와 Read the Docs 공유)

├── pyproject.toml            # 패키지 설정 파일

├── MANIFEST.in               # 패키징에 포함할 추가 파일 설정

└── .readthedocs.yaml         # Read the Docs 설정 파일

---

테스트 방법
-----------

테스트 코드는 `OSS_Library/test/test_library.py`에 구현되어 있습니다.

테스트 실행:

    python -m unittest discover -s test

---

개발 가이드라인
----------------

1. 브랜치 규칙
   - **main**: 최종 릴리스 브랜치. 제출용으로 사용.
   - **dev**: 기본 브랜치로, 모든 개인 작업은 dev로 병합.
   - **indiv**: 개별 작업 브랜치.

2. 작업 흐름
   1. 레포지토리 클론:

         git clone <레포지토리 URL>
         cd OSS_Library

   2. 브랜치 작업:

         git checkout dev           # dev 브랜치로 이동
         git pull origin dev        # dev 브랜치 최신화
         git checkout -b <indiv>    # 개별 작업 브랜치 생성

   3. 작업 완료 후:

         git add .
         git commit -m "작업 내용"
         git push origin <indiv>    # 개별 작업 브랜치 푸시

   4. Pull Request 생성:
      - GitHub에서 Pull Request를 만들어 dev에 병합.

---

이슈 작성 규칙
--------------

1. **제목**: 간단하고 명확하게 작성.
2. **설명**: 문제 상황, 발생한 오류, 해결 방법 등을 구체적으로 작성.
3. **상태 변경**: 해결 완료된 이슈는 **Closed**로 상태 변경.

---

