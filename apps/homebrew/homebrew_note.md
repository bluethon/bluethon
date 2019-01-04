Homebrew Note
=============

Linux
-----

> <https://linuxbrew.sh/>

源
---

``` shell
### 清华
# Homebrew binary
cd "$(brew --repo)"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

brew update

# Homebrew-bottles
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.zshrc

### USTC
# 替换brew.git:
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
# 替换homebrew-core.git:
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
# Homebrew cask 软件仓库，提供 macOS 应用和大型二进制文件
cd "$(brew --repo)"/Library/Taps/homebrew/homebrew-cask
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

brew update

# Homebrew-bottles
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.zshrc
```
