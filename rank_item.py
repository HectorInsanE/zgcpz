# this file implement different ways of ranking 
# item with related factor, such as thumbs up/down and timing

# references:
  # http://www.ruanyifeng.com/blog/2012/02/ranking_algorithm_hacker_news.html

# I think age particles in day(24 hours) or MORE would be good in our site

from math import exp
from math import log

ESTABLISHED_TIME = 1337493029
HACKER_ALGO_GRAVITY = 1.8
REDDIT_ALGO_COOLDOWN_TIME = (86400*7)
WILSON_Z = 1.96 # 95% confidence
NEWTON_COOLING_PARAMETER = 3


def get_rank (algorithm, age_set, thumbsup_set, thumbsdown_set,  remark_set, view_set ) :
    score = map(algorithm, age_set, thumbsup_set, thumbsdown_set, remark_set, view_set)
    itemlist = zip(score, range(len(age_set)))
    return sorted(itemlist, key = lambda item: item[0], reverse = True) 

def test_algo (age, thumbsup, thumbsdown, remark, view):
    return ( thumbsup - thumbsdown) / (age+1)

def delicious_algo (age, thumbsup, thumbsdown, remark, view):
    return thumbsup - 1

def hacker_algo (age, thumbsup, thumbsdown, remark, view):
    return (thumbsup - 1 ) / ((age + 2) ** HACKER_ALGO_GRAVITY)

def reddit_algo (age, thumbsup, thumbsdown, remark, view):
    """ 
        the scoring way make reddit_algo mainly depend on age 
        http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_reddit.html 
    """
    score = thumbsup - thumbsdown
    order = log(max(abs(score),10))
    sign = 1 if score>0 else -1

    return round(order + sign * age / REDDIT_ALGO_COOLDOWN_TIME, 7)

def stack_algo (age, thumbsup, thumbsdown, remark, view):
    """ 
        remarks take a important role in stack_algo.
        http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_stack_overflow.html
        slightly changed to eliminate answer score and update-age factor
    """
    views_score = log(view, 10) * 4
    content_score = (thumbsup - thumbsdown) * remark / 5
    divisor = pow( (age+1), 1.5)

    return (views_score + content_score) / divisor

def newton_law_cooling (age, thumbsup, thumbsdown, remark, views):
    score = thumbsup - thumbsdown
    return score * exp(-1 * NEWTON_COOLING_PARAMETER * age)

def wilson_interval (age, thumbsup, thumbsdown, remark, views):
    n = thumbsup + thumbsdown
    p = float (thumbsup / n)
    dividend = float( p + WILSON_Z**2 / (2*n) \
                 - WILSON_Z*pow(p*(1-p)/n + pow(WILSON_Z/(2*n),2),2))
    divisor = float (1 + WILSON_Z**2 / n)
    return dividend / divisor

ages = [1.0,2.5,1.2]
thumbsups = [30,40,50]
thumbsdowns = [2,15,20]
remarks = [1,2,3]
views = [4200,3500,2900]

for algo in [test_algo, delicious_algo, hacker_algo, reddit_algo, stack_algo, newton_law_cooling, wilson_interval ]:
    print get_rank( algo, ages, thumbsups, thumbsdowns, remarks, views)

