# Customer Invite

Files Included - 
- CustomerInvite - Orchestrator
- customerInviteTest - Test cases for the script
- setup - setup and running

## How to run
make sure python2 is installed.
clone the project in local

    git clone https://github.com/chitranshi21/CustomerInvite.git

From the command line go to the project directory 

    cd CustomerInvite
To run test cases 

    python setup.py test
To get customer List

    python setup.py run

To change the location of data file edit the customerInvite.py and change the value of variable `CUSTOMER_LIST_FILE_PATH` to desired path.



