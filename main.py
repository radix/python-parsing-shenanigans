"""
An example of using non-Python programming languages in .py file.

The idea is that you have a .py module with a # coding: foo tag at the top,
and the implementation of the "foo" language is one that takes the content of
the file and produces Python source code.
"""
import codecs
from encodings.utf_8 import StreamWriter


class MyStreamReader(codecs.StreamReader):

    def read(self, size=-1, chars=-1, firstline=False):
        # THIS is where the parsing happens. This example just slurps in
        # everything but you could honor size if you want (or otherwise do the
        # reading incrementally).
        data = ""
        new_data = self.stream.read()
        while new_data:
            data += new_data
            new_data = self.stream.read()
        return data.decode("utf-8", errors=self.errors)[::-1]


# Some "shady" things about our CodecInfo object:
# - the simple "encode" function is stock utf_8_encode because it seems the
#   python importer re-encodes the string literals. I don't understand this
#   yet.
# - all of the things set to None aren't used by the python importer.

my_encoding = codecs.CodecInfo(
    codecs.utf_8_encode,
    None,
    streamreader=MyStreamReader,
    streamwriter=None,
    incrementalencoder=None,
    incrementaldecoder=None,
    name="my-encoding")


def my_search_function(name):
    if name == "my-encoding":
        return my_encoding


codecs.register(my_search_function)


import custom_language_example
