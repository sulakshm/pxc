#
# Install:
#   pip3 install --user --upgrade libopenstorage-openstorage
#
import grpc

from openstorage import api_pb2
from openstorage import api_pb2_grpc
from openstorage import connector

c = connector.Connector()
channel = c.connect()

try:
    # Cluster connection
    clusters = api_pb2_grpc.OpenStorageClusterStub(channel)
    ic_resp = clusters.InspectCurrent(api_pb2.SdkClusterInspectCurrentRequest())
    print('Conntected to {0} with status {1}'.format(ic_resp.cluster.id, api_pb2.Status.Name(ic_resp.cluster.status)))

    # Create a volume
    volumes = api_pb2_grpc.OpenStorageVolumeStub(channel)
    v_resp = volumes.Create(api_pb2.SdkVolumeCreateRequest(
        name="myvol",
        spec=api_pb2.VolumeSpec(
            size=10*1024*1024*1024,
            ha_level=3,
        )
    ))
    print('Volume id is {0}'.format(v_resp.volume_id))
except grpc.RpcError as e:
    print('Failed: code={0} msg={1}'.format(e.code(), e.details()))

