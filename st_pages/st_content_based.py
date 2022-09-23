import streamlit as st
import content_based as cb
import meta as mt
from youtube_search import YoutubeSearch
import utils

def main(df_mm, df_kw, df_credits):

    st.header("🔎 İçerik Tabanlı Tavsiye Sistemi 🔍")
    st.write("---")
    left_col, right_col = st.columns(2)

    right_col.image("assets/images/content_based.jpg",width=500)

    left_col.text("\n\n\n")
    left_col.write("**İçerik Tabanlı Tavsiye Sistemi,** kullanıcıdan açıkça (derecelendirme) veya dolaylı olarak "
                   "(bir bağlantıya tıklayarak) aldığımız verilerle çalışır. Bir sonraki adımda kullanıcıya önermek için"
                   "kullanılan, bir kullanıcı profili oluşturduğumuz verilerle, kullanıcı daha fazla girdi sağladığında,"
                   "öneriye göre daha fazla girdi sağladığında ve eylemde bulunduğunda, sistem daha doğru hale gelir."
                   )

    left_col.write("Bu proje kapsamında kullanmış olduğumuz **'İçerik Tabanlı Tavsiye Sisteminde,'** filmlerin içeriklerini"
                   " (ön yazısı, anahtar kelimeler, oyuncular, filmin kategorisi vb...) "
                   "barındıran değişkende belirli anahtar kelimelerin o "
                   "değişkende geçme frekanslarını gösteren bir dataset oluşturulur.")

    left_col.image("assets/images/matrix.png")

    st.write("---")
    st.subheader("Veri Ön İşleme 🎯")
    with st.expander("Veri Ön İşleme Fonksiyonu",
                         expanded=False):
            code = (mt.meta)
            st.code(code, language='python')

    with st.expander("TAGS Feature",
                     expanded=True):
        code = (mt.meta2)
        st.code(code, language='python')

    st.image("assets/images/df_head_image.png")

    st.subheader("Veri Ön İşleme Sonrası 🎯")

    st.write("Projede **'tags'** değişkeni içerisinde TF-IDF yöntemi ile elde edilmiş kelime grupları ile, "
                   "kullanacağımız dataframe oluşturulmuş ve tahmin yapılmıştır. Kelimelerin hem kendi metinlerinde "
                   "hem de bütün korpusta yani bütün odaklandığımız verideki geçme frekansları üzerinden bir normalizasyon"
                   " işlemi yapar. Oluşturacak olduğumuz kelime vektörlerini,  terim matrisini ve bütün dökümanları "
                   "göz önünde bulundurarak terimlerin frekanslarını da göz ününde bulundurarak genel bir standartlaştırma"
                   " işlemi yapar. Böylece count vector yönteminde ortaya çıkabilecek olan bazı yanlılıkları giderir.")

    with st.expander("Similarity",
                         expanded=False):
            code = (mt.meta3)
            st.code(code, language='python')

    st.write("---")

    movie = st.selectbox("Bir Film Seçiniz", df_mm["title"])
    button = st.button("Tavsiye Getir", key=1)


    if button:
        counter = st.text('Lütfen bekleyiniz ⏱️... Yaklaşık 59 saniye sürebilir!')
        print("Debug -1")
        movie_md = df_mm.copy()
        df = utils.preprocessing(movie_md, df_kw, df_credits)
        print("Debug -2")
        similarity = cb.cosine_sim(df)
        rec_list = cb.recommendation(movie,df,similarity)

        yt_url = []
        movie_name = []
        print("Debug -3")

        for i in rec_list:
            title = df.iloc[i[0]].title
            movie_name.append(title)
            result = YoutubeSearch(title + "Trailer", max_results=1).to_json()
            get_yt_key = result.split(",")[-1][16:36]
            yt_url.append("https://www.youtube.com"+get_yt_key)
            print("Debug -4")

        print(len(yt_url))
        print("Debug -5")
        counter.text("")
        print("Debug -6")
        
        utils.get_details(df_mm,yt_url,movie_name)

        print("Debug final")

        """
                for temp in range(3):
            right_col, left_col = st.columns(2)
            st.video(yt_url[temp])
            left_col.video(yt_url[temp])
            movie_title = list(df_mm[df_mm["title"] == movie_name[temp]].title)
            right_col.subheader(movie_title[0])
            movie_overview = list(df_mm[df_mm["title"] == movie_name[temp]].overview)
            right_col.write(movie_overview[0])
            movie_genres = list(df_mm[df_mm["title"] == movie_name[temp]].genres)
            right_col.write(movie_genres)
            imdb_id = list(df_mm[df_mm["title"] == movie_name[temp]].imdb_id)
            right_col.markdown(f[![IMDB](https://img.shields.io/badge/IMDb-F5C518.svg?style=for-the-badge&logo=IMDb&logoColor=black)](https://www.imdb.com/title/{imdb_id[0]}/))
        """
