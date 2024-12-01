#볼륨 관련 모듈
from pydub import AudioSegment
import math

#볼륨 조절 기능함수
#오디오와 볼륨(퍼센트)로 입력받음
#+6dB은 원래 오디오의 2배 볼륨
#-6dB은 원래 오디오의 1/2배 볼륨
def volumeAdjustment(input_audio,volume_persent):
    try:
        if volume_persent>200:
            print("너무 큰 볼륨이 요청되었습니다. (0 ~ 200)")
            return None
        
        elif volume_persent<0:
            print("볼륨(%)에 음수가 입력되었습니다. (0 ~ 200)")
            return None
        
        elif volume_persent==0:
            adjusted_audio=AudioSegment.silent(duration=len(input_audio))

        else:
            volume_dB = 20*math.log10(volume_persent/100)
            adjusted_audio=input_audio+volume_dB

        return adjusted_audio
    except:
        print("볼륨 조절 함수 volumeAdjustment() 사용중에 오류가 발생하였습니다.")
        return None