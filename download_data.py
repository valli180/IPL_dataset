# author: Valli Akella

"""Downloads csv data from a given URL to a local filepath.
Usage: download_data.py --url=<url> --path=<path>
Options:
--url=<url>                     URL for the data file to be downloaded 
--path=<path>     Path (including filename) to save the downloaded file
"""
  
from docopt import docopt
import os
import pandas as pd

opt = docopt(__doc__)

def main(url, path): 
  
  data = pd.read_csv(url)

  try:
    data.to_csv(path, index=False)
  except:
    os.makedirs(os.path.dirname(saving_path))
    data.to_csv(path, index=False)

if __name__ == "__main__":
  main(opt["--url"], opt["--path"])