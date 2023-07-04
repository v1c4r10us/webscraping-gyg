```bash
 ______     __  __     ______    
/\  ___\   /\ \_\ \   /\  ___\   
\ \ \__ \  \ \____ \  \ \ \__ \  
 \ \_____\  \/\_____\  \ \_____\ 
  \/_____/   \/_____/   \/_____/ 
                                 
[*] webscraping in progress...
```
# Intro
Project about obtain information of travel agency.

# Stack
+ Python (Selenium, bs4, requests)
+ Linux environment (default Debian bullseye)
+ Bash script

# Execution
1. Execute requirements.sh
```bash
$ bash requirements.sh
```
2. Create directories
```bash
$ mkdir peru
$ cd peru
$ mkdir html
$ mkdir json
```
3. Obtain all html bodies (change recursive function if is necesary according to country)
```bash
$ bash htmlgen.sh
```
4. When process stop /peru/html will have all html contents saved and ready for scraping
5. Finally execute bs.sh
```bash
$ bash bs.sh
```
6. **Important**: This process take a lot of time (hours) according to quantity of pages in /peru/html, and consume around 2GB of RAM. The result of every operation is visualized on terminal.
7. When the process is completed will generate the same quantity of json files than /peru/html on /peru/json

# Disclaimer
The purpose of this project is only academic. Its execution is under your responsability.
