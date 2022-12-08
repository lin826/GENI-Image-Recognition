import csv
from os import getcwd


def outputCSV(recordTime, recordList):
    totalRTT = 0
    num = len(recordList)
    with open(getcwd() + "/data/" + recordTime + ".csv",'a+',encoding="utf-8", newline='') as csv_file:
        write = csv.writer(csv_file)
        header = ["filename", "request time", "response time", "RTT", "image width", "image height"]
        write.writerow(header)
        for record in recordList:
            tmp = [record.filename, record.requestTime, record.responseTime, record.delta, record.width, record.height]
            write.writerow(tmp)
            totalRTT += record.delta
        write.writerow(["", "", "average RTT", totalRTT/num, "", ""])
    return totalRTT/num


def outputRTT(width, height, RTT):
    with open(getcwd() + "/data/width_height_rtt" + ".csv",'a+',encoding="utf-8", newline='') as csv_file:
        write = csv.writer(csv_file)
        write.writerow([width, height, RTT])
