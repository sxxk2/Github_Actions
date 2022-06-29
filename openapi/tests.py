from labq.my_settings import api_authenticate_key
import xml.etree.ElementTree as ET

# 서울시 강우량계 위치정보(베셀(bessel) 좌표계)
#
# 강우량계코드  강우량계명 구청코드 구청명                주소	                       설치위치(X좌표)	설치위치(Y좌표)
# 101	        강남구청	101	강남구	서울특별시 강남구 삼성동 16-1 강남구청 별관	        44645510	20419810
# 102	        세곡동	101	강남구	서울특별시 강남구 율현동 278-1 세곡동사무소	        44107740	20946730
# 103	        개포2동	101	강남구	서울특별시 강남구 개포동 182-1 개포2동 사무소	    44337240	20603240
# 201	        강동구청	102	강동구	서울특별시 강동구 성내동 강동구청 540	            44785140	21093260
# 202	        고덕2동	102	강동구	서울특별시 강동구 고덕2동 226-4 고덕2동사무소	    45123720	21452360
# 401	        노원구청	104	노원구	서울특별시 도봉구 방학동 720 도봉구청	            46322960	20415540
# 402	        상계1동	104	노원구	서울특별시 노원구 상계동 701-1 노원구청	            46161610	20499990
# 501	        강북구청	105	강북구	서울특별시 노원구 상계동 1259 상계1동 사무소	        46446690	20484150
# 601	        성북구청	106	성북구	서울특별시 강북구 수유동 95(강북구청 별관)	        45999220	20224820
# 602	        상월곡동	106	성북구	서울특별시 성북구 보문동 보문로 168 성북구청(별관)	    45420310	20183300
# 701	        중랑구청	107	중랑구	서울특별시 성북구 상월곡동 97-22 상월곡동사무소	    45624950	20423690
# 702	        면목P	107	중랑구	서울특별시 중랑구 신내동 662번지 중랑구청	        45634240	20820370
# 801	        동대문구청	108	동대문구	서울특별시 중랑구 면목5동 168-1(면목빗물펌프장)   	45352490	20706810
# 802	        휘경P	108	동대문구	서울특별시 동대문구 용두동 39-9(하정로 145) 동대문구청	45276510	20351300
# 901	        성동구청	109	성동구	서울특별시 동대문구 휘경2동 7-17호 휘경펌프장	        45463610	20610870
# 902	        뚝섬P	109	성동구	서울특별시 성동구 행당1동 7번지 성동구청	            45152090	20324660
# 1001	    종로구청	110	종로구	서울특별시 성동구 성수1가 2동 685호 뚝섬펌프장	    45156200	20324380
# 1002	    부암동	110	종로구	서울특별시 종로구 수송동 46-2 종로구청	            45267190	19844900
# 1101	    중구청	111	중구	    서울특별시 종로구 부암동 265-21 부암동사무소	        45478040	19683700
# 1104	    서소문	111	중구	    서울특별시 중구 예관동 120-1번지 중구청	            45156690	19982280
# 1201	    광진구청	112	광진구	서울특별시 광진구 자양동 777 광진구청	            44877140	20728680
# 1301	    은평구청	113	은평구	서울특별시 은평구 녹번동 84 은평구청	            45590180	19371950
# 1302    	증산P	113	은평구	서울특별시 은평구 증산동 238-4호 증산펌프장	        45318900	19143330
# 1303    	갈현1동	113	은평구	서울특별시 은평구 갈현1동 436-14 갈현1동사무소	    45823380	19265000
# 1401    	서대문구청	114	서대문구	서울특별시 서대문구 연희3동 168-6 서대문구청	        45329250	19439900
# 1501    	마포구청	115	마포구	서울특별시 마포구 성산동 370 마포구청	            45182680	19126420
# 1502    	봉원P	115	마포구	서울특별시 마포구 신정동 93-2호 봉원빗물펌프장	        44936460	19382650
# 1601    	용산구청	116	용산구	서울특별시 용산구 이태원동34-87 용산구청	            44812500	19912110
# 1602    	한남P	116	용산구	서울특별시 용산구 한남1동 531-3번지 한남빗물펌프장	    44774390	20068210
# 1701    	강서구청	117	강서구	서울특별시  강서구 화곡동 980-16 강서구청	        45016190	18671560
# 1702    	공항동P	117	강서구	서울특별시 강서구 공항동 706-1 공항빗물펌프장	        45081270	18381700
# 1801    	양천구청	118	양천구	서울특별시 양천구 신정6동 321-4 양천구청	        44640470	18819580
# 1802    	목동P	118	양천구	서울특별시 양천구 목1동 915번지 목동빗물펌프장	        44760150	18919870
# 1901    	영등포구청	119	영등포구	서울특별시 영등포구 당산동3가 385-1 영등포구청	    44742410	19080280
# 1902    	도림2동P	119	영등포구	서울특별시 영등포구 도림2동 254번지 도림2빗물펌프장	    44524910	19092950
# 2001    	구로구청	120	구로구	서울특별시 구로구 구로본동 435 구로구청	            44398740	19006520
# 2002    	개봉2동	120	구로구	서울특별시 구로구 개봉2동 261-6	                44349540	18731680
# 2101    	동작구청	121	동작구	서울특별시 동작구 노량진동 47-2 동작구청	            44587000	19464780
# 2102    	흑석P	121	동작구	서울특별시 동작구 흑석동 114번지 흑석빗물펌프장	    44555270	19677120
# 2201    	금천구청	122	금천구	서울특별시 금천구 시흥동 1020 금천구청	            43972750	19075530
# 2202    	가산2P	122	금천구	서울특별시 금천구 가산동 550-22 가산1펌프장	        44180249	18926290
# 2301    	관악구청	123	관악구	서울특별시 관악구 봉천4동 1570-1 관악구청	        44208620	19573270
# 2302    	신림P	123	관악구	서울특별시 관악구 신림8동 1649 신림빗물펌프장     	44281840	19188710
# 2401    	서초구청	124	서초구	서울특별시 서초구 서초동 1376-3 서초구청	        44270030	20288210
# 2402    	반포P	124	서초구	서울특별시 서초구 반포2동 15-2 반포펌프장	        44456380	19949280
# 2501    	송파구청	125	송파구	서울특별시 송파구 신천동 29-5(올림픽로 326) 송파구청	44613110	20937880
# 2502    	마천2동	125	송파구	서울특별시 송파구 마천2동 127-1 마천 2동 사무소	    44417470	21313980


