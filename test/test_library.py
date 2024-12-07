import unittest
from pydub import AudioSegment
from pydub.generators import Sine
from OSS_Library.proc import volumeAdjustment, StereoToMono, addReverb, Panning

class TestLibraryFunctions(unittest.TestCase):
    def setUp(self):
        # 440Hz 톤 생성 (1초 길이의 스테레오 오디오)
        sine_wave = Sine(440).to_audio_segment(duration=1000)
        self.audio = sine_wave.set_channels(2)  # 스테레오로 설정

    def test_volume_adjustment(self):
        # 0% 볼륨: 무음 확인
        muted_audio = volumeAdjustment(self.audio, volume_persent=0)
        self.assertEqual(muted_audio.dBFS, float("-inf"))

        # 150% 볼륨: 증폭 확인
        amplified_audio = volumeAdjustment(self.audio, volume_persent=150)
        self.assertTrue(amplified_audio.dBFS > self.audio.dBFS)

    def test_stereo_to_mono(self):
        # 스테레오 -> 모노 변환
        mono_audio = StereoToMono(self.audio)
        self.assertEqual(mono_audio.channels, 1)

    def test_add_reverb(self):
        # 테스트할 매개변수
        reverb_count = 3

        # addReverb 함수 호출
        reverb_audio = addReverb(self.audio, reverb_count=reverb_count)

        # 반환값이 AudioSegment인지 확인
        self.assertIsInstance(reverb_audio, AudioSegment, "Returned object is not an AudioSegment instance.")

    def test_panning(self):
        # 테스트할 pan_percent 값
        pan_percent = -50  # 왼쪽으로 50%
        
        # Panning 함수 호출
        panned_audio = Panning(self.audio, pan_percent=pan_percent)
        
        # 반환값이 AudioSegment인지 확인
        self.assertIsInstance(panned_audio, AudioSegment, "Returned object is not an AudioSegment instance.")

        # 왼쪽과 오른쪽 볼륨의 상대적 차이를 확인
        left, right = panned_audio.split_to_mono()
        if pan_percent < 0:
            self.assertTrue(left.dBFS > right.dBFS, "Left channel is not louder when pan_percent < 0.")
        elif pan_percent > 0:
            self.assertTrue(left.dBFS < right.dBFS, "Right channel is not louder when pan_percent > 0.")
        else:
            self.assertAlmostEqual(left.dBFS, right.dBFS, delta=0.5, msg="Channels are not balanced when pan_percent = 0.")

if __name__ == "__main__":
    unittest.main()
