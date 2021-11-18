# Windows Debug

## win10应用商店不能下载

退出当前Microsoft账户, 创建一个普通账户, 然后下载(重装应用商店?), 然后切换回来就可以了

## 迁移系统后休眠失效(hibernate not working)

> <https://www.zhihu.com/question/395989522/answer/1847777547>

硬盘对拷或系统迁移后efi分区不一致造成的。若是GPT+UEFI形式的话，用win10的bcdboot修复引导，先用dg等分区工具给系统盘的efi分区指定盘符,如：Z，然后管理员运行cmd

    bcdboot C:\Windows  /s Z: /f uefi /l zh-cn

然后重启

PS:

重启后发现休眠功能关闭, 打开, cmd

    powercfg -h on
