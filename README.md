# DeepSentiment

### This is a python wrapper around Stanford's CoreNLP project V3.6.0 specifically for Sentiment Analysis.

[![GitHub release](https://img.shields.io/badge/release-0.1.0-green.svg?maxAge=2592000)](https://github.com/AbhinavBhatnagar/DeepSentiment/releases) [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/AbhinavBhatnagar/DeepSentiment/blob/master/LICENSE) 



## Install
You can clone the DeepSentiment but you would need a jar file to run the code, for that you can go to release tab or else below mentioned bitbucket directory and get the file under DeepSentiment/DeepSentiment/resources and put it under the same directory.

Download the jar file from the release tab or https://bitbucket.org/crossviral/deepsentiment 


## Usage

Wrapper's code has been taken from Stanford's deepsentiment project for Sentiment Annotation trees and parsing. The python code here opens up on 9000 port on localhost.

```
from DeepSentiment import GetSentiment
import time
grab = GetSentiment.DeepSentiment()
grab.run_server()
time.sleep(5)
```

After the server is running, parse the text to deepsentiment function and output would be coming as json format which could be handled by get functions. If you just want the sentiment then get_sentiment should work. If you are looking for specific scores for the text then you can make use of get_sentiment_score function. Don't forget to stop the server if you want to set the port free.

```
result = grab.deepsentiment("amazing place you have here")
print(grab.get_sentiment(result))
print(grab.get_sentiment_score(result))
grab.stop_server()
```
