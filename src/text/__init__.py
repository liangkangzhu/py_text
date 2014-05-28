import tft_awk
import tft_grep
import tft_diff
import tft_tools

def tft_awk(regex, target, split, column):
    return tft_awk.awk(regex, target, split, column)
    
def grep(regex, target, model, number=False):
    return tft_grep.grep(regex, target, model, number)

def diff_file(src_filename, dst_filename):
    return tft_diff.diff_file(src_filename, dst_filename)

def load_file_as_list(filename):
    return tft_tools.load_file_as_list(filename)

def load_file(filename):
    return tft_tools.load_file(filename)

def load_property(filename):
    return tft_tools.load_property(filename)

def save_property(filename, config):
    tft_tools.save_property(filename, config)