# Windows Notes

## Debug

### win10应用商店不能下载

退出当前Microsoft账户, 创建一个普通账户, 然后下载(重装应用商店?), 然后切换回来就可以了

## Note

### 系统工具库(检查自启动等)

[Sysinternals Suite](https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite)

### win10 网络连接 文件夹为空

> <https://blog.csdn.net/jizhitp/article/details/52771509>

- netsh winsock  reset
- netcfg -d
- 重启

### 带UAC的自启动

创建任务计划程序, 里面开启最高权限运行选项, 参考坚果云备份的任务
