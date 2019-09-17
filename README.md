# EnviroPhat

<b>You can sense temperature, pressure, light, local color, accelerometer readings, and magnetometer data using EnviroPhat and Raspberry Pi Zero W.</b>  You can publish this sensor data to the Tangle or sell it on a data marketplace such as the [I3 Data Marketplace](http://ec2-18-217-227-236.us-east-2.compute.amazonaws.com:8000/).  Here are step-by-step instructions.

## <a  href="https://shop.pimoroni.com/products/enviro-phat">Getting EnviroPhat<br><img src="images/enviroPhat.png" width=300></a>

## <a href="https://thepihut.com/collections/raspberry-pi/products/raspberry-pi-zero-w">Getting Raspberry Pi Zero W
<img src="images/RasPiZeroHeader.jpg" width=200>
<br>The Raspberry Pi Mega Kit includes a Raspberry Pi Zero W</a> with GPIO header attached plus a 16GB MicroSD memory card with the Raspbian operating system installed.  You can use your own memory card and <a href="https://www.raspberrypi.org/downloads/raspbian/">download and install Raspbian</a> 

## Interacting with Raspberry Pi Zero W

To connect directly to your Raspberry Pi Zero W, you will need a miniHDMI-to-HDMI adaptor and a microUSB-to-USB adaptor.  Power Raspberry Pi with a wall plug or a USB battery capable of powering mobile phones.

You can connect remotely using Secure Shell (SSH).  First, you must enable SSH.  Click the <img src="images/raspberry.png" width=40> raspberry icon on the menu.  Select ```Preferences```, then select ```Raspberry Pi Configuration```.  Click the ```Interfaces``` tab and enable ```SSH```.  

![Window for enabling SSH as described in text](images/SSH.png)


## Building your device

Solder a pin header to the EnviroPhat board and snap the board onto your Raspberry Pi.  Then, install the EnviroPhat software.

```
sudo pip3 install envirophat
```

For other installation methods and details see these [instructions](https://github.com/pimoroni/enviro-phat)


## Verifying the version of Python

The Raspbian operating system comes with two versions of Python pre-installed.  This tutorial uses Python 3.  Verify that this version is installed:

```
python3 --version
$ Python 3.4.2
```

```
pip3 --version
$ pip 1.5.6 from /usr/lib/python3/dist-packages (python 3.4)
```

## Installing the [Python IOTA Workshop scripts](https://github.com/iota-community/python-iota-workshop)

This installs the Pyota client library so you can communicate with the [Tangle](https://docs.iota.org/docs/dev-essentials/0.1/concepts/the-tangle).  The workshop includes a step-by-step tutorial teaching the details of sending and receiving transactions to the Tangle.  They provide the foundation for the code used to store sensor data from EnviroPhat.

Clone the github repository, install the workshop code, and run the "hello world" example.

```
git clone https://github.com/iota-community/python-iota-workshop.git
cd python-iota-workshop
pip3 install -r requirements.txt
python3 code/e01_hello_world.py
```

The Tangle will respond with the latest statistics:

```
{'appName': 'IRI Testnet',
 'appVersion': '1.8.0-RC1',
 'coordinatorAddress': 'EQQFCZBIHRHWPXKMTOLMYUYPCN9XLMJPYZVFJSAY9FQHCCLWTOLLUGKKMXYFDBOOYFBLBI9WUEILGECYM',
 'duration': 0,
 'features': ['dnsRefresher', 'testnet', 'zeroMessageQueue', 'RemotePOW'],
 'jreAvailableProcessors': 8,
 'jreFreeMemory': 11467464304,
 'jreMaxMemory': 22906667008,
 'jreTotalMemory': 16876830720,
 'jreVersion': '1.8.0_181',
 'lastSnapshottedMilestoneIndex': 434525,
 'latestMilestone': TransactionHash(b'9KVQUHSNWATBLGJJAUNNAFPCCOLDK9MPDMLOVLSMVFIYUPLPJLLUFQWPXNLGTCQKOYFBYBLFBCHNUC999'),
 'latestMilestoneIndex': 1313941,
 'latestSolidSubtangleMilestone': TransactionHash(b'9KVQUHSNWATBLGJJAUNNAFPCCOLDK9MPDMLOVLSMVFIYUPLPJLLUFQWPXNLGTCQKOYFBYBLFBCHNUC999'),
 'latestSolidSubtangleMilestoneIndex': 1313941,
 'milestoneStartIndex': 434527,
 'neighbors': 3,
 'packetsQueueSize': 0,
 'time': 1565658746766,
 'tips': 750,
 'transactionsToRequest': 0}
```
## Using your data

You can store sensor directly to the Tangle and view it using the Tangle Explorer.  You can use custom scripts or the ZMQ listener to retrieve it.

[Storing sensor data on the Tangle](enviro-direct2Tangle.md)

[Viewing data using the Devnet Tangle Explorer](https://devnet.thetangle.org/)

[Retrieving data using ZMQ](https://github.com/NelsonPython/IoT-ZMQ-listener/blob/master/README.md)

## Selling your data

You sell data by publishing it on the I3 Marketplace where subscribers can buy it:

[Publishing data to the I3 Data Marketplace](enviro-I3-publish.md)

[Retrieving your data subscription](enviro-I3-subscribe.md)

## Planning for the future

- Add the missing retrieving data example

- Remove unnecessary instructions for generating a seed.  Data transactions do not require a seed
