import base64

def main():
    input_string = input("Nhập thông tin cần mã hóa: ")
    
    # Mã hóa chuỗi thành Base64
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")

    # Ghi vào tệp
    with open("data.txt", "w") as file:
        file.write(encoded_string)

    print("Đã mã hóa và ghi vào tệp data.txt")

if __name__ == "__main__":
    main()