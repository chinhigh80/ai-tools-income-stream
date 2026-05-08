FROM klakegg/hugo:0.124.1-ext-alpine AS builder

WORKDIR /src
COPY site/ .

# Build the site
RUN hugo --minify --baseURL="$HUGO_BASE_URL"

# Production stage
FROM nginx:alpine
COPY --from=builder /src/public /usr/share/nginx/html
# Optional custom nginx config can be added here
EXPOSE 80