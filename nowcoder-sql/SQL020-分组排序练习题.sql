select
    university,
    round(avg(question_cnt), 4) as avg_question_cnt
from user_profile
group by university
order by avg_question_cnt
;