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
git clone https://github.com/<your-username>/tra-cuu-phat-nguoi.git
cd tra-cuu-phat-nguoi
