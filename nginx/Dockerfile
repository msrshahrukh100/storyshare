FROM nginx:latest

ADD conf.d/local.conf /etc/nginx/nginx.conf

RUN mkdir -p /var/www/media \ 
    && mkdir -p /var/www/static \
    && chown -R nginx:nginx /var/www/media \
    && chown -R nginx:nginx /var/www/static

COPY --from=storyshare_web /var/www/storyshare/static_cdn/ /var/www/static/
