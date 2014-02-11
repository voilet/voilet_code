# 安装pip
然后安装python所需扩展

    pip install -r requirements.txt

config.py为所有配置文件

# 安装saltstack
    
    wget -O - http://bootstrap.saltstack.org | sudo sh

    安装参考:http://wiki.saltstack.cn/installation



# 安装salt-api
    
    pip install salt-api

# 生成库结构

    python manage.py syncdb


# 启动django

    
    python manage.py runserver
    

# 下载服务维护脚本
    
    wget https://raw.github.com/saltstack/salt-api/develop/pkg/rpm/salt-api -O /etc/init.d/salt-api
    chmod +x /etc/init.d/salt-api
    chkconfig salt-api on
   

    生成自签名证书(用于ssl)

# 配置salt-api

    cd  /etc/pki/tls/certs
    生成自签名证书
    过程中需要输入key密码及RDNs
    make testcert
    cd /etc/pki/tls/private/
    解密key文件，生成无密码的key文件, 过程中需要输入key密码，该密码为之前生成证书时设置的密码
    openssl rsa -in localhost.key -out localhost_nopass.key


    创建用于salt-api的用户
    useradd -M -s /sbin/nologin sa
    echo "sa" | passwd sa
    配置eauth, /etc/salt/master.d/eauth.conf
    帐号为系统帐号，不可使用root帐号

    external_auth:
      pam:
        sa:
          - .*

# 配置Salt-API

    
    /etc/salt/master.d/api.conf
    rest_cherrypy:
      port: 443
      ssl_crt: /etc/pki/tls/certs/localhost.crt
      ssl_key: /etc/pki/tls/private/localhost_nopass.key

# 启动Salt-API

    service salt-api start
    curl -k https://192.168.38.10/login -H "Accept: application/x-yaml" \
         -d username='sa' \
         -d password='centos' \
         -d eauth='pam'

    
    return:
    - eauth: pam
      expire: 1385579710.806725
      perms:
      - .*
      start: 1385536510.8067241
      token: 784ee23c63794576a50ca5d3d890eb71efb0de6f
      user: sa

# 参考
http://wiki.saltstack.cn/reproduction/salt-api-deploy-and-use
saltstack使用方法参考:http://wiki.saltstack.cn/docs


