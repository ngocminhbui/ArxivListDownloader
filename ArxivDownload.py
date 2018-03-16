
# coding: utf-8

# In[1]:


import arxiv
import argparse
import os
from tqdm import tqdm
# In[6]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', required=True)
    parser.add_argument('-o', '--output_dir', default='./')
    
    args = parser.parse_args()
    if os.path.exists(args.output_dir)==False:
        os.makedirs(args.output_dir)
    l = open(args.list).readlines()
    for i in tqdm(range(len(l))):
        ti=l[i]
        q = 'ti:"{0}"'.format(ti.strip()).replace('-',' ')
        print q
        r = arxiv.query(q)
        try:
            d = arxiv.download(dirname=args.output_dir,obj= r[0])
        except Exception as e:
            print e
            print 'failed downloading: ', ti

