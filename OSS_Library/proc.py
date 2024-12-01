#볼륨 관련 모듈
from pydub import AudioSegment
import math

#볼륨 조절 기능함수
#오디오와 볼륨(퍼센트)로 입력받음
#+6dB은 원래 오디오의 2배 볼륨
#-6dB은 원래 오디오의 1/2배 볼륨
def volumeAdjustment(input_audio,volume_persent):
    
    if volume_persent>200:
        print("너무 큰 볼륨 (200%이상)")
        return 0
    
    elif volume_persent<0:
        print("볼륨(%)에 음수가 입력됨")
        return 0
    
    elif volume_persent==0:
        adjusted_audio=(input_audio-math.inf).normalize()

    else:
        volume_dB = 20*math.log10(volume_persent/100)
        adjusted_audio=(input_audio+volume_dB).normalize()

    return adjusted_audio