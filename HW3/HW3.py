# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:56:55 2020

@author: anils
"""


import numpy as np
import pystan
import pandas as pd
data = pd.read_csv("trend2.csv")
data = data.dropna()
c= data.country.str.strip()
countries = c.unique()
countryp = dict(zip(countries, range(len(countries))))
country = data['county_code'] = data.country.replace(countryp).values
data.outcome = data.church2
ch = data.church2.values
co = data.country.unique()
g = data.gini_net.values
r = data.rgdpl.values

modela_code= """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[country[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 1);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

modela_data= {'N': len(ch),'J': len(co),'country': country+1,'x': g,'y': ch,'z': r}
model_a= pystan.stan(model_code=modela_code, data=modela_data, iter=500, chains=2)
model_a

modelb_code = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[country[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 100);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

modelb_data= {'N': len(ch),'J': len(co),'country': country+1,'x': g,'y': ch,'z': r}
model_b= pystan.stan(model_code=modelb_code, data=modelb_data, iter=500, chains=2)
model_b

#Graphics
model_a.plot()
model_b.plot()


#comments
#model_a beta = 0.36
#model_b beta = 0.38
#when variance is increased, the beta values are also increasing.
#Also Beyza assisted me in this homework



