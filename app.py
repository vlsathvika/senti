import os
import subprocess
import streamlit as st

# Clone the private repository using subprocess to avoid gitpython issues
if not os.path.exists('sentimenttool'):
    subprocess.run(['git', 'clone', f'https://{os.getenv("GITHUB_TOKEN")}@github.com/vlsathvika/sentimenttool.git', 'sentimenttool'], check=True)

# Import your code from the cloned repository
import sentimenttool.final as final 

exec(open('sentimenttool/final.py').read())
