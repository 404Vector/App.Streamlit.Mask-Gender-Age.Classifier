# WebService::Mask & Gender & Age Classifier

- ViT 기반 Mask, Gender, Age Classifier

- Streamlit 기반 WebService

## Prerequisite

- Python 3.8+

## Installation

```
pip install -r requirements.txt
```

## How to Run

```
streamlit run app.py --server.port PORT --server.fileWatcherType none
```

## Git LFS Setting

```
sudo apt-get update
sudo apt install curl
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
git lfs track "assets/*"
```