# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import indradb.indradb_pb2 as indradb__pb2


class IndraDBStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/indradb.IndraDB/Ping',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Sync = channel.unary_unary(
                '/indradb.IndraDB/Sync',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateVertex = channel.unary_unary(
                '/indradb.IndraDB/CreateVertex',
                request_serializer=indradb__pb2.Vertex.SerializeToString,
                response_deserializer=indradb__pb2.CreateResponse.FromString,
                )
        self.CreateVertexFromType = channel.unary_unary(
                '/indradb.IndraDB/CreateVertexFromType',
                request_serializer=indradb__pb2.Identifier.SerializeToString,
                response_deserializer=indradb__pb2.Uuid.FromString,
                )
        self.GetVertices = channel.unary_stream(
                '/indradb.IndraDB/GetVertices',
                request_serializer=indradb__pb2.VertexQuery.SerializeToString,
                response_deserializer=indradb__pb2.Vertex.FromString,
                )
        self.DeleteVertices = channel.unary_unary(
                '/indradb.IndraDB/DeleteVertices',
                request_serializer=indradb__pb2.VertexQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetVertexCount = channel.unary_unary(
                '/indradb.IndraDB/GetVertexCount',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=indradb__pb2.CountResponse.FromString,
                )
        self.CreateEdge = channel.unary_unary(
                '/indradb.IndraDB/CreateEdge',
                request_serializer=indradb__pb2.EdgeKey.SerializeToString,
                response_deserializer=indradb__pb2.CreateResponse.FromString,
                )
        self.GetEdges = channel.unary_stream(
                '/indradb.IndraDB/GetEdges',
                request_serializer=indradb__pb2.EdgeQuery.SerializeToString,
                response_deserializer=indradb__pb2.Edge.FromString,
                )
        self.DeleteEdges = channel.unary_unary(
                '/indradb.IndraDB/DeleteEdges',
                request_serializer=indradb__pb2.EdgeQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetEdgeCount = channel.unary_unary(
                '/indradb.IndraDB/GetEdgeCount',
                request_serializer=indradb__pb2.GetEdgeCountRequest.SerializeToString,
                response_deserializer=indradb__pb2.CountResponse.FromString,
                )
        self.GetVertexProperties = channel.unary_stream(
                '/indradb.IndraDB/GetVertexProperties',
                request_serializer=indradb__pb2.VertexPropertyQuery.SerializeToString,
                response_deserializer=indradb__pb2.VertexProperty.FromString,
                )
        self.GetAllVertexProperties = channel.unary_stream(
                '/indradb.IndraDB/GetAllVertexProperties',
                request_serializer=indradb__pb2.VertexQuery.SerializeToString,
                response_deserializer=indradb__pb2.VertexProperties.FromString,
                )
        self.SetVertexProperties = channel.unary_unary(
                '/indradb.IndraDB/SetVertexProperties',
                request_serializer=indradb__pb2.SetVertexPropertiesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteVertexProperties = channel.unary_unary(
                '/indradb.IndraDB/DeleteVertexProperties',
                request_serializer=indradb__pb2.VertexPropertyQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetEdgeProperties = channel.unary_stream(
                '/indradb.IndraDB/GetEdgeProperties',
                request_serializer=indradb__pb2.EdgePropertyQuery.SerializeToString,
                response_deserializer=indradb__pb2.EdgeProperty.FromString,
                )
        self.SetEdgeProperties = channel.unary_unary(
                '/indradb.IndraDB/SetEdgeProperties',
                request_serializer=indradb__pb2.SetEdgePropertiesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteEdgeProperties = channel.unary_unary(
                '/indradb.IndraDB/DeleteEdgeProperties',
                request_serializer=indradb__pb2.EdgePropertyQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetAllEdgeProperties = channel.unary_stream(
                '/indradb.IndraDB/GetAllEdgeProperties',
                request_serializer=indradb__pb2.EdgeQuery.SerializeToString,
                response_deserializer=indradb__pb2.EdgeProperties.FromString,
                )
        self.BulkInsert = channel.stream_unary(
                '/indradb.IndraDB/BulkInsert',
                request_serializer=indradb__pb2.BulkInsertItem.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.IndexProperty = channel.unary_unary(
                '/indradb.IndraDB/IndexProperty',
                request_serializer=indradb__pb2.IndexPropertyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ExecutePlugin = channel.unary_unary(
                '/indradb.IndraDB/ExecutePlugin',
                request_serializer=indradb__pb2.ExecutePluginRequest.SerializeToString,
                response_deserializer=indradb__pb2.ExecutePluginResponse.FromString,
                )


class IndraDBServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Pings the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sync(self, request, context):
        """Syncs persisted content. Depending on the datastore implementation,
        this has different meanings - including potentially being a no-op.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateVertex(self, request, context):
        """Creates a new vertex. Returns whether the vertex was successfully
        created - if this is false, it's because a vertex with the same UUID
        already exists.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateVertexFromType(self, request, context):
        """Creates a new vertex with just a type specification. As opposed to
        `CreateVertex`, this is used when you do not want to manually specify
        the vertex's UUID. Returns the new vertex's UUID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVertices(self, request, context):
        """Gets a range of vertices specified by a query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVertices(self, request, context):
        """Deletes existing vertices specified by a query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVertexCount(self, request, context):
        """Gets the number of vertices in the datastore.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEdge(self, request, context):
        """Creates a new edge. If the edge already exists, this will update it
        with a new update datetime. Returns whether the edge was successfully
        created - if this is false, it's because one of the specified vertices
        is missing.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEdges(self, request, context):
        """Gets a range of edges specified by a query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEdges(self, request, context):
        """Deletes a set of edges specified by a query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEdgeCount(self, request, context):
        """Gets the number of edges associated with a vertex.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVertexProperties(self, request, context):
        """Gets vertex properties.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllVertexProperties(self, request, context):
        """Gets vertexes and all properties for each vertex.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVertexProperties(self, request, context):
        """Sets vertex properties.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVertexProperties(self, request, context):
        """Deletes vertex properties.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEdgeProperties(self, request, context):
        """Gets edge properties.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetEdgeProperties(self, request, context):
        """Sets edge properties.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEdgeProperties(self, request, context):
        """Deletes edge properties.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllEdgeProperties(self, request, context):
        """Gets edges and all properties for each edge.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BulkInsert(self, request_iterator, context):
        """Bulk inserts many vertices, edges, and/or properties.

        Note that datastores have discretion on how to approach safeguard vs
        performance tradeoffs. In particular:
        * If the datastore is disk-backed, it may or may not flush before
        returning.
        * The datastore might not verify for correctness; e.g., it might not
        ensure that the relevant vertices exist before inserting an edge.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IndexProperty(self, request, context):
        """Enables indexing on a specified property. When indexing is enabled on a
        property, it's possible to query on its presence and values.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecutePlugin(self, request, context):
        """Executes a plugin and returns back the response from the plugin.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IndraDBServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Sync': grpc.unary_unary_rpc_method_handler(
                    servicer.Sync,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateVertex': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateVertex,
                    request_deserializer=indradb__pb2.Vertex.FromString,
                    response_serializer=indradb__pb2.CreateResponse.SerializeToString,
            ),
            'CreateVertexFromType': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateVertexFromType,
                    request_deserializer=indradb__pb2.Identifier.FromString,
                    response_serializer=indradb__pb2.Uuid.SerializeToString,
            ),
            'GetVertices': grpc.unary_stream_rpc_method_handler(
                    servicer.GetVertices,
                    request_deserializer=indradb__pb2.VertexQuery.FromString,
                    response_serializer=indradb__pb2.Vertex.SerializeToString,
            ),
            'DeleteVertices': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteVertices,
                    request_deserializer=indradb__pb2.VertexQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetVertexCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVertexCount,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=indradb__pb2.CountResponse.SerializeToString,
            ),
            'CreateEdge': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEdge,
                    request_deserializer=indradb__pb2.EdgeKey.FromString,
                    response_serializer=indradb__pb2.CreateResponse.SerializeToString,
            ),
            'GetEdges': grpc.unary_stream_rpc_method_handler(
                    servicer.GetEdges,
                    request_deserializer=indradb__pb2.EdgeQuery.FromString,
                    response_serializer=indradb__pb2.Edge.SerializeToString,
            ),
            'DeleteEdges': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEdges,
                    request_deserializer=indradb__pb2.EdgeQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetEdgeCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEdgeCount,
                    request_deserializer=indradb__pb2.GetEdgeCountRequest.FromString,
                    response_serializer=indradb__pb2.CountResponse.SerializeToString,
            ),
            'GetVertexProperties': grpc.unary_stream_rpc_method_handler(
                    servicer.GetVertexProperties,
                    request_deserializer=indradb__pb2.VertexPropertyQuery.FromString,
                    response_serializer=indradb__pb2.VertexProperty.SerializeToString,
            ),
            'GetAllVertexProperties': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllVertexProperties,
                    request_deserializer=indradb__pb2.VertexQuery.FromString,
                    response_serializer=indradb__pb2.VertexProperties.SerializeToString,
            ),
            'SetVertexProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVertexProperties,
                    request_deserializer=indradb__pb2.SetVertexPropertiesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteVertexProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteVertexProperties,
                    request_deserializer=indradb__pb2.VertexPropertyQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetEdgeProperties': grpc.unary_stream_rpc_method_handler(
                    servicer.GetEdgeProperties,
                    request_deserializer=indradb__pb2.EdgePropertyQuery.FromString,
                    response_serializer=indradb__pb2.EdgeProperty.SerializeToString,
            ),
            'SetEdgeProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.SetEdgeProperties,
                    request_deserializer=indradb__pb2.SetEdgePropertiesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteEdgeProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEdgeProperties,
                    request_deserializer=indradb__pb2.EdgePropertyQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetAllEdgeProperties': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllEdgeProperties,
                    request_deserializer=indradb__pb2.EdgeQuery.FromString,
                    response_serializer=indradb__pb2.EdgeProperties.SerializeToString,
            ),
            'BulkInsert': grpc.stream_unary_rpc_method_handler(
                    servicer.BulkInsert,
                    request_deserializer=indradb__pb2.BulkInsertItem.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'IndexProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.IndexProperty,
                    request_deserializer=indradb__pb2.IndexPropertyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ExecutePlugin': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecutePlugin,
                    request_deserializer=indradb__pb2.ExecutePluginRequest.FromString,
                    response_serializer=indradb__pb2.ExecutePluginResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'indradb.IndraDB', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IndraDB(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/Ping',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/Sync',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateVertex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/CreateVertex',
            indradb__pb2.Vertex.SerializeToString,
            indradb__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateVertexFromType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/CreateVertexFromType',
            indradb__pb2.Identifier.SerializeToString,
            indradb__pb2.Uuid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVertices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/indradb.IndraDB/GetVertices',
            indradb__pb2.VertexQuery.SerializeToString,
            indradb__pb2.Vertex.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteVertices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/DeleteVertices',
            indradb__pb2.VertexQuery.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVertexCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/GetVertexCount',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            indradb__pb2.CountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateEdge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/CreateEdge',
            indradb__pb2.EdgeKey.SerializeToString,
            indradb__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEdges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/indradb.IndraDB/GetEdges',
            indradb__pb2.EdgeQuery.SerializeToString,
            indradb__pb2.Edge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEdges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/DeleteEdges',
            indradb__pb2.EdgeQuery.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEdgeCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/GetEdgeCount',
            indradb__pb2.GetEdgeCountRequest.SerializeToString,
            indradb__pb2.CountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVertexProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/indradb.IndraDB/GetVertexProperties',
            indradb__pb2.VertexPropertyQuery.SerializeToString,
            indradb__pb2.VertexProperty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllVertexProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/indradb.IndraDB/GetAllVertexProperties',
            indradb__pb2.VertexQuery.SerializeToString,
            indradb__pb2.VertexProperties.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetVertexProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/SetVertexProperties',
            indradb__pb2.SetVertexPropertiesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteVertexProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/DeleteVertexProperties',
            indradb__pb2.VertexPropertyQuery.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEdgeProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/indradb.IndraDB/GetEdgeProperties',
            indradb__pb2.EdgePropertyQuery.SerializeToString,
            indradb__pb2.EdgeProperty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetEdgeProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/SetEdgeProperties',
            indradb__pb2.SetEdgePropertiesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEdgeProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/DeleteEdgeProperties',
            indradb__pb2.EdgePropertyQuery.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllEdgeProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/indradb.IndraDB/GetAllEdgeProperties',
            indradb__pb2.EdgeQuery.SerializeToString,
            indradb__pb2.EdgeProperties.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BulkInsert(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/indradb.IndraDB/BulkInsert',
            indradb__pb2.BulkInsertItem.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IndexProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/IndexProperty',
            indradb__pb2.IndexPropertyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecutePlugin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indradb.IndraDB/ExecutePlugin',
            indradb__pb2.ExecutePluginRequest.SerializeToString,
            indradb__pb2.ExecutePluginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
