from android.permissions import request_permissions, Permission

def request_storage_permission():
    request_permissions([
        Permission.INTERNET,
        Permission.ACCESS_NETWORK_STATE,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE
    ])
