import socket
import os
from datetime import datetime

# 서버 설정
HOST = '127.0.0.1'  # 로컬호스트
PORT = 8000        # 사용할 포트 번호

# "images" 폴더가 없으면 생성
if not os.path.exists('images'):
    os.makedirs('images')

def save_image(data):
    filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".jpg"
    filepath = os.path.join('images', filename)
    with open(filepath, 'wb') as f:
        f.write(data)
    return filepath

# 소켓 서버 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버 대기 중...')
    conn, addr = s.accept()
    with conn:
        print(f'{addr} 연결됨.')
        data = conn.recv(1024 * 1024)  # 이미지 데이터는 더 클 수 있으므로 1MB 크기
        if data:
            # 이미지 파일 저장
            filepath = save_image(data)
            print(f'이미지를 {filepath}에 저장했습니다.')