# 샘플 URL	서울시 강우량 정보
# http://openAPI.seoul.go.kr:8088/(인증키)/xml/ListRainfallService/1/5/
# 샘플 URL	강남구 강우량 정보
# http://openapi.seoul.go.kr:8088/(인증키)/xml/ListRainfallService/1/5/강남구


# 하수관로_수위
# 고유번호,구분코드,구분명,측정일자,측정일자,측정수위,통신상태
#
# ※ 측정일자 보는법
#    일-월-년 시:분:초  ex)01-APR-16 00:00:00
# ※ DB서버상황으로 인하여 측정일자가 두번 나오는 문제가 발생했습니다.
# 이용에 참고바랍니다.

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import urllib.request
import requests
from bs4 import BeautifulSoup

# for i in range(1, 23):
#     print(f"========================= {i}:page 시작 =========================")
url = f"http://openapi.seoul.go.kr:8088/{api_authenticate_key}/xml/ListRainfallService/1/5"

xml_txt = requests.get(url).text

root = ET.fromstring(xml_txt)
print(root)
for row in root:

    print(row)

# print(html_txt)
# # print("page test")
# # print(json_txt)
# # print("=============================================== end page test")
# soup = BeautifulSoup(html_txt, 'html.parser')
# print(soup)
# category_tr = soup.select('table.grid > tbody > tr > td')
# # print("category_tr test")
# print(category_tr)
# print("=============================================== end page test")
# for j in range(10):
#     try:
#         tr = soup.select('td > a')[j]['onclick']
#         tr = tr.lstrip('fncDtl(')
#         tr = tr.strip().rstrip('eslaf nruter ;)')
#         content_number = tr.replace("'", "")

#         url = f"http://api.nongsaro.go.kr/sample/ajax/ajax_local_callback.jsp?garden/gardenDtl?apiKey=nongsaroSampleKey&htmlArea=nongsaroApiLoadingAreaResult&pageNo={i}&cntntsNo={content_number}&serviceType=ajaxType"
#         content_html = requests.get(url).text

