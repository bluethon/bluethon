# 透视HTTP 笔记

## HTTP 版本区别

### HTTP/0.9

1. 只允许GET
2. 响应后立即关闭连接
3. 只允许文本

### HTTP/1.0(备忘录性质, 不具有强制约束)

1. 增加了HEAD POST等新方法
2. 增加了响应状态码, 标记可能的错误原因
3. 引入了协议版本号概念
4. 引入了HTTP Header(头部)的概念, 让HTTP处理请求和响应更加灵活(?)
5. 传输的数据不仅限于文本

### HTTP/1.1(RFC2616)

2014年修订, 拆分6个小文档, RFC7230-7235, 无实质改动

1. 增加了PUT DELETE等新方法
2. 增加了缓存管理和控制
3. 明确了连接管理, 允许持久连接
4. 允许响应数据分块(chunked), 利于传输大文件
5. 强制要求Host头, 让互联网主机托管成为可能(?)

### HTTP/2(RFC7540)

解决问题: 宽带 移动 不安全, 兼容1.1

1. 二进制协议, 不再是纯文本
2. 可发起多个请求, 废弃1.1的管道
3. 使用专用算法压缩头部, 减少数据传输
4. 允许服务器主动向客户端推送数据
5. 增强安全性, "事实上"要求加密通信

## HTTP协议认识

> HTTP是一个在计算机世界里专门在两点间传输文字/图片/音频/视频等超文本数据的约定和规范

### 协议

> HTTP是一个用在计算机世界的协议, 使用计算机理解的语言确立一种计算机间交流通信的规范, 以及相关的控制和错误处理方式

### 传输

> HTTP是一个在计算机世界里专门用来在两点间传输数据的约定和规范

- 双向协议, 请求方/响应方
- 数据在A/B间传输, 但不限制于仅A/B, 运行有`中转`或`接力`, 即`中间人`, 如安全认证/数据压缩/编码转换等, 优化传输过程

### 超文本

`文本(Text)`是完整 有意义的数据, 可以被浏览器/服务器等上层应用处理, 对比: TCP/UDP中为切分后的`二进制(datagram)`

`超文本`, 包含文字/图片/音频/视频等混合体, 关键是含有`超链接`, 在超文本间跳跃, 形成复杂的非线性/网状结构关系, 例如`HTML`

## CDN

内容分发网络(Content Delivery Network), 应用HTTP中的缓存和代理技术, 代替源站响应客户端的请求

## TCP

位于IP协议之上, 基于IP协议提供可靠的、字节流形式的通信

- 可靠,保证数据不丢失
- 字节流,保证数据完整性

## DNS

`域名（Domain Name）`又称为`主机名（Host)`

## 分层模型

下述层次指OSI7层模型层次

- 四层负载均衡: 指工作在传输层上，基于 TCP/IP 协议的特性，例如 IP 地址、端口号等实现对后端服务器的负载均衡。
- 七层负载均衡: 指工作在应用层上，看到的是 HTTP 协议，解析 HTTP 报文里的 URI、主机名、资源类型等数据，再用适当的策略转发给后端服务器。
- 二层转发：设备工作在链路层，帧在经过交换机设备时，检查帧的头部信息，拿到目标mac地址，进行本地转发和广播
- 三层路由：设备工作在网络(ip)层，报文经过有路由功能的设备时，设备分析报文中的头部信息，拿到ip地址，根据网段范围，进行本地转发或选择下一个网关

UNIX域套接字可以认为在五层

### TCP和UDP区别

- TCP 有状态 需要先建立连接才能发送数据 保证数据不丢失不重复 数据是连续的字节流，有先后顺序
- UDP 无状态 不需要先建立连接也可以发送数据 不保证数据一定会发送到对方 数据是分散的小数据包，顺序发、乱序收

## 09 HTTP报文格式

    起始行      start line
    头部        header
    空行        CRLF(0x0D0A)
    实体        entity body

### 请求行(request line)

描述**客户端想要如何操作服务端的资源**

> SP -> space, CRLF -> /r/n

    Method/SP/URI/SP/Version/CRLF

1. 请求方法: 动词, GET/POST, 表示对资源的操作
2. 请求目标: URI, 标记请求方法要操作的资源
3. 版本号: HTTP协议版本

### 状态行(status line)

描述**服务器响应的状态**

> SP -> space, CRLF -> /r/n

    Version/SP/Status Code/SP/Reason/CRLF

1. 版本号: HTTP协议版本
2. 状态码: 三位数, 表示处理结果
3. 原因: 状态码的补充, 更详细的解释文字

