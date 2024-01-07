use jpql_db;
create index member_idx_name on member(member_name);

select *from member;
select *from member where member_id = "iyou"; -- id는 기본키(PK)이므로 키에서 조회
select *from member where member_name = "아이유"; -- name colum index에서 조회
select *from member where member_addr = "인천 남구 주안동"; -- 테이블 내 모든 조회

create view member_view2 as select *from member;
select *from member_view2;

use jpql_db;
select *from product;

select *from buy;
select *from girl_member;