import streamlit as st

st.title("Điền thông tin giới thiệu bản thân")
myBar = st.progress(0)

quiz = ["Họ và tên: ", "Ngày tháng năm sinh: ", "Sở thích: ", "An Khang có đẹp trai không: "]
answers = []
lenQuiz = len(quiz)
for i in range(lenQuiz):
    answer = st.text_input(quiz[i], '')
    # if answer != '':
    answers.append(answer)

if st.button("Confirm"):
    print(answers)
    if answers[-1].lower().startswith("c") or answers[-1].lower().startswith("y"):
        st.balloons()
        st.write("Bạn thông minh đấy")
    else:
        st.write("Sai lầm lớn rồi đấy")
    if all(answers):
        myBar.progress(100)
        st.write("Bạn đã điền đầy đủ thông tin")
        st.balloons()
    else:
        myBar.progress(len(answers)/lenQuiz)
        st.write("Quên gì kìa")

        for i in range(len(answers)):
            st.write(quiz[i], answers[i])