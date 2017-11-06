FROM centos:7
RUN \
    yum update -y && \
    yum install httpd -y && \
    yum install perl -y && \
    yum install gcc -y && \
    yum install perl-DBD-MySQL -y && \
    yum install perl-XML-Parser.x86_64 -y && \
    yum install perl-XML-Simple.noarch -y && \
    yum install cpanminus -y && \
    cpanm CGI && \
    cpanm Redis::hiredis && \
    rm -rf /etc/apache2/sites-enabled/000-default.conf

#COPY httpd.conf /etc/httpd/conf/


CMD ["/usr/sbin/httpd","-DFOREGROUND"]