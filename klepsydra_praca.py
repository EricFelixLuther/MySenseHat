from SensePlayground import SensePlayGround
x = float(raw_input("Ile godzin? "))
sp = SensePlayGround(low_gamma=True)
sp.klepsydra(60*60*x)
