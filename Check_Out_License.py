""" 
    Checks out the specified license.
    If the account that created the license is the same that is performing the check out, 
    you must specify the account as the beneficiary.
"""

response = client.checkout_license(
    ProductSKU='string',
    CheckoutType='PROVISIONAL'|'PERPETUAL',
    KeyFingerprint='string',
    Entitlements=[
        {
            'Name': 'string',
            'Value': 'string',
            'Unit': 'Count'|'None'|'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'
        },
    ],
    ClientToken='string',
    Beneficiary='string',
    NodeId='string'
)

"""
for more information:
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.checkout_license
"""