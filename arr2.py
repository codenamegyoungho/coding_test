scores_mat = []
for _ in range(5):
    scores_mat.append(list(map(int,input().split())))
sum_scores = [sum(scores_mat[i]) for i in range(5)]
max_score = max(sum_scores)
print(sum_scores.index(max_score)+1,max_score)

# human = [list(map(int,input().split())) for _ in range(5)]
# human_score = [0]*5 
# score = 0
# for i in range(5):
#     sum = 0
#     for j in range(4):
#         sum += human[i][j]
#     human_score[i] = sum
#     score = max(score,sum)

# for i in range(5):
#     if human_score[i] == score:
#         print(i+1,score)
#         break