### 头部字段

    Field Name: Field Value/CRLF

1. 字段名不区分大小写, 但首字母大写可读性好
2. 字段名不允许(RFC)空格, 可以使用'-', 不能使用'_'(但是可以强行使用, 如Nginx的`underscores_in_headers on`)
3. 名称后紧跟':', 但是':'后可以有多个空格
4. 字段顺序不要求
5. 字段原则上不能重复, 除非字段本身语义运行, 如`Set-Cookie`

### 常用头字段

1. 通用字段：在请求头和响应头里都可以出现
2. 请求字段：仅能出现在请求头里，进一步说明请求信息或者额外的附加条件
3. 响应字段：仅能出现在响应头里，补充说明响应报文的信息
4. 实体字段：它实际上属于通用字段，但专门描述 body 的额外信息

- Host: 请求字段, `HTTP/1.1`中唯一要求必须出现的字段, 一般是域名, 当一个服务器托管了多个虚拟主机(域名), 需要靠此字段区分
- User-Agent: 请求字段, 描述发起的客户端
- Date: 通用字段, 但常出现在响应头, 表示HTTP报文创建时间, 客户端可以据此搭配其他字段决定缓存策略
- Server: 响应字段, 表示当前Web服务的软件和版本号, 不是必须出现, 会暴露服务器信息
- Content-Length: 实体字段, 表示body长度, 可以直接接收, 没有表示body不定长, 需要使用`chunked`方式分段传输

## 10 请求方法

- 幂等: GET HEAD DELETE PUT
- 非幂等: POST

## 11 URI

### 编码

非ASCII直接转义为16进制, 然后前面加`%`, CJK转为UTF-8编码后再转义

## 12 响应状态码

### 2XX

- `200 OK`
- `204 No Content`, 响应头后没有body
- `206 Partial Content`, 分块下载或断点续传的基础, 伴随头字段`Content-Range`, `Content-Range: byte 0-99/2000`, 总计2000, 目前0-99块

### 3XX

- `301 Moved Permanently`, 永久重定向, 资源不存在, 使用新URI访问, 字段`Location`指明, 如http升级https
- `302 Found`, 临时重定向, 资源存在, 临时访问新URI, 字段`Location`指明, 如临时维护, 指定静态通知页面, 涉及缓存优化
- `303 See Other`, 类似302, 但是要求重定向后使用`GET`, 避免`POST`等重复操作
- `304 Not Modified`, 资源未修改, 缓存控制

### 4XX

- `400 Bad Request`, 通用错误码, 尽量避免使用
- `403 Forbidden`, 服务器禁止访问资源
- `404 Not Found`, 资源在服务器未找到
- `405 Method Not Allowed`, 不允许使用使用某些方法操作资源，例如不允许POST, 只能GET
- `406 Not Acceptable`, 资源⽆法满⾜客户端请求的条件，例如请求中⽂但只有英⽂
- `408 Request Timeout`, 请求超时，服务器等待了过⻓的时间
- `409 Conflict`, 多个请求发⽣了冲突，可以理解为多线程并发时的竞态
- `413 Request Entity Too Large`, 请求报⽂⾥的body太⼤
- `414 Request URI Too Large`, 请求报⽂⾥的URI太⼤
- `429 Too Many Requests`, 客户端发送请求过多, 通常是由于服务器的限连策略
- `431 Request Header Field Too Large`, 请求头过大

### 5XX

- `500 Internal Server Error`, 通用的错误码
- `501 Not Implemented`, 客户端请求的功能还不支持, 即将完成
- `502 Bad Gateway`, 网关或代理返回的错误, 表示代理正常, 后端错误
- `503 Service Unavailable`, 服务器忙, 暂时无法响应, 是临时状态, 通常伴随`Retry-After`字段, 指明多久后客户端可以再次尝试

## 13 HTTP协议特点

1. 灵活可扩展, 可以任意添加头字段实现任意功能
2. 可靠传输, 基于TCP/IP协议'尽量'保证数据抵达
3. 应用层协议, 但是比FTP等更通用, 功能更多, 能够传输任意数据
4. 请求-应答模式, 客户端发起请求, 服务器被动回复
5. 无状态, 请求间互相独立, 协议不要求C/S任一方记录请求信息

## 14 HTTP优缺点

