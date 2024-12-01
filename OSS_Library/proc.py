#볼륨 관련 모듈
from pydub import AudioSegment
import math

#볼륨 조절 기능함수
#오디오와 볼륨(퍼센트)로 입력받음
#+6dB은 원래 오디오의 2배 볼륨
#-6dB은 원래 오디오의 1/2배 볼륨
def volumeAdjustment(input_audio,volume_persent):
    try:
        #볼륨(퍼센트)가 정수가 아닌것으로 입력되었을때
        if not isinstance(volume_persent,int):
            print("정수가 아닙니다. (0 ~ 200)")
            return None
        
        #볼륨(퍼센트)가 200초과로 입력되었을때
        if volume_persent>200:
            print("너무 큰 볼륨이 입력되었습니다. (0 ~ 200)")
            return None
        
        #볼륨(퍼센트)가 음수로 입력되었을때
        elif volume_persent<0:
            print("볼륨(%)에 음수가 입력되었습니다. (0 ~ 200)")
            return None
        
        #볼륨이 0일때
        elif volume_persent==0:
            #음소거 처리
            adjusted_audio=AudioSegment.silent(duration=len(input_audio))
        
        #그외 모든 경우 일 때 (정수 1~200)
        else:
            #데시벨 수식에 따라 추가해야할 데시벨 계산
            volume_dB = 20*math.log10(volume_persent/100)
            adjusted_audio=input_audio+volume_dB

        return adjusted_audio
    
    #예상하지 못한 예외의 경우
    except Exception as e:
        print("volumeAdjustment() 사용중에 예상하지 못한 오류가 발생하였습니다:",e)
        return None
        