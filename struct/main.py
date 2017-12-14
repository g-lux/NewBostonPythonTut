# use struct to convert data types to bytes.

from struct import *

# store as bytes data
# pack(type of data ie integer, float , and then the values
packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

# calculates how many bytes in a data type
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get byte data back to normal b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'
original_data = unpack('iif', packed_data)
print(original_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))
