# XAMPP Setup
$ cd /opt/lampp
$ sudo /opt/lampp/lampp start
$ xhost si:localuser:root
$ sudo ./manager-linux-x64.run &

-> localhost:8080

- XAMPP Stop
$ sudo /opt/lampp/lampp stop

# XAMPPでlaravel documentが表示されるまで
- プロジェクト名
  - RAT-X=5
/opt/lampp/htdocs/
の下にプロジェクトを作成

-> localhost:8080/RAT-X=5/public
でlaravel documentが表示
