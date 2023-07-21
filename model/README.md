# Cuda install

#### 1. 아래 명령어를 Terminal에 입력해주세요.

```bash
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
chmod +x cuda_11.8.0_520.61.05_linux.run
sh cuda_11.8.0_520.61.05_linux.run
```
#### 2. Accept를 눌러주세요.
<img width="579" alt="Screenshot 2023-07-17 at 9 26 12 PM" src="https://github.com/boostcampaitech5/level2_klue-nlp-08/assets/81630351/7a483729-188e-43ec-ab25-f334549f2bd3">

#### 3. driver를 선택하고 install 해주세요. 
<img width="579" alt="Screenshot 2023-07-17 at 9 26 25 PM" src="https://github.com/boostcampaitech5/level2_klue-nlp-08/assets/81630351/e0405f88-c0b3-4258-8be2-071a0d6518e7">


#### 4. 아래 명령어를 순서대로 Terminal에 입력해주세요.
```bash
export PATH=/usr/local/cuda-11.8/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH
```