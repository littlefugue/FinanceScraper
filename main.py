#%%
import urllib.request
from bs4 import BeautifulSoup
import dart_fss as dart

API_KEY = '336d2dad4c37d6904db39122122510942dc9de6a'  # open dart 인증키
dart.set_api_key(api_key=API_KEY)

corp_list = dart.get_corp_list()

#%%
print(corp_list.corps)
print(corp_list.sectors)

#%%
tg = corp_list.find_by_corp_name(corp_name='태경케미컬')
print(tg)
report = tg[0].extract_fs(bgn_de=20200101)

#%%
print(type(report), report)
report.save()
