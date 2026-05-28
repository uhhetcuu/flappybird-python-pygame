# Flappy Bird Python Pygame

**Sinh viên thực hiện:** Nguyễn Vũ Hoàng
**Mã sinh viên:** 3025113622

---

## Giới thiệu

Đây là project đồ án môn học làm game Flappy Bird bằng Python sử dụng thư viện Pygame.

Game mô phỏng theo Flappy Bird cơ bản. Người chơi điều khiển chim vượt qua các pipe để ghi điểm. Nếu va chạm với pipe hoặc rơi xuống đất thì game kết thúc.

---

## Công nghệ sử dụng

* Python
* Pygame
* Visual Studio Code

---

## Chức năng của game

* Điều khiển chim bằng phím Space
* Chim có trọng lực
* Pipe sinh ngẫu nhiên
* Tính điểm
* Va chạm game over
* Âm thanh khi chơi
* Chơi lại sau khi thua

---

## Cấu trúc project

```text id="ecbql4"
BÀI TẬP ĐỒ ÁN/
│
├── assets/
├── sound/
├── bird.py
├── pipe.py
├── settings.py
├── game.py
└── main.py
```

---

## Cách cài đặt

Cài thư viện pygame:

```bash id="l74byu"
pip install pygame
```

---

## Cách chạy game

Mở terminal trong thư mục project rồi chạy:

```bash id="bm7f4s"
python main.py
```

---

## Cách chơi

* Nhấn Space để chim bay
* Vượt qua pipe để cộng điểm
* Chạm pipe hoặc rơi xuống đất sẽ thua
* Sau khi game over có thể nhấn Space để chơi lại

---

## Các tài nguyên sử dụng

### Hình ảnh

* background-day.png
* base.png
* pipe-green.png
* yellowbird-downflap.png
* yellowbird-midflap.png
* yellowbird-upflap.png
* gameover.png
* message.png
* 0.png đến 9.png

### Âm thanh

* wing.wav
* point.wav
* hit.wav
* die.wav
* swoosh.wav

---

## Kết quả đạt được

Sau khi hoàn thành project em đã:

* hiểu cách làm game bằng pygame
* xử lý va chạm
* sử dụng OOP trong Python
* làm việc với hình ảnh và âm thanh trong game

Project vẫn còn đơn giản nhưng giúp em hiểu thêm về lập trình game 2D bằng Python.
