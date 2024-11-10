select
    gender,
    university,
    count(device_id) as user_num,
    avg(active_days_within_30) as avg_active_days,
    avg(question_cnt) as avg_question_cnt
from
    user_profile
group by
    gender,
    university
;