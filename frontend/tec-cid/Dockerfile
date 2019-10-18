FROM node:alpine as builder
ARG env=prod
ARG BASE_HREF=/
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm install @angular/cli -g
RUN npm install --global gulp-cli
RUN npm install
COPY . /app
RUN cd /app && ng build --configuration $env --base-href $base_href

FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist/* /usr/share/nginx/html/
