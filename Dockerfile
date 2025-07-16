FROM python:3.10-slim

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Copy toàn bộ code vào container
COPY . /app

# Cài pip mới nhất và các thư viện cần thiết
RUN pip install --upgrade pip
RUN pip install flask gunicorn skyfield pyswisseph timezonefinder geopy pytz

# Expose cổng 5000
EXPOSE 5000

# Lệnh chạy ứng dụng
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
