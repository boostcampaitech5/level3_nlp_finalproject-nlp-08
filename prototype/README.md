# Requirements for Web Prototype

아래는 웹 프로토타입 실행을 위한 의존성 패키지 설치 명령어 입니다. 
순서대로 다운로드를 받아주세요.
```bash
### install react
apt install curl 
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
source ~/.profile
nvm install 16.15.1

### Install Tailwind CSS
npm install -g yarn
yarn add tailwindcss postcss autoprefixer 
npx tailwindcss init
```

설치가 끝나셨으면 아래 알맞은 버전이 설치되었는지 확인 부탁드립니다. 
실행 파일은 protoype안에 있는 readme파일을 참고해주세요.
```bash
node -v # v16.15.1가 나와야 합니다. 
npm -v # v8.11.0가 나와야 합니다. 
```

# Getting Started with Create React App

```bash
source ~/.profile # yarn 명령어가 인식되지 않으면 사용해주세요.
nvm install 16.15.1
yarn start
```