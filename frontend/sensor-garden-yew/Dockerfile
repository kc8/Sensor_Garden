FROM nginx:stable
EXPOSE 8080

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/default.conf

## TODO this needs to be updated on each build?
COPY dist/index.html /usr/share/nginx/html/index.html
COPY dist/sensorgardenyew-77f1d44c731e2004_bg.wasm /usr/share/nginx/html/sensorgardenyew-77f1d44c731e2004_bg.wasm
COPY dist/sensorgardenyew-77f1d44c731e2004.js /usr/share/nginx/html/sensorgardenyew-77f1d44c731e2004.js

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
