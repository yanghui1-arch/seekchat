# seekchat
You can talk to the ai while knowing what others have said to the ai as a way to talk across the room.

# Install
```python
conda create -n "seekchat" python==3.10
conda activate seekchat
pip install -r requirements.txt
```
mysql脚本
```mysql
create database seekchat;
create table message
(
    id           int auto_increment
        primary key,
    message      varchar(3500) null,
    message_time datetime      not null
);
```

# 使用
1. 运行main.py
2. 打开index.html
3. 开始对话

# 项目整体截图
![image](https://github.com/user-attachments/assets/93aa8855-8615-4a0c-8787-1db660a2231e)
