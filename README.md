# bitcoin-ticker
Simple bitcoin ticker for the Pimorono InkyPhat Red.

## Equipment
* Raspberry Pi Zero W v1.1
* Pimorono Inky pHAT Red (SSD1608)

## Setup
1. Install Raspbian Lite
2. Update and upgrade 
```Bash
sudo apt update
```
```Bash
sudo apt upgrade
```
3. Install Inky pHAT 
```Bash
curl https://get.pimoroni.com/inky | bash
```
4. Install Git
```Bash 
sudo apt install git
```
5. Clone this repo
```Bash
git clone https://github.com/Rubstubs/bitcoin-ticker.git
```
6. Add job to crontab (runs every minute with this setup)
```Bash
crontab -e
```
Then add this line
```Bash
* * * * * python3 /home/pi/bitcoin-ticker/bitcoin-ticker.py
```