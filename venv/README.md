# venv

## 概要
venvコマンドについて以下に示す。

### コマンド
python3 -m venv .venv  
source .venv/bin/activate  
deactivate

### venv自動有効化
1. 前提条件として、~にvenvが作成されていること。
1. 以下内容のシェルを作成。  
  source ~/{venv名}/bin/activate
1. .bashrcに以下を追加。（~/Toolに、シェルが作成している例）  
  source ~/Tool/{シェル名}.sh
