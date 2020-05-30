# Windows Command

## run(Win+R)

    %appdata%                   appdata/roaming
    %userprofile%               user home
    shell:Startup               开机启动(当前用户)
    shell:Common Startup        开机启动(所有用户)

## cmd

    slmgr.vbs -upk              卸载激活
    slmgr.vbs -xpr              激活(是否)
    slmgr.vbs -dli              激活(系统版本、部分产品密钥、许可证状态)
    slmgr.vbs -dlv              激活(最详细)
    wmic os get caption         windows版本
    slmgr.vbs /skms <server>:<port>
                                可以指定端口
    
    taskkill /f /im notepad.exe 批量结束进程

---

### 定时休眠(Admin)

    # 开启休眠
    powercfg -h on
    # 添加计划任务
    # 名称为<my-standby>
    # 计划执行时间为20:30
    schtasks /create /tn <my-standby> /tr "rundll32.exe powrprof.dll,SetSuspendState" /sc once /st 20:30

### 添加自启动服务

    # 创建
    sc create <name> binPath= C:\path\to\exe.exe start= auto
    # 修改设置
    sc config KMSserver displayName= KMS-Mi-Server

### vlmcsd(active)

    docker run -d -p 1688:1688 --restart=always --name vlmcsd mikolatero/vlmcsd

- [official](http://wind4.github.io/vlmcsd/)
- [KMS Client Setup Keys](https://docs.microsoft.com/zh-cn/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj612867(v=ws.11))
