from pydub import AudioSegment
import math

#볼륨 조절 기능함수(오디오세그멘트,볼륨(퍼센트))
def volumeAdjustment(input_audio,volume_persent):
    
    #AudioSegment클래스의 객체가 아닐때
    if not isinstance(input_audio,AudioSegment):
        raise Exception("parameter 1, AudioSegment가 아닙니다.")


    #볼륨(퍼센트)이 정수혹은 실수가 아닌것으로 입력되었을때
    if not (isinstance(volume_persent,int) or isinstance(volume_persent,float)):
        raise Exception("parameter 2, 정수혹은 실수가 아닙니다. (0 ~ 200)")
    
    #볼륨(퍼센트)이 200을 초과하여 입력되었을때
    if volume_persent>200:
        raise Exception("parameter 2, 너무 큰 볼륨(%)이 입력되었습니다. (0 ~ 200)")
    
    #볼륨(퍼센트)이 음수로 입력되었을때
    if volume_persent<0:
        raise Exception("parameter 2, 볼륨(%)에 음수가 입력되었습니다. (0 ~ 200)")
    

    #볼륨(퍼센트)이 0일때
    if volume_persent==0:
        #음소거 처리
        adjusted_audio=AudioSegment.silent(duration=len(input_audio))
    #그외 모든 경우 일 때 (정수 1~200)
    else:
        #데시벨 수식에 따라 추가해야할 데시벨 계산
        volume_dB = 20*math.log10(volume_persent/100)
        adjusted_audio=input_audio+volume_dB

    return adjusted_audio



def StereoToMono(input_audio):
    if input_audio != 2:
        raise ValueError("입력된 오디오가 스테레오가 아닙니다.")
    else:
        mono_audio = input_audio.set_channels(1)
        return mono_audio