FROM nginx:stable
EXPOSE 8080

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/default.conf

## TODO this needs to be updated on each build?
COPY dist/index.html /usr/share/nginx/html/index.html
COPY dist/sensorgardenyew-3b4d5adfbcaf250e_bg.wasm /usr/share/nginx/html/sensorgardenyew-3b4d5adfbcaf250e_bg.wasm
COPY dist/sensorgardenyew-3b4d5adfbcaf250e.js /usr/share/nginx/html/sensorgardenyew-3b4d5adfbcaf250e.js

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
