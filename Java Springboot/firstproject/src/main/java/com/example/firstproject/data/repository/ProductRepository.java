package com.example.firstproject.data.repository;

import com.example.firstproject.data.entity.ProductEntity;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface ProductRepository extends JpaRepository<ProductEntity, String> {
    //// 쿼리 메소드의 주제 키워드

    // 조회
    List<ProductEntity> findByProductName(String name);
    List<ProductEntity> queryByProductName(String name);


    boolean existsByProductName(String name); // 존재유무
    long countByProductName(String name); // 갯수
    void deleteByProductId(String id); // 삭제
    long removeByProductId(String id); // 삭제 후 갯수 출력
    long removeByProductName(String name); // 삭제 후 갯수 출력

    // 값 개수 제한
    List<ProductEntity> findFirst5ByProductName(String name);
    List<ProductEntity> findTop3ByProductName(String name);

    //// 쿼리 메소드의 조건자 키워드

    // Is, Equals *생략가능
    // Logical Keyword : IS, Keyword Expressions : Is, Equals, (or no keyword)
    // findByNumber 메소드와 동일하게 동작
    // ProductEntity findByProcutId(String id); 와 동일한 메소드
    ProductEntity findByProductIdIs(String id);
    ProductEntity findByProductIdEquals(String id);

    // (Is)Not
    List<ProductEntity> findByProductIdNot(String id);
    List<ProductEntity> findByProductIdIsNot(String id);

    // (Is)Null, (Is)NotNull
    List<ProductEntity> findByProductStockIsNull();
    List<ProductEntity> findByProductStockIsNotNull();

    // And, Or
    List<ProductEntity> findTopByProductIdAndProductName(String id, String name);

    // (Is)GreaterThan(초과), (Is)LessThan(미만), (Is)Between(a~b)
    List<ProductEntity> findByProductPriceGreaterThan(Integer Price);

    // (Is)Like, (Is)Contanining(포함), (Is)StartingWith(시작으로), (Is)EndingWith(끝으로)
    List<ProductEntity> findByProductNameContaining(String name);

    List<ProductEntity> findByProductNameContainingOrProductPriceGreaterThan(String name, Integer price);
    List<ProductEntity> findByProductNameContainingAndProductPriceGreaterThanEqualAndProductPriceLessThanEqual(String name, Integer StartPrice, Integer EndPrice);


    /* 정렬과 페이징 */

    // Asc : 오름차순, Desc : 내림찻순
    List<ProductEntity> findByProductNameContainingOrderByProductStockAsc(String name);
    List<ProductEntity> findByProductNameContainingOrderByProductStockDesc(String name);

    // 여러 정렬 기준 사용
    List<ProductEntity> findByProductNameContainingOrderByProductPriceAscProductStockDesc(String name);

    // 매개변수를 활용한 정렬

    List<ProductEntity> findByProductNameContaining(String name, Sort sort);

    // 페이징 처리하기     PageNumber: zerobase, Size: 페이지당 데이터 수
    List<ProductEntity> findByProductPriceGreaterThan(Integer price, Pageable Pageable);
    List<ProductEntity> findByProductNameContaining(String name, Pageable Pageable);
    List<ProductEntity> findByProductNameContainingOrderByProductNameAsc(String name, Pageable Pageable);


    /* @Query 사용하기 */

    @Query("select p from ProductEntity p where p.productPrice > 2000")
    List<ProductEntity> findPrice();

    @Query(value = "select *from product_table p where p.product_price > 2000", nativeQuery = true)
    List<ProductEntity> findByPriceNativeQ();

    @Query("select p from ProductEntity p where p.productPrice > ?1")
    List<ProductEntity> findByPriceParam(Integer price);

    @Query("select p from ProductEntity p where p.productPrice > :price")
    List<ProductEntity> findByPriceParamName(Integer price);

    @Query("select p from ProductEntity p where p.productPrice > :pri")
    List<ProductEntity> findByPrcieParamPri(@Param("pri") Integer pri);

    @Query(value = "select * from product_table where product_table.product_price > :price",
    countQuery = "select count(*) from product_table where product_table.product_price > ?1",
    nativeQuery = true)
    List<ProductEntity> findByPricePageParam(Integer price, Pageable pageable);
}