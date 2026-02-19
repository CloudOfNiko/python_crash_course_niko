# CloudOfNiko
# 20.02.2026
# Learning to use dictionaries in Python.

pod_0 = {
    'name' : 'Pod 042',
    'occupation' : 'YoRHa Tactical Support Unit',
    'support_to' : ['2B', 'A2']
    }

pod_1 = {
    'name' : 'Pod 153',
    'occupation' : 'YoRHa Tactical Support Unit',
    'support_to' : ['9S']
    }

pod_2 = {
    'name' : 'Pod 006',
    'occupation' : 'YoRHa Tactical Support Unit',
    'support_to' : ['10H']
    }

pods = [pod_0, pod_1, pod_2]

for pod in pods:
    print(f"\n{pod['name']}")
    print(f"\tType: {pod['occupation']}")
    print(f"\tSupports:")
    units = pod['support_to']
    for unit in units:
        print(f"\t\t\t{unit}")