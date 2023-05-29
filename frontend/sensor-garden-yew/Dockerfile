FROM nginx:stable
EXPOSE 8080

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/default.conf

## TODO this needs to be updated on each build?
COPY dist/index.html /usr/share/nginx/html/index.html
COPY dist/sensorgardenyew-74a91302702caa2a_bg.wasm /usr/share/nginx/html/sensorgardenyew-74a91302702caa2a_bg.wasm
COPY dist/sensorgardenyew-74a91302702caa2a.js /usr/share/nginx/html/sensorgardenyew-74a91302702caa2a.js

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
