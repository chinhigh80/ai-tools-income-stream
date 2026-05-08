FROM alpine:latest as builder

RUN apk add --no-cache wget && \
    wget https://github.com/gohugoio/hugo/releases/download/v0.124.1/hugo_extended_0.124.1_Linux-64bit.tar.gz && \
    tar -xzf hugo_extended_0.124.1_Linux-64bit.tar.gz && \
    mv hugo /usr/local/bin/

WORKDIR /src
COPY . .

# Build the site
RUN hugo --minify --baseURL="$HUGO_BASE_URL"

# Production stage
FROM nginx:alpine
COPY --from=builder /src/public /usr/share/nginx/html
# Optional custom nginx config can be added here
EXPOSE 80