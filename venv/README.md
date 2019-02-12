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

### requirements
pip install -r requirements/dev.txt

### freezeによる出力   
pip freeze > requirements.txt   

### Pipenv 
- 手順
  - 準備   
  pip install pipenv  
  cd pipenv-test

  - pythonバージョン指定   
  pipenv --python 3.6.2  
  Pipfileが作成される  
  /home/ec2-user/.local/share/virtualenvs/配下にインストールされる

  - インストール例1  
  pipenv install requests==2.18.4  
  Pipfile,Pipfile.lockが作成される  
  /home/ec2-user/.local/share/virtualenvs/のsite-packages配下にインストールされる  

  - インストール例2  
  pipenv install --dev ipython==6.2.1  
  Pipfile,Pipfile.lockが作成される  
  /home/ec2-user/.local/share/virtualenvs/のsite-packages配下にインストールされる   

  - pipfileのパッケージを一括インストール  
    activateする
    pipenv install

  - activate   
    - pipenv run ipython  
    - pipenv shell
  - deactivate   
    - exit

  - その他
  pipenv install --dev -e .

- 結果  
  - Pipfile   

  ```
  [[source]]
  name = "pypi"
  url = "https://pypi.org/simple"
  verify_ssl = true

  [dev-packages]
  ipython = "==6.2.1"

  [packages]
  requests = "==2.18.4"

  [requires]
  python_version = "3.6"
  ```

  - Pipfile.lock   

  ```
  {
      "_meta": {
          "hash": {
              "sha256": "15f4df171598b5443bb8d912a1c14113972b28857e452953c006c966dd9937e8"
          },
          "pipfile-spec": 6,
          "requires": {
              "python_version": "3.6"
          },
          "sources": [
              {
                  "name": "pypi",
                  "url": "https://pypi.org/simple",
                  "verify_ssl": true
              }
          ]
      },
      "default": {
          "requests": {
              "hashes": [
                  "sha256:6a1b267aa90cac58ac3a765d067950e7dbbf75b1da07e895d1f594193a40a38b",
                  "sha256:9c443e7324ba5b85070c4a818ade28bfabedf16ea10206da1132edaa6dda237e"
              ],
              "index": "pypi",
              "version": "==2.18.4"
          }
      },
      "develop": {
          "ipython": {
              "hashes": [
                  "sha256:51c158a6c8b899898d1c91c6b51a34110196815cc905f9be0fa5878e19355608",
                  "sha256:fcc6d46f08c3c4de7b15ae1c426e15be1b7932bcda9d83ce1a4304e8c1129df3"
              ],
              "index": "pypi",
              "version": "==6.2.1"
          }
      }
  }
  ```

- その他
  - pipenv --rm  
  - pipenv uninstall --all  
  - pipenv uninstall requests  


#### 参考
https://qiita.com/QUANON/items/4a371651b07bb61fde41
