import streamlit as st

st.set_page_config(layout="wide", page_title='Jeu Rap', page_icon='beers')


# ------------------------------------------------ SIDEBAR ------------------------------------------------ #











# ------------------------------------------------ MAIN CONTENT ------------------------------------------------ #


def bienvenue():
    st.title("Bienvenue !")
    st.header("Imaginé par Hadrien, développé par Lucas, voici enfin un jeu de rap idéal pour vos soirées.")

def declarer_joueurs():
    st.subheader("Merci de renseigner le nombre de joueurs : ")
    joueur1 = st.text_input("Nom du joueur 1 : ")
    joueur2 = st.text_input("Nom du joueur 2 : ")
    joueur3 = st.text_input("Nom du joueur 3 : ")
    joueur4 = st.text_input("Nom du joueur 4 : ")
    joueur5 = st.text_input("Nom du joueur 5 : ")
    st.write("Nous jouerons donc avec", joueur1, ",", joueur2, ",", joueur3, ",", joueur4, ",", joueur5,".")
    st.write("Les joueurs ont bien été chargés, vous pouvez cliquer sur la page jeu dans le menu déroulant à gauche pour commencer.")
    st.write("Bonne partie ! :smile: :beers:")

# ------------------------------------------------ JEU ------------------------------------------------ #


def main():
    bienvenue()
    declarer_joueurs()


# ------------------------------------------------ MAIN ------------------------------------------------ #

main()