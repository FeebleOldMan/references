#!/usr/bin/env python3

num_contests, max_loss = map(int, input().strip().split())
impt_score, unimpt_score = [], []

for _ in range(num_contests):
    luck, impt = map(int, input().strip().split())
    if impt:
        impt_score.append(luck)
    else:
        unimpt_score.append(luck)
impt_score.sort(reverse=True)
print(sum(unimpt_score) + sum(impt_score[:max_loss]) - sum(impt_score[max_loss:]))

