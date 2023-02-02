#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import Session, Response
from sys import argv
from typing import Optional
import re




        
class DownloadCardImage:
    __url: str = "https://scptcgjpj.fandom.com/ja/api.php"
    __session = Session()
    
    @staticmethod
    def __isOk(statusCode: int) -> bool:
        if 200 <= statusCode and statusCode < 300:
            return True
        if 300 <= statusCode and statusCode < 400:
            print("[Info] Redirection (StatusCode:{})".format(statusCode))
            return False
        elif 400 <= statusCode and statusCode < 500:
            print("[Error] Client Error (StatusCode:{})".format(statusCode))
            return False
        elif 500 <= statusCode and statusCode < 600:
            print("[Error] Server Error (StatusCode:{})".format(statusCode))
            return False
        else:
            print("[Assert] Undefined Status Code!")
            assert(False)
        
    
    @staticmethod
    def getCardImage(pageTitle: str, outputDirPath: Optional[str] = None):
        print("[Info] Start Download Card Image.")
        
        if pageTitle == "":
            print("[Error] The Page Title isn't Entered.")
            return False
        
        REQUEST_QUERY_IMAGES = {"action" : "query", "prop": "images", "titles" : pageTitle, "format": "json"}

        res = DownloadCardImage.__session.get(url = "https://scptcgjpj.fandom.com/ja/api.php", params=REQUEST_QUERY_IMAGES, verify=True)
        if not DownloadCardImage.__isOk(res.status_code):
            return False
        
        resPages = res.json()["query"]["pages"]
        
        if list(resPages.keys())[0] == "-1":
            print("[Error] No such Page.")
            return False
        
        if not "images" in list(resPages.values())[0]:
            print("[Error] Not Found Images in This Page.")
            return False
        
        imageFileName: str = list(resPages.values())[0]["images"][0]["title"]
        
        REQUEST_IMAGE_DIR = {"action" : "query", "titles" : imageFileName, "prop": "imageinfo", "iiprop": "url", "format": "json"}
        res = DownloadCardImage.__session.get(url = "https://scptcgjpj.fandom.com/ja/api.php", params=REQUEST_IMAGE_DIR, verify=True)
        imageURL: str = list(res.json()["query"]["pages"].values())[0]["imageinfo"][0]["url"]

        originalFileName: str = imageFileName.replace("ファイル:", "")
        imageExt = re.search("\.[^\.]+$", originalFileName)
        if imageExt == None:
            print("[Assert] No Imagefile extention!")
            assert(False)

        ext: str = imageExt.group()        
        outFileName: str = originalFileName if outputDirPath == None else outputDirPath + "/" +  originalFileName
            
        imageContent: bytes = DownloadCardImage.__session.get(url = imageURL, verify=True).content
        with open(outFileName, "wb") as f:
            f.write(imageContent)
        
        print("[Info] Downloaded Card Image.")
        return True
            
if __name__ == "__main__":
    if len(argv) == 1 or 4 <= len(argv):
        print("[Error] Bad Argument.")
        print("Usage: python card_image_downloader.py CardPageTitle <OutputDirectoryPath>")
        print("Note that <...> is optional.")
        exit(1)
    cardPageTitle: str = argv[1]
    outputDirPath: Optional[str] = argv[2] if 3 <= len(argv) else None
    
    if not DownloadCardImage.getCardImage(cardPageTitle, outputDirPath):
        print("[Error] Failed to Download the Card Image.")
        exit(1)




