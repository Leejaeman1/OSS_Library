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



#울림소리를 위한 함수(오디오 세그멘트,울림간격,울림 횟수,감소되는 볼륨)
#울림횟수는 10이하, 감소되는 볼륨은 70%이하만 사용가능
#울림 횟수(reverb_count)만큼 반복해서 decreace_volume데시벨씩 소리줄이기 -> input_audio에 붙이기 
def addReverb(input_audio,gapsecond=0.3,reverb_count=5,decreace_volume_persent=30):

    
    #AudioSegment클래스의 객체가 아닐때
    if not isinstance(input_audio,AudioSegment):
        raise Exception("parameter 1, AudioSegment가 아닙니다.")


    #gapsecond에 정수혹은 실수가 아닌것이 입력되었을때
    if not (isinstance(gapsecond,int) or isinstance(gapsecond,float)):
        raise Exception("parameter 2, 정수혹은 실수가 아닙니다.")
    #gapsecond에 음수가 입력되었을때
    if gapsecond<=0:
        raise Exception("parameter 2, 음수혹은 0이 입력되었습니다.")


    #울림횟수가 정수가 아닐때
    if not isinstance(reverb_count,int) :
        raise Exception("parameter 3, 정수가 아닙니다. (0 ~ 10)") 
    #울림횟수가 10을 초과 했을때
    if reverb_count>10:
        raise Exception("parameter 3, 너무 많은 울림횟수가 입력되었습니다 (0~10)")
    #울림횟수가 음수일때
    if reverb_count<0:
        raise Exception("parameter 3, 음수가 입력되었습니다.")


    #감소되는 볼륨이 정수혹은 실수가 아닐때
    if not (isinstance(decreace_volume_persent,int) or isinstance(decreace_volume_persent,float)):
        raise Exception("parameter 4, 정수혹은 실수가 아닙니다.")
    #감소되는 볼륨이 70초과 일 때
    if decreace_volume_persent>70:
        raise Exception("parameter 4, 70% 초과로 입력되었습니다. (0 ~ 70)")
    #감소되는 볼륨이 음수일 때
    if decreace_volume_persent<0:
        raise Exception("parameter 4, 음수가 입력되었습니다. (0 ~ 70)")

    #울림횟수만큼 반복
    for i in range(reverb_count):
        #i제곱한 볼륨만큼 줄이고 오버레이
        decreace_volume_smallnum=(decreace_volume_persent/100)**i
        input_audio=input_audio.overlay(volumeAdjustment(input_audio,decreace_volume_smallnum*100),(gapsecond*i)*1000)
    return input_audio