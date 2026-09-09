# Static build → nginx, deployed to Proxmox via Argo CD.

FROM node:22-alpine AS build
WORKDIR /src
COPY package.json package-lock.json* ./
RUN npm ci --no-audit --no-fund
COPY . .
RUN npx hugo --minify --environment production

FROM nginx:1.27-alpine
COPY --from=build /src/public /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
