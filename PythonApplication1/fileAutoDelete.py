#coding=utf-8 
#超過n天檔案刪除，並保留每月1日的檔案
#引數傳入目標資料夾

import sys, os, time
from datetime import datetime

class FileDelSys(object):
    def __init__(self, dir_path):
        self.__dir_path = dir_path  #資料夾路徑

    def checkAndDelete(self):
        dirs = os.listdir(self.__dir_path)
        for file in dirs:
           extension = ""
           full_filePath = self.__dir_path + "\\" +file
           m_ts = os.path.getmtime(full_filePath)
           isDir = os.path.isdir(full_filePath)
           if not isDir:
               extension = os.path.splitext(file)[1].lower()
           if(extension == ".bak" or extension == ".zip" or extension == ".txt"):
               #超過90天: 除了月的第一天其餘刪除
               if(self.isDateExceed(m_ts, 90) and not self.isMonthFirstDay(m_ts)):
                   os.remove(full_filePath)
        return "finished"
                   
    #檢查時間是否超過n天
    def isDateExceed(self, m_ts, exceedDay):
        now_ts = time.time()
        diffDay = int((now_ts - m_ts)/(24*60*60))
        return diffDay > exceedDay
    
    #檢查時間是否為月的第一天
    def isMonthFirstDay(self, m_ts):
        date = datetime.utcfromtimestamp(m_ts)
        return date.day == 1
    
    # [Test] 測試更改檔案修改日期
    def testChgFileDate(self, filePath,year=2017,month=11,day=1,hour=19,minute=50,second =0):
        date = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
        modTime = time.mktime(date.timetuple())
        os.utime(filePath, (modTime, modTime))


# ==== 執行 ====
# 引數傳入
def main(argv):
     try:
         dir_path = argv[0]  #r"C:\Users\felixliao\Desktop\TESTFOLDER"
         fileDelSys = FileDelSys(dir_path)
         state = fileDelSys.checkAndDelete()
         print(state)
     except Exception as e: 
         print(str(e))
         
if __name__ == "__main__":
   main(sys.argv[1:])


