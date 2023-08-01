# LawBot - Frontend

## ⚠️ Requirements for Web Frontend

Below is the commands for installing dependency packages to run web frontend. <br/>
Run the following commands in proper order.
```bash
# install react
apt install curl 
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
source ~/.bashr
nvm install 18.04.0

# Install Tailwind CSS
npm install -g yarn
yarn add tailwindcss postcss autoprefixer 
npx tailwindcss init
npm i tailwindcss-animated
```

When installation is completed, please run the following commands to check if proper version is installed. <br/>
Please refer to the README file inside the `frontend` directory for the executable file.

```bash
node -v # v18.04.1
npm -v # v8.11.0 
```

## 💻 Getting Started with Create React App 

```bash
yarn start # npm start
```

## How to Configure nginx

- Below is the commands for installing dependency packages to run web frontend

```
sudo apt install nginx
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default

sudo vim /etc/nginx/sites-available/frontend.conf
sudo ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/myapp.conf
```

- The configuration files that you need to write in `/etc/nginx/sites-available`

```conf
server {
        listen 80;
        listen [::]:80;

        server_name yoonseul.link ;

        root /home/ubuntu/level3_nlp_finalproject-nlp-08/frontend/build;
        index index.html;

        location /generate {

                proxy_pass https://backend_server;
                proxy_connect_timeout 500;
                proxy_send_timeout 500;
                proxy_read_timeout 500;
        }
}
```


## How to start nginx
```bash
sudo systemctl stop nginx # nginx 중단
sudo systemctl start nginx # nginx 시작
``````