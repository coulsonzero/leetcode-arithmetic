select count(gender), AVG(gpa)
from user_profile
where gender = 'male'
;