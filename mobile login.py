# importing the device object as 'me' from uiautomator library
from uiautomator import device as me

# Using Selectors to identify specific UI object in current window, here textMatches, descriptionMatches and resourceIdMatches are selectors.
# Any one of the Selectors (e.g.: text, resource-id, description, etc)
# is sufficient to automate the Android applications.
me(textMatches="thome").click()

# After setting the alarm pressing back to reach home screen
me.press.back()