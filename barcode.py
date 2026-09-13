import barcode
from barcode.writer import ImageWriter

n="123456789012"

code=barcode.get('ean13', n, writer=ImageWriter())
code.save('my_barcode')