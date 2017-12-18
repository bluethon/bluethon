FLask Code Note
===============

### 上下文

产生请求的上下文

    with app.test_request_context():
        print(url_for('item', id='1'))
