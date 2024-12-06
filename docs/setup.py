from setuptools import setup, find_packages

setup(
    name="OSS_Library",                # 패키지 이름 (pip install 시 사용)
    version="1.0.0-alpha",             # 초기 버전 (alpha/beta로 명시)
    description="A library for audio processing",  # 짧은 설명
    long_description=open("README.md").read(),     # README 내용을 상세 설명으로 포함
    long_description_content_type="text/markdown", # README 파일 형식
    author="Your Name",                # 작성자 이름
    author_email="your_email@example.com",         # 작성자 이메일
    url="https://github.com/your_username/OSS_Library", # 프로젝트 URL
    license="MIT",                     # 라이선스 (MIT, Apache 등 선택 가능)
    packages=find_packages(),          # 패키지 목록 자동 탐색
    install_requires=["pydub"],        # 의존성 패키지
    python_requires=">=3.8",           # 최소 Python 버전
    classifiers=[                      # PyPI 분류 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
