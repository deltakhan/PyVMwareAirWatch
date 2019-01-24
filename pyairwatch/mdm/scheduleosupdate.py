from .mdm import MDM


class ScheduleOSUpdate(MDM):
    """
    For Schedule OS Update
    """
    def __init__(self, client):
        MDM.__init__(self, client)
        self.jheader = {'Content-Type': 'application/json'}

    def update_device(self, os_update_product_keys, install_action,
                      serialnumber=None, macaddress=None, udid=None,
                      imeinumber=None, easid=None):

        """
        Needs work
        """
        path = '/devices/commands/scheduleosupdate'
        params = {}
        if serialnumber:
            params['searchby'] = 'Serialnumber'
            params['id'] = str(serialnumber)
        # elif macaddress:
        #     response = self.search(searchby='Macaddress', id=str(macaddress))
        # elif udid:
        #     response = self.search(searchby='Udid', id=str(udid))
        # elif imeinumber:
        #     response = self.search(searchby='ImeiNumber', id=str(imeinumber))
        # elif easid:
        #     response = self.search(searchby='EasId', id=str(easid))
        else:
            return None
        params['installaction'] = 'default'
        body = os_update_product_keys
        return MDM._get(path=path, params=params,)
