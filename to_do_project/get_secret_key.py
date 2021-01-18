# git clone時はこのpythonファイルを実行し、SECRET_KEYを取得して下さい。
# 取得したSECRET_KEYは、local_setting.pyを作成し、その中に記入して下さい。

from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
key_text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(key_text)