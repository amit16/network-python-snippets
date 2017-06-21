si = connect.SmartConnect(host=<vCenter Host IP>, 
                         user=<administrator@vsphere-local>,
                         pwd=<password>)
                         
vm_folders = si.content.rootFolder.childEntity[0].vmFolder.childEntity

for folder in vm_folders:
        VMs = folder.childEntity
        for vm in VMs:
                if vm.runtime.connectionState == 'orphaned':
                        print "Removing from inventory : ", vm.name
                        vm.UnregisterVM()
