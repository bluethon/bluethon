Django Tutorial Note
====================

Chapter 2
---------

### 查询时pk可以指代id

    q = Question.objects.get(pk=1)

### 通过[多端]的field_set可以获取外键的model对象

> <https://docs.djangoproject.com/en/dev/ref/models/relations/>

    q.choice_set.all()

### 通过[多端]对象_set获取后创建[一端]Choice对象, [一端]外键自动赋值

    c = q.choice_set.create(choice_text='Not much', votes=0)
    c.question  # q

### Use double underscores to separate relationships.

    Choice.objects.filter(question__pub_date__year=current_year)
    question__pub_date__year == question.pub_date.year

### delete instance(don't need save)

    instance.delete()

Chapter 4
---------

### `for`tag已循环次数

    forloop.counter

### `request.POST`

- `request.POST` values are always strings.
- 成功处理POST请求后一定要返回一个redirect

### `DetailView`

- default template name = `<app name>/<model name>_detail.html`

Chapter 7
---------

### 查找django源文件 source file

    python -c "import django; print(django.__path__)"
