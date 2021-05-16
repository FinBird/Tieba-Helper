import tiebaBrowser as tb
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    b = os.environ['BDUSS'].split('#')
    CONFIG_LIST = json.loads(os.environ['CONFIG'])

    #封禁
    for n, i in enumerate(b):
        t_browser = tb.Browser(i)
        if CONFIG_LIST['block_list'][n] == []:
            break
        logger.info("开始使用第" + str(n+1) + "个账户进行封禁")
        for ID in CONFIG_LIST['block_list'][n]:
                userinfo=t_browser._get_userinfo(ID['id'])
                flag,user=t_browser.block(userinfo,ID['tb_name'],ID['day'],ID['reason'])
                print(flag)
    logger.info("所有封禁操作已完成")

if __name__ == '__main__':
    main()
