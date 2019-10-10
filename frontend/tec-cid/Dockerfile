FROM node:alpine as builder
ARG env
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm install @angular/cli -g
RUN npm install --global gulp-cli
RUN npm install
COPY . /app
RUN cd /app && ng build --configuration $env

FROM nginx:alpine
COPY --from=builder /app/dist/* /usr/share/nginx/html/

