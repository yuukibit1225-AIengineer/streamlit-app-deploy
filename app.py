import streamlit as st 
st.title("サンプルアプリ2:少し複雑にしたwebアプリケーション")


st.write("### 動作モード１：文字数カウント")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("### 動作モード2： BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体系指数のBMI数値を算出できます。")

selected_item= st.radio(
    "動作モードを選択してください",
    ["文字数カウント","BMI値の計算"]
)

st.divider()

if selected_item == "文字数カウント":
    input_message = st.text_input(label ="文字数カウント対象となる文字を入力してください。")
    text_count = len(input_message)
    
else:
    height=st.text_input(label="身長を入れてください。")
    weight=st.text_input(label="体重を入れてください。")
    
if st.button("実行"):
    st.divider()
    
    if selected_item =="文字数カウント":
        if input_message:
            st.write(f"文字数：**{text_count}**")
        else:
            st.error("カウント対象となる文字を入力後、実行を再度押してください。")
    else:
        if height and weight:
            try:
                bmi = round(int(weight)/((int(height)/100)**2),1)
                st.write(f"BMI値:{bmi}")
            except ValueError as e:
                st.write("身長と体重は数値で入力してください。")
        else:
            st.error("身長と体重をどちらも入力してください。")