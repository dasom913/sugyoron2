import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📐 이차함수 (Quadratic Function)")

st.markdown("""
## 개념 설명

**이차함수**는 최고차항의 지수가 2인 함수입니다.

### 일반형
$$f(x) = ax^2 + bx + c$$
- **a**: 포물선의 모양을 결정 (a > 0이면 아래로 볼록, a < 0이면 위로 볼록)
- **b, c**: 포물선의 위치를 결정

### 꼭짓점 형태
$$f(x) = a(x - h)^2 + k$$
- **(h, k)**: 포물선의 꼭짓점 (최고점 또는 최저점)
""")

st.divider()

# 대화형 그래프
st.subheader("📊 대화형 그래프")

col1, col2, col3 = st.columns(3)

with col1:
    a = st.slider("a 값 (모양)", -3.0, 3.0, 1.0, 0.1)

with col2:
    h = st.slider("h 값 (좌우)", -5.0, 5.0, 0.0, 0.5)

with col3:
    k = st.slider("k 값 (위아래)", -10.0, 10.0, 0.0, 0.5)

# 함수 그리기
x = np.linspace(-10, 10, 200)
y = a * (x - h)**2 + k

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {a}(x - {h})² + {k}')
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
ax.grid(True, alpha=0.3)
ax.plot(h, k, 'ro', markersize=8, label=f'꼭짓점 ({h}, {k})')
ax.set_xlim(-10, 10)
ax.set_ylim(-15, 40)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)
ax.legend(fontsize=11)
ax.set_title('이차함수 그래프', fontsize=14, fontweight='bold')
st.pyplot(fig)
plt.close()

st.divider()

# 예시
st.subheader("📚 예시 문제")

st.write("""
**문제**: f(x) = 2x² - 4x + 1 의 꼭짓점을 구하시오.

**풀이**:
- 표준형: f(x) = a(x - h)² + k
- 완전제곱으로 변환:
  - f(x) = 2(x² - 2x) + 1
  - f(x) = 2(x² - 2x + 1 - 1) + 1
  - f(x) = 2((x - 1)² - 1) + 1
  - f(x) = 2(x - 1)² - 2 + 1
  - f(x) = 2(x - 1)² - 1

**답**: 꼭짓점은 (1, -1)
""")

