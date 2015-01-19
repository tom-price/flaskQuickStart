# flaskQuickStart
Create a server on rackspace & login

Update and install key programs:
$ apt-get update &&  apt-get upgrade && apt-get install curl vim git

Optionally setup rackspace monitoring (this line specific to Ubuntu 14.04)
$ sudo sh -c 'echo "deb http://stable.packages.cloudmonitoring.rackspace.com/ubuntu-14.04-x86_64 cloudmonitoring main" > /etc/apt/sources.list.d/rackspace-monitoring-agent.list' && curl https://monitoring.api.rackspacecloud.com/pki/agent/linux.asc | sudo apt-key add - && sudo apt-get update && sudo apt-get install rackspace-monitoring-agent && sudo rackspace-monitoring-agent --setup
Enter your rackspace credentials and create a new token for the server if asked
$ service rackspace-monitoring-agent start

Optionally change your default text editor
$ update-alternatives --config editor

Set up and configure a user for yourself
$ adduser user
$ visudo
  Add: user ALL=(ALL) ALL

