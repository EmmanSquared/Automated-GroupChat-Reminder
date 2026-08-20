# Automation Group Chat Reminder

An automation project for sending a message to a group chat on Facebook Messenger.

**Solely Tested On:** Linux (Ungoogled Chromium)

****NOTE:**** The UI and accessibility are not yet developed. The project is currently not easily accessible unless the parameters within the code are manually edited.

## Code Structure

The code consists of three core components:

1. **Timechecker**
2. **Chat Manager**
3. **Window and Browser Manager**

### 1. Timechecker

The first component determines and anchors the time at which the script will send a reminder to the group chat.

### 2. Chat Manager

The second component handles the lack of an available API for Facebook Messenger. It navigates to the group chat through the website and manages the sending of multiple lines of messages.

### 3. Window and Browser Manager

The third component is responsible for opening and managing the browser, ensuring that the UI automation can be executed properly.

This component is not yet fully finished. Currently, it only opens the tested browser. Further development is required to fully automate and manage the window switching interaction.
