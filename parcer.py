# import os
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
# from dotenv import load_dotenv
#
# load_dotenv('.env')
#
# EMAIL = os.environ.get('EMAIL')
# PASSWORD = os.environ.get('PASSWORD')
#
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = '/usr/bin/firefox'
#
# browser = webdriver.Firefox(capabilities=firefox_capabilities)
# browser.get("https://account.habr.com/login/")
# browser.find_element(By.ID, "email_field").send_keys(EMAIL)
# browser.find_element(By.ID, "password_field").send_keys(PASSWORD)
# browser.find_element(By.NAME, "go").click()
#
# browser.get('https://habr.com/ru/all/')
# generated_html = browser.page_source
# browser.quit()
#
#
# def get_habr_posts() -> list:
#     soup = BeautifulSoup(generated_html, 'html.parser')
#     articles_list = soup.find_all('article')
#     dict_list = []
#     for i in range(len(articles_list)):
#         article_title = articles_list[i].find('h2').find('a').find('span').text
#         try:
#             article_link = f'https://habr.com{articles_list[i].find("a", class_="tm-article-snippet__readmore").get("href")}'
#             article_desc_list = articles_list[i].find('div', class_="article-formatted-body").find_all('p')
#         except AttributeError:
#             article_desc_list = None
#             article_link = None
#
#         if article_link != None:
#             articles_desc_format_list = [article_desc_format.text for article_desc_format in article_desc_list]
#             if articles_desc_format_list:
#                 dict = {
#                     'title': article_title,
#                     'description': list([''.join(articles_desc_format_list)]),
#                     'link': article_link,
#                 }
#                 dict_list.append(dict)
#     return dict_list
#
#
# get_habr_posts()
#
# # for desc_el in article_desc_list:
# #     print(desc_el.text)
