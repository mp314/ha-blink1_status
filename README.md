# Blink(1) Integration - Fork with new ColorMode

Forked from: https://github.com/tnagels/ha-blink1_status

Updated light.py with newer ColorModes.<br>
So it's only needed to switch the light.py file in the blink1_status Folder

Seems to work on my HomeAssistant Configuration, but use with caution and ON YOUR OWN RISK! (do Backups and stuff....)



This integration sets up and uses a Blink(1) usb status led for use within Home Assistant.


### Installation

Copy this folder to `<config_dir>/custom_components/blink1/`. Thanks to the work of Qu3uk you can now also add this repo to HACS for easy installation.


Add the following entry in your `configuration.yaml`:

```yaml
light:
  - platform: blink1_status 
```

### Remarks
- Use at your own risk. This is far from complete, but for me it works.
- Feel free to do anything with the code, for my work there is no license attached.
