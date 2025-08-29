---
title: Managing QGIS plugins
draft: false
tags:
  - QGIS
---
Plugins are a powerful feature in QGIS that allow you to extend the functionality of the software. Most plugins are available from the official QGIS Plugin Repository—the “app store” for QGIS. This guide will walk you through installing, updating, deactivating, and uninstalling plugins to enhance your QGIS experience.
## Installing Plugins
1. **Open the Plugin Manager:**
   Go to the **Plugins** menu and select **Manage and Install Plugins…** This will open the Plugin Manager window.
   ![[QGIS open plugin manager.png]]

2. **Understand the Plugin Manager Interface:**
   ![[QGIS plugin manager.png]]
• The Plugin Manager has several key sections:
	1. **Tabs/Filters:** Options like **All**, **Installed**, **Not Installed**, **Upgradable**, and **New** help you filter plugins based on their status.
	2. **Search Bar:** Use this to find plugins by entering keywords related to their name or functionality.
	3. **Plugin List:** Displays plugins based on your selected filter and search terms.
	4. **Plugin Information:** Provides details about the selected plugin, including its description, version, author, and more.
	5. **Action Buttons:** Allows you to **Install**, **Uninstall**, **Upgrade**, **Activate**, or **Deactivate** plugins.
3. **Search for a Plugin:**
   In the **All** or **Not Installed** tab, type a keyword (e.g., “geocoding” or “Plot”) into the search bar to find relevant plugins.
   ![[QGIS plugin search.png]]
4. **Install the Plugin:**
    Select the desired plugin from the list.
    Click the **Install Plugin** button at the bottom of the window.
    ![[QGIS plugin install.png]]
    Once installed, the plugin may add new menus, panels, or toolbars to QGIS.
    
## Updating Plugins
Plugins are regularly updated to add new features or fix bugs. By default, you will be notified about updates at startup. You can also "manually" check for updates by opening the plugin manager. If the "Upgrade all" button is active, there are updates. In the "Installed" tab, you can update the plugins individually. 


## Hiding/unhiding installed plugins, including the Processing menu

A problem I often come across is that the processing menu is missing from QGIS, and the typical reason is that the processing is a plugin that (by accident) can be hidden. To hide and unhide plugins, go to the installed tab of the plugin manager

![](https://usercontent.one/wp/www.geoinformatics.online/wp-content/uploads/2023/01/image-4.png?media=1674039083)

Here you can hide plugins by removing the little tick mark in front of a plug-in or unhiding it by adding the little tick mark.

If you encounter any issues or have questions about specific plugins, consult the [QGIS Documentation](https://www.qgis.org/resources/hub/) or reach out to the QGIS community for support.