use jpql_db;

Delimiter $
create procedure MyPrc()
Begin
	select *from member where member_name = '나훈아';
    select *from product where product_name = '삼각김밥';
end $
Delimiter ;

call MyPrc();

Delimiter $$
create procedure BuyAndGirl()
Begin
	select *from buy;
	select *from girl_member;
end $$
Delimiter ;

call BuyAndGirl();
call BuyAndGirl();