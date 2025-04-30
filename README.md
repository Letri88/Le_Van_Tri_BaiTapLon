# Tra Cứu Phạt Nguội (Tự Động)

Dự án Python tự động truy cập trang web phạt nguội [https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html](https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html)
. Sử dụng **Selenium** để điều khiển trình duyệt, xử lý mã Captcha bằng **Tesseract OCR** và có khả năng lập lịch chạy mỗi ngày vào 6:00 và 12:00 bằng thư viện **Schedule**.
## Tính năng
- Tự động nhập biển số, loại phương tiện và Captcha.
- Đọc ảnh Captcha bằng thư viện Tesseract OCR.
- Lưu lại ảnh Captcha gốc và đã xử lý để kiểm tra.
- Lập lịch chạy tự động mỗi ngày bằng `schedule`.
## 📥 Cài đặt

### 1. Clone project về máy
```bash
git clone https://github.com/Letri88/Le_Van_Tri_BaiTapLon.git
cd Le_Van_Tri_BaiTapLon
```
### 2. Cài đặt thư viện
chạy câu lệnh
```bash
pip freeze > requirements.txt
```
### 3. Cài đặt Tesseract OCR
- Tải [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Mở file Python và chỉnh dòng sau theo đúng đường dẫn:
  ```py
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```
### 4.Cách dùng 
#### 1. Sửa biển số xe cần tra cứu
- Ví dụ:
```py
input_bien_so.send_keys("74B112345")
```
#### 2. Sửa thời gain chạy 
- Ví dụ:
  ```py
  schedule.every().day.at("00:00").do(tra_cuu_phat_nguoi)
  ```
#### 3. Chạy chương trình
## Tác giả:
- Họ Tên: Lê Văn Trí
- GitHub
  [https://github.com/Letri88](https://github.com/Letri88)
- Repository:
  [https://github.com/Letri88/Le_Van_Tri_BaiTapLon](https://github.com/Letri88/Le_Van_Tri_BaiTapLon)


