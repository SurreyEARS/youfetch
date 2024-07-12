from requests import get
import psutil

def getpublicip():
    # Use the ifconfig.me service to get the public ip address.
    result = get("https://ifconfig.me").text

    return result

def getcpuinfo():
    physcoretotal = psutil.cpu_count(logical=False)
    coretotal = psutil.cpu_count(logical=True)
    cpufreq = psutil.cpu_freq()
    minfreq = cpufreq.min
    maxfreq = cpufreq.max
    currfreq = cpufreq.current
    usage = psutil.cpu_percent()

    result = {
        "phystotal":physcoretotal,
        "coretotal":coretotal,
        "cpufreq":cpufreq,
        "minfreq":minfreq,
        "maxfreq":maxfreq,
        "currfreq":currfreq,
        "usage":usage
    }

    return result