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

