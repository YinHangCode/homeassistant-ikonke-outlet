import os

from homeassistant.components.switch import SwitchDevice
from homeassistant.const import DEVICE_DEFAULT_NAME

platformVersion = "0.0.2"

# pylint: disable=unused-argument
def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    print("[IkonkeOutletPlatform][INFO]*********************************************************************")
    print("[IkonkeOutletPlatform][INFO]                IkonkeOutletPlatform v%s By YinHang"%(platformVersion))
    print("[IkonkeOutletPlatform][INFO]  GitHub: https://github.com/YinHangCode/homeassistant_ikonke_outlet ")
    print("[IkonkeOutletPlatform][INFO]                                                 QQ Group: 107927710 ")
    print("[IkonkeOutletPlatform][INFO]*********************************************************************")
    print("[IkonkeOutletPlatform][INFO]start success...")
    
    addDeviceArr = []
    
    ikonkeIO = config.get("ikonkeIO")
    deviceCfgs = config.get("deviceCfgs")
    for deviceCfg in deviceCfgs:
            type = deviceCfg.get("type")
            if type == "k2":
                addDeviceArr.append(\
                    K2Outlet("k2_" + deviceCfg.get("mac").replace('-',''), 'mdi:power-socket', ikonkeIO, deviceCfg.get("type"), deviceCfg.get("ip"), deviceCfg.get("mac"), deviceCfg.get("password")))
            elif type == "k2pro":
                addDeviceArr.append(\
                    K2ProOutlet("k2pro_" + deviceCfg.get("mac").replace('-',''), 'mdi:power-socket', ikonkeIO, deviceCfg.get("type"), deviceCfg.get("ip"), deviceCfg.get("mac"), deviceCfg.get("password")))
            elif type == "mini_b":
                addDeviceArr.append(\
                    MiniBOutlet("mini_b_" + deviceCfg.get("mac").replace('-',''), 'mdi:power-socket', ikonkeIO, deviceCfg.get("type"), deviceCfg.get("ip"), deviceCfg.get("mac"), deviceCfg.get("password")))
            else:
                print("[IkonkeOutletPlatform][ERROR]error type" + type)
    
    add_devices_callback(addDeviceArr)

class IkonkeOutletBase(SwitchDevice):
    ikonkeIO = ''
    type = ''
    ip = ''
    mac = ''
    passwd = ''
    
    def __init__(self, name, icon, ikonkeIO, type, ip, mac, passwd):
        self._name = name or DEVICE_DEFAULT_NAME
        self._icon = icon
        self._state = False
        self._available = False
        
        self.ikonkeIO = ikonkeIO
        self.type = type
        self.ip = ip
        self.mac = mac
        self.passwd = passwd
        
        self.update()
    
    @property
    def name(self):
        return self._name
    
    @property
    def icon(self):
        return self._icon
    
    @property
    def available(self) -> bool:
        return self._available
    
    @property
    def should_poll(self):
        return True
    
    def update(self):
        command = 'sh ' + self.ikonkeIO + ' -C ' + self.type + ' ' + self.ip + ' ' + self.mac + ' ' + self.passwd + ' getRelay'
        result = os.popen(command).read().strip('\n')
        if result == 'open':
            self._state = True
            self._available = True
        elif result == 'close':
            self._state = False
            self._available = True
        else:
            self._available = False
    
    @property
    def is_on(self):
        return self._state
    
    def turn_on(self, **kwargs):
        command = 'sh ' + self.ikonkeIO + ' -C ' + self.type + ' ' + self.ip + ' ' + self.mac + ' ' + self.passwd + ' setRelay open'
        result = os.popen(command).read().strip('\n')
        if result == 'success':
            self._state = True
            self.schedule_update_ha_state()
        else:
            pass
    
    def turn_off(self, **kwargs):
        command = 'sh ' + self.ikonkeIO + ' -C ' + self.type + ' ' + self.ip + ' ' + self.mac + ' ' + self.passwd + ' setRelay close'
        result = os.popen(command).read().strip('\n')
        if result == 'success':
            self._state = False
            self.schedule_update_ha_state()
        else:
            pass

class K2Outlet(IkonkeOutletBase):
    pass

class K2ProOutlet(IkonkeOutletBase):
    pass

class MiniBOutlet(IkonkeOutletBase):
    pass


