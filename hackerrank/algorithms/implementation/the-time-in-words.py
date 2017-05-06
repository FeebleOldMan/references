#!/usr/bin/env python

TEST_MODE = True

def main():
  hours = int(raw_input().strip())
  minutes = int(raw_input().strip())
  print convert(hours, minutes)
  return

def convert(hours, minutes):
  h_dict = { 1: "one",
             2: "two",
             3: "three",
             4: "four",
             5: "five",
             6: "six",
             7: "seven",
             8: "eight",
             9: "nine",
             10: "ten",
             11: "eleven",
             12: "twelve" }
  m_dict = { 0: "o' clock",
             1: "one minute past",
             2: "two minutes past",
             3: "three minutes past",
             4: "four minutes past",
             5: "five minutes past",
             6: "six minutes past",
             7: "seven minutes past",
             8: "eight minutes past",
             9: "nine minutes past",
             10: "ten minutes past",
             11: "eleven mintues past",
             12: "twelve minutes past",
             13: "thirteen minutes past",
             14: "fourteen minutes past",
             15: "quarter past",
             16: "sixteen minutes past",
             17: "seventeen mintues past",
             18: "eighteen mintues past",
             19: "nineteen minutes past",
             20: "twenty minutes past",
             21: "twenty one minutes past",
             22: "twenty two minutes past",
             23: "twenty three minutes past",
             24: "twenty four minutes past",
             25: "twenty five minutes past",
             26: "twenty six minutes past",
             27: "twenty seven minutes past",
             28: "twenty eight minutes past",
             29: "twenty nine minutes past",
             30: "half past",
             31: "twenty nine minutes to",
             32: "twenty eight minutes to",
             33: "twenty seven minutes to",
             34: "twenty six minutes to",
             35: "twenty five minutes to",
             36: "twenty four minutes to",
             37: "twenty three minutes to",
             38: "twenty two minutes to",
             39: "twenty one minutes to",
             40: "twenty minutes to",
             41: "nineteen minutes to",
             42: "eighteen minutes to",
             43: "seventeen minutes to",
             44: "sixteen minutes to",
             45: "quarter to",
             46: "fourteen minutes to",
             47: "thirteen minutes to",
             48: "twelve minutes to",
             49: "eleven minutes to",
             50: "ten minutes to",
             51: "nine minutes to",
             52: "eight minutes to",
             53: "seven minutes to",
             54: "six minutes to",
             55: "five minutes to",
             56: "four minutes to",
             57: "three minutes to",
             58: "two minutes to",
             59: "one minute to" }
  if minutes == 0: return h_dict[hours] + " " + m_dict[minutes]
  if minutes > 30: return m_dict[minutes] + " " + h_dict[hours+1]
  return m_dict[minutes] + " " + h_dict[hours]

def test():
  print convert(5, 47)
  return

test() if TEST_MODE else main()
