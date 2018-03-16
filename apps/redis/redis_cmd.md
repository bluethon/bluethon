cmd
---

    dbsize      # 键总数 O(1)
    keys *      # 输出所有键(线上禁用) O(n)

    set <key> <value>       # 字符串

    rpush listkey c b a             # 右插入
    lrange listkey 0 -1             # 左到右获取所有元素
    lpush key value [value]
    linsert key before|after pivot value    # 找到pivot, 插入value

