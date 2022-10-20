# ターミナルのアップグレード

## 1. tmux

1. `$ brew install tmux`
2. tmuxの自動起動化(iTerm起動時に自動でtmuxが起動する)
シェル: zsh
ターミナルクライアント: iTerm2

* 以下のコードを`.zshrc`に追加

```c: .zshrc
if [[ ! -n $TMUX && $- == *l* ]]; then
  # get the IDs
  ID=" `tmux list-sessions` "
  if [[ -z "$ID" ]]; then

    tmux new-session

  fi
  create_new_session="Create New Session"
  ID="$ID\n${create_new_session}:"
  ID=" `echo $ID | peco | cut -d: -f1` "
  if [[ "$ID" = "${create_new_session}" ]]; then

    tmux new-session

  elif [[ -n "$ID" ]]; then

    tmux attach-session -t "$ID"

  else

    :  # Start terminal normally

  fi
fi
```

## 2. mycli

sql操作における、補完や検索機能などの強化をしてくれる。

 `$ brew install mycli`

## 3. tig

gitのためのCLIツール
