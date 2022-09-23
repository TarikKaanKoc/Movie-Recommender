import streamlit as st
import meta as mt
from surprise.prediction_algorithms.matrix_factorization import SVD
import model_and_memory_based as mmbr
import utils

def main(df_mm, df_small_ratings):

    st.header("⚡ Model Tabanlı Tavsiye Sistemi ⚡")
    st.write("---")
    st.image("assets/images/model_based.jpg")
    st.markdown("**Model Tabanlı Tavsiye Sistemleri,** veri kümesine dayalı bir sistem içerir, "
                "kısaca anlatmak gerekirse veri kümesinden bazı bilgiler çıkartılarak tam veri seti "
                "kullanılmadan önerilerde bulunmak için bir model kurulur ve bunun üzerinden işlemler "
                "gerçekleştirilir. Model tabanlı öneri sistemleri için Surprise adlı bir kütüphane kullanılarak"
                "matris çarpanlarına ayırma yöntemi olarak SVD kullanılır.")

    st.write("---")

    st.subheader("Veri Ön İşleme 🎯")
    with st.expander("Veri Ön İşleme Fonksiyonu",
                     expanded=False):
        code = (mt.meta4)
        st.code(code, language='python')

    st.subheader("Veri Ön İşleme Sonrası 🎯")
    with st.expander("Tavsiyeleri Getirmek",
                         expanded=False):
            code = (mt.meta5)
            st.code(code, language='python')

    st.write("---")
    left_col, right_col = st.columns(2)

    left_col.subheader("Selam Tekrardan...")
    left_col.markdown("Model Tabanlı Öneri Sisteminin dinamikleri gereği senin verilerin gerekiyor.\n"
                      "Ama ş-şey ben biraz unutkanım da senin izlediğin milyonlarca filmi aklımda tutamam."
                      "O yüzden seninle bir oyun oynamak istiyorum. Benzersiz **id** lere göre tavsiye almak istersen devam edebilirsin.")


    right_col.markdown("![Baby Yoda](https://c.tenor.com/ddf8w0Z84ucAAAAC/mandalorian-baby-yoda.gif)")

    st.write("---")
    userId = st.selectbox("UserId Belirleyin", df_small_ratings["userId"].unique())
    top_n = st.slider('Top N?', 10, 50)

    button = st.button("Tavsiye Getir")

    if button:

        counter = st.text('Lütfen bekleyiniz ⏱️...yaklaşık 45 saniye sürebilir!')
        movie_md = df_mm.copy()
        trainset, ratings, movie_md = utils.mb_preprocessing(movie_md, df_small_ratings)

        # Initialize model ~ Cross-validate
        svd = SVD()
        svd = svd.fit(trainset)

        # get_rec
        result = mmbr.get_recommendations(ratings, movie_md, userId, top_n, svd)

        movie_name, yt_url = utils.search(result)

        counter.write("")

        utils.get_details(df_mm,yt_url,movie_name)