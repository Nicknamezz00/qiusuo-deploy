FROM ubuntu:20.04

# 选用国内镜像源以提高下载速度
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list
RUN  apt clean
RUN  apt update
RUN apt install -y build-essential python3 python3-pip pip

# 拷贝当前项目到/app目录下
COPY . /app

# 设定当前的工作目录
WORKDIR /app

# 安装依赖到指定的/install文件夹
# 选用国内镜像源以提高下载速度
RUN systemctl restart systemd-timesyncd.service
RUN pip config set global.index-url http://pypi.tuna.tsinghua.edu.cn/simple \
&& pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn \
# && pip install --upgrade pip \
# pip install scipy 等数学包失败，可使用 apk add py3-scipy 进行， 参考安装 https://pkgs.alpinelinux.org/packages?name=py3-scipy&branch=v3.13
&& pip install --user -r requirements.txt

# 设定对外端口
EXPOSE 80

# 设定启动命令
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]