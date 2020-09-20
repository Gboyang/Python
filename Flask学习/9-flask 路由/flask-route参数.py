'''
          rule,                       URL规则
            view_func,                  视图函数名称
            defaults=None,              默认值,当URL中无参数，函数需要参数时，使用defaults={'k':'v'}为函数提供参数
            endpoint=None,              名称，用于反向生成URL，即： url_for('名称')
            methods=None,               允许的请求方式，如：["GET","POST"]


            strict_slashes=None,        对URL最后的 / 符号是否严格要求，
                                        如：
                                            @app.route('/index',strict_slashes=False)，
                                                访问 http://www.xx.com/index/ 或 http://www.xx.com/index均可
                                            @app.route('/index',strict_slashes=True)
                                                仅访问 http://www.xx.com/index
            redirect_to=None,           重定向到指定地址
                                        如：
                                            @app.route('/index/<int:nid>', redirect_to='/home/<nid>')
                                            或
                                            def func(adapter, nid):
                                                return "/home/888"
                                            @app.route('/index/<int:nid>', redirect_to=func)
'''