import requests as rq
import joblib as jb
import os

class DetectPhising:
    link = None

    def __init__(self,link):
        self.link = link

    def predict(self):
        try:
            self._testIfLinkExists()
            return self._loadAndPredict()
        except Exception as e:
            return e

    def _loadAndPredict(self):
        currentPath = os.path.dirname(__file__)
        model = os.path.join(currentPath, "phishingModel.pkl")

        try:
            file = open(model, "rb")
            model = jb.load(file)
            
            X_predict = [self.link.replace("https://", "").replace("http://", "")]
            file.close()
            return model.predict(X_predict)[0]
        except Exception as e:
            print(e)
            raise Exception("Oops, Seems Like We have Encountered an Issue")
        

    def _testIfLinkExists(self):
        if(self.link == None):
            raise Exception("Please Insert Link First")

        elif(self.link == ""):
            raise Exception("Please Insert A Valid Link")

        try:
            r = rq.get(self.link, timeout=5)
            if(r.status_code == 404):
                raise Exception("Oops We Couldn't Find the Requested Link")
            
            return r.status_code
        except rq.exceptions.MissingSchema:
            raise Exception(f"Oops, {self.link} Is Not A Valid Link, please make it (http/https)://{self.link}")
        except Exception:
            raise Exception("Oops, Seems Like We have Encountered an Issue With Fetching the url")
            