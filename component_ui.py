'''

@author: jrosner
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input',  
                    required=True, 
                    help='the input bam file')

args, unknown = parser.parse_known_args()
