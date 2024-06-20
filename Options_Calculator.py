import numpy as np
from scipy.stats import norm

def call_price(S0,c,t,r,k,si):
    d1=(np.log(S0/k)+(r-c+((si**2)/2))*t)/(si*np.sqrt(t))
    d2=d1-(si*np.sqrt(t))
    C0=S0*np.exp(-c*t)*norm.cdf(d1)-k*np.exp(-r*t)*norm.cdf(d2)
    return C0

def digital_call_price(S0,c,t,r,k,si):
    d1=(np.log(S0/k)+(r-c+((si**2)/2))*t)/(si*np.sqrt(t))
    d2=d1-(si*np.sqrt(t))
    C0=np.exp(-r*t)*norm.cdf(d2)
    return C0

def greeks_call(S0,c,t,r,k,si):
    d1=(np.log(S0/k)+(r-c+((si**2)/2))*t)/(si*np.sqrt(t))
    d2=d1-(si*np.sqrt(t))
    C0=S0*np.exp(-c*t)*norm.cdf(d1)-k*np.exp(-r*t)*norm.cdf(d2)
    delta=np.exp(-c*t)*norm.cdf(d1)
    gamma=np.exp(-c*t)*(norm.pdf(d1)/(si*S0*np.sqrt(t)))
    vega=np.exp(-c*t)*(S0*np.sqrt(t)*norm.pdf(d1))
    t1=np.exp(-c*t)*S0*norm.pdf(d1)*si/(2*np.sqrt(t))
    t2=(c*np.exp(-c*t))*S0*norm.cdf(d1)
    t3=(r*k*np.exp(-r*t))*norm.cdf(d2)
    theta=-t1+t2-t3
    return delta,gamma,vega,theta

def ImpliedVolatilityPut(s):
    d1 = ( (np.log(S/X)+(r+0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    d2 = ( (np.log(S/X)+(r-0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    of = (  X*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1) ) - pm
    val = of**2
    print("[σ]=",s,", Object Function Value:", val)
    return(val)

def ImpliedVolatilityCall(s):
    d1 = ( (np.log(S/X)+(r+0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    d2 = ( (np.log(S/X)+(r-0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    of = (  X*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1) ) - pm
    val = of**2
    print("[σ]=",s,", Object Function Value:", val)
    return(val)

def put_price(S0,c,t,r,k,si):
    d1=(np.log(S0/k)+(r-c+((si**2)/2))*t)/(si*np.sqrt(t))
    d2=d1-(si*np.sqrt(t))
    P=-S0*np.exp(-c*t)*norm.cdf(-d1)+k*np.exp(-r*t)*norm.cdf(-d2)
    return P

def greeks_put(S0,c,t,r,k,si):
    d1=(np.log(S0/k)+(r-c+((si**2)/2))*t)/(si*np.sqrt(t))
    d2=d1-(si*np.sqrt(t))
    C0=S0*np.exp(-c*t)*norm.cdf(d1)-k*np.exp(-r*t)*norm.cdf(d2)
    delta=np.exp(-c*t)*norm.cdf(d1)-1
    gamma=np.exp(-c*t)*(norm.pdf(d1)/(si*S0*np.sqrt(t)))
    vega=np.exp(-c*t)*(S0*np.sqrt(t)*norm.pdf(d1))
    t1=-np.exp(-c*t)*S0*norm.pdf(d1)*si/(2*np.sqrt(t))
    t2=(c*np.exp(-c*t))*S0*norm.cdf(d1)
    t3=(r*k*np.exp(-r*t))*norm.cdf(d2)
    theta=t1+t2+t3
    return delta,gamma,vega,theta