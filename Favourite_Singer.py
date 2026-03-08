import streamlit as st

with st.sidebar:
    image = st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Michael_Jackson_1983_%283x4_cropped%29_%28contrast%29.jpg/500px-Michael_Jackson_1983_%283x4_cropped%29_%28contrast%29.jpg", caption = "Michael Jackson")
    st.write("Full Name: Michael Joseph Jackson")
    st.write("Nickname: MJ")
    st.write('Michael Joseph Jackson (29 tháng 8 năm 1958 – 25 tháng 6 năm 2009) là một nam ca sĩ,'
             ' nhạc sĩ, vũ công, nhà sản xuất thu âm kiêm nhà hoạt động thiện nguyện người Mỹ.'
             ' Với biệt danh "Ông hoàng nhạc pop",'
             ' ông được đánh giá là một trong những nhân vật văn hóa quan trọng nhất trong thế kỷ 20'
             ' và là một trong những nhân vật giải trí vĩ đại nhất mọi thời đại. '
             'Trong suốt sự nghiệp trải dài hơn bốn thập kỷ, những đóng góp của ông cho âm nhạc, khiêu vũ và thời trang,'
             ' cùng với biến động đời tư, đã đưa ông trở thành một nhân vật toàn cầu trong nền văn hóa đại chúng. '
             'Jackson đã ảnh hưởng đến các nghệ sĩ thuộc nhiều dòng nhạc khác nhau; '
             'thông qua những màn trình diễn trên sân khấu và video ca nhạc,'
             ' ông đã phổ biến nhiều điệu nhảy phức tạp như moonwalk, mà ông tự đặt tên, và robot.')
st.title("Favourite song")
st.write("Billie Jean")
audio = "Media/Billie Jean - Michael Jackson - Thriller - Michael Jackson - Playlist NhacCuaTui.mp3"
st.audio(audio, "MP3")

st.title("Favourite MV")
st.write("Smooth Criminal")
video = "https://www.youtube.com/watch?v=h_D3VFfhvs4&pp=ygUQc21vb3RoIGNyaW1pbmFsIA%3D%3D"
st.video(video)