# LawBot - Model

## ⚠️ Requirements for Web Prototype

Below is the commands for installing dependency packages to run web prototype. <br/>
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
```

When installation is completed, please run the following commands to check if proper version is installed. <br/>
Please refer to the README file inside the `prototype` directory for the executable file.

```bash
node -v # v18.04.1
npm -v # v8.11.0 
```

## 💻 Getting Started with Create React App

```bash
yarn start # npm start
```