#볼륨 관련 모듈
from pydub import AudioSegment


#볼륨 조절 기능함수
#오디오와 볼륨(퍼센트)로 입력받음
#+6dB은 원래 오디오의 2배 볼륨
#-6dB은 원래 오디오의 1/2배 볼륨
def volumeAdjustment(input_audio,volume_persent):
    
    volume_dB = 6*(volume_persent/100)
    if (volume_dB>6):
        print("너무 큰 볼륨")
        return 0
    elif (volume_dB<-6):
        print("너무 작은 볼륨")
        return 0
    else:
        adjusted_audio=(input_audio+volume_dB).normalize()
        return adjusted_audio