import hashlib

def blake2(message):
    """Hàm tính toán giá trị băm BLAKE2b cho chuỗi đầu vào."""
    blake2_hash = hashlib.blake2b(digest_size=64)  
    blake2_hash.update(message.encode('utf-8'))  
    return blake2_hash.digest()  

def main():
    text = input("Nhập chuỗi văn bản: ")

    hashed_text = blake2(text)

    print("Chuỗi văn bản đã nhập: {}".format(text))
    print("BLAKE2b Hash: {}".format(hashed_text.hex()))  

if __name__ == "__main__":
    main()
