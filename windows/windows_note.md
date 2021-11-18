# Windows Notes

## 系统工具库(检查自启动等)

[Sysinternals Suite](https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite)

## win10 网络连接 文件夹为空

> <https://blog.csdn.net/jizhitp/article/details/52771509>

- netsh winsock  reset
- netcfg -d
- 重启

## 带UAC的自启动

创建任务计划程序, 里面开启最高权限运行选项, 参考坚果云备份的任务

## 休眠自启动

> https://superuser.com/a/15801/603441

管理员执行`powercfg -lastwake`, 找出设备名称, `计算机-管理-设备属性-电源管理`, 关闭允许唤醒

## 设置等默认开机输入法

> https://github.com/microsoft/terminal/issues/1304#issuecomment-706784166

- 系统语言设置中文/简体删除美式键盘
- 添加英语/美国
- 切换热键修改
  - 输入 / 高级键盘设置 /语言栏选项 / 高级键设置 / 在输入语音之间 / Ctrl+Shift
