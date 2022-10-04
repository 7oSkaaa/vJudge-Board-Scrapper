# vJudge Board Scrapper

Simple Scrapper to Rank Page of any contest on VJudge and Export it to CSV file

## Requirements

**Install python and pip on your device.**

```bash
# Linux User
sudo apt install python-pip
```

for windows users see how to install pip to your device from [here](https://www.activestate.com/resources/quick-reads/how-to-install-pip-on-windows/)

```bash
# Linux User open terminal and write this command
# Windows user open cmd and write this command
pip install --upgrade -r requirements.txt
```

## Usage

1. Open your contest page on vjudge
2. Get ID of your contest from the URL
   - Example: 'https://vjudge.net/contest/517904', the ID is `517904`
3. Run the script
4. Enter the ID of your contest
5. After the script finished, you will see a file named `Trainees.csv` in the same directory of the script
