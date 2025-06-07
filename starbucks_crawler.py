from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import warnings

def crawl(region_path, driver, do_all_btn):
    
    # 지역 버튼 클릭
    xpath = region_path
    region_btn = driver.find_element(By.XPATH, xpath)
    region_btn.click()
    time.sleep(0.5)

    if do_all_btn == 1:
        #전체 버튼 클릭
        xpath = '//*[@id="mCSB_2_container"]/ul/li[1]/a'
        all_btn = driver.find_element(By.XPATH, xpath)
        all_btn.click()

    time.sleep(2)
    #현재 페이지의 HTML 전체 소스를 불러온다.
    html = driver.page_source

    #HTML, XML 구문 분석.
    soup = BeautifulSoup(html, 'html.parser')
    starbucks_store_list = soup.select('li.quickResultLstCon')

    # 매장 정보 저장할 초기 변수 선언
    starbucks_list = []

    for store in starbucks_store_list :
    
        store_name = store.select('strong')[0].text.strip()
        store_lat = store['data-lat']
        store_long = store['data-long'] 
        store_type = store.select('i')[0]['class'][0][4:]
        Addr_And_CallNum = store.select('p.result_details')[0].decode_contents().split('<br/>')
        store_addr = Addr_And_CallNum[0]
        store_tel = Addr_And_CallNum[1]

        starbucks_list.append([store_name,store_lat,store_long,store_type,store_addr,store_tel])

    # 지역 검색 버튼 클릭
    xpath = '//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a'
    region_search_btn = driver.find_element(By.XPATH, xpath)
    region_search_btn.click()
    time.sleep(0.5)

    columns = ['매장이름','위도','경도','매장타입','매장주소','매장전화']
    starbucks_df = pd.DataFrame(starbucks_list, columns = columns)

    return starbucks_df

#모든 경고 메시지 무시
warnings.filterwarnings(action='ignore')

#chrome 드라이버 등록 및 홈페이지 URL 지정
driver = webdriver.Chrome()
url = 'https://www.starbucks.co.kr/index.do'
driver.maximize_window()
driver.get(url)

action = ActionChains(driver)
#STORE에 마우스 갖다대기
parent_level_menu = driver.find_element(By.CLASS_NAME, "gnb_nav03")
action.move_to_element(parent_level_menu).perform()
time.sleep(0.5)

# STORE 탭의 지역 검색 버튼 클릭
xpath = '//*[@id="gnb"]/div/nav/div/ul/li[3]/div/div/div/ul[1]/li[3]/a'
child_level_menu = driver.find_element(By.XPATH, xpath)
child_level_menu.click()
time.sleep(0.5)

# 매장 정보 저장할 초기 변수 선언
crawled_list = []

crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[2]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[3]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[4]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[5]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[6]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[7]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[8]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[9]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[10]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[11]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[12]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[13]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[14]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[15]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[16]/a', driver, 1))
crawled_list.append(crawl('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[17]/a', driver, 0))

crawled_df = pd.concat(crawled_list, axis=0, ignore_index=True)

#데이터를 csv파일로 저장
crawled_df.to_csv('Starbucks_stores.csv', index=False, encoding='utf-8')

#웹 사이트 닫기
driver.close()