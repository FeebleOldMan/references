#!/usr/bin/env python3

import sys, getopt

def main(argv):
    help = """CODE! v1.0

Usage:
  python CODE.py [options]

Options:

  -h, --help                help
  -t, --test                test"""

    try:
        opts, args = getopt.getopt(argv, "ht", ["help", "test",])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-t", "--test"):
            test()
            sys.exit()
    print(splice(int(input()), input()))

### v0.4 bug
#def splice(length, gene):
#    min_length = length
#    target_count = length // 4
#    # front then back
#    current_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#    front_idx, back_idx = 0, length - 1
#    for front in range(length):
#        if current_count[gene[front]] == target_count:
#            front_idx = front
#            break
#        else:
#            current_count[gene[front]] += 1
#    for back in range(length - 1, front_idx, -1):
#        if current_count[gene[back]] == target_count:
#            back_idx = back
#            break
#        else:
#            current_count[gene[back]] += 1
#    fragment_length = back_idx - front_idx + 1 
#    if fragment_length < min_length:
#        min_length = fragment_length
#    # back then front 
#    current_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#    front_idx, back_idx = 0, length - 1
#    for back in range(length - 1, -1, -1):
#        if current_count[gene[back]] == target_count:
#            back_idx = back
#            break
#        else:
#            current_count[gene[back]] += 1
#    for front in range(back_idx):
#        if current_count[gene[front]] == target_count:
#            front_idx = front
#            break
#        else:
#            current_count[gene[front]] += 1
#    fragment_length = back_idx - front_idx + 1 
#    if fragment_length < min_length:
#        min_length = fragment_length
#    if min_length == length: min_length = 0
#    return min_length

### v0.2 bug
#def splice(length, gene):
#    target_count = length/4
#    front_idx, back_idx = 0, length - 1
#    current_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#    while (current_count['A'] < target_count
#            and current_count['T'] < target_count 
#            and current_count['C'] < target_count 
#            and current_count['G'] < target_count):
#        current_count[gene[front_idx]] += 1
#        front_idx += 1
#    already_met = [key for key, value in current_count.items()
#            if value == target_count]
#    for back in range(length - 1, front_idx, -1):
#        if gene[back] in already_met:
#            back_idx = back
#            break
#        else:
#            current_count[gene[back]] += 1

### v0.3 bug
#def splice(length, gene):
#    target_count = length//4
#    front_idx, back_idx = 0, length - 1
#    current_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#    already_met = []
#    min_length = length
#    for front in range(length//2):
#        front_idx = front
#        if gene[front] in already_met:
#            break
#        else:
#            current_count[gene[front]] += 1
#            if current_count[gene[front]] == target_count:
#                already_met.append(gene[front])
#    for back in range(length - 1, front_idx, -1):
#        back_idx = back
#        if gene[back] in already_met:
#            break
#        else:
#            current_count[gene[back]] += 1
#            if current_count[gene[back]] == target_count:
#                already_met.append(gene[back])
#    if (back_idx - front_idx) + 1 < min_length:
#        min_length = (back_idx - front_idx) + 1
#    print(front_idx, back_idx)  #debug
#    front_idx, back_idx = 0, length - 1
#    current_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#    already_met = []
#    for back in range(length - 1, length//2 - 1, -1):
#        back_idx = back
#        if gene[back] in already_met:
#            break
#        else:
#            current_count[gene[back]] += 1
#            if current_count[gene[back]] == target_count:
#                already_met.append(gene[back])
#    for front in range(back_idx):
#        front_idx = front
#        if gene[front] in already_met:
#            break
#        else:
#            current_count[gene[front]] += 1
#            if current_count[gene[front]] == target_count:
#                already_met.append(gene[front])
#    if (back_idx - front_idx) + 1 < min_length:
#        min_length = (back_idx - front_idx) + 1
#    print(front_idx, back_idx)  #debug
#    if min_length == 2: min_length = 0
#    print(min_length)   #debug
#    return min_length

### v0.2 bug
#def splice(length, gene):
#    target_count = length/4
#    front_idx, back_idx = 0, length - 1
#    current_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#    while (current_count['A'] < target_count
#            and current_count['T'] < target_count 
#            and current_count['C'] < target_count 
#            and current_count['G'] < target_count):
#        current_count[gene[front_idx]] += 1
#        front_idx += 1
#    already_met = [key for key, value in current_count.items()
#            if value == target_count]
#    for back in range(length - 1, front_idx, -1):
#        if gene[back] in already_met:
#            back_idx = back
#            break
#        else:
#            current_count[gene[back]] += 1
#            if current_count[gene[back]] == goal_count[gene[back]]:
#                already_met.append(gene[back])
#    return (back_idx - front_idx) + 1

### v0.1 bug and veryyyy slow
#def splice(length, gene):
#    from collections import Counter
#    base_count = Counter(gene)
#    target_count = length/4
#    goal_count = {
#            'A': max(base_count['A'] - target_count, 0),
#            'T': max(base_count['T'] - target_count, 0),
#            'C': max(base_count['C'] - target_count, 0),
#            'G': max(base_count['G'] - target_count, 0)
#            }
#    # include any excess letters
#    min_length = length
#    for i in range(length):
#        current_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#        for j, amino_acid in enumerate(gene[i:]):
#            current_count[amino_acid] += 1
#            if (current_count['A'] >= goal_count['A']
#                    and current_count['T'] >= goal_count['T']
#                    and current_count['C'] >= goal_count['C']
#                    and current_count['G'] >= goal_count['G']):
#                if j + 1 < min_length:
#                    min_length = j + 1
#                break
#    return min_length

def test():
    print("TEST01:", "pass" if splice(8, "GAAATAAA") == 5 else "**FAIL**")
    print("TEST02:", "pass" if splice(8, "AAAAAAAA") == 6 else "**FAIL**")
    print("TEST03:", "pass" if splice(8, "AATTCCGG") == 0 else "**FAIL**")
    print("TEST04:", "pass" if splice(8, "GAAGAAAA") == 4 else "**FAIL**")
    print("TEST05:", "pass" if splice(8, "AAAAGAAG") == 4 else "**FAIL**")

if __name__ == '__main__':
    main(sys.argv[1:])


##!/usr/bin/env python2
#
#TEST_MODE = True
#
#def main():
#  print splice(int(raw_input().strip()), raw_input().strip())
#
#def splice(length, gene):
#  gene_dict = {}
#  # narrow down to substring right by finding outside right bound <= n/4
#  # shrink substring from left bound by making sure outside totals <= n/4
#  # continue scanning through gene by stepwise increasing right bound till eol
#  for i in range(length-1, -1, -1):
#    gene_dict[gene[i]] = gene_dict.get(gene[i], 0) + 1
#    if gene_dict[gene[i]] > length/4:
#      gene_dict[gene[i]] -= 1
#      right_bound = i+1
#      break
#  for i in range(i):
#    gene_dict[gene[i]] = gene_dict.get(gene[i], 0) + 1
#    if gene_dict[gene[i]] > length/4:
#      gene_dict[gene[i]] -= 1
#      left_bound = i-1
#      break
#  min_length = right_bound - left_bound - 1
#  return min_length
#
#def test():
#  print "TEST01:", "pass" if splice(8, "GAAATAAA") == 5 else "**FAIL**"
#  print splice(8, "GAAATAAA")
#test() if TEST_MODE else main()
