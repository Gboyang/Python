## Flask 配置文件

创建一个存放配置的py文件

py 文件导入

```
from flask import Flask

app = Flask(__name__)# 通过下面的指定settings文件路径， 手动创建settings文件。所有配置都写到settings文件中

app.config.from_pyfile("settings.py")

@app.route('/index', endpoint='index', methods=['GET', 'POST'])
def index():    
	print('请求来了')    
	return 'hello word'
	
if __name__ == '__main__':    
	app.run()
```

python 类或类的路径 

```
from flask import Flask

app = Flask(__name__)

# 通过下面的指定settings文件路径， 手动创建settings文件。所有配置都写到settings文件中app.config.from_object('settings.Config')

@app.route('/index', endpoint='index', methods=['GET', 'POST'])

def index():    
	print('请求来了')    
	return 'hello word'


if __name__ == '__main__':    
app.run()
```

settings文件

```
class Config(object):
	DEBUG = True
	TESTING = False    
	DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):    
'''生产环境'''
	DATABASE_URI = 'mysql://user@localhost/foo'
	
class DevelopmentConfig(Config):    
'''开发环境'''    
	DEBUG = True

class TestingConfig(Config):    
'''测试环境'''    
	TESTING = True
```

默认配置参数

```
{
  ``'DEBUG'``:                get_debug_flag(default``=``False``), 是否开启Debug模式
  ``'TESTING'``:               ``False``,             是否开启测试模式
  ``'PROPAGATE_EXCEPTIONS'``:         ``None``,             
  ``'PRESERVE_CONTEXT_ON_EXCEPTION'``:    ``None``,
  ``'SECRET_KEY'``:              ``None``,
  ``'PERMANENT_SESSION_LIFETIME'``:      timedelta(days``=``31``),
  ``'USE_X_SENDFILE'``:            ``False``,
  ``'LOGGER_NAME'``:             ``None``,
  ``'LOGGER_HANDLER_POLICY'``:        ``'always'``,
  ``'SERVER_NAME'``:             ``None``,
  ``'APPLICATION_ROOT'``:           ``None``,
  ``'SESSION_COOKIE_NAME'``:         ``'session'``,
  ``'SESSION_COOKIE_DOMAIN'``:        ``None``,
  ``'SESSION_COOKIE_PATH'``:         ``None``,
  ``'SESSION_COOKIE_HTTPONLY'``:       ``True``,
  ``'SESSION_COOKIE_SECURE'``:        ``False``,
  ``'SESSION_REFRESH_EACH_REQUEST'``:     ``True``,
  ``'MAX_CONTENT_LENGTH'``:          ``None``,
  ``'SEND_FILE_MAX_AGE_DEFAULT'``:      timedelta(hours``=``12``),
  ``'TRAP_BAD_REQUEST_ERRORS'``:       ``False``,
  ``'TRAP_HTTP_EXCEPTIONS'``:         ``False``,
  ``'EXPLAIN_TEMPLATE_LOADING'``:       ``False``,
  ``'PREFERRED_URL_SCHEME'``:         ``'http'``,
  ``'JSON_AS_ASCII'``:            ``True``,
  ``'JSON_SORT_KEYS'``:            ``True``,
  ``'JSONIFY_PRETTYPRINT_REGULAR'``:     ``True``,
  ``'JSONIFY_MIMETYPE'``:           ``'application/json'``,
  ``'TEMPLATES_AUTO_RELOAD'``:        ``None``,
}
```

