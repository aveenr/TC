from pushbullet import Pushbullet

# INIT
api_key = '99'
pb = Pushbullet(api_key)
my_device = pb.get_device('TC')  #arbitary device

# GET DATA FOR SENDING (static)
code = ['VET', 'HAM']
analysis = ['Today’s move lower has now closed the gap sitting around the R195.00 level. This important support level will be interesting to monitor as failure below it could see price fall further to go and close the gap down at the R188.00 level. Given that the uptrend support as well as a small congestion zone come in around the R190.00- R195.00 region it is possible that an intraday spike down towards R188.00 occurs and then buyers begin to surface. If this is the case then given the oversold conditions a bounce could begin to develop. Monitor for a reversal up from R190.00 – R195.00 region to buy. Target R207.00 and stop is a close below the reversal low.',
            'This stock ahs one of the better looking bullish chart formations out there at the moment and provided the solid support around the R73.00 – R73.50 region holds and the market can begin to find some stability, it is possible this stock puts in a solid bounce back towards R80.00. The oversold conditions together with positive reverse divergence whereby the stochastic makes a lower low but the price makes a higher low should also begin to favour a bounce higher. The rising 50 day moving average also comes in just below the lateral support and should attract buying interest should weakness persists on Friday. What is also significant is that a solid reversal higher occurred on Thursday from the 50%- 61.8% retracement area which indicates buyers were waiting to pounce from this support zone. Look to buy around current levels and place a stop loss as a close below R72.90. Begin locking in profits as the stock nears R80.00.']
total = len(code)

# SEND PUSH TO PUSHBULLET AND LOCAL TEXT
for i in range(0,total): #lower to upper-1
    push = pb.push_note(code[i],analysis[i], device=my_device)
    with open('weekly.txt','a') as data_file:
        print(i, ' - ', code[i], ' - ', analysis[i],file=data_file)
        # print(i,' - ',code[i],' - ',analysis[i])

# # SINGLE DATA LINE
# push = pb.push_note('For the Stick!','API wrote this for the stick', device=stick)
# push = pb.push_file(file_url='https://www.a.com/img/header/logo.png',
#                     file_name='lalogo.png',
#                     file_type='image/png')
