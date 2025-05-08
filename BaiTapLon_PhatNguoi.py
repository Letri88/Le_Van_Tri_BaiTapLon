from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from PIL import Image
import pytesseract
import schedule
from datetime import datetime
import os
from PIL import ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#3. Trích xuất mã bảo mật bằng thư viện pytesseract hoặc thư viện nào đó ra dạng text rồi nhập tự động vào ô Input, bấm tìm kiếm.
def solve_captcha(driver):
    os.makedirs("captchas", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_path = f"captchas/captcha_raw_{timestamp}.png"
    processed_path = f"captchas/captcha_processed_{timestamp}.png"
    captcha_img = driver.find_element(By.XPATH, '//*[@id="imgCaptcha"]')
    captcha_img.screenshot(raw_path)
    captcha_image = Image.open(raw_path)
    captcha_image = captcha_image.convert("L") 
    captcha_image = captcha_image.resize((captcha_image.width * 3, captcha_image.height * 3))  # Phóng to
    captcha_image = captcha_image.filter(ImageFilter.SHARPEN)  # Làm nét
    captcha_image = captcha_image.point(lambda x: 0 if x < 140 else 255, '1')  # Threshold
    captcha_image.save(processed_path)
    captcha_text = pytesseract.image_to_string(
        captcha_image,
        config='--psm 8 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ).strip()
    print(f"[OCR] Captcha đọc được: {captcha_text}")
    return captcha_text
def tra_cuu_phat_nguoi():
    print(f"[{datetime.now()}] Bắt đầu tra cứu...")
    driver = webdriver.Chrome()
    #1.Vào website đã chọn.
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
    time.sleep(3)
    # 2. Nhập các thông tin Biển số xe, chọn loại phương tiện, 
    try:
        input_bien_so = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[1]/input')
        input_bien_so.send_keys("74B175757") 
        type_vehicle = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[2]/select/option[2]')
        type_vehicle.click()
        captcha_text = solve_captcha(driver)
        captcha_input = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[3]/div/input')
        captcha_input.send_keys(captcha_text)
        # 4. Kiểm tra kết quả phạt nguội.
        driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/input[1]').click()
        time.sleep(5)
        print("Đã tra cứu.")
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        driver.quit()
    #5. Set lịch chạy 6h sáng và 12h trưa hằng ngày.
schedule.every().day.at("06:00").do(tra_cuu_phat_nguoi)
schedule.every().day.at("12:00").do(tra_cuu_phat_nguoi)
print("Đang đợi tới giờ chạy.")
while True:
    schedule.run_pending()
    time.sleep(30)
