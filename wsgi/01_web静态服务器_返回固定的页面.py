
import socket

def main():
    # 1. 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定本地信息
    server_socket.bind(("", 8889))
    # 3. 变为监听套接字
    server_socket.listen(128)
    # 4. 等待对方链接
    while True:
        new_socket, new_addr = server_socket.accept()
        print(new_socket, new_addr)


        # 接收数据
        new_socket.recv(1024)
        # 提取请求的文件(index.html)

        # 读取文件数据
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "\r\n"
        response_body = "hello"

        response = response_header + response_body
        # 将数据返回给浏览器
        new_socket.send(response.encode('utf-8'))
        # 关闭套接字
        new_socket.close()


if __name__ == '__main__':
    main()