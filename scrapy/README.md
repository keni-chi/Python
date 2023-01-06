
## 概要
基本
    プロジェクトの作成
    spiderの作成
    scrapy shell

setting.py
    HTTPキャッシュ
    user Agent
    文字コード
    download_delay
    robotstext_obey

basicテンプレート
    ページめくり
    複数階層（詳細ページ）

crawl spider
    ruleオブジェクト
    settings.pyでのデータ取得順（depth_priorityなど）

scrapyのデバッグ

Item
    Item・・・フィールドを定義
    ItemLoader・・・add_xpathでフィールドにセット。Joinなど
    ItemPipline・・・setting.pyにPiplineクラスを定義。

DB登録
    Mongo
    SQLite3

画像ファイルの保存

webドライバ
    ブラウザごとに必要（chrome driverなど）
    手元のブラウザとバージョンを合わせる
    projectフォルダは以下に、seleniumフォルダを作成し、ダウンロードしたドライバーを解凍して置く。
    from selenium import webdriverでインポートする。

selenium
    検索サイトでの検索
        webdriverのインスタンス作成後、driver.get('url')で、検索サイトをセット。
        driver.find_element_by_idなどで検索文字列を入力。
        検索実行
            検索ボタンを押す方法(click)。
            FORMを使う方法(submit)。
            Enterキーを押す方法もある(Keysをimportし、Keys.ENTER)。

    ヘッドレスモード

scrapy-selenium
    setting.pyに、scrapy-selenium用のコードをgithubを参考に、2箇所コピーする。
    start_requestsをオーバライドする。SeleniumRequestを呼び出す。
    start_urlsは削除する。

scrapy-seleniumでの次のページの方法
    response.urljoin(next_page)

Scrapy-SeleniumでのJS対応
    HTMLコードからの要素の取得
        html = driver.page_source
        selector = Selector(text=html)
        selector.xpath('')

ログイン画面
    ブラウザでの確認
        chromeのディベロッパーツールで、ネットワーク、all、preserve logにチェックを入れる
        clearボタンでログを消去
        300台でリダイレクト成功
    FormRequestクラスで、form送信することで、id,pass以外にtokenを送信



## 参考
[10分で理解する Scrapy](https://qiita.com/Chanmoro/items/f4df85eb73b18d902739)  
[Scrapyのチュートリアルをやってみた](https://monologu.com/try-scrapy-tutorial/)  