#     content = BeautifulSoup(content_html, 'html.parser')
#
#     botanical_name = content.select('tr > td')[0].text
#     english_name = content.select('tr > td')[1].text
#     general_name = content.select('tr > td')[2].text
#     type_name = content.select('tr > td')[3].text
#     origin = content.select('tr > td')[4].text
#     advise_info = content.select('tr > td')[5].text
#     image_link = content.select('tr > td')[6].text
#     heigt_info = content.select('tr > td')[7].text
#     width_info = content.select('tr > td')[8].text
#     leaftype_info = content.select('tr > td')[9].text
#
#     smell_info = content.select('tr > td')[10].text
#     toxic_info = content.select('tr > td')[11].text
#     breeding_info = content.select('tr > td')[12].text
#     extraperiod_info = content.select('tr > td')[13].text
#     grow_level = content.select('tr > td')[14].text
#     growth_speed = content.select('tr > td')[15].text
#     growth_temp = content.select('tr > td')[16].text
#     lowest_temp = content.select('tr > td')[17].text
#     humidity = content.select('tr > td')[18].text
#     fertilizer_info = content.select('tr > td')[19].text
#
#     soil_info = content.select('tr > td')[20].text
#     water_spring = content.select('tr > td')[21].text
#     water_summer = content.select('tr > td')[22].text
#     water_fall = content.select('tr > td')[23].text
#     water_winter = content.select('tr > td')[24].text
#     insect_info = content.select('tr > td')[25].text
#     extragrow_info = content.select('tr > td')[26].text
#     functional_info = content.select('tr > td')[27].text
#     potsize_big = content.select('tr > td')[28].text
#     potsize_mid = content.select('tr > td')[29].text
#
#     potsize_small = content.select('tr > td')[30].text
#     width_big = content.select('tr > td')[31].text
#     width_mid = content.select('tr > td')[32].text
#     width_small = content.select('tr > td')[33].text
#     length_big = content.select('tr > td')[34].text
#     length_mid = content.select('tr > td')[35].text
#     length_small = content.select('tr > td')[36].text
#     heigt_big = content.select('tr > td')[37].text
#     heigt_mid = content.select('tr > td')[38].text
#     heigt_small = content.select('tr > td')[39].text
#
#     volume_big = content.select('tr > td')[40].text
#     volume_mid = content.select('tr > td')[41].text
#     volume_small = content.select('tr > td')[42].text
#     price_big = content.select('tr > td')[43].text
#     price_mid = content.select('tr > td')[44].text
#     price_small = content.select('tr > td')[45].text
#     care_need = content.select('tr > td')[46].text
#     type = content.select('tr > td')[47].text
#     growth_type = content.select('tr > td')[48].text
#     indoor_garden = content.select('tr > td')[49].text
#
#     ecology = content.select('tr > td')[50].text
#     leaf_pattern = content.select('tr > td')[51].text
#     leaf_color = content.select('tr > td')[52].text
#     flower_season = content.select('tr > td')[53].text
#     flower_color = content.select('tr > td')[54].text
#     fluit_season = content.select('tr > td')[55].text
#     fluit_color = content.select('tr > td')[56].text
#     breeding_way = content.select('tr > td')[57].text
#     lux = content.select('tr > td')[58].text
#     location = content.select('tr > td')[59].text
#
#     insect = content.select('tr > td')[60].text
#     print(f"*********** {i} page {j+1} 번째 conetent ***********")
#     print(botanical_name)
#     print(english_name)
#     print(general_name)
#     print(type_name)
#     print(origin)
#     print(advise_info)
#     print(image_link)
#     print(heigt_info)
#     print(width_info)
#     print(leaftype_info)
#
#     print(smell_info)
#     print(toxic_info)
#     print(breeding_info)
#     print(extraperiod_info)
#     print(grow_level)
#     print(growth_speed)
#     print(growth_temp)
#     print(lowest_temp)
#     print(humidity)
#     print(fertilizer_info)
#
#     print(soil_info)
#     print(water_spring)
#     print(water_summer)
#     print(water_fall)
#     print(water_winter)
#     print(insect_info)
#     print(extragrow_info)
#     print(functional_info)
#     print(potsize_big)
#     print(potsize_mid)
#
#     print(potsize_small)
#     print(width_big)
#     print(width_mid)
#     print(width_small)
#     print(length_big)
#     print(length_mid)
#     print(length_small)
#     print(heigt_big)
#     print(heigt_mid)
#     print(heigt_small)
#
#     print(volume_big)
#     print(volume_mid)
#     print(volume_small)
#     print(price_big)
#     print(price_mid)
#     print(price_small)
#     print(care_need)
#     print(type)
#     print(growth_type)
#     print(indoor_garden)
#
#     print(ecology)
#     print(leaf_pattern)
#     print(leaf_color)
#     print(flower_season)
#     print(flower_color)
#     print(fluit_season)
#     print(fluit_color)
#     print(breeding_way)
#     print(lux)
#     print(insect)
#
#     print(botanical_name)
#
#
#
#
#
# except:
#     break
# else:
#     print(f"==================================================================================")
#     print(f"*********** {i} page {j+1} 번째 conetent 끝 ***********")
#     print("==================================================================================")
# print(f"{i}::::::::::{content_number}")

# driver = webdriver.Chrome()
# driver.get("http://api.nongsaro.go.kr/sample/ajax/garden/gardenList.html")
#
# SCROLL_PAUSE_TIME = 1
# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # Scroll down to bottom
#     for i in range(2, 23):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         # Wait to load page
#         time.sleep(SCROLL_PAUSE_TIME)
#         # Calculate new scroll height and compare with last scroll height
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             print("진입" + str(i))
#             try:
#                 driver.find_element_by_css_selector(
#                     "# nongsaroApiLoadingAreaResult > div > div > div.pagination > strong > a:nth-child(" + str(i) + ")").click()
#                 test = driver.find_element_by_css_selector(
#                     "# nongsaroApiLoadingAreaResult > div > div > div.pagination > strong > a:nth-child(" + str(i) + ")")
#                 print(test)
#             except:
#                 break
#         last_height = new_height
#
# # images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# count = 1
#
# time.sleep(10)
