from PyPDF2 import PdfReader
import requests


def read_pdf(f):
    text = ""
    reader = PdfReader(f)
    num_pages = len(reader.pages)
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


def get_vacancy_info(vacancy):
    vacancy_id = vacancy.get("id")
    vacancy_title = vacancy.get("name")
    vacancy_url = vacancy.get("alternate_url")
    vacancy_exp = vacancy.get("experience", {}).get("name")
    vacancy_empl = vacancy.get("employment", {}).get("name")
    company_name = vacancy.get("employer", {}).get("name")
    professional_roles = vacancy.get("professional_roles")
    salary = vacancy.get("salary")
    key_skills = vacancy.get("key_skills")
    vacancy_desc = vacancy.get("description")

    return (f"ID: {vacancy_id}\nНазвание: {vacancy_title}"
            f"\nКомпания: {company_name}\nURL: {vacancy_url}"
            f"\nОпыт: {vacancy_exp}\nЗанятость: {vacancy_empl}"
            f"\nЗП: {salary}\nРоль:{professional_roles}"
            f"\nКлючевые навыки: {key_skills}\n\nОписание: {vacancy_desc}\n"
            )


def read_vacancy_info_from_url(vacancy_url):
    vacancy_id = vacancy_url.split("/")[-1]

    url = f"https://api.hh.ru/vacancies/{vacancy_id}"

    response = requests.get(url)
    if response.status_code == 200:
        vacancy_info = response.json()
        info = get_vacancy_info(vacancy_info)
        return info

    else:
        print(f"Request failed with status code: {response.status_code}")
        return


def read_text(source):
    return source
