# Speedcast Software Engineer task
## Intro
We are looking to continuously assess the connection quality, the metrics we are looking
for are latency measured from an RTT (Round Trip Time) perspective in milliseconds (ms).
Once the latency has been calculated, we’ll want to look at the jitter on the link itself to
assess the stability

## Project Instructions
By using an original well known ping source code.
the application calculate average latency and Jitter per all checked packets.

## command line parameters
The only accepted command line parameters are
* The target host IP
* The packet count [2-50]
* interval between sent packets [0.1ms-10ms]

>**_NOTE_**: Connection fails will not count toward calculation.

## Output
* [IP] Test result: average Latency [F]ms, Jitter [F]ms (N result).
    * If at least 2 results were successful.
    * F is a float rounded to 2 digits fraction.
    * N is a whole number
* [IP] Test Failed
    * If 1 or 0 results were successful
    * Failing pings usually takes more time to report so it might be better to
      determine a failing connection before trying all packets [for example
      the lower of 5 or half of the total requested packets]

## python app
* The python app is using the adv_ping cpp, as a CLI, to Continuously measure ping average latency and jitter according to different inputs(packet count and interval between packets).
* The python keep each and every run of the adv_ping, and accumulate it.
* This data is gathered in memory as a json, in the end a json file is created.

## Build and Use project
### setup environment
1. download git: sudo apt-get install git.
2. clone the project from github: git clone git@github.com:yotamnoy1000/speedcast-task.git
3. download cpp development essentials: sudo apt-get update && sudo apt-get install build-essential
4. install python3: sudo apt-get install python3.
5. install cmake: sudo apt-get install cmake.

### building the project
1. ~/speedcast-task$ mkdir build
2. ~/speedcast-task$ cd build
3. ~/speedcast-task/build$ cmake..
3. ~/speedcast-task/build$ make.

### using the project
1. one way to use the project is to run the cpp project directly for a specific input:
    * example: ~/speedcast-task/build$ sudo ./PingAdvance www.google.com -c 3 -i 0.1
2. second way in using the python script, then will run the cpp project multiple time and gather the data:
    * example: ~/speedcast-task$ ~/speedcast-task  
    * when the python is done the json data will be located at ~/speedcast-task/captured_data.json