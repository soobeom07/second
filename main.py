import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 제목
st.set_page_config(page_title="Google Drive 데이터 시각화", layout="wide")
st.title("📈 구글 드라이브 데이터 Plotly 시각화")
st.markdown("구글 드라이브에서 불러온 데이터를 Plotly로 시각화한 Streamlit 앱입니다.")

# 데이터 불러오기
DATA_URL = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    return df

df = load_data()

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 컬럼 선택
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
non_numeric_cols = df.select_dtypes(exclude=['number']).columns.tolist()

x_axis = st.selectbox("X축 컬럼 선택", non_numeric_cols)
y_axis = st.multiselect("Y축 컬럼 선택", numeric_cols, default=numeric_cols[:1])

# 시각화
if x_axis and y_axis:
    fig = px.line(df, x=x_axis, y=y_axis, title=f"{x_axis}에 따른 {', '.join(y_axis)} 변화")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("X축과 Y축 컬럼을 선택해주세요.")
    streamlit
streamlit
pandas
plotly
