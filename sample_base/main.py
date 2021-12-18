import  os, sys
sys.path.append('./fw')
from app_service import AppService


def main():
    # サービスの実行
    app = AppService()
    app.execute()
 

if __name__ == '__main__':
    main()
