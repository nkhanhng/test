from mongoengine import*

# Create collection - Tạo tủ
class Phone(Document):
    product_main_image = StringField() # Ảnh sản phẩm
    product_size_image = StringField() # Ảnh kích cỡ sản phẩm
    product_name = StringField() # Tên sản phẩm
    #1. Màn hình
    display_technology = StringField() # Công nghệ màn hình
    display_resolution = StringField() # Độ phân giải
    display_size = StringField() # Màn hình rộng
    display_screen = StringField() # Mặt kính cảm ứng
    #2. Camera sau
    back_cam_re = StringField() # Độ phân giải
    back_cam_vid_rercord = StringField() # Quay phim
    back_cam_flash = StringField() # Đèn Flash
    back_cam_features = StringField() # Các tính năng chụp ảnh nâng cao
    #3. Camera trước
    front_cam_res = StringField() # Độ phân giải
    front_cam_vid_call = StringField() # Videocall
    front_cam_features = StringField() # Các tính năng khác
    #4. Hệ điều hành-CPU
    operating_system = StringField() # Hệ điều hành
    chipset = StringField() # CPU
    chipset_speed = StringField() # Tốc độ CPU
    chipset_gpu = StringField() # Chip đồ họa(GPU)
    #5. Bộ nhớ và lưu trữ
    ram = StringField() # RAM
    rom = StringField() # Bộ nhớ trong
    rom_available = StringField() # Bộ nhớ khả dụng
    external_storage = StringField() # Bộ nhớ gắn ngoài
    #6. Kết nối
    data = StringField() # Mạng di động
    sim = StringField() # Loại SIM
    wifi = StringField() # Kết nối Wifi
    gps = StringField() # Công nghệ GPS
    bluetooth = StringField() # bluetooth
    port = StringField() # Cổng kết nối/sạc
    headphone_jack = StringField() # Jack tai nghe
    other_connection = StringField() # Kết nối khác
    #7. Thiết kế và Trọng lượng
    design = StringField() # Thiết kế
    material = StringField() # Chất liệu
    phone_dimension = StringField() # Kích thước
    weight = StringField() # Trọng lượng
    #8. Thông tin pin & Sạc
    battery_capacity = StringField() # Dung lượng pin
    battery_type = StringField()  # Loại pin
    battery_technology = StringField() # Công nghệ pin
    #9. Tiện ích
    protection = StringField() # Bảo mật nâng cao
    special_features = StringField() # Tính năng đặc biệt
    recording = StringField()  # Ghi âm
    radio = StringField()  # Radio
    video_player = StringField() # Định dạng phim
    music_player = StringField() # Định dạng nhạc
    #10. Thông tin khác
    release_date = StringField() # Thời điểm ra mắt
    phone_brand_name = StringField() # Hãng sản xuất