1. 最大的优点是简单、灵活和易于扩展
2. 拥有成熟的软硬件环境, 应用的非常广泛, 是互联网的基础设施
3. 无状态, 可以轻松实现集群化, 扩展性能, 但有时也需要用Cookie技术实现'有状态'
4. 明文传输, 数据肉眼可见, 方便研究分析, 但容易被窃听
5. 不安全, 无法验证通信双方的身份, 也不能判断报文是否被篡改
6. 性能不算差, 但不完全适应现在的互联网(TCP需要稳定的连接质量, 移动互联网无法保证), 还有很大的提示空间(请求应答, 队头阻塞)

## 15 HTTP实体数据(body)

### 数据类型及编码

    MIME    Multipurpose Internet Mail Extensions   多用途互联网邮件扩展

- MIME, 分类为8大类, 和若干子类, 形式`type/subtype`
  - text/html text/plain
  - image/gif image/png
  - audio/mpeg video/mp4
  - application/json application/pdf application/octet-stream(八位字节流)
- 编码, 目的是为了节省带宽, 压缩数据, 需要'Encoding Type'指明编码格式, 帮助对方解码
  - gzip, 最常用
  - deflate, zlib压缩格式, 流行度次之
  - br, 专为HTTP优化, 较新

### 数据类型及编码使用的头字段

> []起来表示未使用可省略

    Accept              请求头      客户端可理解的'MIME type'
    Content-Type        实体头      实体数据类型, 及body内容, 请求响应均可
    Accept-Encoding     [请求头]    客户端支持的压缩格式
    Content-Encoding    [实体头]    实体使用的压缩格式

``` http
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp
Content-Type: text/html
Content-Type: image/png
Accept-Encoding: gzip, deflate, br
Content-Encoding: gzip
```

### 语言类型及编码

- 语言及方言, 格式`type-subtype`
  - en-US
  - en-GB
  - zh-CN
- 字符编码方案, 即字符集
  - ASCII
  - GBK
  - UTF-8

### 语言类型的头字段

    Accept-Language     请求头      客户端可理解的自然语言(可`,`分割)
    Content-Language    实体头      内容语言, 实际不使用, 因为可由响应字符集推断得出
    Accept-Charset      请求头      客户端使用的字符集, 实际不使用(浏览器基本都支持了)
                                    响应包含在Content-Type中, charset部分

``` http
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Content-Type: text/html; charset=utf-8
```

### 内容协商质量值

上述内容协商时可指定优先级, `q`(quality)表示权重, 格式`xxxx;q=0.8`

> `;`在HTTP中断句小于`,`

    1       max
    0.01    min
    1       default
    0       deny

``` http
# 简中权重1, 中文0.9, 英文0.8
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
```

### 内容协商结果

响应头`Vary`字段, 记录服务器协商是参考的请求头字段(可不给), 缓存也会用到此字段

    # 表示参考了以下字段决定了响应内容
    Vary: Accept-Encoding,User-Agent

![header-map](./http/http-header-1.png)

## 16 HTTP传输大文件

### 数据压缩

主要适用于文本文件

### 分块传输

响应头`Transfer-Encoding: chunked`, 报文中body部分是分块(chunk)逐个发送, 与`Content-Length`互斥, 即或长度已知, 或长度为止

- 大文件传输
- 流式数据

格式

1. 每个分块包含2部分, 长度头和数据块
2. 长度头CRLF(回车换行, 即\r\n)结尾, 16进制表示
3. 数据块在长度块后, \r\n结尾
4. 最后`0\r\n`结尾

![分块传输](./http/http-chunk.png)

### 范围请求(range requests)

> 范围请求是根据原文件大小, 不是传输过程压缩后的大小

看视频跳进度/多线程下载/断点续传, 客户端'化整为零'

- 服务器支持: `Accept-Ranges: bytes`
- 服务器不支持: `Accept-Ranges: none`或不发

请求头, `Ranges: bytes=x-y`, x~y是偏移量(0开始), 单位`字节`, x~y可省略, 以下下设为100字节

- `0-`, 0-99, 即整个文件
- `10-`, 10-99
- `-1`, 98-99
- `-10`, 90-99

服务器处理

- 是否合法, 越界返回`416`
- 合法返回`216 Partial Content`, 表示body只是部分
- 服务器添加响应头`Content-Range`, 格式`bytes x-y/length`, 与请求头区别在无`=`

### 多段数据

可以一次请求多个片段, 需要特殊MIME类型`multipart/byteranges`表示body由多段字节序列组成, 使用参数`boundary=xxx`给出分隔标记

![http多段数据](./http/http-multipart.png)

- 每段`--boundary`开始
- `Content-Type`, `Content-Range`标记类型和范围
- 换行结束头
- 分段数据
- 最后`--boundary--`表示分段结束

