import socket
import os
from datetime import datetime

# 서버 설정
HOST = '127.0.0.1'  # 로컬호스트
PORT = 8000        # 사용할 포트 번호

# "request" 폴더가 없으면 생성
if not os.path.exists('request'):
    os.makedirs('request')

# 소켓 서버 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버 대기 중...')
    conn, addr = s.accept()
    with conn:
        print(f'{addr} 연결됨.')
        data = conn.recv(1024)
        if data:
            # 현재 시간을 파일명으로 사용하여 이진 파일 저장
            filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".bin"
            filepath = os.path.join('request', filename)
            with open(filepath, 'wb') as f:
                f.write(data)
            print(f'요청을 {filepath}에 저장했습니다.')
