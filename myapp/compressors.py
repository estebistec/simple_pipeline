from cssmin import cssmin
from pipeline.compressors import CompressorBase


class CssminCompressor(CompressorBase):

    # NOTE Here's one thing that was documented wrong...
    # def compress(self, css):
    def compress_css(self, css):
        return cssmin(css)
