# Facebook Groupchat Reminder Automation
An automation project for reminding members of a group chat within a Facebook Messenger group chat. 

**Solely Tested On:** Linux (Ungoogled Chromium)

**NOTE:** UI and accessibility are not yet developed. Not easily accessible unless parameters within the code are edited.

## Code Structure
Three core components of the code are:

1. Timechecker
1. The chat manager
1. Window and browser manager

The first part anchors which time would the script remind the group chat.

The second part circumvents the lack of API available for Facebook Messenger, landing on the group chat website, and manages the multiple line messaging.

The third part currently isn't fully finished, the code is meant to open a browser and ensure that the circumvention of UI would be fully executed. Currently, the code only opens the tested browser. Further development would be required.