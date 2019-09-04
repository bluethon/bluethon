# VSCode 中 ansible 的格式化支持

## 安装 ansible

## vscode 修改配置

``` json
"files.associations": {
    "**/*.yml": "ansible",
    "**/hosts": "ansible"
}
```

## 安装 prettier

修改`~/.vscode/extensions/esbenp.prettier-vscode-1.8.1/node_modules/prettier/index.js`

``` js
var languages$6 = [
  createLanguage(require$$0$33, {
    override: {
      since: "1.14.0",
      parsers: ["yaml"],
      // vscodeLanguageIds: ["yaml"]  //old
      vscodeLanguageIds: ["yaml", "ansible"] //new
    }
  })
];
```
