from urllib.request import urlopen
from bs4 import BeautifulSoup
import mlab
from models.phone import Phone
from random import randint, choice
from faker import Faker
from selenium import webdriver
import time

mlab.connect()

link1 = "https://www.thegioididong.com/dtdd/bkav-bphone-2"

# samsung = "Samsung"
# iphone = "iPhone (Apple)"
# oppo = "OPPO"
# sony = "Sony"
# nokia = "Nokia"
# vivo ="Vivo"
# huawei = "Huawei"
# xiaomi = "Xiaomi"
# motorola = "Motorola"
# asus = "Asus (Zenfone)"
# htc = "HTC"
# mobiistar = "Mobiistar"
# mobell = "Mobell"
# philips = "Philips"
# itel = "Itel"
# bkav = "BKAV"
# if "samsung" in link1:
#     phone_brand_name = samsung
# elif "iphone" in link1:
#     phone_brand_name = iphone
# elif "oppo" in link1:
#     phone_brand_name = oppo
# elif "sony" in link1:
#     phone_brand_name = sony
# elif "nokia" in link1:
#     phone_brand_name = nokia
# elif "vivo" in link1:
#     phone_brand_name = vivo
# elif "huawei" in link1:
#     phone_brand_name = huawei
# elif "xiaomi" in link1:
#     phone_brand_name = xiaomi
# elif "motorola" in link1:
#     phone_brand_name = motorola
# elif "asus" in link1:
#     phone_brand_name = asus
# elif "htc" in link1:
#     phone_brand_name = htc
# elif "mobiistar" in link1:
#     phone_brand_name = mobiistar
# elif "mobell" in link1:
#     phone_brand_name = mobell
# elif "philips" in link1:
#     phone_brand_name = philips
# elif "itel" in link1:
#     phone_brand_name = itel
# elif "bkav" in link1:
#     phone_brand_name = bkav

#
# browser = webdriver.Firefox()
# browser.get(link1)
quote_page1 = link1

page1 = urlopen(quote_page1).read()

soup1 = BeautifulSoup(page1, "html.parser")

# elem = browser.find_element_by_xpath("//*[@class='tableparameter']//*[text()='Xem cấu hình chi tiết']")
# elem.click()
# time.sleep(0.2)
# elem = browser.find_element_by_xpath('//*')

# soup3 = BeautifulSoup(elem.get_attribute("outerHTML"), "html.parser")

product_name = soup1.find('div', class_='rowtop').find('h1').text
if 'Điện thoại' in product_name:
    product_name = product_name.replace('Điện thoại','')
