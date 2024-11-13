# Sử dụng Alpine Linux nhẹ
FROM alpine:latest

# Cài đặt Netcat
RUN apk update && apk add --no-cache netcat-openbsd

# Đặt thư mục làm việc
WORKDIR /app


# Tùy chọn: mở cổng lắng nghe trong container (ví dụ cổng 1234)
EXPOSE 4449

CMD while true; do echo "Your flag: MSEC{WELCOME_TO_T00L_NetCat}" | nc -lp 4449; done

