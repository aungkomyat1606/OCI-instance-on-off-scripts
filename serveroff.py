import oci

def stop_instance(instance_ocid):
    # Initialize the Compute client
    config = oci.config.from_file()
    compute_client = oci.core.ComputeClient(config)

    try:
        # Get the instance details
        instance = compute_client.get_instance(instance_ocid).data

        # Check if the instance is in a state that can be stopped
        if instance.lifecycle_state == "RUNNING":
            print(f'Stopping instance: {instance_ocid}')
            compute_client.instance_action(instance_ocid, 'STOP')
            print(f'Instance {instance_ocid} is being stopped.')
        else:
            print(f'Instance {instance_ocid} is not in a running state; current state: {instance.lifecycle_state}')
    except oci.exceptions.ServiceError as e:
        print(f'Error stopping instance {instance_ocid}: {str(e)}')

if __name__ == '__main__':
    # Cinema server
    instance_ocid = 'ocid1.instance.oc1.ap-tokyo-1.anxhiljrrf6sm3ycg6r73m5rnteeo6mccshpmqqvz7gk6zjbzwtmbnzcbczq'
    stop_instance(instance_ocid)