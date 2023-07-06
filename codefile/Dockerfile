# 使用官方Python 3.8基础镜像
FROM python:3.8

# 创建工作目录
WORKDIR /app

#换源
RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list

# 更新系统及安装相关依赖
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# 升级pip
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

# 安装numpy, opencv-python, Pillow（PIL)
RUN pip install numpy opencv-python pillow -i https://pypi.tuna.tsinghua.edu.cn/simple