import grpc
from concurrent import futures
import pandas as pd
import json
import pandas_service_pb2
import pandas_service_pb2_grpc
import scipy

from data_frame_method_args import DataFrameMethodArgs

class PandasServiceServicer(pandas_service_pb2_grpc.PandasServiceServicer):

    def RunMethod(self, request, context):
        try:
            # Deserialize the input JSON into a DataFrameMethodArgs object
            input_data = json.loads(request.input_json)
            restored_obj = DataFrameMethodArgs.from_dict(input_data)
            df = restored_obj.df
            method = restored_obj.method
            args = restored_obj.args

            # Dynamically call the specified pandas method
            pandas_method = getattr(df, method)
            result = pandas_method(**args)

            # Convert the result DataFrame to JSON and return it
            return pandas_service_pb2.MethodResponse(result=result.to_json(), status="success")
        except Exception as e:
            # Return the error message as a string
            return pandas_service_pb2.MethodResponse(result="", status="error", error_message=str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pandas_service_pb2_grpc.add_PandasServiceServicer_to_server(PandasServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("GRPC Server started")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
