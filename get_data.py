import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

def parse(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    title = driver.find_element(By.XPATH, "//*[@class='title-brand flex ng-star-inserted']").text
    price = driver.find_element(By.CLASS_NAME, 'price__main-value').text
    price = price.replace('₽','')
    price = price.replace(' ','')
    try:
        description = driver.find_element(By.XPATH, "//*[@class='description with-overflow']").text
    except:
        description = driver.find_element(By.XPATH, "//*[@class='description']").text
    id = int(driver.find_element(By.XPATH, "//*[@class='code']").text.replace(' ','').split(':')[1])

    driver.quit()
    url_data = f'https://www.mvideo.ru/bff/product-details?productId={id}'
    # нужно периодически менять куки
    # и юзер агента если у вас другой браузер в моем случае chrome
    headers = {
        'Cookie':'MVID_GUEST_ID=22629179949; MVID_VIEWED_PRODUCTS=; _ym_d=1687180014; _ym_uid=1687180014711854943; _gid=GA1.2.790768745.1687180014; afUserId=3dc9886c-37e6-4d6c-ad6a-ba51e3ca50d6-p; sub_id1_c=99333; sub_id2_c=015dcd76c95cee7a5ed0c21ac0a420b5cc1fdaf5; partnerSrc=advcake; advcake_click_id=015dcd76c95cee7a5ed0c21ac0a420b5cc1fdaf5; advcake_utm_partner=99333; advcake_utm_webmaster=gdeslon; __cpatrack=advcake_cpa; __SourceTracker=advcake__cpa; admitad_deduplication_cookie=advcake__cpa; __allsource=advcake; __sourceid=advcake; advcake_session_id=d21f9cb1-ba07-aa9f-55b2-46556349aad7; __lhash_=73bea785b7a6898e1c9f4ef7941365f8; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=09ee8519-1001-4f8c-9620-6d71cf1b6515; flocktory-uuid=d2ee5949-94a7-46a2-b896-e40c90f3d7ed-0; tmr_lvid=c0aceac0c98765815bb45d42bc560f44; tmr_lvidTS=1687180022509; AF_SYNC=1687180023012; uxs_uid=2f31fcc0-0ea2-11ee-ad37-35598ba35a7f; adrcid=AD-WGJKk6VcCjtMsTSayh_g; cookie_ip_add=188.17.213.211; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=false; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=false; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; HINTS_FIO_COOKIE_NAME=2; searchType2=1; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; sub_id1_c=99333; sub_id2_c=015dcd76c95cee7a5ed0c21ac0a420b5cc1fdaf5; partnerSrc=advcake; advcake_track_id=46b1229b-c9cd-87e4-d968-2a1c5a6c5dc0; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Ftelevizor-hisense-65a6bg-10030413%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D99333%26advcake_params%3D015dcd76c95cee7a5ed0c21ac0a420b5cc1fdaf5%26sub_id1%3D99333%26sub_id2%3D015dcd76c95cee7a5ed0c21ac0a420b5cc1fdaf5; deviceType=desktop; _ym_isad=2; MVID_ENVCLOUD=prod1; __hash_=0478b54a57998f66675b9f941384457b; JSESSIONID=snbPkSCBYDpvrVHwMJJ6FVTRCGpsFVnBDCq3QdjvhyyqKpn3JBfw!-1242052088; CACHE_INDICATOR=false; BIGipServeratg-ps-prod_tcp80=1678040074.20480.0000; bIPs=389543560; mindboxDeviceUUID=580b8a9f-cc8a-4024-9663-bb1d685602b6; directCrm-session=%7B%22deviceGuid%22%3A%22580b8a9f-cc8a-4024-9663-bb1d685602b6%22%7D; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _ga=GA1.2.442902570.1687180014; _dc_gtm_UA-1873769-37=1; tmr_detect=0%7C1687290581350; gsscgib-w-mvideo=8QP5f8uTN0sccxGJm+3jZu3kiQ1GUlEPKJBR5SKTXT55pGxZB0CgtqYZm6H897E7qtsb1tDJtvHeKNJJWKIEXmPJdqqfRJPEn9If5i7ozuQkO8mJI/nLJTA//X81Z9aT2EQlVmeXK+lNLpxeJSzW+NvdxDOK0/bJGr8hCvhHHgja5WTxgmiYPFG/FgzwytTDjrjHz8zOEEewV4qe4cP3huaVDj7JpK/MF+kBoVnyTHmRbFmkOLm0QDD3s62Rs8PB3m7W9/Mw; gsscgib-w-mvideo=8QP5f8uTN0sccxGJm+3jZu3kiQ1GUlEPKJBR5SKTXT55pGxZB0CgtqYZm6H897E7qtsb1tDJtvHeKNJJWKIEXmPJdqqfRJPEn9If5i7ozuQkO8mJI/nLJTA//X81Z9aT2EQlVmeXK+lNLpxeJSzW+NvdxDOK0/bJGr8hCvhHHgja5WTxgmiYPFG/FgzwytTDjrjHz8zOEEewV4qe4cP3huaVDj7JpK/MF+kBoVnyTHmRbFmkOLm0QDD3s62Rs8PB3m7W9/Mw; _sp_id.d61c=abdfabcb-d277-4f20-8907-e02484cd7a7e.1687180014.6.1687290621.1687286141.8ab2a8d9-5c35-4cba-8f94-06e0052da88d.b44708ee-1ccc-4f98-8692-ed79a7ece3a5.25a5e4a4-2c71-4a4b-9cd1-b25ee0babd03.1687290568203.12; fgsscgib-w-mvideo=uAFV8fa672600461d2c083b68df4405b07025f42; fgsscgib-w-mvideo=uAFV8fa672600461d2c083b68df4405b07025f42; gssc218=; cfidsgib-w-mvideo=JsNXPCb1sGp+DW6bnwXPEk5wkIYxYDP5pMLP43u548TzgISZd3aZkfgx1vfSlw8/Yt+6788mnQe7H+/IhO+MTuIEIA3JoHDxQAaER6RhGemZEWWwRVM35lSwXhNqyGmuhHOUy1+pzLqctSgqKn18eakrurLgXv4Ar7/V58M=; _ga_BNX5WPP3YK=GS1.1.1687290568.6.1.1687290625.3.0.0; _ga_CFMZTSS5FM=GS1.1.1687290568.6.1.1687290625.0.0.0',
        'referer':f'{url}',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    s = requests.get(url_data,headers=headers).json()

    rating = s['body']['rating'].get('star')

    return id,title,price,description,rating