## 17 HTTP连接管理

- 短连接开销大
  - 长连接: 一个连接上收发多个请求, 提高传输效率
  - 表示开启长连接: header中`Connection: keep-alive`
  - 表示即将关闭: `Connection: close`
- 请求应答模式导致的队头阻塞问题, 性能优化(数量解决质量)
  - 并发连接: 同时对一个域名发起多个长连接，用数量来解决质量的问题
  - 域名分片: shard1.xx.com, shard2.xx.com

## 18 HTTP跳转和重定向

- 301永久
- 302临时
- `Location`表示跳转地址, 可相对可绝对
- 注意性能损耗(请求2次)和循环跳转
- 重定向响应可增加`Refresh`头字段设定延时跳转, 但好像不是所有都支持
- `Referer`(拼写错误,历史原因), 跳转来源
- `Referrer-Policy`,策略, 影响上面一个是否存在或者条件

## 19 HTTP Cookie

- 响应头`Set-Cookie`, 可添加多个
- 请求头`Cookie`, 多个用`;`隔开(由于Cookie非HTTP标准, 所以没有用HTTP标准分隔符`,`)
- Key-Value
-
- 词源于计算机术语`Magic Cookie(不透明的数据)`, 并非小甜饼
- 总大小不能超过`4K`
- 属性
  - 生存周期, 可以同时出现, 优先`Max-Age`, 如果都不设定即为会话Cookie(Session Cookie)
    - `Expires`, 过期时间, 绝对时间点
    - `Max-Age`, 相对时间, 单位秒, 为0立即失效
  - 作用域
    - `Domain`, 域名
    - `Paht`, 路径, 通常为`/`或省略, 即域名下任意路径都允许
  - 安全性
    - `HttpOnly`, 仅用于http传输, 禁止js等非http方式访问(针对XSS跨站脚本)
    - `SameSite`
      - `SameSite=Strict`, 严格限定Cookie不能随跳转链接发送(针对XSRF跨站请求伪造)
      - `SameSite=Lax`, 相对宽松, 允许GET/HEAD等安全方法, 禁止POST
    - `Secure`, 仅用于HTTPS, 禁止HTTP

## 20 HTTP缓存控制

- 服务器缓存控制
  - 资源有效期, `Cache-Control:`
    - `max-age=xx`, xx秒后过期, 是生存时间, 从响应报文(`Date`字段)创建开始
    - `no_store`, 不允许缓存, 用于频繁变化, 如秒杀页面
    - `no_cache`, 允许缓存!!, 但是使用前需要向服务器验证是否过期(等价`max-age=0,must-revalidate`)
    - `must-revalidate`, 不过期可用, 过期需要验证
- 客户端缓存控制(F5功能)
  - 资源有效期, `Cache-Control:`
    - `max-age=0`, 要最新数据(F5)
    - `no_cache`, 基本等价(Ctrl+F5)
    - `must-revalidate`, 不过期可用, 过期需要验证
- 条件请求
  - 如果资源没变, 返回`304 Not Modified`
  - 需要第一次响应报文预先提供以下字段
    - `Last-Modified`, 文件最后修改时间
    - `ETag`, 实体标签(Entity Tag), 资源唯一标识, 解决用修改时间无法区分文件变化(如1s内多次修改)
      - 强ETag, 字节级别相符
      - 弱ETag, 值前有'W/'标记, 在语义上没有变化, 内部可能有变化(如多了空格)
  - `If-Modified-Since`, 内容为之前服务器返回的`Last-Modified`
  - `If-None-Match`, 是否匹配强弱ETag
  - 如果请求中不携带条件请求, 缓存就无法生效

## 21 HTTP代理

- `Client <-> Proxy Server <-> Origin Server(源服务器)`
- 提供功能
  - 负载均衡
  - 健康检查, 心跳监控后端服务器, 有故障剔除集群
  - 安全防护, 保护后端服务器, 限制IP或流量, 抵御攻击和过载
  - 加密卸载, 对外SSL/TLS加密, 内部不加密, 降低加解密成本
  - 数据过滤, 拦截上下行数据, 任意指定策略修改请求和响应
  - 内容缓存, 暂存/复用服务器响应
- 相关头字段
  - `Via`, 通用字段, 报文经过代理节点, 代理把自身信息(代理主机名或域名)追加到字段末尾, 请求和响应其内容正好相反
  - `X-Real-IP`, 客户端IP地址, `X-Forwarded-For`的简化版本, 当仅一层, 值相等
  - `X-Forwarded-For`, 为谁而转发, 类似`Via`, 也是追加信息, 但是为请求方的IP地址
  - `X-Forwarded-Host`, 客户端请求的原始域名
  - `X-Forwarded-Proto`, 客户端请求的原始协议名
