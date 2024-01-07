package com.example.firstproject.data.repository;

import com.example.firstproject.data.entity.ProductEntity;
import jakarta.transaction.Transactional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;

import java.util.List;

@SpringBootTest
public class ProductRepositoryTest {
    @Autowired
    ProductRepository productRepository;

    @BeforeEach
    void GenerateData() {
        int count = 1;
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 2000, 3000));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 3000, 3000));
        productRepository.save(new ProductEntity(Integer.toString(--count), "상품" + (count+=2), 1500, 200));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 4000, 5000));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 10000, 1500));

        productRepository.save(getProduct(Integer.toString(count), count++, 1000, 1000));
        productRepository.save(getProduct(Integer.toString(count), count++, 500, 10000));
        productRepository.save(getProduct(Integer.toString(count), count++, 8500, 3500));
        productRepository.save(getProduct(Integer.toString(count), count++, 7200, 2000));
        productRepository.save(getProduct(Integer.toString(count), count++, 5100, 1700));
    }

    private ProductEntity getProduct(String  id, int nameNum, int price, int stock) {
        return new ProductEntity(id, "상품" + nameNum, price, stock);
    }

    @Test
    void findTest() {
        findAll_TestView();

        System.out.println("====↓↓ findByProductName ↓↓====");
        Print(productRepository.findByProductName("상품4"));
        System.out.println("====↑↑ Test Data ↑↑====");

        System.out.println("====↓↓ queryByProductName ↓↓====");
        Print(productRepository.queryByProductName("상품4"));
        System.out.println("====↑↑ Test Data ↑↑====");
    }

    @Test
    void exisTest() {
        findAll_TestView();
        if(productRepository.existsByProductName("상품4")) {
            System.out.println("상품명 '상품4'는(은) 있습니다.");
        }
        if (!productRepository.existsByProductName("상품2")) {
            System.out.println("상품명 '상품2는(은) 없습니다.");
        }
    }

    @Test
    void countTest() {
        findAll_TestView();
        final String id = "상품4";
        System.out.printf("상품명 '%s'는 총 %d개 있습니다.\n", id, productRepository.countByProductName("상품4"));
    }

    @Test
    @Transactional
    void deleteTest() {
        findAll_TestView();
        System.out.println("before 상품 갯수 : "+productRepository.count());

        System.out.println(productRepository.getReferenceById("1").getProductName()+" 삭제");
        productRepository.deleteByProductId("1");
        System.out.println(productRepository.getReferenceById("9").getProductName()+" 삭제");
        System.out.println("삭제 한 상품 갯수 : "+productRepository.removeByProductId("9"));
        System.out.println(productRepository.getReferenceById("4").getProductName()+" 삭제");
        System.out.println("삭제 한 상품 갯수 : "+productRepository.removeByProductName("상품4"));

        findAll_TestView();
        System.out.println("After 상품 갯수 : "+productRepository.count());
    }

    @Test
    void TopTest() {
        int id = 100;
        String Name = "상품123";

        productRepository.save(new ProductEntity(Integer.toString(109), Name, 1500, 1500));
        productRepository.save(new ProductEntity(Integer.toString(id++), Name, 2500, 1500));
        productRepository.save(new ProductEntity(Integer.toString(id++), Name, 3500, 1500));
        productRepository.save(new ProductEntity(Integer.toString(id++), Name, 4500, 1500));
        productRepository.save(new ProductEntity(Integer.toString(id++), Name, 1000, 1500));
        productRepository.save(new ProductEntity(Integer.toString(id++), Name, 2000, 1500));


        // 정렬기준을 정하지 않을 경우 id기준 정렬순위
        System.out.println("상품명이(가) '상품4'인 최상위 2열 출력");
        Print(productRepository.findTop3ByProductName("상품4"));

        System.out.printf("상품명이(가) '%s'인 최상위 3열 출력\n", Name);
        Print(productRepository.findTop3ByProductName(Name));

        System.out.printf("상품명이(가) '%s'인 선위 5열 출력\n", Name);
        Print(productRepository.findFirst5ByProductName(Name));
    }

    // ## 조건자 키워드 테스트 ##

    @Test
    void isEqualsTest() {
        findAll_TestView(); // Test DB 전체 출력 함수

        System.out.println("\n====↓↓ IdIs Test Data ↓↓====");
        System.out.println(productRepository.findByProductIdIs("1"));
        System.out.println("\n====↓↓ IdEquals Test Data ↓↓====");
        System.out.println(productRepository.findByProductIdEquals("1"));
    }

    @Test
    void notTest() {
        System.out.println("\n====↓↓ IdNot Test Id : 3 Data ↓↓====");
        Print(productRepository.findByProductIdNot("3"));
        System.out.println("\n====↓↓ IdIsNot Test Id : 5 Data ↓↓====");
        Print(productRepository.findByProductIdIsNot("5"));
    }

    @Test
    void nullTest() {
        System.out.println("====↓↓ null Test Data ↓↓====");
        Print(productRepository.findByProductStockIsNull());
        Print(productRepository.findByProductStockIsNotNull());
    }

    @Test
    void andTest() {
        Print(productRepository.findTopByProductIdAndProductName("1", "상품1"));
    }
    @Test
    void GreaterTest() {
        Print(productRepository.findByProductPriceGreaterThan(3500));
    }
    @Test
    void Containing() {
        Print(productRepository.findByProductNameContaining("상품1"));
    }

    @Test
    void NameAndPrinceTest() {
        System.out.println("\n\n### 상품명에 '상품1'이 포함되거나, 상품가격이 3500원 이상인 품목 ###");
        Print(productRepository.findByProductNameContainingOrProductPriceGreaterThan("상품1", 3500));

        System.out.println("\n\n### 상품명에 '상품1'이 포함되고, 상품가격이 3500원 이상 5500원 미만인 품목 ###");
        Print(productRepository.findByProductNameContainingAndProductPriceGreaterThanEqualAndProductPriceLessThanEqual("상품1", 3500, 5500));
    }

    // /* 쿼리 메소드 정렬 */

    @Test
    void OrderByTest() {
        System.out.println("\n\n### 상품명에 '상품'글자가 포함된 목록 수량 기준 오름차순 정렬 ###");
        Print(productRepository.findByProductNameContainingOrderByProductStockAsc("상품"));
        System.out.println();

        System.out.println("\n\n### 상품명에 '상품'글자가 포함된 목록 수량 기준 내림차순 정렬 ###");
        Print(productRepository.findByProductNameContainingOrderByProductStockDesc("상품"));
        System.out.println();

        System.out.println("\n\n### 상품명에 '상품'글자가 포함된 목록 가격기준 우선 오름차순, 수량 기준 내림차순 정렬 ###");
        Print(productRepository.findByProductNameContainingOrderByProductPriceAscProductStockDesc("상품"));
        System.out.println();

        System.out.println("\n\n### 상품명에 '상품'글자가 포함된 목록 가격기준 오름차순 정렬 ###");
        Print(productRepository.findByProductNameContaining("상품", Sort.by(Sort.Order.asc("ProductPrice"))));
        System.out.println();

        System.out.println("\n\n### 상품 목록 중 가격이 2500원 이상인 페이지 생성 후 2번째 페이지 ###");
        System.out.println("  ※ 3개의 데이터별로 페이지 생성");
        // PageNumber: zerobase, Size: 페이지당 데이터 수
        Print(productRepository.findByProductPriceGreaterThan(2500, PageRequest.of(1, 3)));
        System.out.println();
    }


    // /* @Query 테스트 */

    @Test
    void QueryTest() {
        System.out.println("\n\n==== findByPrice() Test ====\n" +
                "defalt : 'price > 2000'\n " + "====↓↓ Data ↓↓====");
        Print(productRepository.findPrice());

        System.out.println("\n\n==== findByPriceNativeQ() Test ====\n" +
                "defalt : 'price > 2000'\n " + "====↓↓ Data ↓↓====");
        Print(productRepository.findByPriceNativeQ());

        System.out.println("\n\n==== findByPriceParam('2000') Test ====\n" +
                "'?1 > Param'\n " + "====↓↓ Data ↓↓====");
        Print(productRepository.findByPriceParam(2000));

        System.out.println("\n\n==== findByPriceParamName('3500') Test ====\n" +
                "'price > Param'\n " + "====↓↓ Data ↓↓====");
        Print(productRepository.findByPriceParamName(3500));

        System.out.println("\n\n==== findByPrcieParamPri('5000') Test ====\n" +
                "'pri > Param'\n " + "====↓↓ Data ↓↓====");
        Print(productRepository.findByPrcieParamPri(5000));

        System.out.println("\n\n==== findByPricePageParam('4000') Test ====\n" +
                "PageNum : 1, PageSize : 2\n" + "====↓↓ Data ↓↓====");
        Print(productRepository.findByPricePageParam(4000,
                PageRequest.of(1, 2)));
    }

    void findAll_TestView() {
        System.out.println("====↓↓ FindAll Test Data ↓↓====");
        Print(productRepository.findAll());
        System.out.println("====↑↑ FindAll Test Data ↑↑====");
    }

    void Print(List<ProductEntity> found) {
        for (ProductEntity productEntity : found) {
            System.out.println(productEntity.toString());
        }
    }
}