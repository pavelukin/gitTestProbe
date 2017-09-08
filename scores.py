school = [{'school class':'4a', 'scores':[3,4,2,5,3,2,4,4]},
{'school class':'4b', 'scores':[4,2,5,5,3,2,4,3]},
{'school class':'5c', 'scores':[2,4,5,3,2,2,4,5,4,5]}]
def aver_score_school():
    count = 0
    scores_number = 0
    for school_class in school:
        for score in school_class['scores']:
            count = count + score
            scores_number = scores_number + 1
    print ( 'Cредний балл по школе: ' + str(count/scores_number))
def aver_score_class():
    count = 0
    scores_number = 0
    for school_class in school:
        for score in school_class['scores']:
            count = count + score
            scores_number = scores_number + 1
        print ('Cредний балл в классе: ' + str(count/scores_number))
        count = 0
        scores_number = 0
aver_score_class()
aver_score_school()