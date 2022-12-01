#Librairie fonction perso
import numpy as np
import matplotlib.pyplot as plt


def Anton_test(word):
    print(word)
    
def exemple_low_pass():
    import numpy as np
    from scipy.signal import butter,filtfilt# Filter requirements.
    T = 2800         # Sample Period
    fs = 1/0.05       # sample rate, Hz
    cutoff = 1     # desired cutoff frequency of the filter, Hz ,slightly higher than actual 1.2 
    nyq = 0.5 * fs  #Nyquist Frequency
    order = 2       # sin wave can be approx represented as quadratic
    n = int(T * fs) # total number of samples
    
    
    
    
    def butter_lowpass_filter(data, cutoff, fs, order):
        normal_cutoff = cutoff / nyq
        
        # Get the filter coefficients 
        
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = filtfilt(b, a, data)
        return y
    
    # Filter the data, and plot both the original and filtered signals.
            
        
    y = butter_lowpass_filter(data, cutoff, fs, order)
        
    fig = plt.figure(figsize=(15,8))
    plt.plot(data)
    plt.plot(y)
    plt.legend(['Data','low pass filtered data'])
    plt.legend()


def datetime_to_decimal(date, datatype = "single"):
    # datatype = "list" or "single"
    if datatype == "single" : 
        year = date.year
        month = 1/13 * date.month
        day =  1/365 * date.day
        hour = 1/8760 * date.hour
        minute = 1/525600 * date.minute
        decimal_date =  year + month + day + hour + minute
        
    if datatype == "list" : 
        decimal_date = [ 0 for i in range(len(date))]
        for i in range(len(date)):
            year = date[i].year
            month = 1/13 * date[i].month
            day =  1/365 * date[i].day
            hour = 1/8760 * date[i].hour
            minute = 1/525600 * date[i].minute
            decimal_date[i] = year + month + day + hour + minute
    return decimal_date
        
    
def test_nul_design(design):
    row_null = []
    col_null = []
    #Test lignes 
    for i in range(len(design[:,0])):
        if np.sum(design[i,:]) == 0 :
            row_null.append(i)
            
    #Test colonnes
    for i in range(len(design[0,:])):
        if np.sum(design[:,i]) == 0 :
            col_null.append(i)
    return row_null,col_null


def distance_long_lat(origin, destination):
    """
    
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    """
    #Requires math
    import math
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6378.2064  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


