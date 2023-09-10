# Divar API Backend

## A minimal clone of Divar backend with FastAPI.
[Divar](https://divar.ir) is the largest Persian marketplace where you can sell and buy things.

# Installation

## [Docker](https://www.docker.com)

```shell
git clone https://github.com/khodealib/DivarAPI
cd DivarAPI
docker composer up -d --build
```
## Manual
```shell
git clone https://github.com/khodealib/DivarAPI
cd DivarAPI
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python main.py
```
## Configuration

#### 1 - Create .env file from sample.env.

#### 2 - Change .env configurations variable and run again application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

