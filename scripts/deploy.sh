#!/usr/bin/env bash
# deploy.sh
# Helper script to provision a $5 Ubuntu VPS and deploy the AI Tools Income Stream

set -e

echo "=== AI Tools Income Stream VPS Deploy Script ==="
echo "This script assumes you have a fresh Ubuntu 22.04 server with sudo access."
echo "Update these variables before running:"
READONLY_VAR=""

# Configuration - EDIT THESE
REPO_URL="https://github.com/chinhigh80/ai-tools-income-stream.git"
APP_DIR="/opt/ai-tools-income-stream"
DOMAIN="your-domain.com" # Set your domain or subdomain
EMAIL="admin@your-domain.com" # For Let's Encrypt
# End of configuration

if [[ "$DOMAIN" == "your-domain.com" ]]; then
  echo "Error: Please set DOMAIN and EMAIL variables in deploy.sh before running."
  exit 1
fi

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing dependencies..."
sudo apt install -y git docker.io docker-compose nginx certbot python3-certbot-nginx ufw

echo "Starting Docker..."
sudo systemctl enable docker
sudo systemctl start docker

echo "Cloning repository..."
if [ -d "$APP_DIR" ]; then
  sudo rm -rf "$APP_DIR"
fi
sudo git clone "$REPO_URL" "$APP_DIR"
sudo chown -R $USER:$USER "$APP_DIR"

cd "$APP_DIR"

echo "Copying environment file..."
cp .env.example .env
echo "Please edit .env with your Paystack test keys and AdSense info before continuing."
read -p "Have you edited .env? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "Please edit .env and re-run the script."
  exit 1
fi

echo "Building and starting containers..."
sudo docker compose up -d --build

echo "Configuring Nginx as reverse proxy..."
sudo tee /etc/nginx/sites-available/ai-tools-income-stream > /dev/null <<EOF
server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN;

    location / {
        proxy_pass http://localhost:1313;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    location /microtool/ {
        rewrite ^/microtool/(.*) /\$1 break;
        proxy_pass http://localhost:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

sudo ln -sf /etc/nginx/sites-available/ai-tools-income-stream /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

echo "Obtaining Let's Encrypt certificate..."
sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN --non-interactive --agree-tos --email $EMAIL --redirect

echo "Setup complete! Your site should be live at https://$DOMAIN"
echo "Microtool API available at https://$DOMAIN/microtool/docs"
echo "Don't forget to set up DNS A records pointing to this server's IP."