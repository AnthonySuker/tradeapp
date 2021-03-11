###IKH IKH_spoof


###money_machine

##this makes money_machine

##written by pro coder harry

def IKH_spoof(data, index):
    length = len(data['Close'])
    close = data['Close'][:length-index]
    high = data['High'][:length-index]
    low = data['Low'][:length-index]
    vol = data['Volume'][:length-index]

    resistance = max(high[-26:])*0.7 + np.mean(high[-26:])*0.3

    support_1 = min(low[-27:-1])*0.7 + np.mean(low[-27:-1])*0.3
    support_2 = min(low[-26:])*0.7 + np.mean(low[-26:])*0.3

    stop_loss = min(low[-52:])

    slope, *c, stdev = stats.linregress(np.array(range(0,52)),np.array(close[-52:]))

    order = 'Stay'
    reason = 'None'


    #Sell statements
    if close[-1] <= (support_1 < close[-2]) and (support_2 > close[-1]):
        order = 'Sell'
        reason = 'stop_loss'

    if close[-1] >= resistance:
        order = 'Sell'
        reason = 'resistance'

    # if close[-1] >= close[-2]*1.05:
    #     order = 'Sell'
    #     reason = 'Half close'

    #Buy statement
    if (support_1 < close[-2]) and (support_2 > close[-1]) and (slope >= 0.01):
        order = 'Buy'

    confidence = 100/(stdev**2 + 1)

    # if reason != "None":
    #     print(reason)
    return order, confidence, close[-1], reason, slope, stdev
