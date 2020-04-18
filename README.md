# rasa-chat-bot

conda info --envs
conda create -n rasa python=3.7
conda activate rasa
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

# Working version on MAC
rasa==1.9.5
rasa-sdk==1.9.0
rasa-x==0.27.5
ujson==1.35
tensorflow==2.1.0

# Working version on WIN
rasa==1.9.5
rasa-sdk==1.9.0
rasa-x==0.27.3
ujson==1.35
tensorflow==2.1.0

# To run Action Server (Custom Actions endpoints)
rasa run actions
# To test
rasa shell
