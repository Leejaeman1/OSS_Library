from pydub import AudioSegment
import math

#볼륨 조절 기능함수(오디오세그멘트,볼륨(퍼센트))
def volumeAdjustment(input_audio,volume_persent):
    
    #AudioSegment클래스의 객체가 아닐때
    if not isinstance(input_audio,AudioSegment):
        raise TypeError("인자로 들어온 오디오가 AudioSegment가 아닙니다.")


    #볼륨(퍼센트)이 정수혹은 실수가 아닌것으로 입력되었을때
    if not (isinstance(volume_persent,int) or isinstance(volume_persent,float)):
        raise TypeError("볼륨(%)이 정수혹은 실수가 아닙니다.")
    
    #볼륨(퍼센트)이 200을 초과하여 입력되었을때
    if volume_persent>200:
        raise ValueError("너무 큰 볼륨(%)이 입력되었습니다. (0 ~ 200)")
    
    #볼륨(퍼센트)이 음수로 입력되었을때
    if volume_persent<0:
        raise ValueError("볼륨(%)에 음수가 입력되었습니다. (0 ~ 200)")
    

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


#스테레오를 모노로 변환하는 함수
def StereoToMono(input_audio):
    #AudioSegment클래스의 객체가 아닐 때
    if not isinstance(input_audio, AudioSegment):
        raise TypeError("인자로 들어온 오디오가 AudioSegment가 아닙니다.")
    #입력된 오디오가 스테레오가 아닐 때
    if input_audio.channels != 2:
        raise ValueError("입력된 오디오가 스테레오가 아닙니다.")
    else:
        mono_audio = input_audio.set_channels(1)
        return mono_audio


#울림소리를 위한 함수(오디오 세그멘트,울림간격,울림 횟수,감소되는 볼륨)
#울림횟수는 10이하, 감소되는 볼륨은 70%이하만 사용가능
#울림 횟수(reverb_count)만큼 반복해서 decreace_volume_smallnum*100씩 소리줄이기 -> input_audio에 붙이기 
def addReverb(input_audio,gapsecond=0.3,reverb_count=5,decreace_volume_persent=30):

    
    #AudioSegment클래스의 객체가 아닐때
    if not isinstance(input_audio,AudioSegment):
        raise TypeError("인자로 들어온 오디오가 AudioSegment가 아닙니다.")


    #gapsecond에 정수혹은 실수가 아닌것이 입력되었을때
    if not (isinstance(gapsecond,int) or isinstance(gapsecond,float)):
        raise TypeError("울림간격이 정수혹은 실수가 아닙니다.")
    #gapsecond에 음수가 입력되었을때
    if gapsecond<=0:
        raise ValueError("울림간격이 음수혹은 0으로 입력되었습니다.")


    #울림횟수가 정수가 아닐때
    if not isinstance(reverb_count,int) :
        raise TypeError("울림횟수가 정수로 입력되지 않았습니다.") 
    #울림횟수가 10을 초과 했을때
    if reverb_count>10:
        raise ValueError("너무 많은 울림횟수가 입력되었습니다. (0 ~ 10)")
    #울림횟수가 음수일때
    if reverb_count<0:
        raise ValueError("울림횟수에 음수가 입력되었습니다. (0 ~ 10)")


    #감소되는 볼륨이 정수혹은 실수가 아닐때
    if not (isinstance(decreace_volume_persent,int) or isinstance(decreace_volume_persent,float)):
        raise TypeError("볼륨감소 값이 정수혹은 실수가 아닙니다.")
    #감소되는 볼륨이 70초과 일 때
    if decreace_volume_persent>70:
        raise ValueError("볼륨감소 값이 70% 초과로 입력되었습니다. (0 ~ 70)")
    #감소되는 볼륨이 음수일 때
    if decreace_volume_persent<0:
        raise ValueError("볼륨감소 값이 음수로 입력되었습니다. (0 ~ 70)")

    #울림횟수만큼 반복
    for i in range(reverb_count):
        #i제곱한 볼륨만큼 줄이고 오버레이
        decreace_volume_smallnum=(decreace_volume_persent/100)**i
        input_audio=input_audio.overlay(volumeAdjustment(input_audio,decreace_volume_smallnum*100),(gapsecond*i)*1000)
    return input_audio

#패닝 기능 함수 (오디오세그멘트, pan_percent(퍼센트))
#음수는 왼쪽 소리가 줄어들고 양수는 오른쪽 소리가 줄어듦 (0은 그대로)
def Panning(input_audio, pan_percent):
    #AudioSegment클래스의 객체가 아닐때    
    if not isinstance(input_audio, AudioSegment):
        raise TypeError("인자로 들어온 오디오가 AudioSegment가 아닙니다.")
    
    #pan_percent에 정수혹은 실수가 아닌것이 입력되었을때
    if not (isinstance(pan_percent,int) or isinstance(pan_percent,float)):
        raise TypeError("패닝 값이 정수혹은 실수가 아닙니다.")
    
    #pan_percent에 -100에서 100사이의 값으로 입력하지 않았을 때
    if not -100 <= pan_percent <= 100:
        raise ValueError("패닝 값이 범위에 적절하지 않은 값으로 입력되었습니다. (-100 ~ 100)")

    left, right = input_audio.split_to_mono()
    pan_value = pan_percent / 100

    if -100 < pan_percent < 0:
        right = right + 20 * math.log10(1 - abs(pan_value))
    elif 0 < pan_percent < 100:
        left = left + 20 * math.log10(1 - abs(pan_value))
    elif pan_percent == -100:
        right = right -100
    elif pan_percent == 100:
        left = left -100
        
    panned_audio = AudioSegment.from_mono_audiosegments(left, right)
    return panned_audio