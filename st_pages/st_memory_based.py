import streamlit as st
import meta as mt
import model_and_memory_based as mmb
import utils
from youtube_search import YoutubeSearch


def main(df_mm,df_small_ratings):
    st.header("💾 Bellek Tabanlı Tavsiye Sistemi 💾")
    st.write("---")

    st.markdown(
        "Belleğe dayalı yöntemler, kullanıcılar veya öğeler arasındaki benzerliği hesaplamak için geçmiş kullanıcı "
        "derecelendirmesi verilerini kullanır. Bu yöntemlerin arkasındaki fikir, kullanıcılar veya öğeler arasında "
        "benzerlik ölçüsü tanımlamak ve görünmeyen öğeleri önermek için en benzer olanı bulmaktır."
        "İki ana bellek tabanlı işbirlikçi filtreleme algoritması türü vardır: "
        "Kullanıcı Tabanlı ve Ürün Tabanlı. Aralarında küçük farklar olsa da, pratikte çok farklı yaklaşımlar uygulanır. "
        "Bu nedenle elimizdeki durum için hangisinin uygun olduğunu bilmek çok önemlidir. \n"

        "- **Kullanıcı tabanlı:** Bu yötemde, benzer içeriği gören/derecelendiren kullanıcıları buluyor ve yeni öğeler önermek için tercihlerini kullanıyoruz.\n"
        "- **Ürün tabanlı:** Mantık benzerdir ancak bunun yerine belirli bir filmden (veya film setinden) başlayarak diğer kullanıcıların tercihlerine göre benzer filmler buluyoruz.")

    st.image("assets/images/memory_based.jpg")
    st.write("---")
    st.subheader("Model 🎯")

    with st.expander("Model Fonksiyonu",
                     expanded=False):
        code = (mt.meta6)
        st.code(code, language='python')

    st.subheader("Youtube 🎯")
    with st.expander("YT Üzerinden URL~Key Çekme İşlemi",
                     expanded=False):
        code = (mt.meta7)
        st.code(code, language='python')

    st.subheader("Ayrıntılar 🎯")
    with st.expander("Get_details Fonksiyonu",
                     expanded=False):
        code = (mt.meta8)
        st.code(code, language='python')

    st.write("---")


    userId = st.selectbox("UserId Belirleyin", df_small_ratings["userId"].unique())
    option = st.selectbox(
        'Modeli Belirleyiniz',
        ('User Based', 'Item Based'))

    if option == "User Based":
        status = True
    else:
        status = False

    button = st.button("Tavsiye Getir")

    if button:

        counter = st.text('Lütfen bekleyiniz ⏱️...yaklaşık 45 saniye sürebilir!')
        movie_md = df_mm.copy()
        trainset, ratings, movie_md = utils.mb_preprocessing(movie_md, df_small_ratings)
        sim_ui = mmb.model(trainset, status)

        # get_rec
        result = mmb.get_recommendations(ratings,df_mm,userId,10,sim_ui)

        movie_name, yt_url = utils.search(result)

        counter.write("")

        utils.get_details(df_mm,yt_url,movie_name)
