import time
def setting(sleep,retry_times):
    def retry_(request):
        def respon(*args,**kwargs):
            retry=0
            # print(*args)
            try:
                request()
                retry+=1
            except Exception:
                for i in range(retry_times):
                    print('失败，第{}次重试'.format(i+1),end='\t')
                    time.sleep(sleep)
                    try:
                        request()
                    except Exception:
                        print('重试失败，等待{}秒后重试，剩余重试次数：{}'.format(sleep,retry_times-i-1))
        return respon
    return retry_