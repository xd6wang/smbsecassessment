check_group_map = {
    'check112': ('iam', 'credentialleakage'),
    'check113': ('iam', 'credentialleakage'),
    'check119': ('iam', 'credentialleakage'),
    'check12': ('iam', 'credentialleakage'),
    'extra71': ('iam', 'credentialleakage'),
    'extra7123': ('iam', 'credentialleakage'),
    'extra7141': ('iam', 'credentialleakage'),
    'extra741': ('iam', 'credentialleakage'),
    'extra742': ('iam', 'credentialleakage'),
    'extra759': ('iam', 'credentialleakage'),
    'extra760': ('iam', 'credentialleakage'),
    'extra768': ('iam', 'credentialleakage'),
    'extra775': ('iam', 'credentialleakage'),
    'check11': ('iam', 'leastpriviledge'),
    'check122': ('iam', 'leastpriviledge'),
    'extra7100': ('iam', 'leastpriviledge'),
    'extra7185': ('iam', 'leastpriviledge'),
    'check41': ('infra', 'publicaccess'),
    'check42': ('infra', 'publicaccess'),
    'extra711': ('infra', 'publicaccess'),
    'extra7134': ('infra', 'publicaccess'),
    'extra7135': ('infra', 'publicaccess'),
    'extra7136': ('infra', 'publicaccess'),
    'extra7137': ('infra', 'publicaccess'),
    'extra7140': ('infra', 'publicaccess'),
    'extra7143': ('infra', 'publicaccess'),
    'extra7145': ('infra', 'publicaccess'),
    'extra7147': ('infra', 'publicaccess'),
    'extra716': ('infra', 'publicaccess'),
    'extra7177': ('infra', 'publicaccess'),
    'extra7178': ('infra', 'publicaccess'),
    'extra7179': ('infra', 'publicaccess'),
    'extra7186': ('infra', 'publicaccess'),
    'extra72': ('infra', 'publicaccess'),
    'extra723': ('infra', 'publicaccess'),
    'extra727': ('infra', 'publicaccess'),
    'extra73': ('infra', 'publicaccess'),
    'extra731': ('infra', 'publicaccess'),
    'extra736': ('infra', 'publicaccess'),
    'extra749': ('infra', 'publicaccess'),
    'extra750': ('infra', 'publicaccess'),
    'extra751': ('infra', 'publicaccess'),
    'extra752': ('infra', 'publicaccess'),
    'extra753': ('infra', 'publicaccess'),
    'extra754': ('infra', 'publicaccess'),
    'extra755': ('infra', 'publicaccess'),
    'extra76': ('infra', 'publicaccess'),
    'extra77': ('infra', 'publicaccess'),
    'extra771': ('infra', 'publicaccess'),
    'extra779': ('infra', 'publicaccess'),
    'extra78': ('infra', 'publicaccess'),
    'extra787': ('infra', 'publicaccess'),
    'extra788': ('infra', 'publicaccess'),
    'extra795': ('infra', 'publicaccess'),
    'extra796': ('infra', 'publicaccess'),
    'extra798': ('infra', 'publicaccess'),
    'extra7167m': ('infra', 'ddos'),
    'extra7169m': ('infra', 'ddos'),
    'extra7170m': ('infra', 'ddos'),
    'extra7129': ('infra', 'waf'),
    'extra773': ('infra', 'waf'),
    'extra744': ('infra', 'waf'),
    'check21': ('detection', 'audit'),
    'check22': ('detection', 'audit'),
    'check23': ('detection', 'audit'),
    'check118': ('detection', 'monitoring'),
    'check25': ('detection', 'monitoring'),
    'extra713': ('detection', 'monitoring'),
    'extra7139': ('detection', 'monitoring'),
    'extra730': ('detection', 'monitoring'),
    'extra769m': ('detection', 'monitoring'),
    'extra799': ('detection', 'monitoring'),
    'extra729': ('data', 'encryption'),
    'extra735': ('data', 'encryption'),
    'extra740': ('data', 'encryption'),
    'extra761': ('data', 'encryption'),
    'extra797': ('data', 'encryption'),
    'extra739': ('data', 'backup')
}

category_translate_map = {
    'iam': '身份和访问控制',
    'infra': '基础架构安全',
    'detection': '安全监控',
    'data': '数据安全'
}

# map "CAF Epic" to category
epic_category_map = {
    "Data Protection":'data',
    "IAM":'iam',
    "Infrastructure Security": 'infra',
    "Logging and Monitoring": 'detection',
}

# return category info: iam/infra/detection/data
def getCategory(findingInfo):
    check_id = findingInfo['check_id']
    epic = findingInfo['CAF Epic']
    # default category set to infra
    category = 'infra'
    if check_id in check_group_map.keys():
        category = check_group_map[check_id][0]
    elif epic in epic_category_map.keys():
        category = epic_category_map[epic]
    #print(check_id, epic, category)
    return category

# return subCategory info
# valid subCategory
# "credentialleakage": set(),
# "leastpriviledge": set(),
# "publicaccess": set(),
# "audit": set(),
# "monitoring": set(),
# "encryption": set(),
# "backup": set(),
# "waf": set(),
# "ddos": set(),
# "other": set(),
def getSubCategory(findingInfo):
    check_id = findingInfo['check_id']
    # default subCategory set to other
    subCategory = 'other'
    if check_id in check_group_map.keys():
        subCategory = check_group_map[check_id][1]
    return subCategory