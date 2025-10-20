# 스타트업 수익 예측 애플리케이션

이 프로젝트는 스타트업 회사의 다양한 지출 데이터를 기반으로 수익을 예측하는 머신러닝 기반 웹 애플리케이션입니다.

## 주요 기능

1. **데이터 탐색 (EDA)**
   - 기본 통계 분석
   - 변수별 분포 확인
   - 상관관계 분석
   - 주(State)별 통계 분석
   - 인터랙티브 데이터 시각화

2. **머신러닝 모델**
   - 수익 예측 모델
   - 실시간 예측 기능
   - 모델 성능 평가

## 사용된 데이터

- **데이터셋**: 50 Startups Dataset
- **특성**:
  - R&D Spend: 연구개발 지출
  - Administration: 관리 비용
  - Marketing Spend: 마케팅 지출
  - State: 회사 소재 주
  - Profit: 수익(목표 변수)

## 기술 스택

- **Frontend**: Streamlit
- **Backend**: Python
- **주요 라이브러리**:
  - pandas: 데이터 처리
  - numpy: 수치 연산
  - matplotlib/seaborn: 데이터 시각화
  - plotly: 인터랙티브 시각화
  - scikit-learn: 머신러닝 모델
  - koreanize-matplotlib: 한글 폰트 지원

## 설치 방법

1. 저장소 복제
```bash
git clone https://github.com/blockenters/streamlit-50-startups.git
cd streamlit-50-startups
```

2. 가상환경 생성 및 활성화 (선택사항)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
```

3. 필요한 라이브러리 설치
```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
streamlit run app.py
```

## 프로젝트 구조

```
streamlit-50-startups/
├── app.py              # 메인 애플리케이션
├── app_home.py         # 홈 페이지
├── app_eda.py          # 데이터 분석 페이지
├── app_ml.py          # 머신러닝 예측 페이지
├── data/               # 데이터 폴더
│   └── 50_Startups.csv # 데이터셋
├── model/              # 모델 저장 폴더
└── requirements.txt    # 의존성 패키지 목록
```

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새로운 기능 브랜치를 생성합니다.
3. 변경사항을 커밋합니다.
4. 브랜치에 푸시합니다.
5. Pull Request를 생성합니다.
