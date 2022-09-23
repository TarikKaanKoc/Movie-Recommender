import streamlit as st
from streamlit_option_menu import option_menu
from st_pages import st_content_based as scb
from st_pages import st_memory_based as sm
from st_pages import st_model_based as stm
import utils
# Customize
st.set_page_config(layout="wide", page_title="Movie Recommender", initial_sidebar_state="expanded")

df_credits, df_kw, df_mm, df_ratings, df_small_ratings = utils.load_data()


def main():
    st.title("🎥 Netflix Film Tavsiye Sistemi ")
    st.text("\n\n")
    st.write("---")
    left_col, right_col = st.columns(2)
    right_col.markdown(
        "![Netflix Gif](https://media3.giphy.com/media/UoRR2d1b8xs04A2bV8/giphy.gif?cid=790b761130374fd981872a161bc80d0278f4f165f5b669b7&rid=giphy.gif&ct=s)")

    left_col.markdown(
        """
        **Selam size Gondorlular, Westeroslular, Zionlular, Vikingler veya artık her ne isen..**
        sen ki amansız film aşığı, Jr.Nuri Bilge Ceylan, Entel Feridun ve nicelerinin yansıması. \n
        Kendini film ararken o kadar kaptırdın ve en güzeli için o kadar çaba harcadın ki, bizim MIUUL bitirme projemizin tavsiye sistemine denk geldin.
        Çok uzun yoldan gelmişsindir şimdi sen... İstersen şu köşede bi soluklan.
        Tavsiye sistemlerimiz nasıl çalışıyor bir göz gezdir.
        Belki aradığın o filmi bulursun ha?

        ### Özet
        2019'un ilk çeyreği ile birlikte Statista’ya göre 148.86 milyon kullanıcıya ulaşan Netflix; veriyi yöneten, 
        kullanan ve bu bağlamda kararlar alırken kullanıcıları merkeze yerleştiren ve onların izleme geçmişlerini, 
        içeriklere vermiş oldukları puanları, benzer zevklere sahip kullanıcıları, oyuncular/türler gibi birçok kategoriyi
        dikkate alarak tahminlerde bulunan ve müşterilerine olabildiğine daha iyi bir deneyim yaşatmayı hedefleyen bir şirkettir.
        Belki de Netflix’i başarılı yapan birçok veriyi kategorize ederek makine öğrenmesi algoritmalarını kullanarak kullanıcılara öneriler sunması diyebiliriz.

        """
    )

    st.markdown("---")

    left_col, right_col = st.columns(2)

    left_col.markdown("""
        ### Içerik
        Son yıllarda Youtube, Amazon, Netflix ve benzeri birçok web hizmetinin yükselişi ile tavsiye sistemleri hayatımızda fazlaca yer almaya başladı. E-ticaretten çevrimiçi reklamcılığa, tavsiye sistemleri günlük çevrimiçi yolculuklarımızda kaçınılmaz bir hal almıştır.

         Genel olarak tavsiye sistemleri, kullanıcılara ilgili öğeleri önermeyi amaçlayan algoritmalardır (izlenecek filmler, okunacak metinler, satın alınacak ürünler veya sektörlere bağlı olarak başka herhangi bir şey).

         Tavsiye sistemleri, şirketlere verimli çıktılar verdiklerinde, şirketler büyük miktarda gelir elde edebildikleri veya rakiplerinden önemli ölçüde öne çıkmanın bir yolunu buldukları için bazı endüstrilerde kritik öneme sahiptir. Tavsiye sistemlerinin öneminin bir kanıtı olarak, Netflix'in birkaç yıl önce kendi algoritmasından daha iyi performans gösteren bir öneri sistemi üretmeyi hedeflediği ödüllü bir yarışma (Netflix prize) düzenlediğini söyleyebiliriz. 

         Netflix Film Tavsiye Sistemi projesinde ana amaç tavsiye sistemlerinin farklı yaklaşımlar doğrultusunda zenginleştirmek olmuştur. Projemiz Tavsiye sistemleri yöntemlerini kullanarak film tavsiyesi geliştirmeyi amaçlamaktadır.
        """)
    right_col.markdown("![Netflix Gif](https://gifdb.com/images/high/netflix-and-chill-reality-r2tu34jlq2edkgnd.webp)")

    st.write("---")

    st.subheader("Tavsiye Sistemleri Diyagramı")
    st.image("assets/images/diagram.jpg")

    st.markdown("---")

    left_info_col, right_info_col = st.columns(2)

    left_info_col.markdown(
        f""" 
        ### Proje Ekibi
        Lütfen herhangi bir sorun, yorum veya sorunuz için bizimle iletişime geçmekten çekinmeyin.
        ##### Tarık Kaan Koç [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/TarikKaanKoc)
        - [![Linkedin URL](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tarikkaankoc/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](tarikkaan1koc@gmail.com)
        ##### Göker Berkay [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Gokorotto)
        - [![Linkedin URL](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gokerberkay/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](gokerbbilecen@hotmail.com)
        ##### Ezgi Eftekin [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/ezgiiii)
        - [![Linkedin URL](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ezgi-eftekin-73a8b1184/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ezgieftekin@gmail.com)
        ##### Enes Filiz [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Enes-s)
        - [![Linkedin URL](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/search/results/all/?heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAACURcNoBX8WcTzUqMPNkfKYACLx5ySBiJJI&keywords=enes%20fi̇li̇z&origin=RICH_QUERY_SUGGESTION&position=0&searchId=184a6931-67fb-4d33-b19a-73e7bbf3a8ce&sid=9JE) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](tarikkaan1koc@gmail.com)
        """,
        unsafe_allow_html=True,
    )

    right_info_col.markdown(
        f""" 
        ### Sponsor
          ##### Mustafa Vahit Keskin ~ Guetta  [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/mvahit) [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40Guetta)](https://twitter.com/vahittkeskin)
          - [![Linkedin URL](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vahitkeskin/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](m.vahitkeskin@gmail.com) 
          - [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=lpogwGNgtow)
          """,
        unsafe_allow_html=True,
    )

    right_info_col.markdown(
        """ 
        ### Mentor
        ##### Simge Erek [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/simgeerek)
        - [![Linkedin URL](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/simgeerek/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](simgeerek27@gmail.com) 

        ### Lisans    
        [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)     [![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
        """
    )

with st.sidebar:
    seleceted_page = option_menu(
        "Netflix Film Tavsiye Sistemi",
        ("Anasayfa", "İçerik Tabanlı Tavsiye Sistemi", "Model Tabanlı Tavsiye Sistemi",
         "Bellek Tabanlı Tavsiye Sistemi"),
        icons=["house", "body-text", "lightning-charge", "memory"]
    )



if seleceted_page == "Anasayfa":
    main()
if seleceted_page == "İçerik Tabanlı Tavsiye Sistemi":
    scb.main(df_mm, df_kw, df_credits) # content based recommender - main funciton
if seleceted_page == "Model Tabanlı Tavsiye Sistemi":
    stm.main(df_mm,df_small_ratings) # model based recommender - main funciton
if seleceted_page == "Bellek Tabanlı Tavsiye Sistemi":
    sm.main(df_mm,df_small_ratings) # memory based reccomender - main funciton


