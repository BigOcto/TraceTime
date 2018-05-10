## 脚本使用说明

#环境： python 2.7

#执行方式： python trace_time.py -t xx -p xx -d xx

#参数说明：

-t --time  次数

-p --version_pre  收集至excel中，列第一行标题，示例：M3_1 后面版本会自动获取补全，最终显示为 M3_1_versionName=8.x

-d --device  指定特定的设备，在电脑连接多台设备时使用

-m --mode 默认time，手机手机启动时间；其他，多台设备同时启动，对比启动速度，不收集日志