- 代理协议
  - 解决需要解析HTTP头(成本)/要修改原始报文(HTTPS不允许)的问题
  - `v1`版本直接在HTTP头上方加一行代理的内容

## 22 HTTP缓存代理

![服务端流程](./http/http-cache-server.png)
![客户端流程](./http/http-cache-client.png)

- 以下均是`Cache-Control`的属性值
- 源服务器的缓存控制
  - 区分客户端缓存和代理缓存
    - `private`, 只能客户端, 如Cookie
    - `public`, 都可以
  - 缓存失效后的重新验证
    - `must-revalidate`, 过期必须回源服务器验证
    - `proxy-revalidate`, 只要求代理缓存过期后必须验证, 客户端不必回源, 验证到代理就可以了
  - 缓存生存周期
    - `s-maxage`(s=share, maxage没有`-`), 只限定代理能够缓存多久
    - `max-age`, 普通版本
  - 是否允许变换(仅代理), 如把图片生存png等
    - `no-transform`, 不允许变换
- 客户端的缓存控制
  - 缓存生存时间
    - `max-stale`, 可接受过期x时间内的缓存
    - `min-fresh`, 缓存必须x时间后仍有效

## 23 HTTPS SSL/TLS

- 安全性
  - 机密性(Secrecy/Confidentiality), 指对数据的保密(不相干的人看不到)
  - 完整性(Integrity, or一致性), 没有篡改
  - 身份认证(Authentication), 确认双方的真实身份
  - 不可否认(Non-repudiation/Undeniable), 也叫不可抵赖, 不能否认已经发生过的行为
- HTTPS
  - 协议名, https
  - 默认端口, 443
  - 下层传输协议由TCP/IP(HTTP over TCP/IP)换位SSL/TLS(HTTP over SSL/TLS), 但是TLS下层仍是TCP/IP
- SSL/TLS
  - SSL(Secure Sockets Layer), 安全套接字, OSI 5层(会话层)
  - TLS(Transport Layer Security), 传输层安全, IETF标准化SSL后更名为此
  - 使用加密套件(cipher suite)
    - 格式, 秘钥交换算法 + 签名算法 + 对称加密算法 + 摘要算法
    - `ECDHE-RSA-AES256-GCM-SHA384`
    - “握手时使用 ECDHE 算法进行密钥交换，用 RSA 签名和身份认证，握手后的通信使用 AES 对称算法，密钥长度256 位，分组模式是 GCM，摘要算法 SHA384 用于消息认证和产生随机数。”
- OpenSSL
  - 由SSLeay发展而来, 由于当时TLS未正式确立, 最终使用了SSL命名

## 24 对称加密与非对称加密

> (x)表示不安全

- 对称加密算法
  - 块加密(block cipher)
    - DES(x)
    - AES(秘钥长度可变)
      - AES128
      - AES256
  - 流加密(stream cipher)
    - RC4(x)
    - ChaCha20
  - 加密分组模式, 算法用固定长度的秘钥加密任意长度的明文
    - ECB(x)
    - CBC(x)
    - CFB(x)
    - OFB(x)
    - AEAD(Authenticated Encryption with Associated Data), 加密+认证
      - GCM
      - CCM
      - Poly1305
  - 组合形成对称加密算法
    - AES128-GCM, 秘钥长度128位的AES算法, 分组模式GCM
    - ChaCha20-Poly1305, ChaCha20算法, 分组模式Poly1305
- 非对称加密
  - 解决对称加密秘钥交换问题
    - 公钥加密(客户端用公钥加密token后传递给私钥)
    - 私钥解密
  - 种类
    - DH
    - DSA
    - RSA, 安全性基于整数分解数学难题, 目前认为安全至少2048位
    - ECC(Elliptic Curve Cryptography), 椭圆曲线离散对数数学难题
      - ECDHE, 秘钥交换
      - ECDSA, 数字签名
      - 曲线
        - P-256(x)
        - x25519, 名字来源曲线方程参数'2^255-19'
      - 安全强度和性能较RSA都有明显优势
- 混合加密
  - 非对称慢, 对称需要安全传递秘钥
  - 方案, 又好又快
    - 开始通信使用非对称加密, 传递会话密钥
    - 后续通信使用会话秘钥进行对称加密
