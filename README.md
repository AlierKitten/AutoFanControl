# AutoFanControl

为解决树莓派风扇一直转又不想采用降压减速，关机时风扇不会停转的问题设计了这个简单的程序，可自定义起转温度和停转温度

项目使用了一个PNP三极管（S9012）通过读取本地的CPU温度文件来实现对风扇控制

当温度到达阈值时才会启动，当温度到达停转阈值后会继续工作20S才会停转

原理图如下：

![](https://github.com/AlierKitten/AutoFanControl/blob/main/Schematic.png)


## 开机自启动程序

<!--为了让风扇达到自动控制-->

`sudo nano /etc/systemd/system/AutoFanControl_PNP.service`


在文件中添加以下内容

>[Unit]
>Description=AutoFanControl_PNP
>
>[Service]
>ExecStart=/usr/bin/python3 /home/pi/T
pycharm/fan_speed.py
>WorkingDirectory=/home/pi/pycharm/
>StandardOutput=inherit
>StandardError=inherit
>Restart=always
>User=pi
>
>[Install]
>WantedBy=multi-user.target

启用并启动服务：

`sudo systemctl enable AutoFanControl_PNP.service`

`sudo systemctl start AutoFanControl_PNP.service`
