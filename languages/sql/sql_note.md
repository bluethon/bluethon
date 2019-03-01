SQL Note
=========

CMD
---

``` sql
select * from t1 where id <10 into outfile "D:\\xxx.txt"    # 不带列名
where c1 IS NOT NULL AND c1 <> ''   # 不为空(1)
where length(c1) > 0    # 不为空(2)
```

Note
----

### update

    update tables set name='simaopig' where name='xiaoxiaozi'

### delete

    delete from table where column_name = value
