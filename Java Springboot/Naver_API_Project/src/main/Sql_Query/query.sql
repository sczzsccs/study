-- use sakila; -- sakila 스키마 선택
-- sakila 스키마 전체 테이블 항목 출력
-- show tables;

-- staff 테이블 전체 출력
-- select *from staff;

-- staff 테이블에서 email, first_name, username 항목 출력,
-- first_name 항목은 '성'으로, username 항목은 '이름'으로 표시
-- select email, first_name as 성, username as 이름 from staff;

-- name 항목은 '성'으로 , language 테이블에서 last_name, last_update 항목 출력
-- select name as 이름, last_update from language;

-- first_name 항목은 '성', last_name 항목은 '이름'으로 표시
-- select first_name as 성, last_name as 이름 from actor;

-- first_name이 "NICK"인 항목만 출력
-- select first_name as 성, last_name as 이름 from actor where first_name like "NICK";

-- first_name이 "NICK"인 항목 중 중복을 제외하고 출력
-- select distinct first_name as 성 from actor where first_name like "NICK";


use first_db;

create view articleView as select *from article_table;
select * from  articleView;
-- article_table example InputData
-- insert into article_table(id, title, content) values(3, 'ccc', '3333');

use first_db;
select *from product_table;

select *from product_table 
	where product_price 
    between 3500 and 5500;

select *from product_table
	where product_name like "%상품%" 
		and 3500 <= product_price
        and 5500 >= product_price;

select *from product_table
	where product_name like "%상품%" 
		and 3500 <= product_price
        and 5500 >= product_price;


-- product_table example InputData
-- UPDATE product_table SET product_price = 3000 where product_id = 'book';
-- insert into product_table(product_id, product_name, product_price, product_stook) values('4 번째', '이름', 1300, 333);

select *from listener;