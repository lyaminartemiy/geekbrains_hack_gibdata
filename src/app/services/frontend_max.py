import streamlit as st
import streamlit_shadcn_ui as ui
from src.app.services import utils
import streamlit.components.v1 as components

FUNCTIONS_FROM_OPTION = {
    'URL-ссылка': utils.read_vacancy_info_from_url,
    'PDF-файл': utils.read_pdf,
    'Текстовое описание': utils.read_text
}


def custom_metric_card(title, value, description, text_planes):
    metric_item_html = f"""
    <div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 20px;">
        <h3>{title}</h3>
        <p style="font-size: 20px; font-weight: bold;"></p>
        <h2>{description}</h2>
        <p style="font-size: 70px; font-weight: bold"></p>""" + \
                       "<style>a {text-decoration: none}</style>" + \
        f"""<h3>{value}</h3>      
        <p style="font-size: 20px; font-weight: bold;"></p>
        <div>
            {text_planes}
        </div>
    </div>
    """
    components.html(metric_item_html, height=250, width=300)


def set_visual_components():
    st.set_page_config(
        page_title="Course Recommender",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    with st.sidebar:
        option = st.radio(
            label='Выберите способ ввода',
            options=[
                'URL-ссылка',
                'PDF-файл',
                'Текстовое описание'
            ]
        )

        if option == 'PDF-файл':
            input_media = st.file_uploader(label='', type='pdf')

        else:
            mssg = "Прикрепите текстовое описание вакансии или URL-ссылку"

            """ Плашка для загрузки текста """
            input_media = st.text_input(
                mssg,
                label_visibility='visible'
            )

        st.markdown(
            """
            <style>
                div.stButton > button:first-child {
                    background-color: #FF9700;
                    color: white;
                    font-weight: bold
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        calc_button = st.button(
            label='Подобрать курсы'
        )

    if calc_button:
        calc_courses(option, input_media)


def calc_courses(option, source):
    info = FUNCTIONS_FROM_OPTION[option](source)

    """ Заглушка; заменить на передачу данных модели """
    # st.write(info)

    """
    Заглушка; внедрить сюда полученные реки в формате:
    {наименование: ссылка, цена, ключевые навыки}
    """
    # for i in range(10):
    title = "Главный тренд года 🔥"
    description = "<a href='https://hh.ru/vacancy/96176670?query=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+1C&hhtmFrom=vacancy_search_list'>Системный аналитик</a>"
    price = '57000'
    key_skills = """
    <p>SQL</p>
    <p>Python</p>
    <p>Math</p>
    """
    # ui.metric_card(title=title, content=content, description=price,
    #                key=f"card{str(i)}")
    custom_metric_card(title, price, description, key_skills)


def client_input():
    set_visual_components()