print(product_name)
# product_main_image = soup1.find('div', id='normalproduct').find('aside', class_= 'picture').find('img').get('src')
# product_size_image = soup3.find('img', id='imgKit').get('src')
#
# phone = soup3.find('ul', class_='parameterfull').findAll('li')
# for index, item in enumerate(phone):
#     try:
#         x = item.find('div').text
#         if index == 1:
#             display_technology = x
#         elif index == 2:
#             display_resolution = x # Độ phân giải
#         elif index == 3:
#             display_size = x # Màn hình rộng
#         elif index == 4:
#             display_screen = x # Mặt kính cảm ứng
#         elif index == 6:
#             back_cam_re = x # Độ phân giải
#         elif index == 7:
#             back_cam_vid_rercord = x # Quay phim
#         elif index == 8:
#             back_cam_flash = x # Đèn Flash
#         elif index == 9:
#             back_cam_features = x # Các tính năng chụp ảnh nâng cao
#         elif index == 11:
#             front_cam_res = x # Độ phân giải
#         elif index == 12:
#             front_cam_vid_call = x # Videocall
#         elif index == 13:
#             front_cam_features = x # Các tính năng khác
#         elif index == 15:
#             operating_system = x # Hệ điều hành
#         elif index == 16:
#             chipset = x # CPU
#         elif index == 17:
#             chipset_speed = x # Tốc độ CPU
#         elif index == 18:
#             chipset_gpu = x # Chip đồ họa(GPU)
#         elif index == 20:
#             ram = x # RAM
#         elif index == 21:
#             rom = x # Bộ nhớ trong
#         elif index == 22:
#             rom_available = x # Bộ nhớ khả dụng
#         elif index == 23:
#             external_storage = x # Bộ nhớ gắn ngoài
#         elif index == 25:
#             data = x # Mạng di động
#         elif index == 26:
#             sim = x # Loại SIM
#         elif index == 27:
#             wifi = x # Kết nối Wifi
#         elif index == 28:
#             gps = x # Công nghệ GPS
#         elif index == 29:
#             bluetooth = x # bluetooth
#         elif index == 30:
#             port = x # Cổng kết nối/sạc
#         elif index == 31:
#             headphone_jack = x # Jack tai nghe
#         elif index == 32:
#             other_connection = x # Kết nối khác
#         elif index == 34:
#             design = x # Thiết kế
#         elif index == 35:
#             material = x # Chất liệu
#         elif index == 36:
#             phone_dimension = x # Kích thước
#         elif index == 37:
#             weight = x # Trọng lượng
#         elif index == 39:
#             battery_capacity = x # Dung lượng pin
#         elif index == 40:
#             battery_type = x  # Loại pin
#         elif index == 41:
#             battery_technology = x # Công nghệ pin
#         elif index == 43:
#             protection = x # Bảo mật nâng cao
#         elif index == 44:
#             special_features = x # Tính năng đặc biệt
#         elif index == 45:
#             recording = x  # Ghi âm
#         elif index == 46:
#             radio = x  # Radio
#         elif index == 47:
#             video_player = x # Định dạng phim
#         elif index == 48:
#             music_player = x # Định dạng nhạc
#         elif index == 50:
#             release_date = x # Thời điểm ra mắt
#     except:
#         pass
#
# browser.quit()
#
# phone = Phone(
#     product_main_image = product_main_image, # Ảnh sản phẩm
#     product_size_image = product_size_image, # Ảnh kích cỡ sản phẩm
#     product_name = product_name, # Tên sản phẩm
#     #1. Màn hình
#     display_technology = display_technology, # Công nghệ màn hình
#     display_resolution = display_resolution, # Độ phân giải
#     display_size = display_size, # Màn hình rộng
#     display_screen = display_screen, # Mặt kính cảm ứng
#     #2. Camera sau
#     back_cam_re = back_cam_re, # Độ phân giải
#     back_cam_vid_rercord = back_cam_vid_rercord, # Quay phim
#     back_cam_flash = back_cam_flash, # Đèn Flash
#     back_cam_features = back_cam_features, # Các tính năng chụp ảnh nâng cao
#     #3. Camera trước
#     front_cam_res = front_cam_res, # Độ phân giải
#     front_cam_vid_call = front_cam_vid_call, # Videocall
#     front_cam_features = front_cam_features, # Các tính năng khác
#     #4. Hệ điều hành-CPU
#     operating_system = operating_system, # Hệ điều hành
#     chipset = chipset, # CPU
#     chipset_speed = chipset_speed, # Tốc độ CPU
#     chipset_gpu = chipset_gpu, # Chip đồ họa(GPU)
#     #5. Bộ nhớ và lưu trữ
#     ram = ram, # RAM
#     rom = rom, # Bộ nhớ trong
#     rom_available = rom_available, # Bộ nhớ khả dụng
#     external_storage = external_storage, # Bộ nhớ gắn ngoài
#     #6. Kết nối
#     data = data, # Mạng di động
#     sim = sim, # Loại SIM
#     wifi = wifi, # Kết nối Wifi
#     gps = gps, # Công nghệ GPS
#     bluetooth = bluetooth, # bluetooth
#     port = port, # Cổng kết nối/sạc
#     headphone_jack = headphone_jack, # Jack tai nghe
#     other_connection = other_connection, # Kết nối khác
#     #7. Thiết kế và Trọng lượng
#     design = design, # Thiết kế
#     material = material, # Chất liệu
#     phone_dimension = phone_dimension, # Kích thước
#     weight = weight, # Trọng lượng
#     #8. Thông tin pin & Sạc
#     battery_capacity = battery_capacity, # Dung lượng pin
#     battery_type = battery_type , # Loại pin
#     battery_technology = battery_technology, # Công nghệ pin
#     #9. Tiện ích
#     protection = protection, # Bảo mật nâng cao
#     special_features = special_features, # Tính năng đặc biệt
#     recording = recording , # Ghi âm
#     radio = radio , # Radio
#     video_player = video_player, # Định dạng phim
#     music_player = music_player, # Định dạng nhạc
#     #10. Thông tin khác
#     release_date = release_date, # Thời điểm ra mắt
#     phone_brand_name = phone_brand_name,
#                 )
# phone.save()
