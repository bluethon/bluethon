# Crontab Notes

## Note

### Docker Debian cron not work

> <https://stackoverflow.com/a/38850273/4757521>

`Docker debian`镜像存在bug(overlays), 需要重新生成新的文件才行

    # 重新生成文件
    echo ff > /etc/crontab

### 查看

    crontab -u user1 -l
    crontab -l

### 编辑(必须保存退出文件才生效)

    crontab -e

### 日志

    vim /var/log/syslog
