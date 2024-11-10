select gpa from user_profile
where university = '复旦大学'
order by gpa desc
limit 1
;

select max(gpa) from user_profile
where university = '复旦大学'
;