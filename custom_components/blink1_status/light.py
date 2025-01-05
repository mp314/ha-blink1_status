"""Blink(1) Status Light integration."""
import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
import homeassistant.util.color as color_util

# Import the device class from the component that you want to support
from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_HS_COLOR,
    ATTR_SUPPORTED_COLOR_MODES,
    ColorMode,
    LightEntity,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Blink(1) light platform."""
    from blink1.blink1 import Blink1
    b1 = Blink1()
    async_add_entities([blink1_status(b1)])    


class blink1_status(LightEntity):
    """Representation of a BlinkLight Light."""

    def __init__(self, light):
        """Initialize an AwesomeLight."""
        self._light = light
        self._name = "Blink1"
        self._state = None
        self._hs_color = [0, 0]
        self._brightness = 0

    #new
    @property
    def supported_color_modes(self):
        """Return the supported color modes."""
        return {ColorMode.HS}

    #new
    @property
    def color_mode(self):
        """Return the current color mode."""
        return ColorMode.HS

    @property
    def brightness(self):
        """Read back the brightness of the light."""
        return self._brightness

#    @property
#    def supported_features(self):
#        """Flag supported features."""
#        return SUPPORT_BRIGHTNESS | SUPPORT_COLOR

    @property
    def name(self):
        """Return the display name of this light."""
        return self._name

    @property
    def hs_color(self):
        """Return the color of this light."""
        return self._hs_color

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Instruct the light to turn on."""
        if ATTR_HS_COLOR in kwargs:
            self._hs_color = kwargs[ATTR_HS_COLOR]
        if ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]

        hs_color = [
            max(0, min(360, self._hs_color[0])),
            max(0, min(255, self._hs_color[1]))
        ]
        brightness = max(0, min(self._brightness, 255))
            
            
        self._state = True
        rgb_color = color_util.color_hsv_to_RGB(self._hs_color[0], self._hs_color[1], self._brightness / 255 * 100)
        hex_color = "#" + color_util.color_rgb_to_hex(*rgb_color)
        self._light.fade_to_rgb(100, *rgb_color)

    def turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        self._state = False
        self._light.off()


    def update(self):
        """Fetch the latest state from the device."""
    #   """There is not data to get as we use an assumed state."""
        #try:
        #    self._state = True  # Hier könntest du echte Daten vom Gerät abrufen
        #    self._hs_color = [0, 0]
        #    self._brightness = 255
        #except Exception as e:
        #    _LOGGER.error("Failed to fetch light state: %s", e)



