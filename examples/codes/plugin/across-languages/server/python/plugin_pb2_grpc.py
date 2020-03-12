# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import plugin_pb2 as plugin__pb2


class PluginStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Call = channel.unary_unary(
        '/proto.Plugin/Call',
        request_serializer=plugin__pb2.Request.SerializeToString,
        response_deserializer=plugin__pb2.Response.FromString,
        )


class PluginServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PluginServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Call': grpc.unary_unary_rpc_method_handler(
          servicer.Call,
          request_deserializer=plugin__pb2.Request.FromString,
          response_serializer=plugin__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Plugin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))