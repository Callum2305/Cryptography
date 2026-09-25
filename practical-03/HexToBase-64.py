#decode hex string into bytes, and then encode in base64:
import base64

i ="42617365363420697320776964656C79207573656420666F722073656E64696E6720652D6D61696C206174746163686D656E74732E"

bytes = bytes.fromhex(i)

print(base64.b64encode(bytes).decode())
