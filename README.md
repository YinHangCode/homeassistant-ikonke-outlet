# homeassistant-ikonke-outlet

HomeAssistant的控客插座插件。   
   
**注: 如果有bug请提交到 [issues](https://github.com/YinHangCode/homeassistant-ikonke-outlet/issues) 或 [QQ群: 107927710](//shang.qq.com/wpa/qunwpa?idkey=8b9566598f40dd68412065ada24184ef72c6bddaa11525ca26c4e1536a8f2a3d)。**   

![](https://raw.githubusercontent.com/YinHangCode/homeassistant-ikonke-outlet/master/images/K2.jpg)
![](https://raw.githubusercontent.com/YinHangCode/homeassistant-ikonke-outlet/master/images/K2Pro.jpg)
![](https://raw.githubusercontent.com/YinHangCode/homeassistant-ikonke-outlet/master/images/MiniB.jpg)
![](https://raw.githubusercontent.com/YinHangCode/homeassistant-ikonke-outlet/master/images/MiniW.jpg)

## 支持的设备
1.K2   
2.K2 Pro   
3.K Mini Pro   
4.K Mini   

## 安装说明
1.安装HomeAssistant。   
2.安装[ikonkeIO](https://github.com/YinHangCode/ikonkeIO)。   
3.将homeassistant-ikonke-outlet.py文件放到~/.homeassistant/custom_components/switch/下。

## 配置说明
配置"ikonkeIO"为ikonkeIO目录下sh文件的绝度路径。   
设备的"type"、"ip"、"mac"、"password"可以通过ikonkeIO获取，具体参考[ikonkeIO](https://github.com/YinHangCode/ikonkeIO)项目。   
示例如下：   
```
switch:
  - platform: homeassistant-ikonke-outlet
    ikonkeIO: '/home/pi/ikonkeIO/ikonkeIO.sh'
    deviceCfgs:
      - type: 'k2pro'
        ip: '192.168.88.42'
        mac: '28-d0-8a-08-79-4d'
        password: '36629'
      - type: 'k2'
        ip: '192.168.88.43'
        mac: '28-d0-8a-02-3f-e6'
        password: '88663'
      - type: 'mini_b'
        ip: '192.168.88.41'
        mac: '28-d0-8a-81-77-5f'
        password: 'eA,-J=57'
```
## 版本更新记录
### 0.0.3
1.修复密码的首字母是"/"的情况下报错的bug.   
### 0.0.2
1.增加设备available状态.   
### 0.0.1
1.支持控制K2设备.   
2.支持控制K2 Pro设备.   
3.支持控制K Mini Pro设备.   
