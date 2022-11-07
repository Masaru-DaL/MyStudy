# ターミナルのアップグレード

## 1. tmux

1. `$ brew install tmux`
2. tmuxの自動起動化(iTerm起動時に自動でtmuxが起動する)
シェル: zsh
ターミナルクライアント: iTerm2

* 以下のコードを`.zshrc`に追加



## 4. bat

catの代替コマンド(catを叩くとbatが効くようにする)
 `$ brew install bat`

```c: .zshrc
alias cat="bat"
```

## 5. exa

lsの代替コマンド(lsを叩くとexaが効くようにする)
 `$ brew install exa`

```c: .zshrc
alias ls="exa -FG"
alias ll="exa -al"
```
