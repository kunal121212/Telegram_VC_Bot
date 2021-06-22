HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ
    from dotenv import load_dotenv
    
    load_dotenv()  # take environment variables from .env.
    API_ID = 4195152
    API_HASH = "2642c0b549ceca3a381c26339e0017e0"
    SESSION_STRING = "BQAmR7AWGuChz_k-51vUR1J3JJPf-cBCNp3BPaFeE4b_zk527dB-FfH6iJ2q7AOKVcc007L1o5KhgMuiHdptm9jeLZNrdbS-4BJab1ssVy_rW_DyBOv74a7nXJwiDW35EfMF-7KFcfmAgckTpRb5XZ5Sa4xhb6QWBhf255JHtf_EEVE_6ZDCWZyIKYh9xxNCef1gkovx0-X5_jfumlfb3yUL8jsccjzKyH1qoCCf8sfsA5gFqm-oEEzKdvD4g01M92u0J5VWPEIGen8JiHkGC16Amjbp3JZyAcJqa19LH5mEURy1CAVPigit2qQ1W7Iqrq88Ver9WEWAvysrv0C4xUARZ1sg1AA"  # Check Readme for session
    ARQ_API_KEY = "XGNFME-JZYRAG-SXNFIX-MKKXKA-ARQ"
    DEFAULT_SERVICE = "youtube"

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    DEFAULT_SERVICE = "youtube"     # Must be one of "youtube"/"deezer"/"saavn"

# don't make changes below this line
ARQ_API = "https://thearq.tech"
